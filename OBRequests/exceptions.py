class OBRequestsException(Exception):
    """Base exception.
    """

    pass


class InvalidRoute(OBRequestsException):
    """Raised when route isn't a route object.
    """

    pass


class InvalidMethod(OBRequestsException):
    """Raised when method is invalid
    """

    pass


class InvalidResponse(OBRequestsException):
    """ Raised when OBRequests doesn't
        Understand the response object.
    """

    pass
