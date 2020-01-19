import typing

import requests
from starlette.testclient import AuthType
from starlette.testclient import Cookies
from starlette.testclient import DataType
from starlette.testclient import FileType
from starlette.testclient import Params
from starlette.testclient import TestClient as PureClient
from starlette.testclient import TimeOut


class TestClient(PureClient):
    def __init__(self, prefix: str = "", *args, **kwargs):
        super(TestClient, self).__init__(*args, **kwargs)
        self.prefix = prefix

    def request(
        self,
        method: str,
        url: str,
        params: Params = None,
        data: DataType = None,
        headers: typing.MutableMapping[str, str] = None,
        cookies: Cookies = None,
        files: FileType = None,
        auth: AuthType = None,
        timeout: TimeOut = None,
        allow_redirects: bool = None,
        proxies: typing.MutableMapping[str, str] = None,
        hooks: typing.Any = None,
        stream: bool = None,
        verify: typing.Union[bool, str] = None,
        cert: typing.Union[str, typing.Tuple[str, str]] = None,
        json: typing.Any = None,
    ) -> requests.Response:
        url = self.prefix + url
        return super(TestClient, self).request(
            method,
            url,
            params,
            data,
            headers,
            cookies,
            files,
            auth,
            timeout,
            allow_redirects,
            proxies,
            hooks,
            stream,
            verify,
            cert,
            json,
        )
