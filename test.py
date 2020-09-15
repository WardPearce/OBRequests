from OBRequests import Blocking
from OBRequests.response import Json
from OBRequests.method import Get
from OBRequests.route import Route


json_placeholder = Blocking(
    "https://jsonplaceholder.typicode.com/todos",

    actions={
        200: Json
    },

    __todos=Route(
        "/",
        [
            Get()
        ]
    )
)


print(json_placeholder.todos.get())
