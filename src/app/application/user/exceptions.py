from dataclasses import dataclass

from src.app.application.common.exceptions import GatewayException, ValidationException


class UserGatewayException(GatewayException):
    pass


class UserValidationException(ValidationException):
    pass


@dataclass(eq=False)
class UsernameAlreadyExists(UserGatewayException):
    username: str

    @property
    def title(self) -> str:
        return f'A user with username "{self.username}" already exists'


@dataclass(eq=False)
class UserIdAlreadyExists(UserGatewayException):
    user_id: int

    @property
    def title(self) -> str:
        return f'A user with id {self.user_id} already exists'


@dataclass(eq=False)
class UserIdNotExists(UserGatewayException):
    user_id: int

    @property
    def title(self) -> str:
        return f'A user with id {self.user_id} doesn\'t exist'


@dataclass(eq=False)
class UsernameNotExists(UserGatewayException):
    username: str

    @property
    def title(self) -> str:
        return f'A user with username "{self.username}" doesn\'t exist'
