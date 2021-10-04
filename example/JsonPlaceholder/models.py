class PostModel:
    user_id: int
    id: int
    title: str
    body: str

    def __init__(self, userId: int, id: int, title: str, body: str) -> None:
        self.user_id = userId
        self.id = id
        self.title = title
        self.body = body


class ToDoModel:
    user_id: int
    id: int
    title: str
    completed: bool

    def __init__(self, userId: int, id: int, title: str,
                 completed: bool) -> None:
        self.user_id = userId
        self.id = id
        self.title = title
        self.completed = completed


class AlbumModel:
    user_id: int
    id: int
    title: str

    def __init__(self, userId: int, id: int, title: str) -> None:
        self.user_id = userId
        self.id = id
        self.title = title


class PhotoModel:
    album_id: int
    id: int
    title: str
    url: str
    thumbnail_url: str

    def __init__(self, albumId: int, id: int, title: str, url: str,
                 thumbnailUrl: str) -> None:
        self.album_id = albumId
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnailUrl


class CommentModel:
    post_id: int
    id: int
    name: str
    email: str
    body: str

    def __init__(self, postId: int, id: int, name: str,
                 email: str, body: str) -> None:
        self.post_id = postId
        self.id = id
        self.name = name
        self.email = email
        self.body = body
