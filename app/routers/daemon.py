from aiohttp import web

from app.drivers.linux_driver import LinuxDriver
from app.models import StateResponseModel
from app.services.controller import ControllerService

prefix = "/daemon"
daemon_router = web.RouteTableDef()


@daemon_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/enable")
async def enable(request):
    if not ControllerService.state():
        return web.Response(body=str({"error": "Service is not active"}), status=400)
    LinuxDriver.start()
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/disable")
async def disable(request):
    if not ControllerService.state():
        return web.Response(body=str({"error": "Service is not active"}), status=400)
    LinuxDriver.stop()
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/restart")
async def restart(request):
    if not ControllerService.state():
        return web.Response(body=str({"error": "Service is not active"}), status=400)
    LinuxDriver.restart()
    return web.Response(body=StateResponseModel(state=True).json())
