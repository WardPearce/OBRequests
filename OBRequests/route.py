from httpx import AsyncClient, Client
from typing import Tuple

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
                 methods: list = None,
                 actions: dict = None) -> None:

        self.prefix = prefix
        self.methods = methods
        self.actions = actions

    def _process(self, base_url: str, client: Tuple[AsyncClient, Client],
                 global_actions: dict) -> None:
        """Processes route.

        Parameters
        ----------
        base_url : str
        client : Tuple[AsyncClient, Client]
        global_actions : dict

        Raises
        ------
        InvalidMethod
        """

        if not self.methods:
            return

        for method in self.methods:
            actions = {}
            if global_actions:
                actions.update(global_actions)

            if self.actions:
                actions.update(self.actions)

            if method.actions:
                actions.update(method.actions)

            if isinstance(client, AsyncClient):
                http = HTTPAwaiting(
                    base_url,
                    client,
                    actions,
                    self.prefix,
                    method
                )
            else:
                http = HTTPBlocking(
                    base_url,
                    client,
                    actions,
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
