# uvicorn main:app --reload

from fastapi import FastAPI
from routers import auth, movie, room, session

app = FastAPI()

app.include_router(auth.auth_router)
app.include_router(movie.movie_router)
app.include_router(room.room_router)
app.include_router(session.session_router)