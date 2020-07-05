class RespFunction:
    def __init__(self, func, awaiting=False, **kwargs):
        """
        func: coro
            Function to call.
        awaiting: bool
            If the function is awaiting, only works
            for awaiting requests.
        kwargs
            Parameters to be called in the function.
        """

        self.func = func
        self.kwargs = kwargs
        self.awaiting = awaiting
