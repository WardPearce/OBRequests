from typing import AsyncGenerator, Generator, Union
from .http import Requests, create_http
from .models import PostModel


class JsonPlaceholder:
    _requests: Requests

    def __init__(self, endpoint: str = "https://jsonplaceholder.typicode.com",
                 awaiting: bool = False) -> None:
        self._requests = create_http(
            endpoint, awaiting
        )

    def create_post(self, post_id: int, title: str,
                    body: str, user_id: int) -> PostModel:
        """Create a post.

        Parameters
        ----------
        post_id : int
        title : str
        body : str
        user_id : int

        Returns
        -------
        PostModel
        """
        return self._requests.posts.post(json={
            "id": post_id,
            "title": title,
            "body": body,
            "userId": user_id
        })

    def posts(self) -> Union[Generator[PostModel, None, None],
                             AsyncGenerator[PostModel, None]]:
        """Get all posts.

        Yields
        -------
        Iterator[Union[
            Generator[PostModel, None, None],
            AsyncGenerator[PostModel, None]
        ]]
        """
        for post in self._requests.post.get():
            yield post

    def post(self, post_id: int) -> PostModel:
        return self._requests.post.get(path_params={
            "post_id": post_id
        })
