from fastapi import APIRouter
from app.core.models.tortoise import Item as TItem
from app.core.models.pydantic import Item

router = APIRouter()

@router.post("/", description="Create a new item")
async def post(item: Item):
    i = await TItem.create(**item.dict())
    await i.save()
    return {"response": "Successfully created new one"}

@router.get("/", description="Get all items")
async def get() -> list[Item]:
    items = await TItem.all()
    return items

