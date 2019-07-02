from api import crud
from api.core import config
from api.models.schema import UserInCreate

PASSWORD = os.getenv("PASSWORD")

def init_db(db_session):
    user = crud.user.get_by_email(db_session, email="wytamma.wirth@me.com")
    if not first_user:
        user_in = UserInCreate(
            email="wytamma.wirth@me.com", 
            hashed_password=get_password_hash(PASSWORD)
            )
        user = crud.user.create(db_session, user_in=user_in)

