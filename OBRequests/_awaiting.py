from typing import TYPE_CHECKING, Dict
from httpx import Response
from asyncio import iscoroutinefunction

from ._blocking import _BlockingRequestHandler


if TYPE_CHECKING:
    from . import OBRequests, CallBack


class _AwaitingRequestHandler(_BlockingRequestHandler):
    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: Dict[str, Dict[int, "CallBack"]] = {},
                 method_path_params: dict = {}
                 ) -> None:
        super().__init__(upper, path, method_response, method_path_params)

    async def _handle(self, resp: Response, method: str):
        func = super()._handle(resp, method)
        if iscoroutinefunction(func):
            return await func
        else:
            return func

    async def post(self, **kwargs):
        resp, method = self._make_post(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def get(self, **kwargs):
        resp, method = self._make_get(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def head(self, **kwargs):
        resp, method = self._make_head(**kwargs)
        return await self._handle(
            resp, method
        )

    async def delete(self, **kwargs):
        resp, method = self._make_delete(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def put(self, **kwargs):
        resp, method = self._make_put(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )

    async def patch(self, **kwargs):
        resp, method = self._make_patch(**kwargs)
        return await self._handle(
            await resp,  # type: ignore
            method
        )
