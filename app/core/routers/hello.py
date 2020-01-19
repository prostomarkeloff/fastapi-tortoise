from fastapi import APIRouter
from starlette.responses import HTMLResponse

router = APIRouter()


@router.get("/get", description="Get 'Hello!'", response_description="Some text")
async def get():
    return HTMLResponse("Hello!")
