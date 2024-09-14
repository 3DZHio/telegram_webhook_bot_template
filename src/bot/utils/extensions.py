from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest
from aiogram.fsm.context import FSMContext


## MAIN ##
async def delete_data(names: str | list[str], state: FSMContext) -> None:
    await state.update_data({name: None for name in (names if isinstance(names, list) else [names])})


async def delete_message(message_names: str | list[str], chat_id: int | str, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    if isinstance(message_names, str):
        message_names = [message_names]
    for message_name in message_names:
        message_id = data.get(message_name)
        if message_id:
            try:
                await bot.delete_message(chat_id=chat_id, message_id=message_id)
            except TelegramBadRequest:
                pass
            await state.update_data({message_name: None})


async def delete_keyboard(message_names: str | list[str], chat_id: int | str, state: FSMContext, bot: Bot) -> None:
    data = await state.get_data()
    if isinstance(message_names, str):
        message_names = [message_names]
    for message_name in message_names:
        message_id = data.get(message_name)
        if message_id:
            try:
                await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id)
            except TelegramBadRequest:
                pass
            await state.update_data({message_name: None})
