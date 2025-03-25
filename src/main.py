from typing import Union
from fastapi import FastAPI
from api.events import router as event_router

app = FastAPI()
app.include_router(event_router, prefix="/api/events")


@app.get("/")
def read_root() -> Union[str, dict]:
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None) -> dict:
    return {"item_id": item_id, "q": q}


@app.get("/healthz")
def get_api_health() -> dict:
    return {"status": "ok"}
