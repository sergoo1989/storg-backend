from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.warehouse import Warehouse

router = APIRouter(prefix="/warehouses", tags=["Warehouses"])

@router.get("/")
def list_warehouses():
    with Session(engine) as session:
        return session.exec(select(Warehouse)).all()

@router.post("/")
def create_warehouse(wh: Warehouse):
    with Session(engine) as session:
        session.add(wh)
        session.commit()
        session.refresh(wh)
        return wh
