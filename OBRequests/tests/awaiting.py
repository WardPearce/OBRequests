from .base import TestBase
from .. import HTTPStatusError


class TestAwaiting(TestBase):
    awaiting = True

    async def test_list_posts(self) -> None:
        self.assertIsInstance(
            await self.client.posts.get(), object
        )

    async def test_get_post(self) -> None:
        self.assertIsInstance(
            await self.client.posts.get(path_params={
                "post_id": 1
            }),
            object
        )

    async def test_create_post(self) -> None:
        self.assertIsInstance(
            await self.client.posts.post(
                json={
                    "title": "foo",
                    "body": "bar",
                    "userId": 1
                }
            ),
            object
        )

    async def test_update_post(self) -> None:
        self.assertIsInstance(
            await self.client.posts.put(
                json={
                    "title": "foo",
                    "body": "bar",
                    "userId": 1
                },
                path_params={
                    "post_id": 1
                }
            ),
            object
        )

    async def test_patch_post(self) -> None:
        self.assertIsInstance(
            await self.client.posts.patch(
                json={
                    "title": "woo"
                },
                path_params={
                    "post_id": 1
                }
            ),
            object
        )

    async def test_delete_post(self) -> None:
        self.assertIsInstance(
            await self.client.posts.delete(
                path_params={
                    "post_id": 1
                }
            ),
            object
        )

    async def test_comment_get(self) -> None:
        self.assertIsInstance(
            await self.client.comments.get(path_params={
                "post_id": 1
            }),
            object
        )

    async def test_conditional(self) -> None:
        self.assertEqual(
            await self.client.conditional.get(),
            "await"
        )

    async def test_global(self) -> None:
        self.assertEqual(
            await self.client.global_var.get(),
            1
        )

    async def test_any_status(self) -> None:
        with self.assertRaises(HTTPStatusError):
            await self.client.posts.get(path_params={
                "post_id": "404_error"
            })

    async def test_base(self) -> None:
        self.assertIsInstance(
            await self.client.base_.get(url="/posts"),
            object
        )
