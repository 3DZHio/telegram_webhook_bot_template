from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.bot.texts import outer
from src.bot.utils import routers
from src.database.models import users


## MAIN ##
# START #
@routers.msg.message(CommandStart())
async def start(message: Message) -> None:
    await message.delete()
    await users.add(message.from_user.id)
    await message.answer(text=outer.msg_start)


## ADMIN ##
@routers.admin_msg.message(F.text == outer.get_admin)
async def admin(message: Message) -> None:
    await message.delete()
    await message.answer(text=outer.msg_admin)
