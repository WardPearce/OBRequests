from .method import Get, Post, Head, Options, \
    Put, Patch, Delete

from .response import Json, Read

from .exceptions import InvalidMethod, InvalidResponse


class Methods:
    _client = None

    _get_method = None
    _post_method = None
    _head_method = None
    _options_method = None
    _put_method = None
    _patch_method = None
    _delete_method = None

    def __init__(self, prefix: str, methods: list):
        self.prefix = prefix

        for method in methods:
            if isinstance(method, Get):
                self._get_method = method
                self.get = self._get
            elif isinstance(method, Post):
                self._post_method = method
                self.post = self._post
            elif isinstance(method, Head):
                self._head_method = method
                self.head = self._head
            elif isinstance(method, Options):
                self._options_method = method
                self.options = self._options
            elif isinstance(method, Put):
                self._put_method = method
                self.put = self._put
            elif isinstance(method, Patch):
                self._patch_method = method
                self.patch = self._patch
            elif isinstance(method, Delete):
                self._delete_method = method
                self.delete = self.delete
            else:
                raise InvalidMethod()

    def _determine(self, request, method, kwargs):
        """ Determines the correct response
            or exception to raise.
        """

        additional_params = {}
        path_params = {}
        for name, value in kwargs.items():
            if name.startswith("_"):
                path_params[name[1:]] = value
            else:
                additional_params[name] = value

        if path_params:
            route = self.prefix.format(**path_params)
        else:
            route = self.prefix

        if additional_params:
            resp = request(
                route,
                **{**method.kwargs, **additional_params}
            )
        else:
            resp = request(
                route,
                **method.kwargs
            )

        if method._resp_actions and \
                resp.status_code in method._resp_actions:
            if method._resp_actions[
                resp.status_code
            ] == Json:
                return resp.json()
            elif method._resp_actions[
                resp.status_code
            ] == Read:
                return resp.read()
            else:
                raise InvalidResponse()
        elif method._resp_exceptions and \
                resp.status_code in method._resp_exceptions:
            raise method._resp_exceptions[resp.status_code]()
        elif method._resp_functions and \
                resp.status_code in method._resp_functions:
            return method._resp_functions[resp.status_code].func(
                **method._resp_functions[resp.status_code].kwargs
            )

        return resp

    def _post(self, **kwargs):
        """ Post Request. """

        return self._determine(
            self._client.post,
            self._post_method,
            kwargs
        )

    def _get(self, **kwargs):
        """ Get request. """

        return self._determine(
            self._client.get,
            self._get_method,
            kwargs
        )

    def _head(self, **kwargs):
        """ Head request. """

        return self._determine(
            self._client.head,
            self._get_method,
            kwargs
        )

    def _options(self, **kwargs):
        """ Options request. """

        return self._determine(
            self._client.options,
            self._get_method,
            kwargs
        )

    def _put(self, **kwargs):
        """ Put request. """

        return self._determine(
            self._client.put,
            self._get_method,
            kwargs
        )

    def _patch(self, **kwargs):
        """ Patch request. """

        return self._determine(
            self._client.patch,
            self._get_method,
            kwargs
        )

    def _delete(self, **kwargs):
        """ Delete request. """

        return self._determine(
            self._client.delete,
            self._get_method,
            kwargs
        )
