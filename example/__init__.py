from .http import Requests, create_http


class JsonPlaceholder:
    _requests: Requests

    def __init__(self, endpoint: str = "https://jsonplaceholder.typicode.com",
                 awaiting: bool = False) -> None:
        self._requests = create_http(
            endpoint, awaiting
        )
