from OBRequests import Request


class TestReqest(Request):
    _base_url = "https://jsonplaceholder.typicode.com"

    GET_posts = "posts"
    GET_comment = "comments"


request = TestReqest()

# resp = request.GET_posts()
# if resp.status_code == 200:
#     print(
#         resp.json()
#     )

resp = request.GET_comment()
print(resp.url)
if resp.status_code == 200:
    print(
        resp.json()
    )
else:
    print("Invalid url")
