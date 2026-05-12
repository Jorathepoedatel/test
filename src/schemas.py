from pydantic import BaseModel


class RecipeCreate(BaseModel):
    title: str
    cooking_time: int
    ingredients: str
    description: str


class RecipeOut(BaseModel):
    id: int
    title: str
    cooking_time: int
    views: int

    class ConfigDict:
        from_attributes = True


class RecipeDetail(RecipeOut):
    ingredients: str
    description: str
