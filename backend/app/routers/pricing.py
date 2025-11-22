from fastapi import APIRouter
from sqlmodel import Session
from app.core.db import engine
from app.models.pricing import Pricing
from app.services.pricing_engine import calculate_price

router = APIRouter(prefix="/pricing", tags=["Pricing"])

@router.post("/calculate")
def calculate(data: dict):
    result = calculate_price(
        material_cost=data["material_cost"],
        packing_cost=data["packing_cost"],
        operating_cost=data["operating_cost"],
        fulfillment_cost=data["fulfillment_cost"],
        shipping_cost=data["shipping_cost"],
        target_margin=data["target_margin"]
    )

    return result


@router.post("/")
def save_pricing(price: Pricing):
    with Session(engine) as session:
        session.add(price)
        session.commit()
        session.refresh(price)
        return price
