import abc

from typing import Protocol

from . import dto


class UserGateway(Protocol):
    @abc.abstractmethod
    def get_user_by_id(self, id_: int) -> dto.User | None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_user_by_username(self, username: str) -> dto.User | None:
        raise NotImplementedError

    @abc.abstractmethod
    def create_user(self, user: dto.UserCreate) -> dto.User:
        raise NotImplementedError

    @abc.abstractmethod
    def update_user(self, user: dto.User) -> dto.User:
        raise NotImplementedError

    @abc.abstractmethod
    def list_users(self) -> dto.Users:
        raise NotImplementedError
