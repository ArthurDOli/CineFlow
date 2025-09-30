from fastapi import APIRouter, Depends, HTTPException, status, Response
from models import Movie
from dependencies import getSession
from schemas import MovieSchema, MovieDisplaySchema
from sqlalchemy.orm import Session
from typing import List

movie_router = APIRouter(prefix='/movie', tags=['Movies'])

@movie_router.get('/list-all-movies', response_model=List[MovieDisplaySchema])
async def list_all_movies(session: Session = Depends(getSession)):
    movie = session.query(Movie).all()
    return movie

@movie_router.post('/create-movie', status_code=status.HTTP_201_CREATED, response_model=MovieDisplaySchema)
async def create_movie(movie_base: MovieSchema, session: Session = Depends(getSession)):
    movie = session.query(Movie).filter(Movie.title == movie_base.title).first()
    if movie:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A movie with this title already exists!")
    else:
        new_movie = Movie(**movie_base.model_dump())
        session.add(new_movie)
        session.commit()
        session.refresh(new_movie)
        return new_movie

@movie_router.patch('/update-movie/{movie_id}', response_model=MovieDisplaySchema)
async def update_movie(movie_id: int, movie_base: MovieSchema, session: Session = Depends(getSession)):
    movie = session.query(Movie).filter(Movie.id==movie_id).first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Movie with id {movie_id} does not exist")
    update_data = movie_base.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(movie, key, value)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

@movie_router.delete('/delete-movie/{movie_id}')
async def delete_movie(movie_id: int, session: Session = Depends(getSession)):
    movie = session.query(Movie).filter(Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Movie with id {movie_id} not found')
    else:
        session.delete(movie)
        session.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)