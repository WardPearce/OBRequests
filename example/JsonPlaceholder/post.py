from typing import TYPE_CHECKING, Tuple

from .models import PostModel


if TYPE_CHECKING:
    from . import JsonPlaceholder


class Post:
    def __init__(self, upper: "JsonPlaceholder", post_id: int) -> None:
        self._upper = upper
        self.post_id = post_id

    def update(self, new_post_id: int, title: str, body: str,
               user_id: int) -> Tuple[PostModel, "Post"]:
        self.post_id = new_post_id
        return self._upper._requests.post.put(
            json={
                "id": new_post_id,
                "title": title,
                "body": body,
                "userId": user_id
            },
            path_params={
                "post_id": self.post_id
            }
        )

    def delete(self) -> None:
        return self._upper._requests.post.delete(
            path_params={
                "post_id": self.post_id
            }
        )
