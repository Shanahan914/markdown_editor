from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content : str | None
    filename: str
    version: int 
    uploaded : Optional[datetime] = Field(default_factory=datetime.utcnow)