
from datetime import datetime

from fastapi import APIRouter, Depends, Body, HTTPException

from typing import List

from sqlalchemy.orm import Session

from api.models.db import User as DBUser
from api.models.schema import User, Note, NoteInCreate, NoteInUpdate
from api import crud
from api.utils.security import get_current_active_user
from api.utils.db import get_db

router = APIRouter()

@router.get("/", response_model=List[Note])
async def list_of_notes(current_user: DBUser = Depends(get_current_active_user), db: Session = Depends(get_db)):
    return  crud.note.get_by_user_id(db, user_id=current_user.id)

@router.post("/", response_model=Note)
async def create_note(
    *, 
    current_user: DBUser = Depends(get_current_active_user), 
    db: Session = Depends(get_db),
    title: str = Body(None),
    content: str = Body(None),
    created: datetime = Body(...),
):
    note_in = NoteInCreate(title=title, content=content, created=created, updated=created, user_id=current_user.id)
    return  crud.note.create(db, note_in=note_in)

@router.put("/{note_id}", response_model=Note)
async def update_note(
    *, 
    current_user: DBUser = Depends(get_current_active_user), 
    db: Session = Depends(get_db),
    note_id: int,
    title: str = Body(None),
    content: str = Body(None),
    updated: datetime = Body(...)
):
    note = crud.note.get(db, note_id=note_id)
    if not note or note.user_id != current_user.id:
         raise HTTPException(
            status_code=404,
            detail="Note not found",
        )
    note_in = NoteInUpdate(title=title, content=content, updated=updated, user_id=current_user.id)
    return crud.note.update(db, note=note, note_in=note_in)

@router.get("/{note_id}", response_model=Note)
async def get_note(
    *, 
    current_user: DBUser = Depends(get_current_active_user), 
    db: Session = Depends(get_db),
    note_id: int
):
    note = crud.note.get(db, note_id=note_id)
    if not note or note.user_id != current_user.id:
         raise HTTPException(
            status_code=404,
            detail="Note not found",
        )
    return note

@router.delete("/{note_id}", status_code=200)
async def delete_note(
    *, 
    current_user: DBUser = Depends(get_current_active_user), 
    db: Session = Depends(get_db),
    note_id: int
):
    note = crud.note.get(db, note_id=note_id)
    if not note or note.user_id != current_user.id:
         raise HTTPException(
            status_code=404,
            detail="Note not found",
        )
    crud.note.delete(db, note_id=note_id)
    return {'detail':'deleted'}