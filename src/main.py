from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import  engine, Base, async_session
import src.crud as crud
import src.schemas as schemas





def create_app():

    async def get_db():
        async with async_session() as session:
            yield session

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        yield

    app = FastAPI(lifespan=lifespan)


    @app.get("/recipes", response_model=list[schemas.RecipeOut])
    async def list_recipes(db: AsyncSession = Depends(get_db)):
        return await crud.get_recipes(db)


    @app.get("/recipes/{recipe_id}", response_model=schemas.RecipeDetail)
    async def get_recipe(recipe_id: int, db: AsyncSession = Depends(get_db)):
        recipe = await crud.get_recipe(db, recipe_id)
        if not recipe:
            raise HTTPException(404, "Recipe not found")
        return recipe


    @app.post("/recipes", response_model=schemas.RecipeDetail)
    async def create_recipe(
            recipe: schemas.RecipeCreate,
            db: AsyncSession = Depends(get_db),
    ):
        return await crud.create_recipe(db, recipe)
    return app

if __name__ == "__main__":
    app = create_app()