from httpx import AsyncClient, Client

from .base import RequestBase


__version__ = "1.0.0"
__url__ = "https://OBRequests.readthedocs.io/en/latest/"
__description__ = "About Object-based request library, built on top of HTTPX."
__author__ = "WardPearce"
__author_email__ = "wardpearce@protonmail.com"
__license__ = "GPL v3"


class Awaiting(RequestBase):
    def __init__(self, *args, **kwargs) -> None:
        """Used for awaiting requests.

        Parameters
        ----------
        base_url : str
            Base URL.
        actions : dict, optional
            Actions to call at status codes, by default None
        exceptions : dict, optional
            Exceptions to rase at status codes, by default None
        functions : dict, optional
            Functions to call at status codes, by default None
        kwargs
            Paramters to phrase.
        """

        super().__init__(
            AsyncClient,
            *args,
            **kwargs
        )

    async def close(self) -> None:
        """Closes sessions.
        """

        await self.init_client.aclose()


class Blocking(RequestBase):
    def __init__(self, *args, **kwargs) -> None:
        """Used for blocking requests.

        Parameters
        ----------
        base_url : str
            Base URL.
        actions : dict, optional
            Actions to call at status codes, by default None
        exceptions : dict, optional
            Exceptions to rase at status codes, by default None
        functions : dict, optional
            Functions to call at status codes, by default None
        kwargs
            Paramters to phrase.
        """

        super().__init__(
            Client,
            *args,
            **kwargs
        )

    def close(self) -> None:
        """Closes sessions.
        """

        self.init_client.close()
