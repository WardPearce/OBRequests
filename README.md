# Object-Based Requests
Object-Based Requests reinvents the wheel around how HTTP requests are interfaced by developers, its built around reusability & static typing.

## Index
- [Install](#install)
- [Docs](#docs)
- [Features](#features)
- [Example](#example)
    - [Project example](/example)
- [Thanks to](#thanks-to)

## Install
`pip3 install OBRequests>=2.0.0`

## Docs
[obrequests.readthedocs.io](https://obrequests.readthedocs.io/en/latest/)

## Features
- Unique route typing
- Documented
- Supports sync & async with a flick of a boolean
- Built on top of [HTTPX](https://github.com/encode/httpx) for stability and security.
    - Supports all the amazing [features](https://github.com/encode/httpx#features) of HTTPX

## Example
```py
from OBRequests import (
    OBRequests, Response, CallBack, Route,
    Get, json, raise_for_status,
    HTTPStatusError, AnyStatus, BasicAuth
)


def custom_response(resp: Response, is_get: bool = False,
                    **kwargs) -> None:
    if is_get:
        print(resp.status_code)
    else:
        raise NotImplementedError()


class Requests(OBRequests):
    posts_route = Route(
        "/posts/{post_id}",
        responses={
            AnyStatus: CallBack(raise_for_status)
        },
        path_params={
            "post_id": "404_error"
        },
        methods=[
            Get(
                responses={
                    200: CallBack(custom_response, is_get=True),
                    201: ConditionalCallBack(
                        awaiting=CallBack(custom_response, is_get=True),
                        blocking=CallBack(custom_response, is_get=False)
                    )
                },
                auth=BasicAuth("different", "password")
            ),
        ],
        auth=BasicAuth("username", "password")
    )


request = Requests(
    responses={
        200: CallBack(json)
    },
    base_url="https://jsonplaceholder.typicode.com",
    awaiting=False,
    globals_={
        "example": True
    }
)

try:
    request.posts_route.get()
    # The same as
    request.base_.get(url="/posts")
except HTTPStatusError as error:
    print(error)

# Prints status code
request.posts_route.get(path_params={
    "post_id": 1
})


# Only needed for async
request.close_()
```

## Thanks to
- [HTTPX](https://github.com/encode/httpx)
