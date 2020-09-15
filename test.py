from OBRequests import Blocking
from OBRequests.response import Json, Function
from OBRequests.method import Get
from OBRequests.route import Route


class Error(Exception):
    pass


json_placeholder = Blocking(
    "https://jsonplaceholder.typicode.com",

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
                    404: Error
                },
            )
        ]
    )
)

print(json_placeholder.todos.get(_id=1))

response = json_placeholder.notfound.get()
print(response == 404)

try:
    json_placeholder.exception.get()
except Error:
    print(Error)

json_placeholder._close()
