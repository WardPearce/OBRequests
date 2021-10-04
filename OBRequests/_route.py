from typing import TYPE_CHECKING, List

from ._methods import Method
from ._defaults import METHODS
from ._awaiting import _BlockingRequestHandler

if TYPE_CHECKING:
    from ._types import RESPONSES


class Route(_BlockingRequestHandler):  # Inherits for notaion
    def __init__(self, path: str, methods: List[Method] = [],
                 responses: "RESPONSES" = {},
                 path_params: dict = {}, **kwargs) -> None:
        """Route

        Parameters
        ----------
        path : str
        methods : List[Method], optional
            by default []
        responses : "RESPONSES", optional
            by default {}
        path_params : dict, optional
            by default {}
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
        if path[0] == "/":
            path = path[1:]

        self._path = path

        self._method_response = {}
        self._method_path_params = {}
        self._method_kwargs = {}

        # Preloading Route responses & path_params to all methods
        for method in METHODS:
            self._method_response[method] = responses
            self._method_path_params[method] = path_params
            self._method_kwargs[method] = kwargs

        # Overwriting responses & path_params from Method
        for method in methods:
            self._method_response[method._method] = {
                **self._method_response[method._method],
                **method._responses
            }

            self._method_path_params[method._method] = {
                **self._method_path_params[method._method],
                **method._path_params
            }

            self._method_kwargs[method._method] = {
                **self._method_kwargs[method._method],
                **method._kwargs
            }
