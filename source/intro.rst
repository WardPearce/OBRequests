Intro
=====

OBRequests has support for both asynchronous & synchronous requests thanks to HTTPX.
This intro will cover the basic of both. Lucily for you the API for asynchronous (awaiting) & synchronous (blocking) is identical.


Awaiting
--------

.. code-block:: python

    import OBRequests
    from OBRequests.response import Json
    from OBRequests.method import Get, Post
    from OBRequests.route import Route

    from asyncio import get_event_loop

    client = OBRequests.Awaiting(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Json,
        },

        __posts=Route(
            "posts/{post_id}",
            [
                Post(_post_id=None),
                Get()
            ],
            actions={
                201: Json
            }
        )
    )

    async def async_loop():
        print(await client.posts.get(_post_id=1))
        print(await client.posts.post(
            json={
                "title": "hello world",
                "body": "created with OBRequests",
                "userID": 1
            }
        ))

        if not client.posts.delete:
            print("This isn't a method!")

    get_event_loop().run_until_complete(async_loop())

Blocking
--------

.. code-block:: python

    import OBRequests
    from OBRequests.response import Json
    from OBRequests.method import Get, Post
    from OBRequests.route import Route

    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Json,
        },

        __posts=Route(
            "posts/{post_id}",
            [
                Post(_post_id=None),
                Get()
            ],
            actions={
                201: Json
            }
        )
    )

    print(client.posts.get(_post_id=1))
    print(client.posts.post(
        json={
            "title": "hello world",
            "body": "created with OBRequests",
            "userID": 1
        }
    ))

    if not client.posts.delete:
        print("This isn't a method!")
