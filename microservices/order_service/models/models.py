from tortoise import fields
from tortoise.models import Model

class Order(Model):
    order_id = fields.IntField(pk=True)
    item = fields.JSONField()

    class Meta:
        table = "orders"
