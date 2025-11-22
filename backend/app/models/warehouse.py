from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Warehouse(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    location: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
