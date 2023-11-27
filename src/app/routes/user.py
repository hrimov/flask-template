from flask import Blueprint, Response, g, request, jsonify
from pydantic import ValidationError

from src.app.controllers.errors import NotFoundError
from src.app.schemas.user import UserCreate, UserUpdate
from src.app.schemas.user import User as UserSchema
from src.app.controllers.users import UserController

user_blueprint = Blueprint("user", __name__, url_prefix="/users")


@user_blueprint.route("/")
def list_users():
    session = g.session
    users_list = UserController(session).list_users()
    return [user.model_dump(mode="json") for user in users_list]


@user_blueprint.route("/", methods=["POST"])
def create_user():
    try:
        data = UserCreate.model_validate(request.get_json())
    except ValidationError:
        return jsonify({"error": "Invalid data"}), 400
    session = g.session
    user = UserController(session).create_user(data)
    return user.model_dump(mode="json"), 201


@user_blueprint.route("/<int:user_id>", methods=["PATCH"])
def change_example(user_id: int):
    try:
        data = UserUpdate.model_validate(request.get_json())
    except ValidationError:
        return jsonify({"error": "Invalid data"}), 400
    session = g.session
    try:
        user = UserController(session).update_user(user_id, data)
    except NotFoundError as e:
        return jsonify({"error": str(e)}), 400
    return user.model_dump(mode="json"), 200
