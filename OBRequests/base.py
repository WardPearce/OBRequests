from httpx import AsyncClient, Client

from .route import Route
from .exceptions import InvalidRoute


class RequestBase:
    def __init__(self, base_url: str,
                 client: (Client, AsyncClient),
                 actions: dict = None,
                 exceptions: dict = None,
                 functions: dict = None,
                 **kwargs) -> None:
        """OBRequest Base.

        Parameters
        ----------
        base_url : str
            Base URL.
        client : (Client, AsyncClient)
            HTTPX client.
        actions : dict, optional
            Actions to call at status codes, by default None
        exceptions : dict, optional
            Exceptions to rase at status codes, by default None
        functions : dict, optional
            Functions to call at status codes, by default None
        kwargs
            Paramters to phrase.
        """

        if base_url[:-1] != "/":
            base_url += "/"

        client_params = {}
        for name, value in kwargs.items():
            if name.startswith("_") and not name.startswith("__"):
                client_params[name] = value

        init_client = client(
            base_url=base_url,
            **client_params
        )

        for name, value in kwargs.items():
            if name.startswith("__"):
                if type(value) == object and isinstance(value, Route):
                    value._process(
                        init_client,
                        actions,
                        exceptions,
                        functions
                    )

                    setattr(
                        self,
                        name[2:],
                        value
                    )
                else:
                    raise InvalidRoute()
