from typing import TYPE_CHECKING
from httpx import Response
from asyncio import iscoroutinefunction

from ._blocking import _BlockingRequestHandler


if TYPE_CHECKING:
    from . import OBRequests


class _AwaitingRequestHandler(_BlockingRequestHandler):
    def __init__(self, upper: "OBRequests") -> None:
        super().__init__(upper)

    async def _handle(self, resp: Response):
        func = super()._handle(resp)
        if iscoroutinefunction(func):
            return await func
        else:
            return func

    async def post(self, **kwargs):
        return await self._handle(
            await self._make_post(**kwargs)  # type: ignore
        )

    async def get(self, **kwargs):
        return await self._handle(
            await self._make_get(**kwargs)  # type: ignore
        )

    async def head(self, **kwargs):
        return await self._handle(
            await self._make_head(**kwargs)  # type: ignore
        )

    async def delete(self, **kwargs):
        return await self._handle(
            await self._make_delete(**kwargs)  # type: ignore
        )

    async def put(self, **kwargs):
        return await self._handle(
            await self._make_put(**kwargs)  # type: ignore
        )

    async def patch(self, **kwargs):
        return await self._handle(
            await self._make_patch(**kwargs)  # type: ignore
        )
