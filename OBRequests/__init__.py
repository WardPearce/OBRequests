from typing import TYPE_CHECKING, Awaitable, Callable, Union
from httpx import (
    Response, AsyncClient, Client, codes,
    BasicAuth, Timeout, DigestAuth, Cookies
)

from httpx._exceptions import (
    CloseError,
    ConnectError,
    ConnectTimeout,
    CookieConflict,
    DecodingError,
    HTTPError,
    HTTPStatusError,
    InvalidURL,
    LocalProtocolError,
    NetworkError,
    PoolTimeout,
    ProtocolError,
    ProxyError,
    ReadError,
    ReadTimeout,
    RemoteProtocolError,
    RequestError,
    RequestNotRead,
    ResponseNotRead,
    StreamClosed,
    StreamConsumed,
    StreamError,
    TimeoutException,
    TooManyRedirects,
    TransportError,
    UnsupportedProtocol,
    WriteError,
    WriteTimeout,
)

from ._defined import json, read, response, raise_for_status
from ._awaiting import _AwaitingRequestHandler
from ._blocking import _BlockingRequestHandler
from ._call_back import CallBack
from ._route import Route
from ._errors import InvalidResponse
from ._conditional import ConditionalCallBack
from ._catch_all import AnyStatus
from ._methods import (
    Post,
    Get,
    Head,
    Delete,
    Put,
    Patch
)

if TYPE_CHECKING:
    from ._types import RESPONSES


__all__ = [
    "Response",
    "OBRequests",
    "CallBack",
    "Route",

    "BasicAuth",
    "DigestAuth",
    "Cookies",
    "codes",
    "Timeout",
    "AnyStatus",
    "ConditionalCallBack",

    "json",
    "read",
    "raise_for_status",
    "response",

    "Post",
    "Get",
    "Head",
    "Delete",
    "Put",
    "Patch",

    "CloseError",
    "ConnectError",
    "ConnectTimeout",
    "CookieConflict",
    "DecodingError",
    "HTTPError",
    "HTTPStatusError",
    "InvalidURL",
    "LocalProtocolError",
    "NetworkError",
    "PoolTimeout",
    "ProtocolError",
    "ProxyError",
    "ReadError",
    "ReadTimeout",
    "RemoteProtocolError",
    "RequestError",
    "RequestNotRead",
    "Response",
    "ResponseNotRead",
    "StreamClosed",
    "StreamConsumed",
    "StreamError",
    "TimeoutException",
    "TooManyRedirects",
    "TransportError",
    "UnsupportedProtocol",
    "WriteError",
    "WriteTimeout",

    "InvalidResponse"
]

__version__ = "2.0.1"
__url__ = "https://obrequests.readthedocs.io/en/latest/"
__description__ = "Modern typed requests for Python 3 built on-top of HTTPX"
__author__ = "WardPearce"
__author_email__ = "wardpearce@pm.me"
__license__ = "GNU General Public License v3.0"


class OBRequests:
    """
    Attributes
    ----------
    close_: Callable[[], Awaitable]
        Used to close any underlying sessions.
    base_: Union[_BlockingRequestHandler, _AwaitingRequestHandler]
        Interact with the base of the client.
    """

    close_: Callable[[], Awaitable]
    _root_resp: "RESPONSES"
    _globals: dict
    base_: Union[_BlockingRequestHandler, _AwaitingRequestHandler]

    def __init__(self, base_url: str,
                 responses: "RESPONSES" = {},
                 globals_: dict = {}, awaiting: bool = False, **kwargs
                 ) -> None:
        """This method is called to create a new client .

        Parameters
        ----------
        base_url : URLTypes
        responses : "RESPONSES", optional
            by default {}
        awaiting : bool, optional
            If client should be async or not by default False
        globals_ : dict, optional
            Globals vars to be passed to every callback.
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

        for key in dir(self):
            if not key.startswith("_") and not key.endswith("_"):
                value: Route = getattr(self, key)

                assert isinstance(
                    value, Route
                ), f"{key} must be type 'Route'"

                setattr(
                    self,
                    key,
                    handler(
                        self,
                        value._path,
                        value._method_response,
                        value._method_path_params,
                        value._method_kwargs
                    )
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
        self._globals = globals_

        self.base_ = handler(self)

        if awaiting:
            setattr(self, "close_", self.__aclose)
        else:
            setattr(self, "close_", self.__close)

    def __enter__(self):
        return self

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close_()

    def __close(self) -> None:
        self._client.close()  # type: ignore

    async def __aclose(self) -> None:
        await self._client.aclose()  # type: ignore

    def _inject_url(self, kwargs, path: str = None) -> None:
        if "url" not in kwargs:
            if path:
                kwargs["url"] = str(self._client.base_url) + path
            else:
                kwargs["url"] = self._client.base_url
