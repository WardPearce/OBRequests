class AnyStatus:
    """Used as a catch all for any status not defined.
    """
    def __init__(self) -> None:
        assert False, "'AnyStatus' shouldn't be initialized"
