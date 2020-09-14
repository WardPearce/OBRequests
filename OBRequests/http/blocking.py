import typing

from .base import HTTPBase


class HTTPBlocking(HTTPBase):
    def _get(self, *args, **kwargs) -> typing.Any:
        pass

    def _post(self, *args, **kwargs) -> typing.Any:
        pass

    def _head(self, *args, **kwargs) -> typing.Any:
        pass

    def _options(self, *args, **kwargs) -> typing.Any:
        pass

    def _put(self, *args, **kwargs) -> typing.Any:
        pass

    def _patch(self, *args, **kwargs) -> typing.Any:
        pass

    def _delete(self, *args, **kwargs) -> typing.Any:
        pass
