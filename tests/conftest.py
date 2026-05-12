import pytest
from httpx import AsyncClient, ASGITransport

from main import app
from src.deps import get_db


@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app, lifespan="on"),
        base_url="http://test",
    ) as ac:
        yield ac