import asynctest

from .. import (
    OBRequests,
    Route,
    Response,
    ConditionalCallBack,
    CallBack,
    Get,
    Post,
    Put,
    Patch,
    Delete,
    json,
    raise_for_status,
    codes,
    AnyStatus,
    BasicAuth
)


async def is_awaiting(resp: Response, **kwargs) -> str:
    return "await"


def is_blocking(resp: Response, **kwargs) -> str:
    return "block"


def test_globals(resp: Response, **kwargs) -> int:
    return kwargs["globals_"]["test"]


class Requests(OBRequests):
    posts = Route(
        "/posts/{post_id}",
        responses={
            codes.OK: CallBack(json),
            AnyStatus: CallBack(raise_for_status)
        },
        methods=[
            Get(
                path_params={
                    "post_id": ""
                },
                responses={
                    codes.OK: CallBack(json)
                },
                auth=BasicAuth("different", "password")
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
        ],
        auth=BasicAuth("username", "password")
    )

    conditional = Route(
        "/",
        methods=[
            Get(responses={
                codes.OK: ConditionalCallBack(
                    awaiting=CallBack(is_awaiting),
                    blocking=CallBack(is_blocking)
                )
            })
        ]
    )

    global_var = Route(
        "/",
        methods=[
            Get(responses={
                codes.OK: CallBack(test_globals)
            })
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
            awaiting=self.awaiting,
            globals_={
                "test": 1
            },
            responses={
                200: CallBack(json)
            }
        )

    async def tearDown(self) -> None:
        if self.awaiting:
            await self.client.close_()
        else:
            self.client.close_()
