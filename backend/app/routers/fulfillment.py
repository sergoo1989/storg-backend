from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.order import Order
from app.services.fulfillment_engine import calc_processing_hours, calc_delivery_hours
from app.services.duplicates import find_duplicates

router = APIRouter(prefix="/fulfillment", tags=["Fulfillment"])

@router.get("/orders")
def list_orders():
    with Session(engine) as session:
        return session.exec(select(Order)).all()

@router.post("/orders")
def create_order(o: Order):
    with Session(engine) as session:
        session.add(o)
        session.commit()
        session.refresh(o)
        return o

@router.get("/duplicates")
def get_duplicates():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        return find_duplicates(orders)

@router.get("/kpi")
def kpi():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()

    processing_times = []
    delivery_times = []

    for o in orders:
        p = calc_processing_hours(o.created_at, o.picked_at)
        d = calc_delivery_hours(o.picked_at, o.delivered_at)

        if p: processing_times.append(p)
        if d: delivery_times.append(d)

    return {
        "avg_processing_hours": round(sum(processing_times)/len(processing_times), 2) if processing_times else None,
        "avg_delivery_hours": round(sum(delivery_times)/len(delivery_times), 2) if delivery_times else None,
        "total_orders": len(orders)
    }
