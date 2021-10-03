from typing import Awaitable, Callable, Dict, Union
from httpx import Response, AsyncClient, Client

from ._defined import json, read, raw, response
from ._awaiting import _AwaitingRequestHandler
from ._blocking import _BlockingRequestHandler
from ._call_back import CallBack
from ._route import Route
from .errors import InvalidStatusCode
from ._methods import (
    Post,
    Get,
    Head,
    Delete,
    Put,
    Patch
)


__all__ = [
    "Response",
    "OBRequests",
    "CallBack",
    "Route",

    "json",
    "read",
    "raw",
    "response",

    "Post",
    "Get",
    "Head",
    "Delete",
    "Put",
    "Patch",

    "InvalidStatusCode"
]


class OBRequests:
    _client: Union[AsyncClient, Client]
    _root_resp: Dict[int, CallBack]
    _is_awaiting: bool

    close: Callable[[], Awaitable]

    def __init__(self, base_url: str, responses: Dict[int, CallBack],
                 awaiting: bool = False, **kwargs) -> None:
        """This method is called to create a new client .

        Parameters
        ----------
        base_url : URLTypes
        responses : Dict[int, Callable[[Response], Any]]
        awaiting : bool, optional
            If client should be async or not by default False
        auth : AuthTypes, optional
            by default None
        params : QueryParamTypes, optional
            by default None
        headers : HeaderTypes, optional
            by default None
        cookies : CookieTypes, optional
            by default None
        verify : VerifyTypes, optional
            by default True
        cert : CertTypes, optional
            by default None
        http1 : bool, optional
            by default True
        http2 : bool, optional
            by default False
        proxies : ProxiesTypes, optional
            by default None
        mounts : Mapping[str, BaseTransport], optional
            by default None
        timeout : TimeoutTypes, optional
            by default ...
        limits : Limits, optional
            by default ...
        max_redirects : int, optional
            by default ...
        event_hooks : Mapping[str, List[Callable]], optional
            by default None
        transport : BaseTransport, optional
            by default None
        app : Callable, optional
            by default None
        trust_env : bool, optional
            by default True
        """

        if not base_url.endswith("/"):
            base_url += "/"

        handler = (
            _AwaitingRequestHandler if awaiting
            else _BlockingRequestHandler
        )

        for key, value in dict(kwargs).items():
            if key.endswith("__"):
                value: Route = value

                kwargs.pop(key)

                setattr(
                    self,
                    key[:-2],
                    handler(self, value._path, value._method_response)
                )

        if awaiting:
            client = AsyncClient
        else:
            client = Client

        self._client = client(
            base_url=base_url,
            **kwargs
        )
        self._root_resp = responses

        self.base = handler(self)

        if awaiting:
            setattr(self, "close", self.__aclose)
        else:
            setattr(self, "close", self.__close)

    def __close(self) -> None:
        self._client.close()  # type: ignore

    async def __aclose(self) -> None:
        await self._client.aclose()  # type: ignore

    def _inject_url(self, kwargs, path: str = None) -> dict:
        if "url" not in kwargs:
            if path:
                kwargs["url"] = str(self._client.base_url) + path
            else:
                kwargs["url"] = self._client.base_url
        return kwargs
