class MethodBase:
    def __init__(self, actions: dict = None,
                 **kwargs) -> None:
        """
        Parameters
        ----------
        actions: dict
        kwargs:
            Different parameters to pass to the request.
        """

        self.actions = actions

        self.kwargs = {}
        self.path_params = {}
        for name, value in kwargs.items():
            if not name.startswith("_"):
                self.kwargs[name] = value
            else:
                self.path_params[name[1:]] = value if value else ""


class Get(MethodBase):
    pass


class Post(MethodBase):
    pass


class Head(MethodBase):
    pass


class Options(MethodBase):
    pass


class Put(MethodBase):
    pass


class Patch(MethodBase):
    pass


class Delete(MethodBase):
    pass
