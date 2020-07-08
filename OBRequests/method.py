class MethodModel:
    def __init__(self, resp_actions: dict = None,
                 resp_exceptions: dict = None,
                 resp_functions: dict = None, **kwargs) -> None:
        """
        resp_actions: dict
            Dictionary of response actions to do at
            different status codes.
            e.g. {200: Json, 404: Read}.
        resp_exceptions: dict
            Dictionary of response exceptions to
            raise at different status codes.
            e.g. {404: NotImplemented}.
        resp_functions: dict
            Dictionary of response functions to
            call at different status codes.

            resp_functions should have values of
            RespFunction(
                    func,
                    **kwargs
            )

            e.g. {
                200: RespFunction(
                    made_up_func,
                    parameter_name='Name'
                )
            }
        kwargs:
            Different parameters to pass to the request.
        """

        self.resp_actions = resp_actions
        self.resp_exceptions = resp_exceptions
        self.resp_functions = resp_functions

        self.kwargs = {}
        self.path_params = {}

        for name, value in kwargs.items():
            if not name.startswith("_"):
                self.kwargs[name] = value
            else:
                self.path_params[name[1:]] = value


class Get(MethodModel):
    pass


class Post(MethodModel):
    pass


class Head(MethodModel):
    pass


class Options(MethodModel):
    pass


class Put(MethodModel):
    pass


class Patch(MethodModel):
    pass


class Delete(MethodModel):
    pass
