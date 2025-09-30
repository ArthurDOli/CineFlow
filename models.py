from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import timedelta

db_url = 'sqlite:///database.db'
engine = create_engine(db_url, connect_args={'check_same_thread': False})

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    duration_minutes = Column(Integer)
    sessions = relationship('Session', back_populates='movie')

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    sessions = relationship('Session', back_populates='room')

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(DateTime, index=True)
    ticket_price = Column(Float)
    movie_id = Column(Integer, ForeignKey('movies.id'))
    room_id = Column(Integer, ForeignKey('rooms.id'))
    movie = relationship('Movie', back_populates='sessions')
    room = relationship('Room', back_populates='sessions')
    tickets = relationship('Ticket', back_populates='session')

    @property
    def end_time(self):
        if self.movie and self.start_time:
            return self.start_time + timedelta(minutes=self.movie.duration_minutes)
        return None

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    seat_number = Column(Integer)
    session_id = Column(Integer, ForeignKey('sessions.id'))
    session = relationship('Session', back_populates='tickets')