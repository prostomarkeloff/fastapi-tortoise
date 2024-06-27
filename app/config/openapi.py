"""OpenAPI-schema"""
from betterconf import Config, field

OPENAPI_API_NAME = "The best API ever"
OPENAPI_API_VERSION = "0.0.1 beta"
OPENAPI_API_DESCRIPTION = "API for humans"


class OpenAPISettings(Config):
    name: str = field("name", default=OPENAPI_API_NAME)
    version: str = field("version", default=OPENAPI_API_VERSION)
    description: str = field("description", default=OPENAPI_API_DESCRIPTION)
