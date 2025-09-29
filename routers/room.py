from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from models import Room
from dependencies import getSession
from schemas import RoomSchema, RoomDisplaySchema
from typing import List

room_router = APIRouter(prefix='/rooms', tags=['Rooms'])

@room_router.get('/list-rooms', response_model=List[RoomDisplaySchema])
async def list_rooms(session: Session = Depends(getSession)):
    room = session.query(Room).all()
    return room
    
@room_router.post('/create-room', response_model=RoomDisplaySchema, status_code=status.HTTP_201_CREATED)
async def create_room(room_base: RoomSchema, session: Session = Depends(getSession)):
    room = session.query(Room).filter(Room.name==room_base.name).first()
    if room:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f'The room {room_base.name} already exists')
    else:
        new_room = Room(**room_base.model_dump())
        session.add(new_room)
        session.commit()
        session.refresh(new_room)
        return new_room
    
@room_router.put('/update-room/{room_id}', response_model=RoomDisplaySchema)
async def update_room(room_id: int, room_base: RoomSchema, session: Session = Depends(getSession)):
    room = session.query(Room).filter(Room.id==room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The room with id {room_id} does not exist")
    update_data = room_base.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(room, key, value)
    session.add(room)
    session.commit()
    session.refresh(room)
    return room

@room_router.delete('/delete-room/{room_id}')
async def delete_room(room_id: int, session: Session = Depends(getSession)):
    room = session.query(Room).filter(Room.id==room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The room with id {room_id} does not exist")
    else:
        session.delete(room)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)