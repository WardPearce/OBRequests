class InvalidResponse(BaseException):
    """Response code doesn't match any typed responses
    """
    def __init__(self, message: str) -> None:
        super().__init__(message)
