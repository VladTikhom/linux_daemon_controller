from aiohttp import web
from app.models import StateResponseModel


prefix = "/service"
service_router = web.RouteTableDef()


@service_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())


@service_router.get(prefix + "/enable")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())


@service_router.get(prefix + "/disable")
async def state(request):
    return web.Response(body=StateResponseModel(state=True).json())
