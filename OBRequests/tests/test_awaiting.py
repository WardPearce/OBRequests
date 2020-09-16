import asynctest

from .. import Awaiting
from .shared_vars import CLIENT_PARAMS


class TestAwaiting(asynctest.TestCase):
    use_default_loop = True

    async def setUp(self):
        self.client = Awaiting(
            **CLIENT_PARAMS
        )

    async def tearDown(self):
        await self.client._close()

    async def test_todo(self):
        self.assertTrue(type(await self.client.todos.get()) == list)

    async def test_todo_passed_id(self):
        self.assertTrue(
            type(await self.client.todos.get(_id=1)) == dict
        )

    async def test_post(self):
        self.assertTrue(
            type(
                await self.client.posts.post(json={
                    "title": "foo",
                    "body": "bar",
                    "userId": 1
                })
            ) == dict
        )

    async def test_function(self):
        self.assertEqual(
            await self.client.notfound.get(),
            404
        )

    async def test_read(self):
        self.assertTrue(
            type(
                await self.client.read.get()
            ) == bytes
        )
