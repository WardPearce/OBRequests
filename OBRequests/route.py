from httpx import AsyncClient, Client

from .exceptions import InvalidMethod
from .method import (
    Get,
    Post,
    Head,
    Options,
    Put,
    Patch,
    Delete
)


class Route:
    def __init__(self, prefix: str,
                 methods: list,
                 actions: dict = None,
                 exceptions: dict = None,
                 functions: dict = None) -> None:

        self.__prefix = prefix
        self.__methods = methods
        self.__actions = actions
        self.__exceptions = exceptions
        self.__functions = functions

    def _process(self, client: (AsyncClient, Client),
                 global_actions: dict, global_exceptions: dict,
                 global_functions: dict) -> None:
        """Processes route.

        Parameters
        ----------
        client : (AsyncClient, Client)
            HTTPX client.
        """

        for method in self.__methods:
            if method.actions is None:
                if self.__actions:
                    method.actions = self.__actions
                else:
                    method.actions = global_actions

            if method.exceptions is None:
                if self.__exceptions:
                    method.exceptions = self.__exceptions
                else:
                    method.exceptions = global_exceptions

            if method.functions is None:
                if self.__functions:
                    method.functions = self.__functions
                else:
                    method.functions = global_functions

            if type(method) != object:
                raise InvalidMethod()

            if isinstance(method, Get):
                pass
            elif isinstance(method, Post):
                pass
            elif isinstance(method, Head):
                pass
            elif isinstance(method, Options):
                pass
            elif isinstance(method, Put):
                pass
            elif isinstance(method, Patch):
                pass
            elif isinstance(method, Delete):
                pass
            else:
                raise InvalidMethod()
