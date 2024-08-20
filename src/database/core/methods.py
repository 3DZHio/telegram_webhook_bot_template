from asyncpg import create_pool

from src.config import settings


async def fetchone(query: str, *args) -> dict:
    """FetchOne"""
    async with create_pool(dsn=settings.database_dsn) as pool:
        async with pool.acquire() as connection:
            return await connection.fetchrow(query, *args)


async def fetchall(query: str, *args) -> list[dict]:
    """FetchAll"""
    async with create_pool(dsn=settings.database_dsn) as pool:
        async with pool.acquire() as connection:
            return [dict(fetch) for fetch in await connection.fetch(query, *args)]


async def transaction(query: str, *args) -> None:
    """Transaction"""
    async with create_pool(dsn=settings.database_dsn) as pool:
        async with pool.acquire() as connection:
            async with connection.transaction():
                await connection.execute(query, *args)
