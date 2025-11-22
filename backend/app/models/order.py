from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    order_reference: str
    sku: str
    partner: str      # شركة الشحن
    city: str
    status: str       # created / picked / shipped / delivered / returned

    created_at: datetime
    picked_at: datetime | None = None
    delivered_at: datetime | None = None
    returned_at: datetime | None = None

    awb: str | None = None
