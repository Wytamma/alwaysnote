from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from api.utils.security import get_current_active_user
from api.utils.db import get_db
from api.models.schema import Token
from api.models.db import User as DBUser
from api import crud
from api.core.jwt import create_access_token

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = 30

@router.post("/auth", response_model=Token)
async def route_login_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(get_db)
    ):
    email = form_data.username #username is an OPENAPI standard
    print(email, form_data.password)
    user = crud.user.authenticate(db, email=email, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="There is no user with that email in the system.",
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": email}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)

    response = JSONResponse({"access_token": token, "token_type": "bearer"})
    # response.set_cookie("Authorization", value=token, domain=None, httponly=True, secure=True)
    return response

@router.post("/refresh", response_model=Token) # this should probably accessed with a refresh token...
async def route_login_access_token(current_user: DBUser = Depends(get_current_active_user)):
    email = current_user.email #username is an OPENAPI standard

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"email": email}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)

    response = JSONResponse({"access_token": token, "token_type": "bearer"})
    # response.set_cookie("Authorization", value=token, domain=None, httponly=True, secure=True)
    return response

@router.get("/remove")
async def route_logout_and_remove_cookie():
    response = JSONResponse({'logout': True})
    response.delete_cookie("Authorization")
    return response