from .method import Get, Post, Head, Options, \
    Put, Patch, Delete

from .response import Json

from .exceptions import InvalidMethod


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

    def _determine(self, request, method):
        """ Determines the correct response
            or exception to raise.
        """

        resp = request(
            self.prefix,
            **method.kwargs
        )

        if resp.status_code in method._resp_actions:
            if method._resp_actions[
                resp.status_code
            ] == Json:
                return resp.json()
        elif resp.status_code in method._resp_exceptions:
            raise method._resp_exceptions[resp.status_code]()

        return resp

    def _post(self):
        """ Post Request. """

        return self._determine(
            self._client.post,
            self._post_method
        )

    def _get(self):
        """ Get request. """

        return self._determine(
            self._client.get,
            self._get_method
        )

    def _head(self):
        """ Head request. """

        return self._determine(
            self._client.head,
            self._get_method
        )

    def _options(self):
        """ Options request. """

        return self._determine(
            self._client.options,
            self._get_method
        )

    def _put(self):
        """ Put request. """

        return self._determine(
            self._client.put,
            self._get_method
        )

    def _patch(self):
        """ Patch request. """

        return self._determine(
            self._client.patch,
            self._get_method
        )

    def _delete(self):
        """ Delete request. """

        return self._determine(
            self._client.delete,
            self._get_method
        )
