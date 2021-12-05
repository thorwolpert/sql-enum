"""The Business Model."""
from __future__ import annotations

from typing import Optional

from enum import Enum, EnumMeta, auto

from .db import db


class BaseMeta(EnumMeta):
    """Meta class for the enum."""

    def __contains__(self, other):  # pylint: disable=C0203
        """Return True if 'in' the Enum."""
        try:
            self(other)  # pylint: disable=no-value-for-parameter
        except ValueError:
            return False
        else:
            return True


class BaseEnum(str, Enum, metaclass=BaseMeta):
    """Replace autoname from Enum class."""

    @classmethod
    def get_enum_by_value(cls, value: str) -> Optional[str]:
        """Return the enum by value."""
        for enum_value in cls:
            if enum_value.value == value:
                return enum_value
        return None

    #pragma warning disable S5720; # noqa: E265
    # disable sonar cloud complaining about this signature
    def _generate_next_value_(name, start, count, last_values):  # pylint: disable=E0213
        """Return the name of the key."""
        return name


class State(BaseEnum):
    """Enum for the Business state."""
    ACTIVE = auto()
    HISTORICAL = auto()
    LIQUIDATION = auto()


class Business(db.Model):
    """Business data access object."""
    __tablename__ = 'businesses'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column('state', db.Enum(State))
