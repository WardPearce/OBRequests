from ..response import Json, Read, Function
from ..method import Get, Post
from ..route import Route
from .exception import TestException


BASE_URL = "https://jsonplaceholder.typicode.com"
CLIENT_PARAMS = dict(
    base_url=BASE_URL,
    actions={
        200: Json,
        404: Function(lambda: 404)
    },

    __todos=Route(
        "todos/{id}",
        [
            Get(_id=None)
        ]
    ),
    __posts=Route(
        "posts",
        [
            Post()
        ],
        actions={
            201: Json
        }
    ),
    __notfound=Route(
        "404",
        [
            Get()
        ]
    ),
    __exception=Route(
        "error",
        [
            Get(
                actions={
                    404: TestException
                }
            )
        ]
    ),
    __read=Route(
        "",
        [
            Get(
                actions={
                    200: Read
                }
            )
        ]
    )
)
