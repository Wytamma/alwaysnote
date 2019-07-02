# steal some ideas from here https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/app
from starlette.responses import Response
from starlette.requests import Request
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

import os

from api.models.db import SessionLocal
from api.routers import users, token, notes
from api.core import config

app = FastAPI(title="Alwaysnote API", version='0.2.3')

# CORS
origins = []

# Set all CORS enabled origins
if config.BACKEND_CORS_ORIGINS:
    origins_raw = config.BACKEND_CORS_ORIGINS.split(",")
    for origin in origins_raw:
        use_origin = origin.strip()
        origins.append(use_origin)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    ),

app.include_router(
    token.router, 
    prefix="/token",
    tags=["tokens"]
)
app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)
app.include_router(
    notes.router,
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)

@app.get("/ping")
async def ping():
    return {"pong": True}

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response