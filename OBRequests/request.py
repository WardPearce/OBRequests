import httpx


class Request:
    def __init__(self, base_url: str,
                 resp_actions: dict = None,
                 resp_exceptions: dict = None,
                 resp_functions: dict = None,
                 **kwargs):
        """ Request wrapper.

            base_url: str
                Base url for requests.
                base_url will always end in a '/' slash.
            kwargs:
                Methods to create.

                Any kwargs will be treated as a httpx.Client parameter.
                https://www.python-httpx.org/api/#client
        """

        if base_url[:-1] != "/":
            base_url += "/"

        client_params = {}
        for name, value in kwargs.items():
            if not name.startswith("_") and not name.startswith("__"):
                client_params[name] = value

        client = httpx.Client(base_url=base_url, **client_params)

        for name, value in kwargs.items():
            if name.startswith("__"):
                value._client = client

                if resp_actions:
                    value._global_resp_actions = resp_actions

                if resp_exceptions:
                    value._global_resp_exceptions = resp_exceptions

                if resp_functions:
                    value._global_resp_functions = resp_functions

                value._process()

                setattr(
                    self,
                    name[2:],
                    value
                )
