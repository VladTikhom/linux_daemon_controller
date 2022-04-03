from aiohttp import web
from app.models import StateResponseModel

prefix = "/daemon"
daemon_router = web.RouteTableDef()


@daemon_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/enable")
async def enable(request):
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/disable")
async def enable(request):
    return web.Response(body=StateResponseModel(state=True).json())


@daemon_router.post(prefix + "/restart")
async def enable(request):
    return web.Response(body=StateResponseModel(state=True).json())
