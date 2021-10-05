Example
=======

Find a more advance example on our Github: https://github.com/Object-Based/Requests/tree/Development/example

.. code-block:: python

    from OBRequests import (
        OBRequests, Response, CallBack, Route,
        Get, json, raise_for_status,
        HTTPStatusError, AnyStatus, BasicAuth
    )


    def custom_response(resp: Response, is_get: bool = False,
                        **kwargs) -> None:
        if is_get:
            print(resp.status_code)
        else:
            raise NotImplementedError()


    class Requests(OBRequests):
        posts = Route(
            "/posts/{post_id}",
            responses={
                AnyStatus: CallBack(raise_for_status)
            },
            path_params={
                "post_id": "404_error"
            },
            methods=[
                Get(
                    responses={
                        200: CallBack(custom_response, is_get=True),
                        201: ConditionalCallBack(
                            awaiting=CallBack(custom_response, is_get=True),
                            blocking=CallBack(custom_response, is_get=False)
                        )
                    },
                    auth=BasicAuth("different", "password")
                ),
            ],
            auth=BasicAuth("username", "password")
        )


    request = Requests(
        responses={
            200: CallBack(json)
        },
        base_url="https://jsonplaceholder.typicode.com",
        awaiting=False,
        globals_={
            "example": True
        }
    )

    try:
        request.posts.get()
    except HTTPStatusError as error:
        print(error)

    # Prints status code
    request.posts.get(path_params={
        "post_id": 1
    })

    # Returns phased JSON
    request.base_.get(url="/posts")

    # Only needed for async
    request.close_()