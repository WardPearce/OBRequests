class PostModel:
    user_id: int
    id: int
    title: str
    body: str

    def __init__(self, user_id: int, id: int, title: str, body: str) -> None:
        self.user_id = user_id
        self.id = id
        self.title = title
        self.body = body


class ToDoModel:
    user_id: int
    id: int
    title: str
    completed: bool

    def __init__(self, user_id: int, id: int, title: str,
                 completed: bool) -> None:
        self.user_id = user_id
        self.id = id
        self.title = title
        self.completed = completed


class AlbumModel:
    user_id: int
    id: int
    title: str

    def __init__(self, user_id: int, id: int, title: str) -> None:
        self.user_id = user_id
        self.id = id
        self.title = title


class PhotoModel:
    album_id: int
    id: int
    title: str
    url: str
    thumbnail_url: str

    def __init__(self, album_id: int, id: int, title: str, url: str,
                 thumbnail_url: str) -> None:
        self.album_id = album_id
        self.id = id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url


class CommentModel:
    post_id: int
    id: int
    name: str
    email: str
    body: str

    def __init__(self, post_id: int, id: int, name: str,
                 email: str, body: str) -> None:
        self.post_id = post_id
        self.id = id
        self.name = name
        self.email = email
        self.body = body
