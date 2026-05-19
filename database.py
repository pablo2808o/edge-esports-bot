from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import declarative_base

DATABASE_URL = "sqlite+aiosqlite:///edge.db"

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)

Base = declarative_base()
