import functools
import json
import sys
from pathlib import Path

import docker
import requests
import typer

from empaia_app_test_suite import __version__, settings
from empaia_app_test_suite.apps_commands import apps_register, get_mps_apps_list
from empaia_app_test_suite.jobs_commands import (
    get_jobs_list,
    jobs_abort,
    jobs_export,
    jobs_register,
    jobs_run,
    jobs_set_running,
    jobs_status,
    jobs_wait,
)
from empaia_app_test_suite.print_helpers import (
    convert_jobs_list_to_pretty_table,
    convert_mps_apps_list_to_pretty_table,
    convert_slides_list_to_pretty_table,
    print_failed,
    print_table,
    print_table_column,
)
from empaia_app_test_suite.services_commands import (
    services_down,
    services_health,
    services_list,
    services_up,
    services_volumes,
    services_wait,
)
from empaia_app_test_suite.slides_commands import get_slides_list, slides_register


class ExceptionHandlingTyper(typer.Typer):
    eats_settings = settings.EatsSettings()

    def command(self, *cmd_args, **cmd_kwargs):
        def decorator(function):
            @functools.wraps(function)
            def wrapper(*args, **kwargs):
                try:
                    return function(*args, **kwargs)
                except requests.exceptions.HTTPError as exc:
                    if self.eats_settings.debug:
                        raise exc
                    print_failed(f"{type(exc).__name__}: {exc}")
                    response_dict = exc.response.json()
                    if "detail" in response_dict:
                        if isinstance(response_dict["detail"], str):
                            print_failed(response_dict["detail"])
                        if isinstance(response_dict["detail"], dict):
                            for detail_name, detail in response_dict["detail"].items():
                                print_failed(f"{detail_name.upper()}: {detail}")
                    sys.exit(1)
                except Exception as exc:
                    if self.eats_settings.debug:
                        raise exc
                    print_failed(f"{type(exc).__name__}: {exc}")
                    sys.exit(1)

            return typer.Typer.command(self, *cmd_args, **cmd_kwargs)(wrapper)

        return decorator


app = ExceptionHandlingTyper(name="eats")
services_app = ExceptionHandlingTyper()
jobs_app = ExceptionHandlingTyper()
apps_app = ExceptionHandlingTyper()
slides_app = ExceptionHandlingTyper()
app.add_typer(services_app, name="services")
app.add_typer(jobs_app, name="jobs")
app.add_typer(apps_app, name="apps")
app.add_typer(slides_app, name="slides")


WSI_MOUNT_POINTS_FILE_HELP = (
    "Path to JSON file containing mount point mappings of local WSI storage dirs (keys) "
    "to be mounted in WSI Service container dirs (values)."
)
EAD_FILE_HELP = "Path to EMPAIA App Description (EAD) JSON file."
INPUT_DIR_HELP = "Path to job input dir"
APP_ID_HELP = "ID of previously registered App."
V1_SUPPORT = "Setup job to use 'user' as creator of job inputs (support for WBC v1)"
BUILD_HELP = "Force to build service images"
PULL_HELP = "Force to pull service images"
GPU_HELP = "Enable GPU utilization for containerized app."
OUTPUT_DIR_HELP = "Path to job output dir"
TRIALS_SERVICES_HELP = "Number of times to try connecting to all services"
CONFIG_FILE_HELP = "Path to a JSON file containing the configuration items (e.g., secrets) if defined in the EAD"
APP_UI_URL_HELP = "URL and Port of App specific UI to use in WBC 2.0 (e.g., http://host.docker.internal:4300)"
APP_UI_CONFIG_FILE_HELP = "Path to a JSON file containing the app ui configuration"
WBC_PORT_HELP = "Listen port of workbench-client container"
WBC2_PORT_HELP = "Listen port of workbench-client-v2 container"
WBS_PORT_HELP = "Listen port of workbench-service container"
NGINX_PORT_HELP = "Listen port of nginx container"
WBS_URL_HELP = "URL used by workbench-client to access workbench-service (enables custom hosting setups)"
ISYNTAX_SDK_HELP = "Full path to philips-pathologysdk-2.0-ubuntu18_04_py36_research.zip for isyntax support"
VOLUME_PREFIX_HELP = "Prefix for the names of the container volumes holding service state"
GPU_DRIVER_HELP = "GPU driver to use for App images, e.g. 'nvidia' (default: no GPU)"
SLIDE_FILE_HELP = (
    "JSON file containing a [path] defined in WSI_MOUNT_POINTS_FILE "
    "and optionally also [id], [tissue], [stain], [block]"
)
VERSION_HELP = "Shows eats verison"
DOCKER_IMAGE_HELP = (
    "Local docker image name or registry url, e.g. registry.gitlab.com/empaia/integration/sample-apps/"
    "org-empaia-vendor_name-tutorial_app_01:v1"
)
DOCKER_CONFIG_FILE_HELP = (
    "Docker config file. E.g. to pass proxy configuration to the apps by the job-execution-service."
)
APP_LIST_OPTION = "Only output APP IDs list without a heading"
JOB_LIST_OPTION = "Only output JOB IDs list without a heading"
SLIDE_LIST_OPTION = "Only output SlIDE IDs list without a heading"
LIST_BORDER_OPTION = "Add borders to the list ouput"
LIST_FORMAT = "Select another output format (json, markdown, html)"
FE_TOKEN_EXP = "Expiration time in seconds of frontend token (needed to retrieve app ui from workbench service)"
S_TOKEN_EXP = (
    "Expiration time in seconds of scope token (needed to send or retrieve app data to / from workbench service)"
)
APP_UI_FA_HELP = (
    "Content security policy to set allowed frame ancestors for App UI iframes (e.g., http://localhost:8888)"
)
APP_UI_CS_HELP = "Content security policy to set allowed connect sources for App UI iframes (e.g., 'self')"


def _read_job_env(job_env_file):
    try:
        job_env = settings.JobEnv(env_file=job_env_file)
    except UnicodeDecodeError:
        # windows
        job_env = settings.JobEnv(env_file=job_env_file, encoding="utf-16")

    return job_env


def version_callback(value: bool):
    if value:
        typer.echo(__version__)
        raise typer.Exit()


@app.callback()
def _(
    version: bool = typer.Option(None, "--version", callback=version_callback, is_eager=True, help=VERSION_HELP),
):
    return


@app.command("exec")
def _(
    wsi_mount_points_file: Path = typer.Argument(..., help=WSI_MOUNT_POINTS_FILE_HELP),
    ead_file: Path = typer.Argument(..., help=EAD_FILE_HELP),
    docker_image: str = typer.Argument(..., help=DOCKER_IMAGE_HELP),
    input_dir: Path = typer.Argument(..., help=INPUT_DIR_HELP),
    output_dir: Path = typer.Argument(..., help=OUTPUT_DIR_HELP),
    build: bool = typer.Option(False, "--build", help=BUILD_HELP),
    pull: bool = typer.Option(False, "--pull", help=PULL_HELP),
    docker_config: Path = typer.Option(None, "--docker-config", help=DOCKER_CONFIG_FILE_HELP),
    config_file: Path = typer.Option(None, "--config-file", help=CONFIG_FILE_HELP),
    nginx_port: int = typer.Option(8888, "--nginx-port", help=NGINX_PORT_HELP),
    wbs_url: str = typer.Option(None, "--wbs-url", help=WBS_URL_HELP),
    isyntax_sdk: str = typer.Option(None, "--isyntax-sdk", help=ISYNTAX_SDK_HELP),
    volume_prefix: str = typer.Option(None, "--volume-prefix", help=VOLUME_PREFIX_HELP),
    gpu_driver: str = typer.Option(None, "--gpu-driver", help=GPU_DRIVER_HELP),
    frontend_token_exp: int = typer.Option(60, "--frontend-token-exp", help=FE_TOKEN_EXP),
    scope_token_exp: int = typer.Option(300, "--scope-token-exp", help=S_TOKEN_EXP),
    app_ui_frame_ancestors: str = typer.Option(None, "--app-ui-frame-ancestors", help=APP_UI_FA_HELP),
    app_ui_connect_src: str = typer.Option(None, "--app-ui-connect-src", help=APP_UI_CS_HELP),
    v1: bool = typer.Option(False, "--v1", help=V1_SUPPORT),
):
    with open(wsi_mount_points_file, encoding="utf-8") as f:
        wsi_mount_points = json.load(f)

    with open(ead_file, "r", encoding="utf-8") as f:
        ead = json.load(f)

    client = docker.from_env()

    services_down(client=client, volume_prefix=volume_prefix)
    services_up(
        client=client,
        wsi_mount_points=wsi_mount_points,
        docker_config=docker_config,
        build=build,
        pull=pull,
        nginx_port=nginx_port,
        wbs_url=wbs_url,
        isyntax_sdk=isyntax_sdk,
        volume_prefix=volume_prefix,
        gpu_driver=gpu_driver,
        frontend_token_exp=frontend_token_exp,
        scope_token_exp=scope_token_exp,
        app_ui_frame_ancestors=app_ui_frame_ancestors,
        app_ui_connect_src=app_ui_connect_src,
    )
    services_wait(client=client)

    sss_app = apps_register(client, ead, docker_image, config_file)
    app_id = sss_app["id"]

    job_id, token, app_api = jobs_register(client=client, app_id=app_id, input_dir=input_dir, v1=v1)
    jobs_run(client=client, job_id=job_id, token=token, app_api=app_api)

    jobs_wait(client=client, job_id=job_id)
    jobs_export(client=client, job_id=job_id, output_dir=output_dir)

    container = client.containers.get(job_id)
    container.remove(force=True)

    services_down(client=client, volume_prefix=volume_prefix)


@jobs_app.command("exec")
def _(
    app_id: str = typer.Argument(..., help=APP_ID_HELP),
    input_dir: Path = typer.Argument(..., help=INPUT_DIR_HELP),
    output_dir: Path = typer.Argument(..., help=OUTPUT_DIR_HELP),
    v1: bool = typer.Option(False, "--v1", help=V1_SUPPORT),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    job_id, token, app_api = jobs_register(client=client, app_id=app_id, input_dir=input_dir, v1=v1)
    jobs_run(client=client, job_id=job_id, token=token, app_api=app_api)

    jobs_wait(client=client, job_id=job_id)
    jobs_export(client=client, job_id=job_id, output_dir=output_dir)

    container = client.containers.get(job_id)
    container.remove(force=True)

    print(f"EMPAIA_JOB_ID={job_id}")
    print(f"EMPAIA_TOKEN={token}")
    print(f"EMPAIA_APP_API={app_api}")


@services_app.command("up")
def _(
    wsi_mount_points_file: Path = typer.Argument(..., help=WSI_MOUNT_POINTS_FILE_HELP),
    build: bool = typer.Option(False, "--build", help=BUILD_HELP),
    pull: bool = typer.Option(False, "--pull", help=PULL_HELP),
    docker_config: Path = typer.Option(None, "--docker-config", help=DOCKER_CONFIG_FILE_HELP),
    nginx_port: int = typer.Option(8888, "--nginx-port", help=NGINX_PORT_HELP),
    wbs_url: str = typer.Option(None, "--wbs-url", help=WBS_URL_HELP),
    isyntax_sdk: str = typer.Option(None, "--isyntax-sdk", help=ISYNTAX_SDK_HELP),
    volume_prefix: str = typer.Option(None, "--volume-prefix", help=VOLUME_PREFIX_HELP),
    gpu_driver: str = typer.Option(None, "--gpu-driver", help=GPU_DRIVER_HELP),
    frontend_token_exp: int = typer.Option(60, "--frontend-token-exp", help=FE_TOKEN_EXP),
    scope_token_exp: int = typer.Option(300, "--scope-token-exp", help=S_TOKEN_EXP),
    app_ui_frame_ancestors: str = typer.Option(None, "--app-ui-frame-ancestors", help=APP_UI_FA_HELP),
    app_ui_connect_src: str = typer.Option(None, "--app-ui-connect-src", help=APP_UI_CS_HELP),
):
    with open(wsi_mount_points_file, encoding="utf-8") as f:
        wsi_mount_points = json.load(f)

    client = docker.from_env()
    services_down(client=client, volume_prefix=volume_prefix)
    services_up(
        client=client,
        wsi_mount_points=wsi_mount_points,
        docker_config=docker_config,
        build=build,
        pull=pull,
        nginx_port=nginx_port,
        wbs_url=wbs_url,
        isyntax_sdk=isyntax_sdk,
        volume_prefix=volume_prefix,
        gpu_driver=gpu_driver,
        frontend_token_exp=frontend_token_exp,
        scope_token_exp=scope_token_exp,
        app_ui_frame_ancestors=app_ui_frame_ancestors,
        app_ui_connect_src=app_ui_connect_src,
    )


@services_app.command("wait")
def _(
    trials: int = typer.Option(10, "--trials", help=TRIALS_SERVICES_HELP),
):
    client = docker.from_env()
    services_wait(client=client, trials=trials)


@services_app.command("health")
def _():
    client = docker.from_env()
    services_health(client=client)


@jobs_app.command("list")
def _(
    q: bool = typer.Option(None, "-q", help=JOB_LIST_OPTION),
    border: bool = typer.Option(None, "--border", help=LIST_BORDER_OPTION),
    table_format: str = typer.Option(None, "--format", help=LIST_FORMAT),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    jobs = get_jobs_list(client)
    table = convert_jobs_list_to_pretty_table(jobs)
    if q:
        print_table_column(table, "JOB ID")
    else:
        print_table(table, table_format, border)


@jobs_app.command("register")
def _(
    app_id: str = typer.Argument(..., help=APP_ID_HELP),
    input_dir: Path = typer.Argument(..., help=INPUT_DIR_HELP),
    v1: bool = typer.Option(False, "--v1", help=V1_SUPPORT),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    job_id, token, app_api = jobs_register(client=client, app_id=app_id, input_dir=input_dir, v1=v1)

    print(f"EMPAIA_JOB_ID={job_id}")
    print(f"EMPAIA_TOKEN={token}")
    print(f"EMPAIA_APP_API={app_api}")


@jobs_app.command("run")
def _(
    job_env_file: Path = typer.Argument(
        ..., help="Path to job env file containing EMPAIA_JOB_ID, EMPAIA_TOKEN and EMPAIA_APP_API env vars."
    )
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    job_env = _read_job_env(job_env_file)

    job_id = job_env.settings.empaia_job_id
    token = job_env.settings.empaia_token
    app_api = job_env.settings.empaia_app_api

    jobs_run(client=client, job_id=job_id, token=token, app_api=app_api)


@jobs_app.command("status")
def _(job_id: str = typer.Argument(..., help="Job ID.")):
    client = docker.from_env()
    services_health(client=client, silent=True)

    status = jobs_status(client=client, job_id=job_id)

    print(status)


@jobs_app.command("wait")
def _(job_id: str = typer.Argument(..., help="Job ID.")):
    client = docker.from_env()
    services_health(client=client, silent=True)

    jobs_wait(client=client, job_id=job_id)


@jobs_app.command("export")
def _(
    job_id: str = typer.Argument(..., help="Job ID."),
    output_dir: Path = typer.Argument(..., help=OUTPUT_DIR_HELP),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    jobs_export(client=client, job_id=job_id, output_dir=output_dir)


@jobs_app.command("abort")
def _(job_id: str = typer.Argument(..., help="Job ID.")):
    client = docker.from_env()
    services_health(client=client, silent=True)

    jobs_abort(client=client, job_id=job_id)


@jobs_app.command("set-running")
def _(job_id: str = typer.Argument(..., help="Job ID.")):
    client = docker.from_env()
    services_health(client=client, silent=True)

    jobs_set_running(client=client, job_id=job_id)


@services_app.command("list")
def _():
    client = docker.from_env()
    # services_wait(client=client, silent=True)

    services = services_list(client)
    for service in services:
        print(service)


@services_app.command("down")
def _(
    del_volumes: bool = typer.Option(None, "-v", help="Delete volumes"),
    volume_prefix: str = typer.Option(None, "--volume-prefix", help=VOLUME_PREFIX_HELP),
):
    client = docker.from_env()
    services_down(client=client, del_volumes=del_volumes, volume_prefix=volume_prefix)


@services_app.command("volumes")
def _(volume_prefix: str = typer.Option(None, "--volume-prefix", help=VOLUME_PREFIX_HELP)):
    volumes = services_volumes(volume_prefix)
    for volume in volumes:
        print(volume)


@apps_app.command("list")
def _(
    q: bool = typer.Option(None, "-q", help=APP_LIST_OPTION),
    border: bool = typer.Option(None, "--border", help=LIST_BORDER_OPTION),
    table_format: str = typer.Option(None, "--format", help=LIST_FORMAT),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    apps = get_mps_apps_list(client)
    table = convert_mps_apps_list_to_pretty_table(apps)
    if q:
        print_table_column(table, "APP ID")
    else:
        print_table(table, table_format, border)


@apps_app.command("register")
def _(
    ead_file: Path = typer.Argument(..., help=EAD_FILE_HELP),
    docker_image: str = typer.Argument(..., help=DOCKER_IMAGE_HELP),
    config_file: Path = typer.Option(None, "--config-file", help=CONFIG_FILE_HELP),
    app_ui_url: str = typer.Option(None, "--app-ui-url", help=APP_UI_URL_HELP),
    app_ui_config_file: Path = typer.Option(None, "--app-ui-config-file", help=APP_UI_CONFIG_FILE_HELP),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    with open(ead_file, "r", encoding="utf-8") as f:
        ead = json.load(f)
    registered_app = apps_register(client, ead, docker_image, config_file, app_ui_url, app_ui_config_file)
    print(f"APP_ID={registered_app['active_preview']['app']['id']}")


@slides_app.command("register")
def _(
    slide_file: Path = typer.Argument(..., help=SLIDE_FILE_HELP),
    q: bool = typer.Option(None, "-q", help=APP_LIST_OPTION),
    table_format: str = typer.Option(None, "--format", help=LIST_FORMAT),
    border: bool = typer.Option(None, "--border", help=LIST_BORDER_OPTION),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    new_wsis, existing_wsis = slides_register(client=client, slide_file=slide_file, quiet=True)
    added_ids = [wsi.id for wsi in new_wsis + existing_wsis]
    raw_slides = get_slides_list(client)["items"]
    added_slides = []
    for raw_slide in raw_slides:
        if raw_slide["id"] in added_ids:
            added_slides.append(raw_slide)

    table = convert_slides_list_to_pretty_table({"items": added_slides})
    if q:
        print_table_column(table, "SLIDE ID")
    else:
        print_table(table, table_format, border)


@slides_app.command("list")
def _(
    q: bool = typer.Option(None, "-q", help=APP_LIST_OPTION),
    border: bool = typer.Option(None, "--border", help=LIST_BORDER_OPTION),
    table_format: str = typer.Option(None, "--format", help=LIST_FORMAT),
):
    client = docker.from_env()
    services_health(client=client, silent=True)

    slides = get_slides_list(client)
    table = convert_slides_list_to_pretty_table(slides)
    if q:
        print_table_column(table, "SLIDE ID")
    else:
        print_table(table, table_format, border)


if __name__ == "__main__":
    app()
