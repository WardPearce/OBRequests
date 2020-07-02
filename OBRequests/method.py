class MethodModel:
    def __init__(self, _resp_actions=None, _resp_exceptions=None,
                 _resp_functions=None, **kwargs):
        self._resp_actions = _resp_actions
        self._resp_exceptions = _resp_exceptions
        self._resp_functions = _resp_functions
        self.kwargs = kwargs


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
