Introduction to OBRequests
==========================
OBRequests is pretty different compared to most HTTP clients, so reading the introduction is worth while.

OBRequests is built on-top of HTTPX
-----------------------------------
1st thing to be understood is that OBRequests is built on-top of HTTPX, reading the developer interface page on HTTPX documentation goes into details around what HTTP parameters
you can pass to OBRequests. HTTPX aims to be "A broadly requests-compatible API." So if you're use to the requests library this shouldn't be anything new.

https://www.python-httpx.org/api/


The basics 
----------
Base
####
"Base" refers to the base client of OBRequests, everything is applied globally, unless overwritten in a Method or Route.

.. code-block:: python

    from OBRequests import OBRequests, BasicAuth, CallBack, json


    class Requests(OBRequests):
        pass


    request = Requests(
        responses={
            200: CallBack(json),  # If the status code equals run "json", unless overwritten in a Route or Method
        },
        base_url="https://jsonplaceholder.typicode.com",
        headers={"some-header": "value"},  # Applies headers to every request
        auth=BasicAuth("username", "password"),  # Applies basic auth to every request
        awaiting=False  # Change to True to make requests async
    )

    # Makes a get request to 'https://jsonplaceholder.typicode.com/posts'
    request.base_.get(url="/posts")


Responses & CallBacks
#####################
OBRequests uses "CallBacks" to run functions when a status code is given. OBRequests provides predefined CallBacks, but you can easily just create your own.

- json
    Returns phased JSON
- read
    Returns bytes
- response
    Returns response object
- raise_for_status
    Raises HTTPStatusError

.. code-block:: python

    from OBRequests import OBRequests, CallBack, Response, AnyStatus, json


    # Custom response what returns status_code
    def custom_response(resp: Response, allow: bool = False, **kwargs) -> None:
        if kwargs["globals_"]["print_status"]:
            print(resp.status_code)
        return resp.status_code if allow else None


    class Requests(OBRequests):
        pass


    request = Requests(
        responses={
            200: CallBack(json),  # Any response with status 200, return phased json.
            AnyStatus: CallBack(custom_response, allow=True)  # Any response with any status, return status code.
        },
        base_url="https://jsonplaceholder.typicode.com",
        globals_={
            "print_status": True  # Passed to kwargs of all callbacks
        }
    )

    # Makes a get request to 'https://jsonplaceholder.typicode.com/posts'
    request.base_.get(url="/posts")

Conditional CallBacks
*********************
OBRequests provides "ConditionalCallBacks" to run different functions depending on if OBRequests is used async or sync.

.. code-block:: python

    from OBRequests import OBRequests, ConditionalCallBack, CallBack, Response

    def custom_response(resp: Response, **kwargs) -> None:
        return resp.status_code

    async def a_custom_response(resp: Response, **kwargs) -> None:
        return resp.status_code

    class Requests(OBRequests):
        pass


    request = Requests(
        responses={
            200: ConditionalCallBack(
                awaiting=CallBack(a_custom_response),  # This doesn't need to be an async function
                blocking=CallBack(custom_response)
            ),
        },
        awaiting=False,  # 'custom_response' will be called when status code 200
        base_url="https://jsonplaceholder.typicode.com",
    )

    # Makes a get request to 'https://jsonplaceholder.typicode.com/posts'
    request.base_.get(url="/posts")


Route
#####
What makes OBRequests unique compared to other HTTP clients is our routing & methods, what allows you to apply callbacks per route or method.

.. code-block:: python

    from OBRequests import OBRequests, Route, CallBack, AnyStatus, BasicAuth, json

    class Requests(OBRequests):
        # Can never start or end with a '_'
        posts = Route(
            "/posts/{post_id}",
            responses={
                200: CallBack(json)
            },
            path_params={
                "post_id": ""
            },
            # Maybe we want different basic auth on '/posts'
            auth=BasicAuth("username", "password")
        )


    request = Requests(
        responses={
            # Any status not defined raise for status
            AnyStatus: CallBack(raise_for_status)
        },
        base_url="https://jsonplaceholder.typicode.com",
    )

    # Returns phased JSON
    request.posts.get()

    # Raises HTTPStatusError
    request.posts.get(path_params={
        "post_id": "404_error"
    })

Method
######
OBRequests lets you apply callbacks & define payloads per HTTP method too.

.. code-block:: python

    from OBRequests import OBRequests, CallBack, Route, Delete, AnyStatus, BasicAuth, json

    class Requests(OBRequests):
        # Can never start or end with a '_'
        posts = Route(
            "/posts/{post_id}",
            responses={
                200: CallBack(json)
            },
            path_params={
                "post_id": ""
            },
            methods=[
                # The Delete method doesn't return json, so instead lets check the status code
                Delete(
                    responses={
                        AnyStatus: CallBack(raise_for_status)
                    }
                )
            ]
        )


    request = Requests(
        base_url="https://jsonplaceholder.typicode.com",
    )

    # Returns phased JSON
    request.posts.get()

    # Raises HTTPStatusError
    request.posts.get(path_params={
        "post_id": "404_error"
    })
