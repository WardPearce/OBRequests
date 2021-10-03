from OBRequests import (
    OBRequests,
    Response,
    CallBack,
    Route,
    json,
    Get
)


def custom_response(resp: Response, is_get: bool = False) -> None:
    if is_get:
        print(resp.status_code)
    else:
        raise NotImplementedError()


request = OBRequests(
    responses={
        200: CallBack(json)
    },
    base_url="https://jsonplaceholder.typicode.com",
    posts__=Route(
        "/posts",
        methods=[
            Get(
                responses={
                    200: CallBack(custom_response, is_get=True)
                }
            )
        ]
    )
)


# Prints Status code
request.posts.get()

# Returns phased JSON
request.base.get(url="/posts")
