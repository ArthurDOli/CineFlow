from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Movie
from schemas import MovieSchema
from dependencies import getSession

auth_router = APIRouter(prefix='/users', tags=['Users'])

@auth_router.get('/')
async def list_users():
    return {'message': 'Teste'}

