# Async SQLAlchemy engine + session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

# Database connection URL (PostgreSQL, MySQL, etc.)
DATABASE_URL = ""

# Create async engine that manages connection pooling and SQL execution
# echo=True logs all SQL statements
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a session factory for managing database sessions
# expire_on_commit=False keeps objects accessible after commit
AsyncSession = async_sessionmaker(engine, expire_on_commit=False)


# Dependency function for FastAPI that provides a database session
# Yields a session object and ensures cleanup after use
async def get_db_session() -> AsyncSession:
    async with AsyncSession() as session:
        yield session
