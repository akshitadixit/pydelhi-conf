import pytest

@pytest.mark.asyncio
async def test_get_items(test_client):
    response = await test_client.get("/service_one/items")
    assert response.status_code == 200
    data = response.json()
    assert "items" in data

@pytest.mark.asyncio
async def test_get_item(test_client):
    response = await test_client.get("/service_one/items/1")
    assert response.status_code == 404  # Assuming item_id 1 doesn't exist

@pytest.mark.asyncio
async def test_create_item(test_client):
    new_item_data = {"name": "New Item"}
    response = await test_client.post("/service_one/items", json=new_item_data)
    assert response.status_code == 200
    data = response.json()
    assert "item_id" in data
    assert data["name"] == new_item_data["name"]

