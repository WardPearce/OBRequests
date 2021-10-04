from .base import TestBase


class TestBlocking(TestBase):
    awaiting = False

    def test_list_posts(self) -> None:
        self.assertIsInstance(
            self.client.posts.get(), object
        )

    def test_get_post(self) -> None:
        self.assertIsInstance(
            self.client.posts.get(path_params={
                "post_id": 1
            }),
            object
        )

    def test_create_post(self) -> None:
        self.assertIsInstance(
            self.client.posts.post(
                json={
                    "title": "foo",
                    "body": "bar",
                    "userId": 1
                }
            ),
            object
        )

    def test_update_post(self) -> None:
        self.assertIsInstance(
            self.client.posts.put(
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

    def test_patch_post(self) -> None:
        self.assertIsInstance(
            self.client.posts.patch(
                json={
                    "title": "woo"
                },
                path_params={
                    "post_id": 1
                }
            ),
            object
        )

    def test_delete_post(self) -> None:
        self.assertIsInstance(
            self.client.posts.delete(
                path_params={
                    "post_id": 1
                }
            ),
            object
        )

    def test_comment_get(self) -> None:
        self.assertIsInstance(
            self.client.comments.get(path_params={
                "post_id": 1
            }),
            object
        )

    def test_conditional(self) -> None:
        self.assertEqual(
            self.client.conditional.get(),
            "block"
        )

    def test_global(self) -> None:
        self.assertEqual(
            self.client.global_var.get(),
            1
        )