class InvalidRoute(Exception):
    """Raised when route isn't a route object.
    """

    pass


class InvalidMethod(Exception):
    """Raised when method is invalid
    """

    pass


class InvalidResponse(Exception):
    """ Raised when OBRequests doesn't
        Understand the response object.
    """

    pass
