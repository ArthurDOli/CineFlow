from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from schemas import TicketDisplaySchema, TicketSchema, TicketCreateSchema
from dependencies import getSession
from sqlalchemy.orm import Session as DbSession
from models import Ticket, Session

ticket_router = APIRouter(prefix='/tickets', tags=['Tickets'])

@ticket_router.get('/session/{session_id}', response_model=List[TicketDisplaySchema])
async def list_tickets_for_sesssion(session_id: int, db: DbSession = Depends(getSession)):
    tickets = db.query(Ticket).filter(Ticket.session_id==session_id).all()
    return tickets

@ticket_router.post('/', status_code=status.HTTP_201_CREATED, response_model=TicketDisplaySchema)
async def buy_ticket(ticket_base: TicketCreateSchema, db: DbSession = Depends(getSession)):
    tickets = db.query(Session).filter(Session.id==ticket_base.session_id).first()
    if not tickets:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Session not found")
    existing_ticket = db.query(Ticket).filter(Ticket.session_id==ticket_base.session_id, Ticket.seat_number==ticket_base.seat_number).first()
    if existing_ticket:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Seat {ticket_base.seat_number} is already taken for this session.")
    new_ticket = Ticket(**ticket_base.model_dump())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket