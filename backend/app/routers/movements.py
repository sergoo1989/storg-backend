from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.movement import Movement
from app.models.inventory import Inventory

router = APIRouter(prefix="/movements", tags=["Movements"])

@router.post("/")
def create_movement(mv: Movement):
    with Session(engine) as session:
        session.add(mv)

        # update inventory
        inv = session.exec(
            select(Inventory)
            .where(Inventory.product_id == mv.product_id)
            .where(Inventory.warehouse_id == mv.warehouse_id)
        ).first()

        if not inv:
            inv = Inventory(product_id=mv.product_id, warehouse_id=mv.warehouse_id, quantity=0)
            session.add(inv)

        if mv.movement_type == "IN":
            inv.quantity += mv.quantity
        else:
            inv.quantity -= mv.quantity

        session.commit()
        session.refresh(mv)
        return mv
