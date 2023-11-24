from sqlalchemy.orm.session import Session

from src.app.application.user.dto import UserCreate, User
from src.app.application.user.interfaces import UserGateway
from src.app.persistence.gateways.user import UserGatewayImpl


class CreateUserUseCase:

    def __init__(self, session: Session, raw_data: dict) -> None:
        self.session = session
        self.raw_data = raw_data
        self.user_gateway: UserGateway = UserGatewayImpl(session)

        self.validated_data: dict | None = None
        self.raw_user: UserCreate | None = None

    def validate(self) -> None:
        # here goes any validation
        self.validated_data = self.raw_data

    def prepare(self):
        self.validate()

        self.raw_user = UserCreate(
            self.validated_data["username"],
            self.validated_data["first_name"],
            self.validated_data["last_name"],
        )

    def create(self) -> User:
        self.prepare()
        with self.session.begin():
            user = self.user_gateway.create_user(self.raw_user)
        return user
