from aiogram import Dispatcher

from State.auto import Auto
from handler.message import message_auto_code


async def register_handlers_message(dp: Dispatcher):
    dp.register_message_handler(message_auto_code, state=Auto.code)
