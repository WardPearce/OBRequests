from typing import Any, Callable
from httpx import Response


class CallBack:
    def __init__(self, func: Callable[[Response], Any], **kwargs) -> None:
        """Initialize the method to be called after the request is executed .

        Parameters
        ----------
        func : Callable[[Response], Any]
        """

        self._func = func
        self._kwargs = kwargs
