from app.core.routers.hello import router as hello_router
from app.utils.api.router import TypedAPIRouter

hello_router = TypedAPIRouter(router=hello_router, prefix="/hello", tags=["hello"])
