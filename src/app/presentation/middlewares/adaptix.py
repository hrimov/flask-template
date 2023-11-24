from adaptix import Retort
from flask import g, Flask


class AdaptixMiddleware:
    # noinspection PyMethodMayBeStatic
    def create(self):
        g.adaptix_retort = Retort()

    def register(self, app: Flask):
        app.before_request(self.create)
