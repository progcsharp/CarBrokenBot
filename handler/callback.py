from aiogram import types
from aiogram.dispatcher import FSMContext

from State.auto import Auto
from handler.commands import cmd_start


async def call_auto(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    car_id = callback.data
    car_id = car_id.replace("Car_id:", "")
    async with state.proxy() as data:
        data['auto'] = car_id

    print(car_id)
    await state.set_state(Auto.code.state)
    inline_kb = types.InlineKeyboardMarkup(row_width=3)
    inline_kb.add(types.InlineKeyboardButton(
        "Вернуться назад",
        callback_data=f"back"))
    await callback.message.answer("введи код ошибки", reply_markup=inline_kb)


async def call_back(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await state.finish()
    await cmd_start(callback.message, state)
