# Index
- [Important Details](#important-details)
- [Hierarchy](#hierarchy)
- [Request](#request)
- [Methods](#methods)
- [Method](#method)
- [Response](#response)
- [RespFunction](#RespFunction)
- [Exceptions](#exceptions)
- [Supported methods](support-methods)

## Important Details
- Pathway parameters always start with a underscore ('_').
- Pathway parameters can only be passed inside methods.
- Methods are defined using a double underscore ('__').
- If a pathway parameter is set as None, it will give a blank string.

## Hierarchy
- Request
    - Any response actions, exceptions & functions here will apply to all methods.
- Methods
    - Any response actions, exceptions & functions here will apply to all Methods defined & overwrite any existing Request  response actions, exceptions or functions already defined.
- Method 
    -  Any response actions, exceptions & functions here will apply to the given method.

## Request
##### Parameters
- base_url: str
    - Base URL for requests.
- resp_actions: dict
    - Dictionary of actions.
- resp_exceptions: dict
    - Dictionary of exceptions to raise.
- resp_functions: dict
    - Dictionary of RespFunction(s).
- awaiting: bool
    - If the async httpx client should be used.
        - If enabled all calls must be awaited within context of the event loop.
- kwargs
    - Pass httpx.Client parameters.
    - Pass routes with a double underscore '__'.

##### Example
```python
from OBRequests import Request, Methods
from OBRequests.method import Get
from OBRequests.response import Json

import asyncio


EXAMPLE = Request(
    "https://jsonplaceholder.typicode.com",
    awaiting=True,
    resp_actions={
        200: Json
    },
    headers={
        "Authorization": "api_key"
    },
    __comments=Methods(
        "comments/{id}",
        [
            Get(
                _id=None
            )
        ],
    ),
)

async def example_async():
    await EXAMPLE.comments.get(_id=1)

loop = asyncio.get_event_loop()
loop.run_until_complete(example_async())
```

## Methods
- prefix: str
    - To prefix the add to the base.
- methods: list
    - List of methods, e.g. get, post etc.
- resp_actions: dict
    - Dictionary of actions.
- resp_exceptions: dict
    - Dictionary of exceptions to raise.
- resp_functions: dict
    - Dictionary of RespFunction(s).


## Method
- resp_actions: dict
    - Dictionary of actions.
- resp_exceptions: dict
    - Dictionary of exceptions to raise.
- resp_functions: dict
    - Dictionary of RespFunction(s).
- kwargs:
    - Different parameters to pass to the request.

## Response
- Json
    - Attempt to read response as json.
- Read
    - Read response.

## RespFunction
- func: coro
    - Function to call.
- awaiting: bool
    - If the function is awaiting, only works for awaiting requests.
- kwargs
    - Parameters to pass.

## Exceptions
```python
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
```

## Supported methods
- Get
- Post
- Head
- Options
- Put
- Patch
- Delete