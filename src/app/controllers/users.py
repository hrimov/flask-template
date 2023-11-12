from sqlalchemy import select

from src.app.models.user import User

from .base import Controller


class UserController(Controller[User]):

    # some operations with the user
    def list_users(self):
        stmt = select(User)
        result = self.session.scalars(stmt).all()
        return result
