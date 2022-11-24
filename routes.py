from fastapi import APIRouter
from api import YacineTV

ytv = YacineTV()
router = APIRouter(tags=["YacineTV"])


@router.get("/categories")
def categories():
    return ytv.get_categories()

@router.get("/events")
def events():
    return ytv.get_events()

@router.get("/categories/{category_id}/channels")
def channels(category_id: int):
    return ytv.get_category_channels(category_id)

@router.get("/channel/{channel_id}")
def channel(channel_id: int):
    return ytv.get_channel(channel_id)

@router.get("/event/{channel_id}")
def event(event_id: int):
    return ytv.get_events(event_id)
