from aiohttp import web

from app.drivers.web import AioHTTPSetupDriver

web.run_app(AioHTTPSetupDriver.get_app(), host="localhost")
