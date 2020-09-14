from httpx import Client, AsyncClient


class HTTPBase:
    def __init__(self, client: (Client, AsyncClient),
                 actions: dict, exceptions: dict,
                 functions: dict) -> None:

        self.actions = actions
        self.exceptions = exceptions
        self.functions = functions
