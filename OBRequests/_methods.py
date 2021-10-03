from typing import Dict

from ._call_back import CallBack


class Method:
    _method: str

    def __init__(self, responses: Dict[int, CallBack]) -> None:
        self._responses = responses


class Get(Method):
    _method = "GET"


class Post(Method):
    _method = "POST"


class Head(Method):
    _method = "HEAD"


class Delete(Method):
    _method = "DELETE"


class Put(Method):
    _method = "PUT"


class Patch(Method):
    _method = "PATCH"
