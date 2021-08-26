import typing as t

import aiohttp

import ws
import web


class Server:
    def __init__(self) -> None:
        self.app = aiohttp.web.Application()  # type: ignore

    def setup(self) -> None:
        _ = self.app.add_routes  # type: ignore

        _(ws .routes)
        _(web.routes)

    def run(self) -> t.NoReturn:
        return aiohttp.web.run_app(self.app)  # type: ignore
