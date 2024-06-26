from flask import Flask

from app import middlewares, routes
from app.infrastructure.config import load_config
from app.infrastructure.log import configure_logging
from app.infrastructure.database.session import create_session_maker


def main() -> Flask:
    config = load_config()
    configure_logging(config.app_config)
    session_maker = create_session_maker(config.db_config.full_url)

    app = Flask(__name__)

    middlewares.register(app, session_maker)
    routes.register(app)

    return app


def run():
    app = main()
    app.run("localhost", 5000)


if __name__ == "__main__":
    run()
