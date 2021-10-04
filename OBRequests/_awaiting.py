from typing import TYPE_CHECKING
from httpx import Response
from inspect import isawaitable

from ._blocking import _BlockingRequestHandler
from ._defaults import METHOD_DICT


if TYPE_CHECKING:
    from . import OBRequests
    from ._types import METHOD_RESPONSES


class _AwaitingRequestHandler(_BlockingRequestHandler):
    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: "METHOD_RESPONSES" = METHOD_DICT,
                 method_path_params: dict = METHOD_DICT,
                 method_kwargs: dict = METHOD_DICT
                 ) -> None:
        super().__init__(
            upper, path, method_response,
            method_path_params, method_kwargs
        )

    async def _handle(self, resp: Response, method: str):
        func = super()._handle(resp, method, True)
        if isawaitable(func):
            return await func
        else:
            return func

    async def post(self, **kwargs):
        """Makes a POST request to the API endpoint
        """
        resp, method = self._make_post(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def get(self, **kwargs):
        """Makes a GET request to the API endpoint
        """
        resp, method = self._make_get(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def head(self, **kwargs):
        """Makes a HEAD request to the API endpoint
        """
        resp, method = self._make_head(**kwargs)
        return await self._handle(
            resp, method
        )

    async def delete(self, **kwargs):
        """Makes a DELETE request to the API endpoint
        """
        resp, method = self._make_delete(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def put(self, **kwargs):
        """Makes a PUT request to the API endpoint
        """
        resp, method = self._make_put(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def patch(self, **kwargs):
        """Makes a PATCH request to the API endpoint
        """
        resp, method = self._make_patch(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )
