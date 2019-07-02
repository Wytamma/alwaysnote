import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

if os.getenv("HEROKU_ENV") == 'production': 
    BACKEND_CORS_ORIGINS = os.getenv("BACKEND_CORS_ORIGINS")
else:
    BACKEND_CORS_ORIGINS = "*"


