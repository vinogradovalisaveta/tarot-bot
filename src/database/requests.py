from random import randint

from sqlalchemy import select

from src.database.database import async_session
from src.database.models import CardValue, Card, Theme


async def get_themes():
    """
    now there is only 1 theme of reading in this project, but in future
    i'm planning to add more (maybe)), that's the reason i get themes via request
    """
    async with async_session() as session:
        result = await session.scalars(select(Theme))
        return result


async def get_number() -> int:
    return randint(1, 78)


async def get_card_from_db():
    id = await get_number()
    async with async_session() as session:
        prediction = await session.scalar(
            select(CardValue).where(CardValue.card_id == id)
        )
        card = await session.scalar(select(Card).where(Card.id == id))
        return {"card": card.url, "prediction": prediction.description}
