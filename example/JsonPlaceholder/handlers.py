from typing import AsyncGenerator, Generator, Tuple, Union
from OBRequests import Response

from .models import (
    PostModel, ToDoModel, AlbumModel, PhotoModel, CommentModel
)
from .post import Post


def post_handle(resp: Response, **kwargs) -> Tuple[PostModel, Post]:
    resp.raise_for_status()
    resp_json = resp.json()
    return (
        PostModel(**resp_json),
        Post(kwargs["globals_"]["base"], resp_json["id"])
    )


def posts_handle(resp: Response, **kwargs
                 ) -> Generator[PostModel, None, None]:
    resp.raise_for_status()
    for post in resp.json():
        yield PostModel(**post)


def todo_handle(resp: Response, **kwargs
                ) -> Union[
                    AsyncGenerator[ToDoModel, None],
                    Generator[ToDoModel, None, None]]:
    resp.raise_for_status()
    for todo in resp.json():
        yield ToDoModel(**todo)


def album_handle(resp: Response, **kwargs
                 ) -> Union[
                    AsyncGenerator[AlbumModel, None],
                    Generator[AlbumModel, None, None]]:
    resp.raise_for_status()
    for album in resp.json():
        yield AlbumModel(**album)


def photo_handle(resp: Response, **kwargs
                 ) -> Union[
                    AsyncGenerator[PhotoModel, None],
                    Generator[PhotoModel, None, None]]:
    resp.raise_for_status()
    for photo in resp.json():
        yield PhotoModel(**photo)


def comment_handle(resp: Response, **kwargs
                   ) -> Union[
                    AsyncGenerator[CommentModel, None],
                    Generator[CommentModel, None, None]]:
    resp.raise_for_status()
    for comment in resp.json():
        yield CommentModel(**comment)
