import aiohttp_jinja2
from aiohttp import web

from app.models import StateResponseModel
from app.services.controller import ControllerService

prefix = "/service"
service_router = web.RouteTableDef()


@service_router.get(prefix + "/state")
async def state(request):
    return web.Response(body=StateResponseModel(state=ControllerService.state()).json())


@service_router.post(prefix + "/enable")
async def enable(request):
    return web.Response(body=StateResponseModel(state=ControllerService.enable()).json())


@service_router.post(prefix + "/disable")
async def disable(request):
    return web.Response(body=StateResponseModel(state=ControllerService.disable()).json())


@service_router.get("/")
async def index(request) -> web.Response:

    context = {
        'service_state': "active" if ControllerService.state() else "inactive",
        # 'daemon_state': "active" if LinuxDriver.state() else "inactive"
    }
    response = aiohttp_jinja2.render_template(
        "index.html", request,
        context=context
    )

    return response
