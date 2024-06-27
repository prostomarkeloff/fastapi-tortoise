"""
Tortoise models.
"""

from tortoise import Model, fields

class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()