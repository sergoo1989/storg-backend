from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.order import Order
from app.models.inventory import Inventory
from app.services.qc_engine import qc_check_orders

router = APIRouter(prefix="/qc", tags=["QC"])

@router.get("/errors")
def qc_errors():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        inventory = session.exec(select(Inventory)).all()

    errors = qc_check_orders(orders, inventory)
    return [e.dict() for e in errors]
