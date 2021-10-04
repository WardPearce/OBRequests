from typing import TYPE_CHECKING, Dict, Union, Type

if TYPE_CHECKING:
    from . import CallBack, AnyStatus, ConditionalCallBack


RESPONSES = Dict[
    Union[Type["AnyStatus"], int],
    Union["CallBack", "ConditionalCallBack"]
]


METHOD_RESPONSES = Dict[
    str,
    RESPONSES
]
