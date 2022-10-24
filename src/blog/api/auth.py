from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from models.auth import UserCreate, Token


roter = APIRouter(
    prefix='/auth',
    )


@roter.post('/sign-up', response_model=Token)
def sign_up(user_data: UserCreate):
    pass


@roter.post('/sign-in', response_model=Token)
def sign_in(form_data: OAuth2PasswordRequestForm = Depends()):
    pass
