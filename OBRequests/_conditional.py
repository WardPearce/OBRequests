from ._call_back import CallBack


class ConditionalCallBack:
    def __init__(self, awaiting: CallBack, blocking: CallBack) -> None:
        """Conditional call backs.

        Parameters
        ----------
        awaiting : CallBack
            Ran if set to awaiting
        blocking : CallBack
            Ran if set to blocking
        """
        self._awaiting = awaiting
        self._blocking = blocking
