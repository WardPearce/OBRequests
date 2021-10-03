from typing import Dict

from ._call_back import CallBack


class Method:
    _method: str

    def __init__(self, responses: Dict[int, CallBack] = {},
                 path_params: dict = {}) -> None:
        self._responses = responses
        self._path_params = path_params


class Get(Method):
    """GET method
    """
    _method = "GET"


class Post(Method):
    """DELETE method
    """
    _method = "POST"


class Head(Method):
    """HEAD method
    """
    _method = "HEAD"


class Delete(Method):
    """DELETE method
    """
    _method = "DELETE"


class Put(Method):
    """PUT method
    """
    _method = "PUT"


class Patch(Method):
    """PATCH method
    """
    _method = "PATCH"
