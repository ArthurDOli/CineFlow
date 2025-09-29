# uvicorn main:app --reload

from fastapi import FastAPI
from routers import auth, movie

app = FastAPI()

app.include_router(auth.auth_router)
app.include_router(movie.movie_router)