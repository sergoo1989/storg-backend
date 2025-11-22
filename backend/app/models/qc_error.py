from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class QCError(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    order_reference: str
    error_code: str
    error_message: str
    severity: str      # low / medium / high / critical
    created_at: datetime = Field(default_factory=datetime.utcnow)
