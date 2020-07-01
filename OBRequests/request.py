import httpx


class Request:
    def __init__(self, base_url: str, **kwargs):

        if base_url[:-1] != "/":
            base_url += "/"

        client_params = {}
        for name, value in kwargs.items():
            if name.startswith("_"):
                client_params[name[1:]] = value

        client = httpx.Client(base_url=base_url, **client_params)

        for name, value in kwargs.items():
            if not name.startswith("_"):
                value._client = client

                setattr(
                    self,
                    name,
                    value
                )
