import asynctest

from .. import (
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
        responses={
            codes.OK: CallBack(json),
            codes.NOT_FOUND: CallBack(raise_for_status)
        },
        methods=[
            Get(
                path_params={
                    "post_id": ""
                },
                responses={
                    codes.OK: CallBack(json)
                }
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
            Get(
                responses={
                    codes.OK: CallBack(json)
                }
            )
        ]
    )


class TestBase(asynctest.TestCase):
    client: Requests
    awaiting: bool = False

    use_default_loop = True

    def setUp(self) -> None:
        self.client = Requests(
            base_url="https://jsonplaceholder.typicode.com",
            awaiting=self.awaiting
        )

    async def tearDown(self) -> None:
        if self.awaiting:
            await self.client.close_()
        else:
            self.client.close_()
