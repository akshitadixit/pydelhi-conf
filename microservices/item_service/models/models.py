from tortoise import fields
from tortoise.models import Model

class Item(Model):
    item_id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)

    class Meta:
        table = "items"
