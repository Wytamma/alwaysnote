from api.core.security import get_password_hash
from api.core.config import SQLALCHEMY_DATABASE_URI

from sqlalchemy import Boolean, Column, Integer, String, create_engine, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import Session, sessionmaker
import os

engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class CustomBase(object):
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'


Base = declarative_base(cls=CustomBase)

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    attempted_login_count = Column(Integer, default=0)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean(), default=True)
    notes = relationship("Note")

class Note(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created = Column(DateTime)
    updated = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

Base.metadata.create_all(bind=engine)