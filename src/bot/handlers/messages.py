from aiogram import Bot, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.bot.texts import outer
from src.bot.utils import routers, extensions
from src.database.models import users


### MAIN ###
## START ##
@routers.msg.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext, bot: Bot) -> None:
    uid = message.from_user.id
    await message.delete()
    if not await users.exists(uid):
        await users.add(uid)
    await extensions.delete_message("msg_start", uid, state, bot)
    await state.update_data(msg_start=(await message.answer(text=outer.msg_start)).message_id)


### ADMIN ###
@routers.admin_msg.message(F.text == outer.get_admin)
async def cmd_admin(message: Message) -> None:
    await message.delete()
    await message.answer(text=outer.msg_admin)
