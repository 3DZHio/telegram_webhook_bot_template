from aiogram.filters import Filter
from aiogram.types import Message

from src.config import settings


### ADMIN ###
class Admin(Filter):
    def __init__(self) -> None:
        self.admin_ids = settings.ADMIN_IDS.get_secret_value()

    async def __call__(self, message: Message) -> bool:
        return f"{message.from_user.id}" in self.admin_ids
