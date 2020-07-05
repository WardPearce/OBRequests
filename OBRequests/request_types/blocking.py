from ..response import Json, Read

from ..exceptions import InvalidResponse

from .base import RequestsBase


class BlockingRequests(RequestsBase):
    def _determine(self, request, method, kwargs):
        """ Determines the correct response
            or exception to raise.
        """

        additional_params, route = self._format_route(kwargs, method)

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

        if method.resp_actions and \
                resp.status_code in method.resp_actions:
            if method.resp_actions[
                resp.status_code
            ] == Json:
                return resp.json()
            elif method.resp_actions[
                resp.status_code
            ] == Read:
                return resp.read()
            else:
                raise InvalidResponse()
        elif method.resp_exceptions and \
                resp.status_code in method.resp_exceptions:
            raise method.resp_exceptions[resp.status_code]()
        elif method.resp_functions and \
                resp.status_code in method.resp_functions:
            return method.resp_functions[resp.status_code].func(
                **method.resp_functions[resp.status_code].kwargs
            )

        return resp

    def _post(self, **kwargs):
        """ Post Request. """

        return self._determine(
            self.obj._client.post,
            self.obj._post_method,
            kwargs
        )

    def _get(self, **kwargs):
        """ Get request. """

        return self._determine(
            self.obj._client.get,
            self.obj._get_method,
            kwargs
        )

    def _head(self, **kwargs):
        """ Head request. """

        return self._determine(
            self.obj._client.head,
            self.obj._get_method,
            kwargs
        )

    def _options(self, **kwargs):
        """ Options request. """

        return self._determine(
            self.obj._client.options,
            self.obj._get_method,
            kwargs
        )

    def _put(self, **kwargs):
        """ Put request. """

        return self._determine(
            self.obj._client.put,
            self.obj._get_method,
            kwargs
        )

    def _patch(self, **kwargs):
        """ Patch request. """

        return self._determine(
            self.obj._client.patch,
            self.obj._get_method,
            kwargs
        )

    def _delete(self, **kwargs):
        """ Delete request. """

        return self._determine(
            self.obj._client.delete,
            self.obj._get_method,
            kwargs
        )
