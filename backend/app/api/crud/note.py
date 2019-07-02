from typing import List, Optional

from api.models.db import Note
from api.models.schema import NoteInCreate, NoteInUpdate

from fastapi.encoders import jsonable_encoder

def get(db_session, *, note_id: int) -> Optional[Note]:
    return db_session.query(Note).filter(Note.id == note_id).first()

def get_by_user_id(db_session, *, user_id: int) -> List[Optional[Note]]:
    return db_session.query(Note).filter(Note.user_id == user_id).all()

def delete(db_session, *, note_id: int) -> True:
    db_session.query(Note).filter(Note.id == note_id).delete()
    db_session.commit()
    return True

def create(db_session, *, note_in: NoteInCreate) -> Note:
    note = Note(
        title=note_in.title,
        content=note_in.content,
        created=note_in.created,
        updated=note_in.updated,
        user_id=note_in.user_id,
    )
    db_session.add(note)
    db_session.commit()
    db_session.refresh(note)
    return note

def update(db_session, *, note: Note, note_in: NoteInUpdate) -> Note:
    note_data = jsonable_encoder(note)
    for field in note_data:
        if field in note_in.fields:
            value_in = getattr(note_in, field)
            if value_in is not None:
                setattr(note, field, value_in)

    db_session.add(note)
    db_session.commit()
    db_session.refresh(note)
    return note