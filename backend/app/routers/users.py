from fastapi import APIRouter
from sqlmodel import Session, select
from app.models.user import User
from app.core.db import engine

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/")
def list_users():
    with Session(engine) as session:
        users = session.exec(select(User)).all()
        return users
