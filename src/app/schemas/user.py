from pydantic import BaseModel, ConfigDict


class UserCreate(BaseModel):

    username: str | None
    first_name: str
    last_name: str


class User(UserCreate):

    id: int

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(UserCreate):
    pass
