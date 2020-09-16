import typing

from .base import HTTPBase


class HTTPBlocking(HTTPBase):
    def __request(self, request, **kwargs):
        additional_params, route = self._format(**kwargs)
        return self._response(
            request(route, **additional_params)
        )

    def _get(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.get,
            **kwargs
        )

    def _post(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.post,
            **kwargs
        )

    def _head(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.head,
            **kwargs
        )

    def _options(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.options,
            **kwargs
        )

    def _put(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.put,
            **kwargs
        )

    def _patch(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.patch,
            **kwargs
        )

    def _delete(self, **kwargs) -> typing.Any:
        return self.__request(
            self._client.delete,
            **kwargs
        )
