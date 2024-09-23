from random import randint

from sqlalchemy import select

from src.database.database import async_session
from src.database.models import CardValue


async def get_number() -> int:
    return randint(1, 23)


async def get_card_from_db():
    async with async_session() as session:
        card = await session.scalar(
            select(CardValue).where(CardValue.card_id == await get_number())
        )
        return card
