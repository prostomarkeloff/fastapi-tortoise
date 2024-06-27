import typing

from fastapi import APIRouter
from fastapi.params import Depends
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse


class TypedAPIRouter(BaseModel):
    """ Typed APIRouter. Needed for initalizer """

    router: APIRouter
    prefix: str = str()
    tags: typing.List[str] = []
    dependencies: typing.List[Depends] = []
    responses: typing.Dict[
        typing.Union[int, str], typing.Dict[str, typing.Any]
    ] = dict()
    default_response_class: typing.Optional[typing.Type[Response]] = JSONResponse

    class Config:
        arbitrary_types_allowed = True
