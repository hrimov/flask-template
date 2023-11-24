from flask import Flask
from sqlalchemy.orm.session import sessionmaker

from .adaptix import AdaptixMiddleware
from .database import DatabaseMiddleware


def register(app: Flask, session_maker: sessionmaker) -> None:
    AdaptixMiddleware().register(app)
    DatabaseMiddleware(session_maker).register(app)
