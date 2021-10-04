from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._types import RESPONSES


class Method:
    _method: str

    def __init__(self, responses: "RESPONSES" = {},  # noqa: E501
                 path_params: dict = {}, **kwargs) -> None:
        """Initialize the method for this request.

        Parameters
        ----------
        responses : "RESPONSES", optional
            by default {}
        path_params : dict
            by default {}
        auth : AuthTypes, optional
            by default None
        params : QueryParamTypes, optional
            by default None
        headers : HeaderTypes, optional
            by default None
        cookies : CookieTypes, optional
            by default None
        verify : VerifyTypes, optional
            by default True
        cert : CertTypes, optional
            by default None
        http1 : bool, optional
            by default True
        http2 : bool, optional
            by default False
        proxies : ProxiesTypes, optional
            by default None
        mounts : Mapping[str, BaseTransport], optional
            by default None
        timeout : TimeoutTypes, optional
            by default ...
        limits : Limits, optional
            by default ...
        max_redirects : int, optional
            by default ...
        event_hooks : Mapping[str, List[Callable]], optional
            by default None
        transport : BaseTransport, optional
            by default None
        app : Callable, optional
            by default None
        trust_env : bool, optional
            by default True
        """

        self._responses = responses
        self._path_params = path_params
        self._kwargs = kwargs


class Get(Method):
    """GET method
    """
    _method = "GET"


class Post(Method):
    """DELETE method
    """
    _method = "POST"


class Head(Method):
    """HEAD method
    """
    _method = "HEAD"


class Delete(Method):
    """DELETE method
    """
    _method = "DELETE"


class Put(Method):
    """PUT method
    """
    _method = "PUT"


class Patch(Method):
    """PATCH method
    """
    _method = "PATCH"
