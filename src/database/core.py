import asyncpg

from src.config import settings


class DataBase:
	### MAIN ###
	def __init__(self) -> None:
		self.pool = None
	
	async def connect(self) -> None:
		self.pool = await asyncpg.create_pool(dsn=settings.database_dsn)
	
	async def disconnect(self) -> None:
		await self.pool.close()
	
	### METHODS ###
	async def execute(self, query: str, *args) -> None:
		async with self.pool.acquire() as connection:
			await connection.execute(query, *args)
	
	async def fetchone(self, query: str, *args) -> asyncpg.Record:
		async with self.pool.acquire() as connection:
			return await connection.fetchrow(query, *args)
	
	async def fetchall(self, query: str, *args) -> list[asyncpg.Record]:
		async with self.pool.acquire() as connection:
			return await connection.fetch(query, *args)
	
	### COMMANDS ###
	@staticmethod
	def select(columns: str, table: str, where: str = "TRUE", extra: str = "") -> str:
		return f"SELECT {columns} FROM {table} WHERE {where} {extra};"
	
	@staticmethod
	def insert(table: str, columns: str, values: str) -> str:
		return f"INSERT INTO {table} ({columns}) VALUES ({values});"
	
	@staticmethod
	def update(table: str, columns_values: str, where: str = "TRUE") -> str:
		return f"UPDATE {table} SET {columns_values} WHERE {where};"
	
	@staticmethod
	def delete(table: str, where: str = "TRUE") -> str:
		return f"DELETE FROM {table} WHERE {where};"


db = DataBase()
