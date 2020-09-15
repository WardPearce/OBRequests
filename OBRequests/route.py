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
from .http.awaiting import HTTPAwaiting
from .http.blocking import HTTPBlocking


class Route:
    get = None
    post = None
    head = None
    options = None
    put = None
    patch = None
    delete = None

    def __init__(self, prefix: str,
                 methods: list,
                 actions: dict = None,
                 exceptions: dict = None,
                 functions: dict = None) -> None:

        self.prefix = prefix
        self.methods = methods
        self.actions = actions
        self.exceptions = exceptions
        self.functions = functions

    def _process(self, client: (AsyncClient, Client),
                 global_actions: dict, global_exceptions: dict,
                 global_functions: dict) -> None:
        """Processes route.

        Parameters
        ----------
        client : (AsyncClient, Client)
            HTTPX client.
        """

        for method in self.methods:
            if method.actions is None:
                if self.actions:
                    method.actions = self.actions
                else:
                    method.actions = global_actions

            if method.exceptions is None:
                if self.exceptions:
                    method.exceptions = self.exceptions
                else:
                    method.exceptions = global_exceptions

            if method.functions is None:
                if self.functions:
                    method.functions = self.functions
                else:
                    method.functions = global_functions

            if isinstance(client, AsyncClient):
                http = HTTPAwaiting(
                    client,
                    method.actions,
                    method.exceptions,
                    method.functions,
                    self.prefix,
                    method
                )
            else:
                http = HTTPBlocking(
                    client,
                    method.actions,
                    method.exceptions,
                    method.functions,
                    self.prefix,
                    method
                )

            if isinstance(method, Get):
                self.get = http._get
            elif isinstance(method, Post):
                self.post = http._post
            elif isinstance(method, Head):
                self.head = http._head
            elif isinstance(method, Options):
                self.options = http._options
            elif isinstance(method, Put):
                self.put = http._put
            elif isinstance(method, Patch):
                self.patch = http._patch
            elif isinstance(method, Delete):
                self.delete = http._delete
            else:
                raise InvalidMethod()
