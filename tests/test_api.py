import pytest


@pytest.mark.anyio
async def test_create_recipe(client):
    response = await client.post("/recipes", json={
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


@pytest.mark.anyio
async def test_get_recipes(client):
    response = await client.get("/recipes")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.anyio
async def test_get_recipe_and_increment_views(client):
    create = await client.post("/recipes", json={
        "title": "Views Test",
        "cooking_time": 10,
        "ingredients": "x",
        "description": "y"
    })

    recipe_id = create.json()["id"]

    r1 = await client.get(f"/recipes/{recipe_id}")
    assert r1.json()["views"] == 1

    r2 = await client.get(f"/recipes/{recipe_id}")
    assert r2.json()["views"] == 2