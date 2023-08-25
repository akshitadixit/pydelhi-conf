from sanic import Blueprint, response
from models.models import Order
from sanic.log import logger
from .item import fetch_item

blueprint = Blueprint("service_two_endpoints", url_prefix="/service_two")

@blueprint.route("/orders", methods=["GET"])
async def get_orders(request):
    orders = await Order.all()
    order_list = [{"order_id": order.order_id, "item": order.item} for order in orders]
    if order_list:
        return response.json({"orders": order_list})
    return response.json({"Error": "No orders found"}, status=500)

@blueprint.route("/orders/<order_id:int>", methods=["GET"])
async def get_order(request, order_id):
    try:
        order = await Order.get(order_id=order_id)
        return response.json({"order_id": order.order_id, "item": order.item})
    except Exception as exc:
        logger.error(exc)
        return response.json({"error": "Order not found"}, status=404)

@blueprint.route("/orders", methods=["POST"])
async def create_order(request):
    try:
        data = request.json
        item_id = data.get("item_id")
        status_code, item = await fetch_item(item_id=item_id)
        logger.info(item)
        if status_code!=200:
            return response.json({"error": "Item not found"}, status=404)
        data["item"] = item
        order = await Order.create(**data)
        return response.json({"order_id": order.order_id, "item": order.item})
    except Exception as exc:
        logger.error(exc)
        return response.json({"error": "Order not created"}, status=500)
