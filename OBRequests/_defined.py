from httpx import Response


def json(resp: Response, **kwargs) -> dict:
    kwargs.pop("globals_")
    return resp.json(**kwargs)


def read(resp: Response, **kwargs) -> bytes:
    kwargs.pop("globals_")
    return resp.read(**kwargs)


def response(resp: Response, **kwargs) -> Response:
    return resp


def raise_for_status(resp: Response, **kwargs) -> None:
    resp.raise_for_status()
