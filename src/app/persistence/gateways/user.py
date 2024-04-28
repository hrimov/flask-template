from typing import Iterable, NoReturn

from sqlalchemy import select
from sqlalchemy.exc import DBAPIError, IntegrityError

from app.application.user.interfaces import UserGateway
from app.application.user import dto
from app.application.user.exceptions import (
    GatewayException,
    UserIdAlreadyExists,
    UserIdNotExists,
    UsernameAlreadyExists,
    UsernameNotExists,
)
from app.infrastructure.database import models
from app.infrastructure.database.converters import (
    convert_user_dto_to_model,
    convert_user_model_to_dto,
)
from app.infrastructure.database.exception_mapper import exception_mapper

from .base import DatabaseGateway


class UserGatewayImpl(DatabaseGateway, UserGateway):

    @exception_mapper
    def get_user_by_id(self, user_id: int) -> dto.User | None:
        user: models.User | None = self.session.get(models.User, user_id)

        if user is None:
            raise UserIdNotExists(user_id)

        return convert_user_model_to_dto(user)

    @exception_mapper
    def get_user_by_username(self, username: str) -> dto.User | None:
        stmt = select(models.User).where(models.User.username == username)
        user: models.User | None = self.session.scalar(stmt)

        if user is None:
            raise UsernameNotExists(username)

        return convert_user_model_to_dto(user)

    @exception_mapper
    def create_user(self, user: dto.UserCreate) -> dto.User:
        database_user = convert_user_dto_to_model(user)
        self.session.add(database_user)

        try:
            self.session.flush((database_user,))
        except IntegrityError as error:
            self._parse_error(error, user)

        return convert_user_model_to_dto(database_user)

    @exception_mapper
    def update_user(self, user: dto.User) -> dto.User:
        database_user = convert_user_dto_to_model(user)
        self.session.add(database_user)

        try:
            self.session.merge(database_user)
        except IntegrityError as error:
            self._parse_error(error, user)

        return convert_user_model_to_dto(database_user)

    @exception_mapper
    def list_users(self) -> dto.Users:
        stmt = select(models.User)
        result: Iterable[models.User] = self.session.scalars(stmt)
        users: dto.Users = [convert_user_model_to_dto(user) for user in result]
        return users

    # noinspection PyMethodMayBeStatic
    def _parse_error(self, err: DBAPIError, user: dto.User | dto.UserCreate) -> NoReturn:
        match err.orig.diag.constraint_name:  # type: ignore
            case "pk_users":
                raise UserIdAlreadyExists(int(user.id)) from err
            case "uq_users_username":
                raise UsernameAlreadyExists(str(user.username)) from err
            case _:
                raise GatewayException from err
