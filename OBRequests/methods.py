from .method import Get, Post, Head, Options, \
    Put, Patch, Delete

from .exceptions import InvalidMethod

from .request_types.awaiting import AwaitingRequests
from .request_types.blocking import BlockingRequests


class Methods:
    _methods = None

    _client = None
    _async_client = None

    _get_method = None
    _post_method = None
    _head_method = None
    _options_method = None
    _put_method = None
    _patch_method = None
    _delete_method = None

    _global_resp_actions = None
    _global_resp_exceptions = None
    _global_resp_functions = None

    def __init__(self, prefix: str, methods: list,
                 resp_actions: dict = None,
                 resp_exceptions: dict = None,
                 resp_functions: dict = None) -> None:
        """
        Pass different Methods for a prefix.

        prefix: str
            To prefix the add to the base
            url, e.g. https://.../<prefix goes after this>.
        methods: list
            List of methods, e.g. get, post etc.
        resp_actions: dict
            Method response actions.
        resp_exceptions: dict
            Method response exceptions.
        resp_functions: dict
            Method functions.
        """

        self.methods = methods
        self.prefix = prefix

        self.resp_actions = resp_actions
        self.resp_exceptions = resp_exceptions
        self.resp_functions = resp_functions

    def _process(self) -> None:
        """ Processes all paramters. """

        if self._client:
            request = BlockingRequests(obj=self)
        else:
            request = AwaitingRequests(obj=self)

        for method in self.methods:
            if method.resp_actions is None:
                if self.resp_actions:
                    method.resp_actions = self.resp_actions
                else:
                    method.resp_actions = self._global_resp_actions

            if method.resp_exceptions is None:
                if self.resp_exceptions:
                    method.resp_exceptions = self.resp_exceptions
                else:
                    method.resp_exceptions = self._global_resp_exceptions

            if method.resp_functions is None:
                if self.resp_functions:
                    method.resp_functions = self.resp_functions
                else:
                    method.resp_functions = self._global_resp_functions

            if isinstance(method, Get):
                self._get_method = method
                self.get = request._get
            elif isinstance(method, Post):
                self._post_method = method
                self.post = request._post
            elif isinstance(method, Head):
                self._head_method = method
                self.head = request._head
            elif isinstance(method, Options):
                self._options_method = method
                self.options = request._options
            elif isinstance(method, Put):
                self._put_method = method
                self.put = request._put
            elif isinstance(method, Patch):
                self._patch_method = method
                self.patch = request._patch
            elif isinstance(method, Delete):
                self._delete_method = method
                self.delete = request._delete
            else:
                raise InvalidMethod("""{} isn't a method
                                    what I understand""".format(method))
