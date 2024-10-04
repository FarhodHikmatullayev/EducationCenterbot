from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import db


async def all_groups_default_keyboard():
    groups = await db.select_all_groups()
    markup = ReplyKeyboardMarkup()
    markup.resize_keyboard = True
    markup.row_width = 2
    for group in groups:
        text_button = group['name']
        markup.insert(KeyboardButton(text_button))

    markup.insert(KeyboardButton(text="🔙 Orqaga"))

    return markup
