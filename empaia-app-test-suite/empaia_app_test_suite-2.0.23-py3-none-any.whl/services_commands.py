import json
from pathlib import Path
from time import sleep

import docker
import requests

from . import settings
from .constants import SERVICE_API_MAPPING
from .print_helpers import PrintStep
from .shared import get_service_url


def _ensure_net(client):
    try:
        client.networks.get(settings.EATS_NET)
    except (docker.errors.NotFound, requests.exceptions.ChunkedEncodingError):
        client.networks.create(name=settings.EATS_NET, driver="bridge")


def _remove_net(client):
    net = client.networks.get(settings.EATS_NET)
    net.remove()


def _is_service_alive(client, service_name, raise_exception=False):
    alive = False
    try:
        service_url = get_service_url(client=client, service_name=service_name)
        if service_url:
            r = requests.get(service_url + "/alive")
            r.raise_for_status()
            status = r.json()["status"]
            if status == "ok":
                alive = True
    except (docker.errors.NotFound, docker.errors.APIError, requests.exceptions.RequestException) as e:
        if raise_exception:
            raise e
    if not alive and raise_exception:
        raise Exception(service_name + " not alive")
    return alive


def _volume_name(volume_name, volume_prefix=None):
    if volume_prefix and "/" not in volume_name:
        return f"{volume_prefix}_{volume_name}"
    return volume_name


def services_wait(client, trials=20):
    services = get_exposed_services()
    with PrintStep("Waiting for all services to be ready"):
        for _ in range(trials):
            services_alive = [_is_service_alive(client, s) for s in services]
            if all(services_alive):
                return
            sleep(1)
        raise Exception(
            f"Unable to reach all services (tried {trials} times). Check if services are running and try again."
        )


def services_health(client, silent=False):
    services = get_exposed_services()
    if silent:
        services_alive = [_is_service_alive(client, s) for s in services]
        if all(services_alive):
            return
        else:
            raise Exception("Unable to reach all services. Check if services are running and try again.")
    for service in services:
        with PrintStep(service, catch_exc=True):
            _is_service_alive(client, service, raise_exception=True)


def get_exposed_services():
    services = settings.get_services()
    exposed_services = []
    for service in services:
        if service["name"] in SERVICE_API_MAPPING and "service" in service["name"]:
            exposed_services.append(service["name"])
    return exposed_services


def services_list(client):
    services = settings.get_services()
    try:
        client.containers.get("isyntax-backend")
        services.append({"name": "isyntax-backend"})
    except docker.errors.NotFound:
        pass
    databases = settings.get_databases()
    return [service["name"] for service in services] + [db["name"] for db in databases]


def services_volumes(volume_prefix):
    services = settings.get_services()
    databases = settings.get_databases()
    volumes = [_volume_name(db["volume"]["name"], volume_prefix) for db in databases]
    volumes += [_volume_name(service["volume"]["name"], volume_prefix) for service in services if "volume" in service]
    volumes = [volume for volume in volumes if volume != "/var/run/docker.sock"]
    return volumes


def services_down(client, del_volumes=False, volume_prefix=None):
    services = services_list(client)
    for name in services:
        with PrintStep(f"Removing container: {name}", catch_exc=True):
            container = client.containers.get(name)
            container.remove(force=True)

    with PrintStep(f"Removing network: {settings.EATS_NET}", catch_exc=True):
        _remove_net(client)

    if del_volumes:
        volumes = services_volumes(volume_prefix)
        for v in volumes:
            with PrintStep(f"Removing volume: {v}", catch_exc=True):
                vol = client.volumes.get(v)
                vol.remove(force=True)


def services_up(
    client,
    wsi_mount_points,
    build,
    pull,
    docker_config=None,
    nginx_port=None,
    wbs_url=None,
    isyntax_sdk=None,
    volume_prefix=None,
    gpu_driver=None,
    frontend_token_exp=None,
    scope_token_exp=None,
    app_ui_frame_ancestors=None,
    app_ui_connect_src=None,
):
    with PrintStep("Check WSI mount points"):
        for key, val in wsi_mount_points.items():
            key_path = Path(key)
            val_path = val

            assert key_path.is_absolute()
            assert val_path.startswith("/")

    services = settings.get_services(
        nginx_port=nginx_port,
        wbs_url=wbs_url,
        isyntax_sdk=isyntax_sdk,
        gpu_driver=gpu_driver,
        frontend_token_exp=frontend_token_exp,
        scope_token_exp=scope_token_exp,
        app_ui_frame_ancestors=app_ui_frame_ancestors,
        app_ui_connect_src=app_ui_connect_src,
    )
    databases = settings.get_databases()
    _ensure_net(client)

    for service in services:
        pull_for_service = pull
        build_for_service = build
        image = service["image"]
        name = service["name"]

        if not image.startswith("eats"):
            if not pull_for_service:
                try:
                    client.images.get(image)
                except docker.errors.ImageNotFound:
                    pull_for_service = True

            if pull_for_service:
                with PrintStep(f"Pulling image: {image}"):
                    client.images.pull(image)

        else:
            if not build_for_service:
                try:
                    client.images.get(image)
                except docker.errors.ImageNotFound:
                    build_for_service = True

            if build_for_service:
                with PrintStep(f"Building image: {image}"):
                    buildargs = None
                    dockerfile_path = service.get("dockerfile_path")
                    client.images.build(
                        path=service["path"], tag=image, buildargs=buildargs, dockerfile=dockerfile_path
                    )
    for db in databases:
        name = db["name"]

        volumes = {_volume_name(db["volume"]["name"], volume_prefix): {"bind": db["volume"]["mount"], "mode": "rw"}}

        with PrintStep(f"Starting: {name}"):
            client.containers.run(
                db["image"],
                name=name,
                detach=True,
                network=settings.EATS_NET,
                environment=db["environment"],
                volumes=volumes,
            )

    for service in services:
        name = service["name"]

        with PrintStep(f"Starting: {name}"):
            volumes = {}

            if "volume" in service:
                volume = service["volume"]
                volumes[_volume_name(volume["name"], volume_prefix)] = {"bind": volume["mount"], "mode": "rw"}

            if name == "wsi-service" or name == "isyntax-backend":
                for key, val in wsi_mount_points.items():
                    volumes[key] = {"bind": val, "mode": "ro"}

            if name == "job-execution-service":
                if docker_config is not None:
                    # just check valid json:
                    with open(docker_config, encoding="utf-8") as f:
                        _docker_conf = json.load(f)
                    volumes[docker_config] = {"bind": "/root/.docker/config.json", "mode": "ro"}

            network = settings.EATS_NET

            client.containers.run(
                service["image"],
                name=service["name"],
                detach=True,
                network=network,
                environment=service["environment"],
                command=service["command"],
                ports=service.get("ports"),
                volumes=volumes,
                extra_hosts=service.get("extra_hosts"),
            )
