from aiogram import Dispatcher

from State.auto import Auto
from handler.callback import call_auto, call_back


async def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(call_auto,
                                       lambda call: call.data.find("Car_id:") != -1,
                                       state=Auto.auto)
    dp.register_callback_query_handler(call_back,
                                       lambda call: call.data == "back",
                                       state="*")

