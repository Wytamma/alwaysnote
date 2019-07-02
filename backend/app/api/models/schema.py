from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    email: str = None
    reactivation_key: Optional[bool] = False


class UserBase(BaseModel):
    email: str = None

class UserBaseInDB(UserBase):
    id: int = None


# Properties to receive via API on creation
class UserInCreate(UserBaseInDB):
    email: str
    password: str

# Properties to receive via API on update
class UserInUpdate(UserBaseInDB):
    password: Optional[str] = None
    attempted_login_count: Optional[int] = None
    is_active: Optional[bool] = None

# Additional properties to return via API
class User(UserBaseInDB):
    pass

# Additional properties stored in DB
class UserInDB(UserBaseInDB):
    hashed_password: str
    is_active: bool = True
    attempted_login_count: int = 0


# Notes 

class NoteBase(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    created: Optional[datetime] = None
    updated: Optional[datetime] = None

class NoteBaseInDB(NoteBase):
    id: int = None
    user_id: int

# Properties to receive via API on creation
class NoteInCreate(NoteBaseInDB):
    created: datetime # local required

# Properties to receive via API on update
class NoteInUpdate(NoteBaseInDB):
    updated: datetime # local required

# Additional properties to return via API
class Note(NoteBase):
    id: int
