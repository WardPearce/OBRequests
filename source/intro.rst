Intro
=====

OBRequests has support for both asynchronous & synchronous requests thanks to HTTPX.
This intro will cover the basic of both. Lucily for you the API for asynchronous (awaiting) & synchronous (blocking) is identical.


Parameters Syntax
-----------------

- Double underscore before the parameter name (e.g. '__foo') declears a parameter as a route.
- A signle underscore before the parameter name (e.g. '_bar') declears a parameter as a path value.
- Excluding 'actions' & 'base_url', parameters without any starting underscore will be passed to the HTTPX client.


Notes
-----

- Path parameters with a value of 'None' will be set as a blank string, if you want to pass None or null make it a string.
- If the response status code doesn't match any of the actions the HTTPX response object will be returned.


Action hierarchy
----------------
The hierarchy system of OBRequests is very simple.

- Method actions always have priority .
- Route actions will have priority over global actions.
- Global actions are only used if non of the above match.


Awaiting
--------

.. code-block:: python

    import OBRequests
    from OBRequests.response import Json
    from OBRequests.method import Get, Post
    from OBRequests.route import Route

    from httpx import BasicAuth
    from asyncio import get_event_loop


    client = OBRequests.Awaiting(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Json,
        },

        auth=BasicAuth("username", "password"),

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

    from httpx import BasicAuth


    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Json,
        },

        auth=BasicAuth("username", "password"),

        __posts=Route(
            "posts/{post_id}",
            [
                Post(_post_id=None),
                Get()
            ],
            actions={
                201: Json
            },
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
