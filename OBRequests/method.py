class MethodModel:
    def __init__(self, actions: dict = None,
                 exceptions: dict = None,
                 functions: dict = None,
                 **kwargs) -> None:
        """
        actions: dict
        exceptions: dict
        functions: dict
        kwargs:
            Different parameters to pass to the request.
        """

        self.actions = actions
        self.exceptions = exceptions
        self.functions = functions

        self.kwargs = {}
        self.path_params = {}
        for name, value in kwargs.items():
            if not name.startswith("_"):
                self.kwargs[name] = value
            else:
                self.path_params[name[1:]] = value if value else ""


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
