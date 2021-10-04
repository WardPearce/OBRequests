from typing import TYPE_CHECKING, List

from ._methods import (
    Method,
    Get,
    Post,
    Head,
    Delete,
    Put,
    Patch
)
from ._awaiting import _BlockingRequestHandler

if TYPE_CHECKING:
    from ._types import RESPONSES


class Route(_BlockingRequestHandler):  # Inherits for notaion
    def __init__(self, path: str, methods: List[Method] = [],
                 responses: "RESPONSES" = {},
                 path_params: dict = {}) -> None:
        """Route

        Parameters
        ----------
        path : str
        methods : List[Method], optional
            by default []
        responses : Dict[
            Union[AnyStatus, int], Union[CallBack, ConditionalCallBack]
        ], optional
            by default {}
        path_params : dict, optional
            by default {}
        """
        if path[0] == "/":
            path = path[1:]

        self._path = path

        self._method_response = {}
        self._method_path_params = {}

        # Preloading Route responses & path_params to all methods
        for method in [Get._method, Post._method, Head._method,
                       Delete._method, Put._method, Patch._method]:
            self._method_response[method] = responses
            self._method_path_params[method] = path_params

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
