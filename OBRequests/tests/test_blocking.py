import unittest

from .. import Blocking
from .shared_vars import CLIENT_PARAMS


class TestBlocking(unittest.TestCase):
    def setUp(self):
        self.client = Blocking(
            **CLIENT_PARAMS
        )

    def tearDown(self):
        self.client._close()

    def test_todo(self):
        self.assertTrue(type(self.client.todos.get()) == list)

    def test_todo_passed_id(self):
        self.assertTrue(
            type(self.client.todos.get(_id=1)) == dict
        )

    def test_post(self):
        self.assertTrue(
            type(
                self.client.posts.post(json={
                    "title": "foo",
                    "body": "bar",
                    "userId": 1
                })
            ) == dict
        )

    def test_function(self):
        self.assertEqual(
            self.client.notfound.get(),
            404
        )

    def test_read(self):
        self.assertTrue(
            type(
                self.client.read.get()
            ) == bytes
        )
