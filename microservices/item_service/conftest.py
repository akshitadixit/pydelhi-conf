import asyncio
import pytest
from sanic import Sanic
from app import init_db
from handlers.routes import blueprint
from tortoise.contrib.test import initializer, finalizer


import asyncio

import pytest
from pytest_sanic.utils import TestClient


@pytest.fixture(scope="function")
def loop():
    """
    Default event loop, you should only use this event loop in your tests.
    """
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    yield loop
    loop.close()


@pytest.fixture(scope="function")
def sanic_client(loop):
    """
    Create a TestClient instance for test easy use.

    test_client(app, **kwargs)
    """
    clients = []

    async def create_client(app, **kwargs):
        client = TestClient(app, **kwargs)
        await client.start_server()
        clients.append(client)
        return client

    yield create_client

    # Clean up
    if clients:
        for client in clients:
            loop.create_task(client.close())


@pytest.fixture(scope="function")
async def app(loop):
    """Create an app for tests"""
    app = Sanic("test_app")
    yield app


@pytest.fixture(scope="function")
async def test_client(loop, app, sanic_client):
    """Setup a test sanic app"""
    Sanic.test_mode = True
    app.blueprint(blueprint)
    app.register_listener(init_db, "before_server_start")
    _cli = await loop.create_task(sanic_client(app))
    yield _cli