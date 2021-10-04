from typing import Generator, Tuple
from .http import Requests, create_http
from .models import PostModel
from .post import Post


class JsonPlaceholder:
    _requests: Requests

    def __init__(self, endpoint: str = "https://jsonplaceholder.typicode.com",
                 awaiting: bool = False) -> None:
        self._requests = create_http(
            endpoint, self, awaiting
        )

    def close(self):
        return self._requests.close_()

    def create_post(self, post_id: int, title: str,
                    body: str, user_id: int) -> Tuple[PostModel, Post]:
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

    def posts(self) -> Generator[PostModel, None, None]:
        """Get all posts.

        Yields
        -------
        PostModel
        """
        return self._requests.posts.get()

    def post(self, post_id: int) -> Tuple[PostModel, Post]:
        return self._requests.post.get(path_params={
            "post_id": post_id
        })
