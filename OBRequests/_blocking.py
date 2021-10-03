from typing import TYPE_CHECKING
from httpx import Response

from .errors import InvalidStatusCode


if TYPE_CHECKING:
    from . import OBRequests


class _BlockingRequestHandler:
    _upper: "OBRequests"

    def __init__(self, upper: "OBRequests") -> None:
        self._upper = upper

    def _make_post(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.post(**kwargs)  # type: ignore

    def _make_get(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.get(**kwargs)  # type: ignore

    def _make_head(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.head(**kwargs)  # type: ignore

    def _make_delete(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.delete(**kwargs)  # type: ignore

    def _make_put(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.put(**kwargs)  # type: ignore

    def _make_patch(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs)
        return self._upper._client.patch(**kwargs)  # type: ignore

    def _handle(self, resp: Response):
        if resp.status_code in self._upper._root_resp:
            call_back = self._upper._root_resp[resp.status_code]
            return call_back._func(resp, **call_back._kwargs)
        else:
            raise InvalidStatusCode()

    def post(self, **kwargs):
        return self._handle(
            self._make_post(**kwargs)
        )

    def get(self, **kwargs):
        return self._handle(
            self._make_get(**kwargs)
        )

    def head(self, **kwargs):
        return self._handle(
            self._make_head(**kwargs)
        )

    def delete(self, **kwargs):
        return self._handle(
            self._make_delete(**kwargs)
        )

    def put(self, **kwargs):
        return self._handle(
            self._make_put(**kwargs)
        )

    def patch(self, **kwargs):
        return self._handle(
            self._make_patch(**kwargs)
        )
