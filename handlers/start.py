from aiogram import types
from handlers.constants import START_TEXT
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


start_kb = InlineKeyboardMarkup(resize_keyboard=True)
start_kb.add(
    InlineKeyboardButton('Магазин', callback_data='shop_start'),
    InlineKeyboardButton('Адрес', callback_data='adress')
)


async def start_command(message: types.Message):
    """
        Функция приветсвия пользователья по имени
    """
    await message.answer(
        text=START_TEXT.format(
            first_name=message.from_user.first_name),
        reply_markup=start_kb
        )
    await message.delete()

