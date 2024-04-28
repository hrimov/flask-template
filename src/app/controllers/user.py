from pydantic import TypeAdapter
from sqlalchemy import select

from app.models.user import User as UserModel
from app.schemas.user import User as UserSchema

from .base import Controller


class UserController(Controller[UserModel]):

    # some operations with the user
    def list_users(self) -> list[UserSchema]:
        stmt = select(UserModel)
        result = self.session.scalars(stmt.order_by(UserModel.id)).fetchall()
        return TypeAdapter(list[UserSchema]).validate_python(result)
