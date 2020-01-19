"""Config of application"""
from .db import TortoiseSettings
from .openapi import OpenAPISettings

tortoise_config = TortoiseSettings.generate()
openapi_config = OpenAPISettings.generate()
