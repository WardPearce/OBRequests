class InvalidMethod(Exception):
    """ Raised when the given method
        Isn't understood by OBRequests.
    """

    pass


class InvalidResponse(Exception):
    """ Raised when OBRequests doesn't
        Understand the response object.
    """

    pass
