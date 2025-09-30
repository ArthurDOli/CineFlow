from fastapi import APIRouter, Depends, HTTPException, status
from schemas import SessionSchema, SessionDisplaySchema
from sqlalchemy.orm import Session as DbSession
from dependencies import getSession
from typing import List
from models import Session as SessionModel
from models import Movie as MovieModel
from datetime import timedelta
from sqlalchemy import and_

session_router = APIRouter(prefix='/sessions', tags=['Sessions'])

@session_router.get('/list-sessions', response_model=List[SessionDisplaySchema])
async def list_sessions(db: DbSession = Depends(getSession)):
    sessions = db.query(SessionModel).all()
    return sessions

@session_router.post('/create-session', status_code=status.HTTP_201_CREATED, response_model=SessionDisplaySchema)
async def create_session(session_base: SessionSchema, db: DbSession = Depends(getSession)):
    movie = db.query(MovieModel).filter(MovieModel.id==session_base.movie_id).first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found")
    new_session_end_time = session_base.start_time + timedelta(minutes=movie.duration_minutes)
    conflict_sessions = db.query(SessionModel).filter(SessionModel.room_id == session_base.room_id).all()
    for existing_session in conflict_sessions:
        if (session_base.start_time < existing_session.end_time and new_session_end_time > existing_session.start_time):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Time slot conflict with existing session (ID: {existing_session.id}) in this room.")
    new_session = SessionModel(**session_base.model_dump())
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@session_router.patch('/update-session/{session_id}', response_model=SessionDisplaySchema)
async def update_session(session_id: int, session_base: SessionSchema, db: DbSession = Depends(getSession)):
    session_to_update = db.query(SessionModel).filter(SessionModel.id == session_id).first()
    if not session_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The session with id {session_id} does not exist')
    update_data = session_base.model_dump(exclude_unset=True)
    if 'start_time' in update_data or 'movie_id' in update_data or 'room_id' in update_data:
        new_start_time = update_data.get('start_time', session_to_update.start_time)
        new_movie_id = update_data.get('movie_id', session_to_update.movie_id)
        new_room_id = update_data.get('room_id', session_to_update.room_id)
        movie = db.query(MovieModel).filter(MovieModel.id==new_movie_id).first()
        if not movie:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found for update")
        new_end_time = new_start_time + timedelta(minutes=movie.duration_minutes)
        potential_conflicts = db.query(SessionModel).filter(
            and_(
                SessionModel.id != session_id,
                SessionModel.room_id == new_room_id,
            )
        ).all()
        for existing_session in potential_conflicts:
            if (new_start_time < existing_session.end_time and new_end_time > existing_session.start_time):
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Update would cause a time slot conflict.")
    for key, value in update_data.items():
        setattr(session_to_update, key, value)
    db.add(session_to_update)
    db.commit()
    db.refresh(session_to_update)
    return session_to_update

@session_router.delete('/delete-session/{session_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_session(session_id: int, db: DbSession = Depends(getSession)):
    session_to_delete = db.query(SessionModel).filter(SessionModel.id==session_id).first()
    if not session_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The sessions with id {session_id} does not exist')
    db.delete(session_to_delete)
    db.commit()
    return None