from datetime import date
from random import randint
from sqlalchemy import select
from src.database.database import async_session
from src.database.models import CardValue, Card, Theme, User


async def get_user_from_db(telegram_id: int) -> User:
    async with async_session() as session:
        user = (
            await session.execute(select(User).where(User.telegram_id == telegram_id))
        ).scalar_one_or_none()
        return user


async def add_new_user(telegram_id: int) -> User:
    async with async_session() as session:
        new_user = User(telegram_id=telegram_id)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return new_user


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


async def add_cart_of_the_day(telegram_id):
    async with async_session() as session:
        id = await get_number()
        user = await get_user_from_db(telegram_id)
        user.card_id = id
        user.date = date.today()
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user.card_id


async def get_card_from_db(card_id: int):
    async with async_session() as session:
        prediction = await session.scalar(
            select(CardValue).where(CardValue.card_id == card_id)
        )
        card = await session.scalar(select(Card).where(Card.id == card_id))
        return {"card": card.url, "prediction": prediction.description}
