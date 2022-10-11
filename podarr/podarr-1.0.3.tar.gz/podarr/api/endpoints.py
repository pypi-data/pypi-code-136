from json import loads
from requests import get
from fastapi_utils.inferring_router import InferringRouter
from fastapi import FastAPI
from fastapi_utils.cbv import cbv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel  # pylint: disable=no-name-in-module


import podarr


class CommandSchema(BaseModel):
    """
    Setup schema
    """
    port: str
    service: str
    command: str | dict

    class Config:
        """
        Schema config
        """
        orm_mode = True


app = FastAPI()

router = InferringRouter()

origins = [
    'http://localhost:3000',
    'http://127.0.0.1:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@cbv(router)
class SystemView:

    @router.get('/api/system/status')
    def system_get_endpoint(self):
        return JSONResponse(status_code=200, content={
            'cpu_usage': podarr.SystemInfo.get_cpu_usage(),
            'ram_usage': podarr.SystemInfo.get_ram_usage(),
            'swap_usage': podarr.SystemInfo.get_swap_usage(),
            'disk_usage': podarr.SystemInfo.get_disk_usage(),
            'uptime': podarr.SystemInfo.get_system_uptime(),
        })

    @router.get('/api/system/test')
    def system_test_endpoint(self):
        return JSONResponse(status_code=200, content={
            'cpu_usage': podarr.SystemInfo.get_cpu_usage(),
            'ram_usage': podarr.SystemInfo.get_ram_usage(),
            'swap_usage': podarr.SystemInfo.get_swap_usage(),
            'disk_usage': podarr.SystemInfo.get_disk_usage(),
            'uptime': podarr.SystemInfo.get_system_uptime(),
        })


@cbv(router)
class ServiceView:

    @router.get('/api/service/status')
    def service_get_endpoint(self, service: str):
        if service not in podarr.__available_services__ and service not in ['all']:
            return JSONResponse(status_code=400, content={
                'error': 'Invalid service'
            })

        response = {}
        if service == 'all':
            for available_service in podarr.__available_services__:
                if available_service == 'web':
                    continue
                response[available_service] = getattr(podarr,
                                                      available_service.upper().replace('_', ''))().status()
            return JSONResponse(status_code=200, content=response)
        response = getattr(podarr, service.upper().replace('_', ''))().status()
        return JSONResponse(status_code=200, content=response)

    @router.post('/api/service/rc')
    def service_post_endpoint(self, obj: CommandSchema):
        if obj.service not in podarr.__available_services__ and obj.service not in ['all'] and obj.service == 'web':
            return JSONResponse(status_code=400, content={
                'error': 'Invalid service'
            })
        if obj.command not in podarr.__available_commands__:
            return JSONResponse(status_code=400, content={
                'error': 'Invalid command'
            })

        all_response = {}
        if obj.service != 'all':
            return JSONResponse(status_code=200, content={
                obj.service: getattr(getattr(podarr, obj.service.upper().replace('_', ''))(), obj.command)()})
        for available_service in podarr.__available_services__:
            if available_service == 'web':
                continue
            all_response[available_service] = getattr(
                getattr(podarr, available_service.upper().replace('_', ''))(), obj.command)()
        return JSONResponse(status_code=200, content=all_response)

    @router.post('/api/service/rclone/rc')
    def rclone_rc_post_endpoint(self, obj: CommandSchema):
        available_ports = [
            port.number for port in podarr.RCLONE().service.ports]
        if obj.port not in available_ports + ['all']:
            return JSONResponse(status_code=400, content={
                'error': f'Rclone is listening only in the following ports: {", ".join(available_ports + ["all"])}'
            })

        response = {}

        if obj.command == 'core/stats':
            defaults = {
                'bytes': 0,
                'checks': 0,
                'deletedDirs': 0,
                'deletes': 0,
                'elapsedTime': 0,
                'errors': 0,
                'eta': 0,
                'fatalError': False,
                'lastError': '',
                'renames': 0,
                'retryError': False,
                'speed': 0,
                'totalBytes': 0,
                'totalChecks': 0,
                'totalTransfers': 0,
                'transferTime': 0,
                'transfers': 0
            }
            if obj.port == 'all':
                for index, port in enumerate(available_ports):
                    rc_response = podarr.Podman().exec(podarr.RCLONE().service,
                                                       f'rclone rc --rc-addr=192.168.1.104:{port} {obj.command}')
                    if rc_response.return_bool and 'transferring' in rc_response.stdout:
                        response[index] = loads(rc_response.stdout)
                    else:
                        response[index] = defaults
                return JSONResponse(status_code=200, content=response)
            elif obj.port != 'all':
                rc_response = podarr.Podman().exec(podarr.RCLONE().service,
                                                   f'rclone rc --rc-addr=192.168.1.104:{obj.port} {obj.command}')
                if rc_response.return_bool and 'transferring' in rc_response.stdout:
                    response[obj.port] = loads(rc_response.stdout)
                else:
                    response[obj.port] = defaults
                return JSONResponse(status_code=200, content=response)
            else:
                return JSONResponse(status_code=400, content={
                    'error': 'Invalid command'
                })

    @router.post('/api/service/sabnzbd/rc')
    def sabznbd_rc_get_endpoint(self, obj: CommandSchema):
        service_obj = podarr.SABNZBD()
        if obj.command == 'status':
            return JSONResponse(status_code=200, content={
                'queue': get(f'http://localhost:'
                             f'{service_obj.service.ports[0].number}/sabnzbd/api?output=json'
                             f'&apikey={service_obj.get_apit_key()}&mode=queue', timeout=5).json()['queue'],
                'history': get(f'http://localhost:'
                               f'{service_obj.service.ports[0].number}/sabnzbd/api?output=json'
                               f'&apikey={service_obj.get_apit_key()}&mode=history', timeout=5).json()['history']
            })
        return JSONResponse(status_code=400, content={
            'error': 'Invalid command'
        })


app.include_router(router)
