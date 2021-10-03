from typing import Any, Callable
from httpx import Response


class CallBack:
    def __init__(self, func: Callable[[Response], Any], **kwargs) -> None:
        self._func = func
        self._kwargs = kwargs
