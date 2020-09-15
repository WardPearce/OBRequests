import typing

from .base import HTTPBase


class HTTPAwaiting(HTTPBase):
    async def __request(self, request, **kwargs):
        additional_params, route = self._format(**kwargs)
        return self._response(
            await request(route, **additional_params)
        )

    async def _get(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.get,
            **kwargs
        )

    async def _post(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.post,
            **kwargs
        )

    async def _head(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.head,
            **kwargs
        )

    async def _options(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.options,
            **kwargs
        )

    async def _put(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.put,
            **kwargs
        )

    async def _patch(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.patch,
            **kwargs
        )

    async def _delete(self, **kwargs) -> typing.Any:
        return await self.__request(
            self._client.delete,
            **kwargs
        )
