import pytest

@pytest.mark.asyncio
async def test_get_orders(test_client):
    response = await test_client.get("/service_two/orders")
    assert response.status_code == 200
    assert response.json()["orders"]

@pytest.mark.asyncio
async def test_get_order(test_client):
    # Assuming there's an order with ID 1 in the database
    response = await test_client.get('/service_two/orders/1')
    assert response.status_code == 200
    assert response.json()["order_id"] == 1
    assert response.json()["item"]

@pytest.mark.asyncio
async def test_get_order_not_found(test_client):
    response = await test_client.get('/service_two/orders/999')
    assert response.status_code == 404
    assert response.json()["error"] == "Order not found"

