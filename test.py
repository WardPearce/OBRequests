from OBRequests import Blocking
from OBRequests.response import Json, Function
from OBRequests.method import Get
from OBRequests.route import Route


json_placeholder = Blocking(
    "https://jsonplaceholder.typicode.com",

    actions={
        200: Json,
        404: Function(lambda: 404)
    },

    __todos=Route(
        "todos/{id}",
        [
            Get()
        ]
    ),
    __notfound=Route(
        "404",
        [
            Get()
        ]
    )
)

print(json_placeholder.todos.get(_id=1))

response = json_placeholder.notfound.get()
print(response == 404)

json_placeholder._close()
