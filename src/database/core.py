import asyncpg

from src.config import settings


class DataBase:
	def __init__(self, dsn: str) -> None:
		"""INIT"""
		self.dsn = dsn
		self.pool = None
	
	## MAIN ##
	async def connect(self) -> None:
		"""CONNECT"""
		if not self.pool:
			self.pool = await asyncpg.create_pool(dsn=self.dsn)
	
	async def disconnect(self) -> None:
		"""DISCONNECT"""
		if self.pool:
			self.pool.close()
			self.pool.is_closing()
			self.pool = None
	
	## METHODS ##
	async def execute(self, query: str, *args) -> None:
		"""EXECUTE"""
		async with self.pool.acquire() as connection:
			await connection.execute(query, *args)
	
	async def fetchone(self, query: str, *args) -> dict:
		"""FETCHONE"""
		async with self.pool.acquire() as connection:
			return await connection.fetchrow(query, *args)
	
	async def fetchall(self, query: str, *args) -> list[dict]:
		"""FETCHALL"""
		async with self.pool.acquire() as connection:
			return [dict(fetch) for fetch in await connection.fetch(query, *args)]
	
	## FUNCTIONS ##
	@staticmethod
	def select(columns: str, table: str, conditions: str = "TRUE", offset: str = "NULL", limit: str = "NULL") -> str:
		"""SELECT"""
		return f"SELECT {columns} FROM {table} WHERE {conditions} OFFSET {offset} LIMIT {limit};"
	
	@staticmethod
	def insert(table: str, columns: str, extra: str = "") -> str:
		"""INSERT"""
		values = ",".join(f"${i}" for i in range(1, len(columns.split(",")) + 1))
		return f"INSERT INTO {table} ({columns}) VALUES ({values}) {extra};"
	
	@staticmethod
	def update(table: str, column: str, value: str = "$1", conditions: str = "TRUE") -> str:
		"""UPDATE"""
		return f"UPDATE {table} SET {column} = {value} WHERE {conditions};"
	
	@staticmethod
	def multiple_update(table: str, columns: str, conditions: str = "TRUE") -> str:
		"""MULTIPLE UPDATE"""
		columns_values = ",".join(f"{column}=${i}" for i, column in enumerate(columns.split(","), start=1))
		return f"UPDATE {table} SET {columns_values} WHERE {conditions};"
	
	@staticmethod
	def delete(table: str, conditions: str = "TRUE") -> str:
		"""DELETE"""
		return f"DELETE FROM {table} WHERE {conditions};"


db = DataBase(dsn=settings.database_dsn)
