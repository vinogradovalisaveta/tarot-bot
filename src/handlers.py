from aiogram import Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from src.database.requests import get_card_from_db

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"hello {html.bold(message.from_user.full_name)}")


@router.message(Command("tarot"))
async def send_prediction(message: Message):
    prediction = await get_card_from_db()
    await message.answer(prediction.description)
