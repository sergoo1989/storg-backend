from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.db import engine
from app.models.transaction import Transaction
from app.models.order import Order
from app.services.accounting_engine import detect_financial_errors

router = APIRouter(prefix="/accounting", tags=["Accounting"])

@router.get("/errors")
def accounting_errors():
    with Session(engine) as session:
        orders = session.exec(select(Order)).all()
        transactions = session.exec(select(Transaction)).all()

    errors = detect_financial_errors(orders, transactions)
    return errors
