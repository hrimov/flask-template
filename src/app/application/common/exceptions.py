from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=False)
class ApplicationException(Exception):
    status: ClassVar[int] = 500

    @property
    def title(self) -> str:
        return "An application error occurred"


class GatewayException(ApplicationException):
    pass


class ValidationException(ApplicationException):
    pass
