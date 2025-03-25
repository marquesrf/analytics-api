from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()


# /api/events
@router.get("/")
def get_events() -> dict:
    return {"events": [1, 2, 3]}

# /api/events/{event_id}


@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {"id": event_id}
