# uvicorn main:app --reload

from fastapi import FastAPI
from routers import movie, room, session, ticket

app = FastAPI()

app.include_router(movie.movie_router)
app.include_router(room.room_router)
app.include_router(session.session_router)
app.include_router(ticket.ticket_router)