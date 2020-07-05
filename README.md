[![GitHub issues](https://img.shields.io/github/issues/WardPearce/OBRequests)](https://github.com/WardPearce/OBRequests/issues)
[![GitHub license](https://img.shields.io/github/license/WardPearce/OBRequests)](https://github.com/WardPearce/OBRequests/blob/master/LICENSE)
[![Actions Status](https://github.com/WardPearce/OBRequests/workflows/Python%20application/badge.svg)](https://github.com/WardPearce/OBRequests/actions)

# About
OBRequests is a object-based request library for HTTP built on top of HTTPX. It's feature rich, easy to use & fast. Currently supports all major request methods & also includes asyncio support.

# Install
- Pypi: ``pip3 install OBRequests``
- Git: ``pip3 install git+https://github.com/WardPearce/OBRequests.git``

# So how does it work?
You can read the full documentation [here](/DOCS.md) and find more detailed examples in the tests folder.

Here is a basic look at OBRequests.
```python
# 1st thing 1st, lets import all the modules we'll need.
from OBRequests import Request, Methods
from OBRequests.method import Get
from OBRequests.response import Json


# Now lets create a request object.
typicode_api = Request(
    # Here we're setting the base url.
    "https://jsonplaceholder.typicode.com",

    # Here we're setting the client to synchronous and not asynchronous.
    awaiting=False,

    # Here we're setting a global response action.
    # Basically saying if we get the status code 200
    # we want json returned, if a status code doesn't match
    # the resp_actions then well just return the HTTPX response
    # object.
    resp_actions={
        200: Json
    },
    
    # jsonplaceholder doesn't need authorization
    # but this is an example on how to have some
    # global headers, any httpx.Client parameter
    # can be passed here. 
    headers={
        "Authorization": "api_key"
    },

    # Now lets make our 1st route,
    # routes are identified but a double underscore
    # e.g. '__'
    # All routes expect the Methods object.
    __comments=Methods(
        # Here we're passing the prefix
        # to attach to the end of the base
        # URL.
        "comments/{id}",
        [
            # Here we can list all the
            # different request methods
            # this route supports.

            Get(
                # Lets set a default value for
                # id.
                _id=None,
                
                # Now lets raise a custom
                # expectation if we 404.
                resp_exceptions={
                    404: NotImplemented
                }
            )
        ]
    )
)

# Now lets make a request.
try:
    json = typicode_api.comments.get(
        # Here we are setting
        # the path parameter to 1.
        _id=1
    )
except NotImplemented:
    # Here is where we can
    # catch that 404 expectation we set.
    pass
else:
    print(json)

```