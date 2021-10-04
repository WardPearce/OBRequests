from typing import Dict, Union

from ._call_back import CallBack
from ._conditional import ConditionalCallBack


class Method:
    _method: str

    def __init__(self, responses: Dict[int, Union[CallBack, ConditionalCallBack]] = {},  # noqa: E501
                 path_params: dict = {}) -> None:
        """Initialize the method for this request.

        Parameters
        ----------
        responses : Dict[int, Union[CallBack, ConditionalCallBack]], optional
            by default {}
        path_params : dict
            by default {}
        """

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
