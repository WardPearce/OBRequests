class Requests:
    func_params = {}

    def __init__(self, client, route):
        self.route = route
        self.client = client

    def _format_route(self):
        if self.kwargs:
            route_params = {}

            for key, param in self.kwargs.items():
                if not key.startswith("_"):
                    self.func_params[key] = param
                else:
                    route_params[
                        key[1:]
                    ] = param

            if route_params:
                self.route = self.route.format(**route_params)

        return self.route

    def post(self, **kwargs):
        self.kwargs = kwargs

        return self.client.post(
            self._format_route(),
            **self.func_params
        )

    def get(self, **kwargs):
        self.kwargs = kwargs

        return self.client.get(
            self._format_route(),
            **self.func_params
        )

    def head(self, **kwargs):
        self.kwargs = kwargs

        return self.client.head(
            self._format_route(),
            **self.func_params
        )

    def delete(self, **kwargs):
        self.kwargs = kwargs

        return self.client.delete(
            self._format_route(),
            **self.func_params
        )

    def options(self, **kwargs):
        self.kwargs = kwargs

        return self.client.options(
            self._format_route(),
            **self.func_params
        )

    def patch(self, **kwargs):
        self.kwargs = kwargs

        return self.client.patch(
            self._format_route(),
            **self.func_params
        )
