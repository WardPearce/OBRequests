import typing

from .base import HTTPBase


class HTTPAwaiting(HTTPBase):
    async def _get(self, *args, **kwargs) -> typing.Any:
        pass

    async def _post(self, *args, **kwargs) -> typing.Any:
        pass

    async def _head(self, *args, **kwargs) -> typing.Any:
        pass

    async def _options(self, *args, **kwargs) -> typing.Any:
        pass

    async def _put(self, *args, **kwargs) -> typing.Any:
        pass

    async def _patch(self, *args, **kwargs) -> typing.Any:
        pass

    async def _delete(self, *args, **kwargs) -> typing.Any:
        pass
