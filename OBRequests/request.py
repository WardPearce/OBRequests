import httpx


class Request:
    def __init__(self, base_url: str,
                 resp_actions: dict = None,
                 resp_exceptions: dict = None,
                 resp_functions: dict = None,
                 awaiting: bool = False,
                 **kwargs) -> None:
        """ Request wrapper.

            base_url: str
                Base url for requests.
                base_url will always end in a '/' slash.
            kwargs:
                Methods to create.

                Any kwargs will be treated as a httpx.Client parameter.
                https://www.python-httpx.org/api/#client

            resp_actions: dict
                Global response actions.
            resp_exceptions: dict
                Global response exceptions.
            resp_functions: dict
                Global functions.
        """

        # Adds '/' to end of base
        # url if missing.
        if base_url[:-1] != "/":
            base_url += "/"

        # Getting client parameters.
        client_params = {}
        for name, value in kwargs.items():
            if not name.startswith("_") and not name.startswith("__"):
                client_params[name] = value

        # Determining what httpx client to use.
        if not awaiting:
            async_client = None
            client = httpx.Client(
                base_url=base_url,
                **client_params
            )
        else:
            async_client = httpx.AsyncClient(
                base_url=base_url,
                **client_params
            )
            client = None

        # Sets variables need for requests.
        for name, value in kwargs.items():
            if name.startswith("__"):
                # Passing the client to the method.
                value._async_client = async_client
                value._client = client

                # Determining if the global parameters
                # show be set.
                if resp_actions:
                    value._global_resp_actions = resp_actions

                if resp_exceptions:
                    value._global_resp_exceptions = resp_exceptions

                if resp_functions:
                    value._global_resp_functions = resp_functions

                # Processing passed parameters.
                value._process()

                # Setting attribute.
                setattr(
                    self,
                    name[2:],
                    value
                )
