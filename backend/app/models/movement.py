from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Movement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    warehouse_id: int = Field(foreign_key="warehouse.id")
    movement_type: str  # "IN" or "OUT"
    quantity: float
    reference: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
