from OBRequests import (
    OBRequests,
    Response,
    CallBack,
    Route,
    Get,
    json,
    raise_for_status,
    HTTPStatusError
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
        "/post",
        responses={
            404: CallBack(raise_for_status)
        },
        methods=[
            Get(
                responses={
                    200: CallBack(custom_response, is_get=True)
                }
            ),
        ]
    )
)


try:
    request.posts.get()
except HTTPStatusError as error:
    print(error)

# Returns phased JSON
request.base.get(url="/posts")
