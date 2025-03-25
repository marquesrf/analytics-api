from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema
from api.db.config import DATABASE_URL
import os

router = APIRouter()


# GET /api/events
@router.get("/")
def get_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return {"results": [
        {"id": 1},
        {"id": 2},
        {"id": 3}
    ]}


# GET /api/events/{event_id}
@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}


# POST /api/events/
@router.post("/")
def create_event(payload: EventCreateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": 123, **data}


# PUT /api/events/
@router.put("/{event_id}")
def update_event(event_id: int, payload: EventUpdateSchema) -> EventSchema:
    data = payload.model_dump()
    return {"id": event_id, **data}
