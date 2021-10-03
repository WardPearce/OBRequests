from OBRequests import OBRequests, CallBack, json


request = OBRequests(
    responses={
        200: CallBack(json)
    },
    base_url="https://jsonplaceholder.typicode.com/posts"
)


print(request.create.get())
