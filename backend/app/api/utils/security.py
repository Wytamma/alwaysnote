from fastapi.security import OAuth2PasswordBearer
from fastapi.security.api_key import APIKeyCookie
from starlette.status import HTTP_403_FORBIDDEN
from fastapi import Depends, HTTPException, Security
from sqlalchemy.orm import Session
import jwt

from api.utils.db import get_db
from api.models.schema import User
from api.core.jwt import get_token_payload
from api import crud

import os

oauth2_scheme_header = OAuth2PasswordBearer(tokenUrl="/token/auth", auto_error=False)
oauth2_scheme_cookie = APIKeyCookie(name="Authorization", auto_error=False)

def oauth2_cookie_password_scheme(
    header_token: str = Security(oauth2_scheme_header),
    cookie_token: str = Security(oauth2_scheme_cookie)
    ):
    if cookie_token:
        return cookie_token
    elif header_token:
        return header_token
    else:
        raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )

async def get_current_user(token: str = Depends(oauth2_scheme_header), db: Session = Depends(get_db)):
    token_data = get_token_payload(token=token)
    user = crud.user.get_by_email(db, email=token_data.email)
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user