from aiohttp import web
from app.models import StateResponseModel
from app.drivers.linux_driver import LinuxDriver


prefix = "/daemon"
daemon_router = web.RouteTableDef()


@daemon_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/enable")
async def enable(request):
    LinuxDriver.start()
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/disable")
async def enable(request):
    LinuxDriver.stop()
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/restart")
async def enable(request):
    LinuxDriver.restart()
    return web.Response(body=StateResponseModel(state=True).json())
