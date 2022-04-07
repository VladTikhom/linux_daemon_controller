import aiohttp_jinja2
import jinja2
from aiohttp import web

from app.routers import service_router, daemon_router
from .pickledb import PickleDB


class AioHTTPSetupDriver:
    @classmethod
    async def connect_db(cls, app):
        PickleDB.connect()

    @classmethod
    async def disconnect_db(cls, app):
        PickleDB.disconnect()

    @classmethod
    def get_app(cls):
        app = web.Application()
        app.on_startup.append(cls.connect_db)
        app.add_routes(daemon_router)
        app.add_routes(service_router)
        app.on_cleanup.append(cls.disconnect_db)
        app.logger.addHandler(get_handler())
        aiohttp_jinja2.setup(
            app, loader=jinja2.FileSystemLoader("./static/templates")
        )
        return app
