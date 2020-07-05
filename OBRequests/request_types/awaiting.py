from ..response import Json, Read

from ..exceptions import InvalidResponse

from .base import RequestsBase


class AwaitingRequests(RequestsBase):
    async def _determine(self, request, method, kwargs):
        """ Determines the correct response
            or exception to raise.
        """

        additional_params, route = self._format_route(kwargs, method)

        if additional_params:
            resp = await request(
                route,
                **{**method.kwargs, **additional_params}
            )
        else:
            resp = await request(
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
            if method.resp_functions[resp.status_code].awaiting:
                return await method.resp_functions[resp.status_code].func(
                    **method.resp_functions[resp.status_code].kwargs
                )
            else:
                return method.resp_functions[resp.status_code].func(
                    **method.resp_functions[resp.status_code].kwargs
                )

        return resp

    async def _post(self, **kwargs):
        """ Post Request. """

        return await self._determine(
            self.obj._async_client.post,
            self.obj._post_method,
            kwargs
        )

    async def _get(self, **kwargs):
        """ Get request. """

        return await self._determine(
            self.obj._async_client.get,
            self.obj._get_method,
            kwargs
        )

    async def _head(self, **kwargs):
        """ Head request. """

        return await self._determine(
            self.obj._async_client.head,
            self.obj._get_method,
            kwargs
        )

    async def _options(self, **kwargs):
        """ Options request. """

        return await self._determine(
            self.obj._async_client.options,
            self.obj._get_method,
            kwargs
        )

    async def _put(self, **kwargs):
        """ Put request. """

        return await self._determine(
            self.obj._async_client.put,
            self.obj._get_method,
            kwargs
        )

    async def _patch(self, **kwargs):
        """ Patch request. """

        return await self._determine(
            self.obj._async_client.patch,
            self.obj._get_method,
            kwargs
        )

    async def _delete(self, **kwargs):
        """ Delete request. """

        return await self._determine(
            self.obj._async_client.delete,
            self.obj._get_method,
            kwargs
        )
