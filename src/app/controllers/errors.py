class BaseServiceError(Exception):
    pass


class NotFoundError(BaseServiceError):
    pass


class AlreadyExistError(BaseServiceError):
    pass
