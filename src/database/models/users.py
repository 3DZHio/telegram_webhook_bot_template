from src.database.core import db


async def exists(uid: int) -> str:
	return await db.fetchone(db.select("1", "users", "uid = $1"), uid)


async def add(uid: int) -> None:
	await db.execute(db.insert("users", "uid", "$1"), uid)
