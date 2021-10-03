from typing import Iterable
from httpx import Response


def json(resp: Response, **kwargs) -> dict:
    return resp.json(**kwargs)


def read(resp: Response, **kwargs) -> bytes:
    return resp.read(**kwargs)


def raw(resp: Response, **kwargs) -> Iterable[bytes]:
    return resp.iter_raw(**kwargs)


def response(resp: Response, **kwargs) -> Response:
    return resp


def raise_for_status(resp: Response, **kwargs) -> None:
    resp.raise_for_status()
