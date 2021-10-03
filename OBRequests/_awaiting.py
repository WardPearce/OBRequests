from typing import TYPE_CHECKING, Dict
from httpx import Response
from asyncio import iscoroutinefunction

from ._blocking import _BlockingRequestHandler


if TYPE_CHECKING:
    from . import OBRequests, CallBack


class _AwaitingRequestHandler(_BlockingRequestHandler):
    def __init__(self, upper: "OBRequests", path: str = None,
                 method_response: Dict[str, Dict[int, "CallBack"]] = {}
                 ) -> None:
        super().__init__(upper, path, method_response)

    async def _handle(self, resp: Response, method: str):
        func = super()._handle(resp, method)
        if iscoroutinefunction(func):
            return await func
        else:
            return func

    async def post(self, **kwargs):
        return await self._handle(
            await self._make_post(**kwargs), "POST"  # type: ignore
        )

    async def get(self, **kwargs):
        return await self._handle(
            await self._make_get(**kwargs), "GET"  # type: ignore
        )

    async def head(self, **kwargs):
        return await self._handle(
            await self._make_head(**kwargs), "HEAD"  # type: ignore
        )

    async def delete(self, **kwargs):
        return await self._handle(
            await self._make_delete(**kwargs), "DELETE"  # type: ignore
        )

    async def put(self, **kwargs):
        return await self._handle(
            await self._make_put(**kwargs), "PUT"  # type: ignore
        )

    async def patch(self, **kwargs):
        return await self._handle(
            await self._make_patch(**kwargs), "PATCH"  # type: ignore
        )
