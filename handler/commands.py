from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from State.auto import Auto
from db.handler.create import create_user
from db.handler.get import get_cars, get_user_by_tg_id


async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = await get_user_by_tg_id(message.from_user.id)
    if user is None:
        await create_user(message.from_user.id)
    cars = await get_cars()
    print(cars)
    buttons = []
    for car in cars:
        buttons.append(InlineKeyboardButton(
        car.name,
        callback_data=f"Car_id:{car.id}"))
    print(buttons)
    inline_kb = InlineKeyboardMarkup(row_width=3)
    inline_kb.add(*buttons)
    await state.set_state(Auto.auto.state)
    await message.answer("""Здравствуй!
Я бот справочник по ошибкам в автомобилях. 
Чтобы узнать, что означает нужная тебе ошибка сначала выбери авто, а после напиши свою ошибку

Пока что у меня мало автомобилей в базе, и я буду благодарен тебе если ты напишешь моему создателю какие автомобили ты хочешь здесь видеть. Сделать ты это можешь, написав в личные сообщения этому пользователю @artsay2003

Если у тебя остались вопросы или появились, пиши сюда @artsay2003""", reply_markup=inline_kb)
