from OBRequests import (
    OBRequests,
    Route,
    CallBack,
    Get,
    Post,
    Put,
    Patch,
    Delete,
    raise_for_status,
    codes
)

from .handlers import (
    post_handle, todo_handle, album_handle,
    photo_handle, comment_handle, posts_handle
)


class Requests(OBRequests):
    posts = Route(
        "/posts",
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(posts_handle)
                }
            ),
            Post(
                responses={
                    201: CallBack(post_handle)
                }
            )
        ]
    )

    post = Route(
        "/posts/{post_id}",
        responses={
            codes.OK: CallBack(post_handle)
        },
        methods=[
            Get(),
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
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(comment_handle)
                }
            )
        ]
    )

    albums = Route(
        "/albums/{user_id}/photos",
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(photo_handle)
                }
            )
        ]
    )

    user_albums = Route(
        "/users/{user_id}/albums",
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(album_handle)
                }
            )
        ]
    )

    user_todos = Route(
        "/users/{user_id}/todos",
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(todo_handle)
                }
            )
        ]
    )

    user_posts = Route(
        "/users/{user_id}/posts",
        methods=[
            Get(
                responses={
                    codes.OK: CallBack(posts_handle)
                }
            )
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
