import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.database import Base

@pytest.fixture(autouse=True, scope="session")
async def setup_database():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)