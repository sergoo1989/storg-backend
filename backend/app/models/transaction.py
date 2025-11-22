from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    source: str         # salla / fulfillment / bank / gateway / manual
    reference: str      # order reference / invoice number / bank ref
    amount: float
    vat: float
    type: str           # revenue / cogs / expense / transfer / refund
    date: datetime
