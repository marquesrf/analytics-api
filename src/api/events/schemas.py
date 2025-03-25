from pydantic import BaseModel
from typing import List, Optional


class EventSchema(BaseModel):
    id: int
    path: Optional[str] = None
    description: Optional[str] = None


class EventListSchema(BaseModel):
    results: List[EventSchema]


class EventCreateSchema(BaseModel):
    path: str


class EventUpdateSchema(BaseModel):
    description: str
