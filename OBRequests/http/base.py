from httpx import Client, AsyncClient, Response
from typing import Any

from ..response import Json, Read
from ..exceptions import InvalidResponse
from ..method import MethodBase


class HTTPBase:
    def __init__(self, base_url: str, client: (Client, AsyncClient),
                 actions: dict, exceptions: dict,
                 functions: dict,
                 prefix: str,
                 method: MethodBase) -> None:
        self.actions = actions
        self.exceptions = exceptions
        self.functions = functions
        self.prefix = prefix
        self.method = method
        self.base_url = base_url
        self._client = client

    def _response(self, response: Response) -> Any:
        if self.actions and response.status_code in self.actions:
            if self.actions[response.status_code] == Json:
                return response.json()
            elif self.actions[response.status_code] == Read:
                return response.read()
            else:
                raise InvalidResponse()

        if self.exceptions and response.status_code in self.exceptions:
            raise self.exceptions[response.status_code]()

        if self.functions and response.status_code in self.functions:
            self.functions[response.status_code]()

        return response

    def _format(self, **kwargs) -> dict:
        additional_params = {}
        path_params = {}
        for name, value in kwargs.items():
            if name.startswith("_"):
                path_params[name[1:]] = value if value else ""
            else:
                additional_params[name] = value

        if path_params:
            formatted_route = self.prefix.format(**path_params)
        elif self.method.path_params:
            formatted_route = self.prefix.format(**self.method.path_params)
        else:
            formatted_route = self.prefix

        return additional_params, self.base_url + formatted_route
