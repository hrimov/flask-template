from flask import g
from sqlalchemy.orm import Session

from src.app.models.user import User as UserModel
from src.app.controllers.users import UserController
from src.app.schemas.user import User, UserCreate
from tests.conftest import TestBaseClientDBClass
from tests.factory import UserCreationFactory


def create_test_user(session: Session) -> UserModel:
    user_data = UserCreationFactory.build()
    user = UserController(session).create_user(
        creation=user_data
    )
    return user


class TestUsersCreate(TestBaseClientDBClass):

    def test_create(self, app, _a_provide_session):
        user_data: UserCreate = UserCreationFactory.build()
        payload = {
            "username": user_data.username,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name
        }

        response = self.client.post('/users/', json=payload)

        assert response.status_code == 201
        assert response.json()["username"] == payload["username"]


class TestUserUpdate(TestBaseClientDBClass):
    def test_update(self, app, _a_provide_session):
        exist_user = create_test_user(g.session)
        user_data: UserCreate = UserCreationFactory.build()
        payload = {
            "username": exist_user.username,
            "first_name": user_data.first_name,
            "last_name": user_data.last_name
        }

        response = self.client.patch(f'/users/{exist_user.id}', json=payload)
        assert response.json == 'asdasd'
        assert response.status_code == 200
        assert response.json()["username"] == payload["username"]
        assert response.json()["first_name"] == payload["first_name"]
