from typing import TYPE_CHECKING, Dict
from httpx import Response

from .errors import InvalidStatusCode


if TYPE_CHECKING:
    from . import OBRequests, CallBack


class _BlockingRequestHandler:
    _upper: "OBRequests"

    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: Dict[str, Dict[int, "CallBack"]] = {}
                 ) -> None:
        self._upper = upper
        self._path = path
        self._method_response = method_response

    def _make_post(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.post(**kwargs)  # type: ignore

    def _make_get(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.get(**kwargs)  # type: ignore

    def _make_head(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.head(**kwargs)  # type: ignore

    def _make_delete(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.delete(**kwargs)  # type: ignore

    def _make_put(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.put(**kwargs)  # type: ignore

    def _make_patch(self, **kwargs) -> Response:
        self._upper._inject_url(kwargs, self._path)
        return self._upper._client.patch(**kwargs)  # type: ignore

    def _handle(self, resp: Response, method: str):
        if method in self._method_response:
            responses = {
                **self._upper._root_resp,
                **self._method_response[method]
            }
        else:
            responses = self._upper._root_resp

        if resp.status_code in responses:
            call_back = responses[resp.status_code]
            return call_back._func(
                resp=resp, **call_back._kwargs  # type: ignore
            )
        else:
            raise InvalidStatusCode()

    def post(self, **kwargs):
        return self._handle(
            self._make_post(**kwargs), "POST"
        )

    def get(self, **kwargs):
        return self._handle(
            self._make_get(**kwargs), "GET"
        )

    def head(self, **kwargs):
        return self._handle(
            self._make_head(**kwargs), "HEAD"
        )

    def delete(self, **kwargs):
        return self._handle(
            self._make_delete(**kwargs), "DELETE"
        )

    def put(self, **kwargs):
        return self._handle(
            self._make_put(**kwargs), "PUT"
        )

    def patch(self, **kwargs):
        return self._handle(
            self._make_patch(**kwargs), "PATCH"
        )
