class RespFunction:
    def __init__(self, func, *args, **kwargs):
        """
        func
            Function coroutine to call.
        args
        kwargs
        """

        self.func = func
        self.kwargs = kwargs
