from aiogram import Router, html, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from src.database.requests import get_card_from_db

from src import keyboards as kb

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"hello {html.bold(message.from_user.full_name)}",
        reply_markup=await kb.themes(),
    )


@router.callback_query(F.data.startswith('theme_'))
async def get_card_of_the_day(callback: CallbackQuery):
    prediction = await get_card_from_db()
    await callback.message.answer_photo(photo=prediction['card'], caption=prediction['prediction'])


# @router.message(Command("tarot"))
# async def send_prediction(message: Message):
#     prediction = await get_card_from_db()
#     await message.answer_photo(photo=prediction['card'], caption=prediction['prediction'])
