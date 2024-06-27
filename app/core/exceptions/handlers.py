"""Handler for those exceptions."""

from tortoise.exceptions import BaseORMException
from fastapi import Request
from fastapi.responses import JSONResponse

# base handler for Tortoise exceptions
async def tortoise_exception_handler(request: Request, exc: BaseORMException) -> JSONResponse:
    return JSONResponse(
        status_code=418,
        content={"message": f"Something went wrong.. And it is that: {repr(exc)}"},
    )