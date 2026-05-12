import pytest
from httpx import ASGITransport, AsyncClient

from src.main import app


# тест создания рецепта
@pytest.mark.anyio
async def test_create_recipe():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
    ) as ac:
        response = await ac.post("/recipes", json={
            "title": "Test Recipe",
            "cooking_time": 20,
            "ingredients": "water, salt",
            "description": "boil"
        })

    assert response.status_code == 200
    data = response.json()

    assert data["title"] == "Test Recipe"
    assert data["views"] == 0
    assert "id" in data


# тест списка рецептов
@pytest.mark.anyio
async def test_get_recipes():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
    ) as ac:
        response = await ac.get("/recipes")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)


# тест получения рецепта + проверка views
@pytest.mark.anyio
async def test_get_recipe_and_increment_views():
    async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test"
    ) as ac:
        create = await ac.post("/recipes", json={
            "title": "Views Test",
            "cooking_time": 10,
            "ingredients": "x",
            "description": "y"
        })

        recipe_id = create.json()["id"]

        r1 = await ac.get(f"/recipes/{recipe_id}")
        assert r1.status_code == 200
        assert r1.json()["views"] == 1

        r2 = await ac.get(f"/recipes/{recipe_id}")
        assert r2.json()["views"] == 2
