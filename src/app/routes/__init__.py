from flask import Flask

from .user import user_blueprint


def register(app: Flask) -> None:
    app.register_blueprint(user_blueprint)

