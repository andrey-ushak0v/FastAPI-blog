
from datetime import datetime, timedelta
from pydantic import ValidationError
from jose import jwt, JWTError
from passlib.hash import bcrypt

from models.auth import User, Token
import tables
from settings import settings

from fastapi import HTTPException, status


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_pssword: str) -> bool:
        return bcrypt.verify(plain_password, hashed_pssword)

    @classmethod
    def hadh_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='could not valid credentials',
            headers={
                'WWW-authenticate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: tables.User) -> Token:
        user_data = User.from_orm(user)
        now = datetime.now

        payload = {
             'iat': now,
             'nbf': now,
             'exp': now + timedelta(seconds=settings.jwt_expiration),
             'sub': str(user_data.id),
             'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret,
            algorithm=settings.jwt_algorithm,
        )

        return Token(access_token=token)
