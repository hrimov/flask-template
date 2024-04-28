from collections.abc import Callable
from functools import wraps
from typing import Any, Coroutine, ParamSpec, TypeVar

from sqlalchemy.exc import SQLAlchemyError

from app.application.common.exceptions import GatewayException


Param = ParamSpec("Param")
ReturnType = TypeVar("ReturnType")
Func = Callable[Param, ReturnType]


def exception_mapper(
        func: Callable[Param, Callable]
) -> Callable[Param, ReturnType]:
    @wraps(func)
    def wrapped(*args: Param.args, **kwargs: Param.kwargs) -> ReturnType:
        try:
            return func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise GatewayException from err

    return wrapped
