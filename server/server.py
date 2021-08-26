import typing as t
from http import HTTPStatus as S

from aiohttp import web

import http_ as http


class Server:
    def __init__(self) -> None:
        self.app = web.Application()
        self.rooms = {}

    def setup(self) -> None:
        _ = self.app.add_routes

        _(http.routes)
        _(web.get("/ws", self._handle))  # type: ignore

    def run(self):
        return web.run_app(self.app)

    async def _handle(self, request: web.Request) -> web.StreamResponse:
        room = request.query.get("room")
        if not room:
            return web.Response(status=S.BAD_REQUEST)

        room = room.lower()

        if room not in self.rooms:
            return web.Response(status=S.NOT_FOUND)

        room = self.rooms[room]

        ws = web.WebSocketResponse()
        await ws.prepare(request)

        # Sends setup event
        await ws.send_json(room.state)

        return ws
