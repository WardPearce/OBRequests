from OBRequests import Request, Methods
from OBRequests.method import Get
from OBRequests.response import Json


class FooBar(Exception):
    pass


test = Request(
    "https://jsonplaceholder.typicode.com",
    comment=Methods(
        "comments/{something}",
        [
            Get(
                _resp_actions={
                    200: Json
                },
                _resp_exceptions={
                    404: FooBar
                }
            )
        ]
    ),
    posts=Methods(
        "posts",
        [
            Get(
                _resp_actions={
                    200: Json
                },
                _resp_exceptions={
                    404: FooBar
                },
            )
        ]
    )
)

try:
    print(test.posts.get())
except FooBar:
    print("Worked")
else:
    print(":)")
