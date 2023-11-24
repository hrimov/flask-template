from src.app.application.user import dto
from src.app.infrastructure.database import models


def convert_user_model_to_dto(user: models.User) -> dto.User:
    return dto.User(
        id=user.id,
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )


def convert_user_dto_to_model(user: dto.User | dto.UserCreate) -> models.User:
    return models.User(
        username=user.username,
        first_name=user.first_name,
        last_name=user.last_name,
    )
