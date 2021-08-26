import json
from aiohttp import web, WSMsgType as MType

routes = web.RouteTableDef()


@routes.get("/ws")
async def websocket(request):
    ws = web.WebSocketResponse()
    print("Connecting", ws)

    await ws.prepare(request)
    print("Connected", ws)
    await ws.send_json({'e': "setup", 'd': 1})

    async for message in ws:
        if message.type in (MType.TEXT, MType.BINARY):
            try:
                data = json.loads(message.data)
            except Exception:
                await ws.close(message=b"Invalid message.")
                break

            print(data)
        print(message)

    print("Closing", ws)

    return ws
