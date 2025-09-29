from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    username: str
    email: str 
    hashed_password: str
    is_admin: Optional[bool] = None

class MovieSchema(BaseModel):
    title: str
    duration_minutes: int

class RoomSchema(BaseModel):
    name: str
    capacity: int

class SessionSchema(BaseModel):
    ticket_price: float

class TicketSchema(BaseModel):
    seat_number: int