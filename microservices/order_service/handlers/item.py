import aiohttp


async def fetch_item(item_id):
    url = "http://0.0.0.0:8001/service_one/items/{item_id}".format(item_id=item_id)

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            status_code = response.status
            data = await response.json()
            return status_code, data