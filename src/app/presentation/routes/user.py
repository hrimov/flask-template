import json

from adaptix import Retort
from flask import Blueprint, g, request

from app.application.user.usecases import (
    CreateUserUseCase,
    ListUsersUseCase,
)
from app.application.user.dto import Users


user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/", methods=["GET"])
def list_users():
    adaptix_retort: Retort = g.adaptix_retort
    usecase = ListUsersUseCase(g.session)
    users = usecase.users_list()
    result: dict = adaptix_retort.dump(users, Users)
    return result


@user_blueprint.route("/", methods=["POST"])
def create_user():
    adaptix_retort: Retort = g.adaptix_retort
    usecase = CreateUserUseCase(g.session, request.json)
    user = usecase.create()
    result: dict = adaptix_retort.dump(user)
    return result
