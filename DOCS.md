# Index
- [Hierarchy](#hierarchy)
- [Request](#request)
- [Methods](#methods)
- [Response](#response)

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
- kwargs
    - Pass httpx.Client parameters.
    - Pass routes with a double underscore '__'.

##### Example
```python
from OBRequests import Request, Methods
from OBRequests.method import Get
from OBRequests.response import Json


EXAMPLE = Request(
    "https://jsonplaceholder.typicode.com",
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
                _id=""
            )
        ],
    ),
)

EXAMPLE.comments.get(_id=1)
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

## Response
- Json
    - Attempt to read response as json.
- Read
    - Read response.
