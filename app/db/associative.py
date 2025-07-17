import enum
from typing import Type

from sqlalchemy import String, ForeignKey, Column, Enum, Integer, Float
from sqlalchemy.orm import relationship, Mapped

from app.db.base import Base


class Role(enum.Enum):
    teamlead = enum.auto()
    member = enum.auto()


class UserTeamAssoc(Base):
    __tablename__ = "user_team_assoc"

    user_id = Column(String(100), ForeignKey("users.id", ondelete="cascade", onupdate="cascade"), primary_key=True)
    team_id = Column(String(100), ForeignKey("teams.id", ondelete="cascade", onupdate="cascade"), primary_key=True)
    role = Column(Enum(Role), default=Role.member)
    user: Mapped["User"] = relationship(lazy="selectin")
    team: Mapped["Team"] = relationship(lazy="selectin")


class Result(Base):
    __tablename__ = "results"

    team_id = Column(String(100), ForeignKey("teams.id"), primary_key=True)
    tournament_id = Column(String(100), ForeignKey("tournaments.id"), primary_key=True)
    vota_result = Column(Integer())
    result = Column(Float())
    team: Mapped["Team"] = relationship(lazy="selectin")
    tournament: Mapped["Tournament"] = relationship(lazy="selectin")