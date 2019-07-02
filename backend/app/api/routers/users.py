
from datetime import timedelta

from fastapi import APIRouter, HTTPException, Depends, Body
from fastapi.encoders import jsonable_encoder

from api.models.db import User as DBUser
from api.models.schema import User, UserInCreate, UserInUpdate
from api.core.jwt import create_access_token, get_token_payload

from sqlalchemy.orm import Session

from api.utils.security import get_current_active_user

from pydantic.types import EmailStr
from api.utils.db import get_db

from api import crud

router = APIRouter()

@router.get("/me", response_model=User)
async def read_users_me(current_user: DBUser = Depends(get_current_active_user)):
    return current_user

@router.put("/me", response_model=User)
async def update_user_me(
    password: str,
    *, 
    current_user: DBUser = Depends(get_current_active_user), 
    db: Session = Depends(get_db),
):
    current_user_data = jsonable_encoder(current_user)
    user_in = UserInUpdate(**current_user_data)
    if password is not None:
        user_in.password = password
    return crud.user.update(db, user=current_user, user_in=user_in)

@router.post("/", response_model=User)
async def create_user_new(
    *, 
    db: Session = Depends(get_db),
    email: EmailStr = Body(...),
    password: str = Body(...),
):
    #check 
    user = crud.user.get_by_email(db, email=email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system.",
        )
    user_in = UserInCreate(password=password, email=email)
    return crud.user.create(db, user_in=user_in)

# change this to a reset password route and force the inactive user to reset their password.
@router.get("/reactivate")
async def reactivate_user(
    email: EmailStr,
    *,
    db: Session = Depends(get_db),
    ):  
    user = crud.user.get_by_email(db, email=email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="There is no user with that email in the system.",
        )
    if user.is_active:
        return {'detail':'User already active.'}
    access_token_expires = timedelta(hours=24)
    access_token = create_access_token(
        data={"email": user.email, "reactivation_key": True}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    # Email this to user
    return {'reactivation_key': token}

@router.get("/reactivate/<reactivation_key>")
async def reactivate_user(
    reactivation_key,
    *,
    db: Session = Depends(get_db),
    ):
    token_data = get_token_payload(token=reactivation_key)
    user = crud.user.get_by_email(db, email=token_data.email)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="There is no user with that email in the system.",
        )
    if user.is_active:
        return {'detail':'User already active.'}
    current_user_data = jsonable_encoder(user)
    user_in = UserInUpdate(**current_user_data)
    user_in.attempted_login_count = 0
    user_in.is_active = True
    crud.user.update(db, user=user, user_in=user_in)
    return {'detail':'User reactivated.'}