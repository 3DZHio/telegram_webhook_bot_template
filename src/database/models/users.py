from src.database.core import db


async def exists(uid: int) -> str:
    """EXISTS"""
    return await db.fetchone(db.select("1", "users", "uid = $1"), uid)


async def add(uid: int) -> None:
    """ADD"""
    await db.execute(db.insert("users", "uid", "$1"), uid)


async def info(uid: int) -> dict:
    """INFO"""
    return await db.fetchone(db.select("*", "users", "uid = $1"), uid)