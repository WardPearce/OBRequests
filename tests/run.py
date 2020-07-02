from OBRequests import Request, Methods, RespFunction
from OBRequests.method import Get
from OBRequests.response import Json, Read


class FooBar(Exception):
    pass


def test_func(value):
    return value


test = Request(
    "https://jsonplaceholder.typicode.com",
    comment=Methods(
        "comments/{id}",
        [
            Get(
                _id=1,
                _resp_actions={
                    200: Json
                },
                _resp_functions={
                    404: RespFunction(
                        test_func,
                        value="Got 404d"
                    )
                }
            )
        ]
    ),
    posts=Methods(
        "posts",
        [
            Get(
                _resp_actions={
                    200: Read
                },
                _resp_exceptions={
                    404: FooBar
                },
            )
        ]
    )
)

try:
    print(test.comment.get(
        _id=2
    ))
except FooBar:
    print("Worked")
else:
    print(":)")
