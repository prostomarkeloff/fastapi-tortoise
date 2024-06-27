"""
Pydantic models.
"""
from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
