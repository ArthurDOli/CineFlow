from fastapi import APIRouter

session_router = APIRouter(prefix='/session', tags=['Session'])

# @session_router.get('/list_sessions')
# async def list_sessions()