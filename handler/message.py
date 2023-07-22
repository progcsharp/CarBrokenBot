from aiogram import types
from aiogram.dispatcher import FSMContext

from State.auto import Auto
from db.handler.get import get_code_by_car_id_and_name


async def message_auto_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        print(data["auto"])
        code = await get_code_by_car_id_and_name(data['auto'], message.text.upper())
    print(code)
    await state.set_state(Auto.code.state)
    if code is None:
        await message.answer("Вы ввели неправильный код ошибки")
    else:
        await message.answer(f"Код ошибки:<b> {code.code}</b>\n\n{code.description}")