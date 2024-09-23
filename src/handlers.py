from datetime import date

from aiogram import Router, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from src.database.requests import (
    get_card_from_db,
    get_user_from_db,
    add_new_user,
    add_cart_of_the_day,
)

from src import keyboards as kb

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"hello {html.bold(message.from_user.full_name)}",
        reply_markup=await kb.themes(),
    )


@router.callback_query(F.data.startswith("theme_"))
async def get_card_of_the_day(callback: CallbackQuery):
    user = await get_user_from_db(callback.from_user.id)
    if not user:
        user = await add_new_user(callback.from_user.id)

    if not user.card_id or user.date != date.today():
        card_id = await add_cart_of_the_day(callback.from_user.id)
        prediction = await get_card_from_db(card_id)
        await callback.message.answer_photo(
            photo=prediction["card"], caption=prediction["prediction"]
        )

    else:
        await callback.message.answer(f"you've already got your predictiion for today!")
