from sqlalchemy.orm.session import Session

from src.app.application.user.dto import Users
from src.app.application.user.interfaces import UserGateway
from src.app.persistence.gateways.user import UserGatewayImpl


class ListUsersUseCase:
    # TODO: add pagination and filters
    def __init__(self, session: Session) -> None:
        self.session = session
        self.user_gateway: UserGateway = UserGatewayImpl(session)

    def users_list(self) -> Users:
        users = self.user_gateway.list_users()
        return users
