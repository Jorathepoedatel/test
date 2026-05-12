from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Recipe


async def get_recipes(db: AsyncSession):
    result = await db.execute(
        select(Recipe)
        .order_by(Recipe.views.desc(), Recipe.cooking_time.asc())
    )
    return result.scalars().all()


async def get_recipe(db: AsyncSession, recipe_id: int):
    result = await db.execute(
        select(Recipe).where(Recipe.id == recipe_id)
    )
    recipe = result.scalar_one_or_none()

    if recipe:
        recipe.views += 1
        await db.commit()

    return recipe


async def create_recipe(db: AsyncSession, data):
    recipe = Recipe(**data.model_dump())
    db.add(recipe)
    await db.commit()
    await db.refresh(recipe)
    return recipe