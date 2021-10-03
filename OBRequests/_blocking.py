from typing import TYPE_CHECKING, Dict, Tuple
from httpx import Response

from ._errors import InvalidResponse
from ._methods import (
    Post,
    Get,
    Head,
    Delete,
    Put,
    Patch
)


if TYPE_CHECKING:
    from . import OBRequests, CallBack


class _BlockingRequestHandler:
    _upper: "OBRequests"

    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: Dict[str, Dict[int, "CallBack"]] = {},
                 method_path_params: dict = {}
                 ) -> None:
        self._upper = upper
        self._path = path
        self._method_response = method_response
        self._method_path_params = method_path_params

    def _request_injects(self, kwargs: dict, method: str) -> None:
        self._upper._inject_url(kwargs, self._path)

        if method in self._method_path_params:
            if "path_params" in kwargs:
                kwargs["url"] = kwargs["url"].format_map({
                    **self._method_path_params[method],
                    **kwargs["path_params"]
                })
                kwargs.pop("path_params")
            else:
                kwargs["url"] = kwargs["url"].format_map(
                    self._method_path_params[method]
                )
        elif "path_params" in kwargs:
            kwargs["url"] = kwargs["url"].format_map(
                kwargs["path_params"]
            )
            kwargs.pop("path_params")

    def _make_post(self, **kwargs) -> Tuple[Response, str]:
        method = Post._method
        self._request_injects(kwargs, method)
        return self._upper._client.post(**kwargs), method  # type: ignore

    def _make_get(self, **kwargs) -> Tuple[Response, str]:
        method = Get._method
        self._request_injects(kwargs, method)
        return self._upper._client.get(**kwargs), method  # type: ignore

    def _make_head(self, **kwargs) -> Tuple[Response, str]:
        method = Head._method
        self._request_injects(kwargs, method)
        return self._upper._client.head(**kwargs), method  # type: ignore

    def _make_delete(self, **kwargs) -> Tuple[Response, str]:
        method = Delete._method
        self._request_injects(kwargs, method)
        return self._upper._client.delete(**kwargs), method  # type: ignore

    def _make_put(self, **kwargs) -> Tuple[Response, str]:
        method = Put._method
        self._request_injects(kwargs, method)
        return self._upper._client.put(**kwargs), method  # type: ignore

    def _make_patch(self, **kwargs) -> Tuple[Response, str]:
        method = Patch._method
        self._request_injects(kwargs, method)
        return self._upper._client.patch(**kwargs), method  # type: ignore

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
            raise InvalidResponse()

    def post(self, **kwargs):
        """Makes a POST request to the API endpoint
        """
        resp, method = self._make_post(**kwargs)
        return self._handle(
            resp, method
        )

    def get(self, **kwargs):
        """Makes a GET request to the API endpoint
        """
        resp, method = self._make_get(**kwargs)
        return self._handle(
            resp, method
        )

    def head(self, **kwargs):
        """Makes a HEAD request to the API endpoint
        """
        resp, method = self._make_head(**kwargs)
        return self._handle(
            resp, method
        )

    def delete(self, **kwargs):
        """Makes a DELETE request to the API endpoint
        """
        resp, method = self._make_delete(**kwargs)
        return self._handle(
            resp, method
        )

    def put(self, **kwargs):
        """Makes a PUT request to the API endpoint
        """
        resp, method = self._make_put(**kwargs)
        return self._handle(
            resp, method
        )

    def patch(self, **kwargs):
        """Makes a PATCH request to the API endpoint
        """
        resp, method = self._make_patch(**kwargs)
        return self._handle(
            resp, method
        )
