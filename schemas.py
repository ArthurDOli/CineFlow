from pydantic import BaseModel, ConfigDict
from typing import Optional
import datetime

class MovieSchema(BaseModel):
    title: str
    duration_minutes: int

class MovieDisplaySchema(BaseModel):
    id: int
    title: str
    duration_minutes: int
    model_config = ConfigDict(from_attributes=True)

class RoomSchema(BaseModel):
    name: str
    capacity: int

class RoomDisplaySchema(BaseModel):
    id: int
    name: str
    capacity: int
    model_config = ConfigDict(from_attributes=True)

class SessionSchema(BaseModel):
    movie_id: int
    room_id: int
    start_time: datetime.datetime
    ticket_price: float

class SessionDisplaySchema(BaseModel):
    id: int
    start_time: datetime.datetime
    end_time: datetime.datetime | None
    ticket_price: float
    model_config = ConfigDict(from_attributes=True)

class TicketSchema(BaseModel):
    customer_name: str
    seat_number: int
    session_id: int

class TicketCreateSchema(TicketSchema):
    pass

class TicketDisplaySchema(TicketSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)