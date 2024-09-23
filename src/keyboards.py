from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.database.requests import get_themes


async def themes():
    themes_kb = InlineKeyboardBuilder()
    themes = await get_themes()
    for theme in themes:
        themes_kb.add(
            InlineKeyboardButton(text=theme.name, callback_data=f"theme_{theme.id}")
        )

    return themes_kb.adjust(2).as_markup()
