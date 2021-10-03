from asyncio import get_event_loop
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


async def main() -> None:
    request = OBRequests(
        responses={
            200: CallBack(json)
        },
        base_url="https://jsonplaceholder.typicode.com",
        posts__=Route(
            "/posts/{post_id}",
            responses={
                404: CallBack(raise_for_status)
            },
            path_params={
                "post_id": "404_error"
            },
            methods=[
                Get(
                    responses={
                        200: CallBack(custom_response, is_get=True)
                    },
                ),
            ]
        ),
        awaiting=True
    )

    try:
        await request.posts.get()
    except HTTPStatusError as error:
        print(error)

    # Prints status code
    await request.posts.get(path_params={
        "post_id": 1
    })

    # Returns phased JSON
    await request.base.get(url="/posts")

    await request.close()


loop = get_event_loop()
loop.run_until_complete(main())
