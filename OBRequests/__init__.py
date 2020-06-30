from httpx import Client

from .exceptions import InvalidMethod

from .requests import Requests


__version__ = "0.0.1"


class OBRequest:
    __client = None

    _base_url = None

    def __init__(self):
        if self._base_url[-1:] != "/":
            self._base_url += "/"

        given_global_params = [
            attr for attr in dir(self.__class__)
            if not callable(getattr(self.__class__, attr))
            and attr.startswith("_")
            and not attr.startswith("__")
            and OBRequest.__name__ not in attr
        ]

        global_params = {}
        for name in given_global_params:
            if name[:1] == "_":
                clean_name = name[1:]
            else:
                clean_name = name

            global_params[
                clean_name
            ] = getattr(
                self,
                name
            )

        self.__client = Client(**global_params)

        routes = [
            attr for attr in dir(self.__class__)
            if not callable(getattr(self.__class__, attr))
            and not attr.startswith("_")
        ]

        for route in routes:
            setattr(
                self,
                route,
                self._determine_methord(
                    route,
                    getattr(
                        self,
                        route
                    )
                )
            )

    def _determine_methord(self, route_name, route):
        if route_name.startswith("POST"):
            return Requests(self.__client, route).post
        elif route_name.startswith("GET"):
            return Requests(self.__client, route).get
        elif route_name.startswith("DELETE"):
            return Requests(self.__client, route).delete
        elif route_name.startswith("PATCH"):
            return Requests(self.__client, route).patch
        elif route_name.startswith("HEAD"):
            return Requests(self.__client, route).head
        elif route_name.startswith("OPTIONS"):
            return Requests(self.__client, route).options
        else:
            raise InvalidMethod()
