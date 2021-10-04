from ._methods import (
    Get,
    Post,
    Head,
    Delete,
    Put,
    Patch
)


METHODS = [Get._method, Post._method, Head._method,
           Delete._method, Put._method, Patch._method]


# Used so base requests always have the method defined
METHOD_DICT = {
    method: {} for method in METHODS
}
