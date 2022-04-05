from aiohttp import web

from app.models import StateResponseModel
from app.services.controller import ControllerService

prefix = "/service"
service_router = web.RouteTableDef()


@service_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=ControllerService.state()).json())


@service_router.get(prefix + "/enable")
async def enable(request):
    return web.Response(body=StateResponseModel(state=ControllerService.enable()).json())


@service_router.get(prefix + "/disable")
async def disable(request):
    return web.Response(body=StateResponseModel(state=ControllerService.disable()).json())
