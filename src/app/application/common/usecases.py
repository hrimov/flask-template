from dataclasses import dataclass


@dataclass(frozen=True)
class RequestParameters:
    query: dict
    path: dict


@dataclass(frozen=True)
class UseCaseData:
    params: RequestParameters
    body: dict
