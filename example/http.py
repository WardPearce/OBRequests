from OBRequests import (
    OBRequests,
    Route,
    CallBack,
    Get,
    Post,
    Put,
    Patch,
    Delete,
    json,
    raise_for_status,
    codes
)


class Requests(OBRequests):
    posts = Route(
        "/posts/{post_id}",
        methods=[
            Get(
                path_params={
                    "post_id": ""
                },
            ),
            Post(
                path_params={
                    "post_id": ""
                },
                responses={
                    201: CallBack(json)
                }
            ),
            Put(),
            Patch(),
            Delete(
                responses={
                    codes.OK: CallBack(raise_for_status)
                }
            )
        ]
    )

    comments = Route(
        "/posts/{post_id}/comments",
        responses={
            codes.NOT_FOUND: CallBack(raise_for_status)
        },
        methods=[
            Get()
        ]
    )

    albums = Route(
        "/albums/{album_id}/photos",
        methods=[
            Get()
        ]
    )

    user_albums = Route(
        "/users/{user_id}/albums",
        methods=[
            Get()
        ]
    )

    user_todos = Route(
        "/users/{user_id}/todos",
        methods=[
            Get()
        ]
    )

    user_posts = Route(
        "/users/{user_id}/posts",
        methods=[
            Get()
        ]
    )


def create_http(base_url: str, awaiting: bool = False) -> Requests:
    """Create a Requests object from the given base_url.

    Parameters
    ----------
    base_url : str
    awaiting : bool, optional
        by default False

    Returns
    -------
    Requests
    """

    return Requests(
        base_url=base_url,
        awaiting=awaiting,
        responses={
            codes.NOT_FOUND: CallBack(raise_for_status)
        }
    )
