from httpx import Client, AsyncClient, Response
from typing import Any, Tuple

from ..response import Json, Read, Function
from ..exceptions import InvalidResponse
from ..method import MethodBase


class HTTPBase:
    def __init__(self, base_url: str,
                 client: Tuple[Client, AsyncClient],
                 actions: dict,
                 prefix: str,
                 method: MethodBase) -> None:

        self.actions = actions
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
            elif isinstance(
                    self.actions[response.status_code], Function):
                func = self.actions[response.status_code]
                return func.coro(*func.args, **func.kwargs)
            elif issubclass(self.actions[response.status_code], Exception):
                raise self.actions[response.status_code]()
            else:
                raise InvalidResponse()

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
