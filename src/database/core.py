import asyncpg

from src.config import settings


class DataBase:
	## MAIN ##
	def __init__(self) -> None:
		"""INIT"""
		self.pool = None
	
	async def connect(self) -> None:
		"""CONNECT"""
		self.pool = await asyncpg.create_pool(dsn=settings.database_dsn)
	
	async def disconnect(self) -> None:
		"""DISCONNECT"""
		await self.pool.close()
	
	## METHODS ##
	async def execute(self, query: str, *args) -> None:
		"""EXECUTE"""
		async with self.pool.acquire() as connection:
			await connection.execute(query, *args)
	
	async def fetchone(self, query: str, *args) -> dict:
		"""FETCHONE"""
		async with self.pool.acquire() as connection:
			return await connection.fetchrow(query, *args)
	
	async def fetchall(self, query: str, *args) -> list:
		"""FETCHALL"""
		async with self.pool.acquire() as connection:
			return await connection.fetch(query, *args)
	
	## COMMANDS ##
	@staticmethod
	def select(columns: str, table: str, conditions: str = "TRUE") -> str:
		"""SELECT"""
		return f"SELECT {columns} FROM {table} WHERE {conditions};"
	
	@staticmethod
	def insert(table: str, columns: str, values: str) -> str:
		"""INSERT"""
		return f"INSERT INTO {table} ({columns}) VALUES ({values});"
	
	@staticmethod
	def update(table: str, columns_values: str, conditions: str = "TRUE") -> str:
		"""UPDATE"""
		return f"UPDATE {table} SET {columns_values} WHERE {conditions};"
	
	@staticmethod
	def delete(table: str, conditions: str = "TRUE") -> str:
		"""DELETE"""
		return f"DELETE FROM {table} WHERE {conditions};"


db = DataBase()
