from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Pricing(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")

    material_cost: float            # المواد الخام
    packing_cost: float             # التغليف
    operating_cost: float           # التشغيل
    fulfillment_cost: float         # الفلفلمنت
    shipping_cost: float            # الشحن

    target_margin: float            # هامش الربح المستهدف %

    suggested_price: float          # الناتج
    created_at: datetime = Field(default_factory=datetime.utcnow)
