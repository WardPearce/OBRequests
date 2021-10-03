from typing import Awaitable, Callable, Dict, Union
from httpx import Response, AsyncClient, Client

from ._defined import json, read, raw, response
from ._awaiting import _AwaitingRequestHandler
from ._blocking import _BlockingRequestHandler
from ._call_back import CallBack

from .errors import InvalidStatusCode


__all__ = [
    "Response",
    "OBRequests",
    "CallBack",

    "json",
    "read",
    "raw",
    "response",

    "InvalidStatusCode"
]


class OBRequests:
    _client: Union[AsyncClient, Client]
    _root_resp: Dict[int, CallBack]
    _is_awaiting: bool

    close: Callable[[], Awaitable]

    def __init__(self, responses: Dict[int, CallBack],
                 awaiting: bool = False, **kwargs) -> None:
        """This method is called to create a new client .

        Parameters
        ----------
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
        base_url : URLTypes, optional
            by default ""
        transport : BaseTransport, optional
            by default None
        app : Callable, optional
            by default None
        trust_env : bool, optional
            by default True
        """

        if awaiting:
            client = AsyncClient
        else:
            client = Client

        self._client = client(**kwargs)
        self._root_resp = responses

        self.create = (
            _AwaitingRequestHandler(self) if awaiting
            else _BlockingRequestHandler(self)
        )

        if awaiting:
            setattr(self, "close", self.__aclose)
        else:
            setattr(self, "close", self.__close)

    def __close(self) -> None:
        self._client.close()  # type: ignore

    async def __aclose(self) -> None:
        await self._client.aclose()  # type: ignore

    def _inject_url(self, kwargs) -> dict:
        if "url" not in kwargs:
            kwargs["url"] = self._client.base_url
        return kwargs
