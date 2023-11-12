import json

from flask import Blueprint, g

from src.app.controllers.users import UserController

user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/")
def list_users():
    session = g.session
    users_list = UserController(session).list_users()
    return json.dumps(
        {"result": users_list}
    )
