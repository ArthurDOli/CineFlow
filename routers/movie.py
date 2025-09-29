from fastapi import APIRouter, Depends, HTTPException, status
from models import Movie
from dependencies import getSession
from schemas import MovieSchema
from sqlalchemy.orm import Session

movie_router = APIRouter(prefix='/movie', tags=['Movies'])

@movie_router.post('/create-movie')
async def create_movie(movie_base: MovieSchema, session: Session = Depends(getSession)):
    movie = session.query(Movie).filter(movie_base.title == Movie.title).first()
    if movie:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A movie with this title already exists!")
    else:
        # new_movie = Movie(title=movie_base.title, duration_minutes=movie_base.duration_minutes)
        new_movie = Movie(**movie_base.model_dump())
        session.add(new_movie)
        session.commit()
        return new_movie