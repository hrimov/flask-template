from sqlalchemy.orm.session import Session


class DatabaseGateway:
    def __init__(self, session: Session):
        ...
