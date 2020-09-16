Examples
========

Reading Json
~~~~~~~~~~~~

.. code-block:: python

    import OBRequests
    from OBRequests.route import Route
    from OBRequests.method import Get
    from OBRequests.response import Json


    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Json,
        },

        __comments=Route(
            "comments",
            [
                Get()
            ]
        )
    )

    comments = client.comments.get()
    for comment in comments:
        print(comment["id"])


Calling Functions
~~~~~~~~~~~~~~~~~

.. code-block:: python

    import OBRequests
    from OBRequests.route import Route
    from OBRequests.method import Get
    from OBRequests.response import Function


    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Function(lambda: True),
        },

        __comments=Route(
            "comments",
            [
                Get()
            ]
        )
    )

    print(client.comments.get())


Reading data
~~~~~~~~~~~~

.. code-block:: python

    import OBRequests
    from OBRequests.route import Route
    from OBRequests.method import Get
    from OBRequests.response import Read


    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            200: Read,
        },

        __comments=Route(
            "comments",
            [
                Get()
            ]
        )
    )

    print(client.comments.get())


Raising Exceptions
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import OBRequests
    from OBRequests.route import Route
    from OBRequests.method import Get

    class NotFound(Exception):
        pass

    client = OBRequests.Blocking(
        "https://jsonplaceholder.typicode.com",
        actions={
            404: NotFound,
        },

        __comments=Route(
            "404",
            [
                Get()
            ]
        )
    )

    try:
        client.comments.get()
    except NotFound:
        print("Not found")
