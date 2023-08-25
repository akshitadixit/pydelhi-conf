from sanic import Blueprint, response
from models.models import Item
from sanic.log import logger

blueprint = Blueprint("service_one_endpoints", url_prefix="/service_one")

@blueprint.route("/items", methods=["GET"])
async def get_items(request):
    try:
        items = await Item.all()
        if items:
            item_list = [{"id": item.item_id, "name": item.name} for item in items]
            return response.json({"items": item_list})
        return response.json({"Error": "No items found"}, status=500)
    except Exception as exc:
        logger.error(exc)
        return response.json({"error": "Something went wrong"}, status=500)

@blueprint.route("/items/<item_id:int>", methods=["GET"])
async def get_item(request, item_id):
    try:
        item = await Item.get(item_id=item_id)
        return response.json({"item_id": item.item_id, "name": item.name})
    except Exception as exc:
        logger.error(exc)
        return response.json({"error": "Item not found"}, status=404)

@blueprint.route("/items", methods=["POST"])
async def create_item(request):
    try:
        data = request.json
        item = await Item.create(**data)
        return response.json({"item_id": item.item_id, "name": item.name})
    except Exception as exc:
        logger.error(exc)
        return response.json({"error": "Item not created"}, status=500)
