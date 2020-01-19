"""Some vars"""
from os import environ

IS_TEST = bool(environ.get("API_TEST"))
