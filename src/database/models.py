from typing import List

from sqlalchemy import Integer, String, ForeignKey, func, BigInteger, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)

    values: Mapped[list["CardValue"]] = relationship(
        "CardValue", backref="card", cascade="all"
    )

    # users: Mapped[List['User']] = relationship('User', back_populates='card')


class Theme(Base):
    __tablename__ = "themes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    values: Mapped[list["CardValue"]] = relationship(
        "CardValue", backref="theme", cascade="all"
    )


class CardValue(Base):
    __tablename__ = "cardvalues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    card_id: Mapped[int] = mapped_column(Integer, ForeignKey("cards.id"), index=True)
    theme_id: Mapped[int] = mapped_column(Integer, ForeignKey("themes.id"))
    description: Mapped[str] = mapped_column(String, nullable=False)


# class User(Base):
#     __tablename__ = 'users'
#
#     id: Mapped[int] = mapped_column(Integer, primary_key=True)
#     telegram_id: Mapped[int] = mapped_column(BigInteger)
#     card_id: Mapped[int] = mapped_column(Integer, ForeignKey('cards.id'))
#     date: Mapped[Date] = mapped_column(Date, onupdate=func.now())
#
#     card: Mapped['Card'] = relationship('Card', back_populates='users')
