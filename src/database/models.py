from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.database import Base


class Card(Base):
    __tablename__ = "cards"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    url: Mapped[str] = mapped_column(String, nullable=False)

    values: Mapped[list["CardValue"]] = relationship(
        "CardValue", backref="card", cascade="all"
    )


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
    card_id: Mapped[int] = mapped_column(Integer, ForeignKey("cards.id"))
    theme_id: Mapped[int] = mapped_column(Integer, ForeignKey("themes.id"))
    description: Mapped[str] = mapped_column(String, nullable=False)
