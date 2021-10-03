from typing import List, Dict

from ._call_back import CallBack
from ._methods import Method


class Route:
    def __init__(self, path: str, methods: List[Method] = [],
                 responses: Dict[int, CallBack] = {}) -> None:
        if path[0] == "/":
            path = path[1:]

        self._path = path

        self._method_response = {}
        for method in methods:
            self._method_response[method._method] = {
                **responses,
                **method._responses
            }
