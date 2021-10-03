from typing import List, Dict

from ._call_back import CallBack
from ._methods import (
    Method,
    Get,
    Post,
    Head,
    Delete,
    Put,
    Patch
)


class Route:
    def __init__(self, path: str, methods: List[Method] = [],
                 responses: Dict[int, CallBack] = {},
                 path_params: dict = {}) -> None:
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
