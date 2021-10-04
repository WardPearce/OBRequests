from typing import TYPE_CHECKING, Tuple
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
from ._conditional import ConditionalCallBack
from ._catch_all import AnyStatus
from ._defaults import METHOD_DICT


if TYPE_CHECKING:
    from . import OBRequests
    from ._types import METHOD_RESPONSES


class _BlockingRequestHandler:
    _upper: "OBRequests"

    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: "METHOD_RESPONSES" = METHOD_DICT,
                 method_path_params: dict = METHOD_DICT,
                 method_kwargs: dict = METHOD_DICT
                 ) -> None:
        self._upper = upper
        self._path = path
        self._method_response = method_response
        self._method_path_params = method_path_params
        self._method_kwargs = method_kwargs

    def _request_injects(self, kwargs: dict, method: str) -> dict:
        self._upper._inject_url(kwargs, self._path)

        # Method key should always be in dict
        if self._method_path_params[method]:
            if "path_params" in kwargs:
                kwargs["url"] = str(kwargs["url"]).format_map({
                    **self._method_path_params[method],
                    **kwargs["path_params"]
                })
                kwargs.pop("path_params")
            else:
                kwargs["url"] = str(kwargs["url"]).format_map(
                    self._method_path_params[method]
                )
        elif "path_params" in kwargs:
            kwargs["url"] = str(kwargs["url"]).format_map(
                kwargs["path_params"]
            )
            kwargs.pop("path_params")

        if self._method_kwargs[method]:
            kwargs = {
                **self._method_kwargs[method],
                **kwargs
            }

        return kwargs

    def _make_post(self, **kwargs) -> Tuple[Response, str]:
        method = Post._method
        return self._upper._client.post(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _make_get(self, **kwargs) -> Tuple[Response, str]:
        method = Get._method
        return self._upper._client.get(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _make_head(self, **kwargs) -> Tuple[Response, str]:
        method = Head._method
        return self._upper._client.head(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _make_delete(self, **kwargs) -> Tuple[Response, str]:
        method = Delete._method
        return self._upper._client.delete(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _make_put(self, **kwargs) -> Tuple[Response, str]:
        method = Put._method
        return self._upper._client.put(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _make_patch(self, **kwargs) -> Tuple[Response, str]:
        method = Patch._method
        return self._upper._client.patch(
            **self._request_injects(kwargs, method)
        ), method  # type: ignore

    def _handle(self, resp: Response, method: str, is_awaiting: bool = False):
        # Method key should always be in dict
        if self._method_response[method]:
            responses = {
                **self._upper._root_resp,
                **self._method_response[method]
            }
        else:
            responses = self._upper._root_resp

        if resp.status_code in responses:
            call_back = responses[resp.status_code]
        elif AnyStatus in responses:
            call_back = responses[AnyStatus]
        else:
            raise InvalidResponse(f"{resp.status_code} Client Error: Not Found for url: {resp.url} \nFor more information check: https://httpstatuses.com/{resp.status_code}")  # noqa: E501

        if isinstance(call_back, ConditionalCallBack):
            if is_awaiting:
                call_back = call_back._awaiting
            else:
                call_back = call_back._blocking

        return call_back._func(
            resp=resp,  # type: ignore
            **{**call_back._kwargs, "globals_": self._upper._globals}
        )

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
