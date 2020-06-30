##### This library is due to change in future version but is considered stable.
##### For now it's recommend lock this package to 0.0.1

## Index
- [OBRequests](#OBRequests)
- [Todo](#Todo)
- [Using](#Using)
- [Example](#Example)


## OBRequests
Object-based request library, may the force be with you. OBRequests is built using [HTTPX](https://www.python-httpx.org/).

## Todo
- Asyncio support.
- Fully testing everything.
- Optimizing.

## Using
Start by creating a class with the Request object.


```python
class JsonPlaceHolder(Request):
    pass
```

Then set "global" request parameters. Parameters are the same as [here](https://www.python-httpx.org/api/#client) but with "_" (underscores).

```python
class JsonPlaceHolder(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

```

Then add some routes, start by specifying the method in UPPER-CASE.

```python
class JsonPlaceHolder(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

    POST_create = "example"
    GET_info = ""
```

Add path variables like this

```python
class JsonPlaceHolder(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

    POST_create = "example/{example_var}?nothing={example_var_two}"


request = JsonPlaceHolder()

resp = request.POST_create(
    _example_var="Example",
    _example_var_two="woo"
)
if resp.status_code == 200:
    print(
        resp.json()
    )
```

You an pass parameters like [this](https://www.python-httpx.org/api/#request) by doing this

```python
class JsonPlaceHolder(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

    POST_create = "example/{example_var}?nothing={example_var_two}"


request = JsonPlaceHolder()

resp = request.POST_create(
    _example_var="Example",
    _example_var_two="woo",
    json={
        "foo": "bar",
    }
)
if resp.status_code == 200:
    print(
        resp.json()
    )
```

## Example
```python
from OBRequests import Request


class JsonPlaceHolder(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

    GET_posts = "posts"
    GET_comment = "comments"


request = JsonPlaceHolder()

resp = request.GET_posts()
if resp.status_code == 200:
    print(
        resp.json()
    )

resp = request.GET_comment()
if resp.status_code == 200:
    print(
        resp.json()
    )
else:
    print("Invalid url")

```