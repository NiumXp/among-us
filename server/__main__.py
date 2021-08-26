import aiohttp

import ws
import web

app = aiohttp.web.Application()

app.add_routes(ws .routes)
app.add_routes(web.routes)

aiohttp.web.run_app(app)
