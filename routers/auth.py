from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserDisplay, Token
from dependencies import getSession
from security import bcrypt_context, get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

# auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

# @auth_router.post('/register', status_code=status.HTTP_201_CREATED, response_model=UserDisplay)
# async def register(user_base: UserCreate, session: Session = Depends(getSession)):
#     user = session.query(User).filter(User.email==user_base.email).first()
#     if user:
#         raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"The user with email '{user_base.email}' already exists")
#     else:
#         user_data = user_base.model_dump()
#         hashed_password = get_password_hash(user_data.pop('password'))
#         user_data['hashed_password'] = hashed_password
#         new_user = User(**user_data)
#         session.add(new_user)
#         session.commit()
#         session.refresh(new_user)
#         return new_user

# @auth_router.post('/login', status_code=status.HTTP_200_OK, response_model=Token)
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(getSession)):
#     user = session.query(User).filter(User.email==form_data.username).first()
#     if not user or not verify_password(form_data.password, user.hashed_password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
#     access_token = create_access_token(data={'sub': user.email})
#     return {
#         'access_token': access_token,
#         'token_type': 'bearer',
# }