class InvalidResponse(BaseException):
    def __init__(self, message: str = "Response code doesn't match any typed responses") -> None:  # noqa: E501
        super().__init__(message)
