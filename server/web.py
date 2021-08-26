from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/p")
async def a(request):
    return web.Response()
