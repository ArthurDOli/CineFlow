from sqlalchemy import create_engine, Column, String, ForeignKey, Integer, Boolean, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship

db_url = 'sqlite:///database.db'
engine = create_engine(db_url, connect_args={'check_same_thread': False})

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
    tickets = relationship('Ticket', back_populates='user')

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    title = Column(String, index=True)
    duration_minutes = Column(Integer)
    sessions = relationship('Session', back_populates='movie')

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String, unique=True, index=True)
    capacity = Column(Integer)
    sessions = relationship('Session', back_populates='room')

class Session(Base):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    start_time = Column(DateTime, index=True)
    ticket_price = Column(Float)
    movie_id = Column(ForeignKey('movies.id'))
    room_id = Column(ForeignKey('rooms.id'))
    movie = relationship('Movie', back_populates='sessions')
    room = relationship('Room', back_populates='sessions')
    tickets = relationship('Ticket', back_populates='session')

class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    seat_number = Column(Integer)
    user_id = Column(ForeignKey('users.id'))
    session_id = Column(ForeignKey('sessions.id'))
    user = relationship('User', back_populates='tickets')
    session = relationship('Session', back_populates='tickets')