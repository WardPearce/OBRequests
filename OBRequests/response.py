class Json:
    """Json response.
    """

    pass


class Read:
    """Read response.
    """

    pass


class Function:
    """
    Parameters
    ----------
    coro
        Function coroutine to call.
    args
    kwargs
    """

    def __init__(self, coro, *args, **kwargs):
        self.coro = coro
        self.args = args
        self.kwargs = kwargs
