from typing import List, Dict

from ._call_back import CallBack
from ._methods import Method


class Route:
    def __init__(self, path: str, methods: List[Method] = [],
                 responses: Dict[int, CallBack] = {},
                 path_params: dict = {}) -> None:
        if path[0] == "/":
            path = path[1:]

        self._path = path

        # TODO: NEED TO ADD GLOBAL ROUTE RESPONSE / METHODS

        self._method_response = {}
        self._method_path_params = {}
        for method in methods:
            self._method_response[method._method] = {
                **responses,
                **method._responses
            }

            self._method_path_params[method._method] = {
                **path_params,
                **method._path_params
            }
