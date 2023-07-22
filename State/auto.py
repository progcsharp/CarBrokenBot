from aiogram.dispatcher.filters.state import StatesGroup, State


class Auto(StatesGroup):
    auto = State()
    code = State()
