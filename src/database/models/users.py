from src.database.core import db


async def add(uid: int) -> None:
    """Add"""
    await db.execute(db.insert("users", "uid", "ON CONFLICT (uid) DO NOTHING"), uid)


async def info(uid: int) -> dict:
    """Information"""
    return await db.fetchone(db.select("*", "users", "uid = $1"), uid)
