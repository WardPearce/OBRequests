from OBRequests import Request, Methods, RespFunction
from OBRequests.method import Get
from OBRequests.response import Json, Read


class FooBar(Exception):
    pass


def test_func(value):
    return value


test = Request(
    "https://jsonplaceholder.typicode.com",
    resp_actions={
        200: Json
    },
    headers={
        "Authorization": "api_key"
    },
    __comment=Methods(
        "comments/{id}",
        [
            Get(
                _id=1,
                resp_functions={
                    404: RespFunction(
                        test_func,
                        value="Got 404d"
                    )
                }
            )
        ],
    ),
    __posts=Methods(
        "posts",
        [
            Get(
                resp_actions={
                    200: Read
                },
                resp_exceptions={
                    404: FooBar
                },
                headers={
                    "Authorization": "Different_key_for_some_reason"
                }
            )
        ]
    )
)

try:
    print(test.comment.get(
        _id=2
    ))
except FooBar:
    print("Some expection")
else:
    print(":)")
