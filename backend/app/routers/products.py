from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.product import Product

router = APIRouter(prefix="/products", tags=["Products"])

@router.get("/")
def list_products():
    with Session(engine) as session:
        return session.exec(select(Product)).all()

@router.post("/")
def create_product(product: Product):
    with Session(engine) as session:
        session.add(product)
        session.commit()
        session.refresh(product)
        return product
