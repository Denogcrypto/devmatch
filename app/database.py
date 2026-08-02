from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

Base = declarative_base()

engine: AsyncEngine = create_async_engine(
    settings.DATABASE_URL,
    future=True,
    echo=False,
    connect_args={"statement_cache_size": 0},
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

async def init_db() -> None:
    from app.models import user, profile, match

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
