from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.inventory import Inventory

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/")
def list_inventory():
    with Session(engine) as session:
        return session.exec(select(Inventory)).all()
