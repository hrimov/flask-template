from dataclasses import dataclass
from typing import TypeAlias

from src.app.application.common.dto import DTO


@dataclass
class UserCreate(DTO):
    username: str
    first_name: str
    last_name: str


@dataclass(frozen=True)
class User(DTO):
    id: int
    username: str
    first_name: str
    last_name: str


Users: TypeAlias = list[User]
