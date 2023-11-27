from psycopg.errors import UniqueViolation
from pydantic import TypeAdapter
from sqlalchemy import select, insert, update
from sqlalchemy.exc import IntegrityError

from src.app.models.user import User as UserModel
from src.app.schemas.user import User as UserSchema, UserCreate, UserUpdate

from .base import Controller
from .errors import AlreadyExistError, NotFoundError


class UserController(Controller[UserModel]):

    def get_user(self, user_id: int) -> UserSchema:
        stmt = select(UserModel).filter(UserModel.id == user_id)

        user = self.session.scalar(stmt)
        if not user:
            raise NotFoundError(f'User(id={user_id}) not found')
        return UserSchema.model_validate(user)

    def list_users(self) -> list[UserSchema]:
        stmt = select(UserModel)
        result = self.session.scalars(stmt.order_by(UserModel.id)).fetchall()
        return TypeAdapter(list[UserSchema]).validate_python(result)

    def create_user(self, creation: UserCreate) -> UserSchema:
        self._validate_data(creation)
        stmt = (
            insert(UserModel)
            .values(
                username=creation.username,
                first_name=creation.first_name,
                last_name=creation.last_name,
            )
            .returning(UserModel)
        )
        try:
            stmt = self.session.scalar(stmt)
        except IntegrityError as e:
            if isinstance(e.orig, UniqueViolation):
                raise AlreadyExistError('User not unique')
            raise e
        return UserSchema.model_validate(stmt)

    def update_user(self, user_id: int, updates: UserUpdate) -> UserSchema:
        self._validate_data(updates)
        self.get_user(user_id)
        stmt = (
            update(UserModel)
            .filter(UserModel.id == user_id)
            .values(
                username=updates.username,
                first_name=updates.first_name,
                last_name=updates.last_name,
            )
            .returning(UserModel)
        )
        updated_user = self.session.scalar(stmt)

        return UserSchema.model_validate(updated_user)

    def _validate_data(self, data: UserCreate | UserUpdate):
        """Data validation"""
