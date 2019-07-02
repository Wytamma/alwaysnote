
from typing import List, Optional

from api.models.db import User
from api.models.schema import UserInCreate, UserInUpdate
from api.core.security import verify_password, get_password_hash

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder

def get(db_session, *, user_id: int) -> Optional[User]:
    return db_session.query(User).filter(User.id == user_id).first()

def get_by_email(db_session, *, email: str) -> Optional[User]:
    return db_session.query(User).filter(User.email == email).first()

def delete(db_session, *, user_id: int) -> True:
    db_session.query(User).filter(User.id == user_id).delete()
    db_session.commit()
    return True

def authenticate(db_session, *, email: str, password: str) -> Optional[User]:
    user = get_by_email(db_session, email=email)
    
    if not user:
        return None
    
    if not user.is_active:
        raise HTTPException(status_code=403, detail="This account is deactivated. Check Email for reactivation link")
   
    if not verify_password(password, user.hashed_password):
        user.attempted_login_count += 1
        if user.attempted_login_count > 3:
            user.is_active = False
            # send email
        db_session.add(user)
        db_session.commit()
        print(user.email, "attempted login with wrong password")
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # login successful
    user.attempted_login_count = 0
    db_session.add(user)
    db_session.commit()
    return user

def create(db_session, *, user_in: UserInCreate) -> User:
    user = User(
        email=user_in.email,
        hashed_password=get_password_hash(user_in.password),
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user


def update(db_session, *, user: User, user_in: UserInUpdate) -> User:
    user_data = jsonable_encoder(user)
    for field in user_data:
        if field in user_in.fields:
            value_in = getattr(user_in, field)
            if value_in is not None:
                setattr(user, field, value_in)
    if user_in.password:
        passwordhash = get_password_hash(user_in.password)
        user.hashed_password = passwordhash
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)
    return user