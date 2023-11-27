from polyfactory.factories.pydantic_factory import ModelFactory

from src.app.schemas.user import UserCreate


class UserCreationFactory(ModelFactory[UserCreate]):
    __model__ = UserCreate
