import os
import pathlib
import shutil

import toml
import yaml
from dotenv import dotenv_values
from pydantic import BaseModel, BaseSettings

from . import __version__
from .constants import STATIC_ORGANIZATION_ID, STATIC_USER_ID

EAD_SCHEMA_FILE = "ead-app-schema-draft-3.json"
EATS_NET = "eats"


def get_docker_compose_dict():
    path_to_this_file = pathlib.Path(__file__).parent.absolute()
    path_to_docker_compose_file = os.path.join(path_to_this_file, "services", "docker-compose.yml")
    with open(path_to_docker_compose_file, encoding="utf-8") as stream:
        return yaml.safe_load(stream)


class JobEnv:
    class JobEnvSettings(BaseModel):
        empaia_job_id: str
        empaia_token: str
        empaia_app_api: str

    def __init__(self, env_file, encoding="utf-8"):
        values = dotenv_values(env_file, encoding=encoding)
        values = {key.lower(): val for key, val in values.items()}
        self.settings = self.JobEnvSettings(**values)


class EatsSettings(BaseSettings):
    debug: bool = False

    class Config:
        env_prefix = "eats_"
        env_file = ".env"


def get_databases():
    docker_compose_dict = get_docker_compose_dict()
    return [
        {
            "name": "eats-postgres-db",
            "image": docker_compose_dict["services"]["eats-postgres-db"]["image"],
            "command": "postgres -c config_file=/etc/postgresql/postgresql.conf",
            "environment": {
                "POSTGRES_DB": "eats",
                "POSTGRES_USER": "empaia",
                "POSTGRES_PASSWORD": "empaia",
            },
            "volume": {
                "name": "eats-postgres-db-vol",
                "mount": "/var/lib/postgresql/data",
            },
        },
        {
            "name": "eats-mongo-db",
            "image": docker_compose_dict["services"]["eats-mongo-db"]["image"],
            "environment": {},
            "volume": {
                "name": "eats-mongo-db-vol",
                "mount": "/data/db",
            },
        },
    ]


def get_services(
    nginx_port=None,
    wbs_url=None,
    isyntax_sdk=None,
    gpu_driver=None,
    frontend_token_exp=None,
    scope_token_exp=None,
    app_ui_frame_ancestors=None,
    app_ui_connect_src=None,
):
    nginx_port = nginx_port or 8888
    frontend_token_exp = frontend_token_exp or 86400
    scope_token_exp = scope_token_exp or 86400

    wbs_url = wbs_url.rstrip("/") if wbs_url else f"http://localhost:{nginx_port}/wbs-api"

    if app_ui_frame_ancestors is None:
        app_ui_frame_ancestors = ""

    if app_ui_connect_src is None:
        app_ui_connect_src = ""

    path_to_this_file = pathlib.Path(__file__).parent.absolute()
    path_to_services = os.path.join(path_to_this_file, "services")
    default_version = f"eats-{__version__}"

    docker_compose_dict = get_docker_compose_dict()

    services = [
        {
            "name": "app-service",
            "image": docker_compose_dict["services"]["app-service"]["image"],
            "environment": {
                "AS_IDP_URL": "https://url",
                "AS_MPS_URL": "http://marketplace-service-mock:8000",
                "AS_MPS_USE_V1_ROUTES": "True",
                "AS_CLIENT_ID": "id",
                "AS_CLIENT_SECRET": "secret",
                "AS_MDS_URL": "http://medical-data-service:8000",
                "AS_ROOT_PATH": "/app-api",
                "NO_PROXY": "url,marketplace-service-mock,medical-data-service",
                "AS_ORGANIZATION_ID": STATIC_ORGANIZATION_ID,
            },
            "command": ["--port=8000", "--host=0.0.0.0"],
            "ports": {},
        },
        {
            "name": "annotation-service",
            "image": docker_compose_dict["services"]["annotation-service"]["image"],
            "environment": {
                "ANNOT_DB_HOST": "eats-postgres-db",
                "ANNOT_DB_PORT": 5432,
                "ANNOT_DB": "eats",
                "ANNOT_DB_USERNAME": "empaia",
                "ANNOT_DB_PASSWORD": "empaia",
                "ANNOT_API_V1_INTEGRATION": "annotation_service.api.v1.integrations.disable_auth:DisableAuth",
                "ANNOT_ALLOW_EXTERNAL_IDS": "True",
                "ANNOT_ITEM_LIMIT": 10000,
                "ANNOT_POST_LIMIT": 10000,
                "NO_PROXY": "eats-postgres-db",
            },
            "command": ["run.sh", "--host=0.0.0.0", "--workers=4", "--port=8000"],
            "ports": {},
        },
        {
            "name": "job-service",
            "image": docker_compose_dict["services"]["job-service"]["image"],
            "environment": {
                "JS_DB_HOST": "eats-postgres-db",
                "JS_DB_PORT": 5432,
                "JS_DB": "eats",
                "JS_DB_USERNAME": "empaia",
                "JS_DB_PASSWORD": "empaia",
                "JS_RSA_KEYS_DIRECTORY": "/app/rsa",
                "NO_PROXY": "eats-postgres-db",
            },
            "command": ["run.sh", "--host=0.0.0.0", "--port=8000"],
            "ports": {},
            "volume": {
                "name": "job-service-vol",
                "mount": "/app/rsa",
            },
        },
        {
            "name": "examination-service",
            "image": docker_compose_dict["services"]["examination-service"]["image"],
            "environment": {
                "ES_DB_HOST": "eats-postgres-db",
                "ES_DB_PORT": 5432,
                "ES_DB": "eats",
                "ES_DB_USERNAME": "empaia",
                "ES_DB_PASSWORD": "empaia",
                "ES_API_V1_INTEGRATION": "examination_service.api.v1.integrations.disable_auth:DisableAuth",
                "ES_SCOPE_TOKEN_EXP": scope_token_exp,
                "NO_PROXY": "eats-postgres-db",
            },
            "command": ["run.sh", "--host=0.0.0.0", "--port=8000"],
            "ports": {},
        },
        {
            "name": "clinical-data-service",
            "image": docker_compose_dict["services"]["clinical-data-service"]["image"],
            "environment": {
                "CDS_DB_HOST": "eats-postgres-db",
                "CDS_DB_PORT": 5432,
                "CDS_DB": "eats",
                "CDS_DB_USERNAME": "empaia",
                "CDS_DB_PASSWORD": "empaia",
                "CDS_ALLOW_EXTERNAL_IDS": "True",
                "NO_PROXY": "eats-postgres-db",
            },
            "command": ["run.sh", "--host=0.0.0.0", "--port=8000"],
            "ports": {},
        },
        {
            "name": "storage-mapper-service",
            "image": docker_compose_dict["services"]["storage-mapper-service"]["image"],
            "environment": {
                "SM_DB_USERNAME": "empaia",
                "SM_DB_PASSWORD": "empaia",
                "SM_DB": "eats",
                "SM_DB_HOST": "eats-postgres-db",
                "SM_DB_PORT": 5432,
                "NO_PROXY": "eats-postgres-db",
            },
            "command": [],
            "ports": {},
        },
        {
            "name": "wsi-service",
            "image": docker_compose_dict["services"]["wsi-service"]["image"],
            "environment": {
                "WS_DATA_DIR": "/data",
                "WS_MAPPER_ADDRESS": "http://storage-mapper-service:8000/v1/slides/{slide_id}",
                "NO_PROXY": "storage-mapper-service",
            },
            "command": [],
            "ports": {},
        },
        {
            "name": "medical-data-service",
            "image": docker_compose_dict["services"]["medical-data-service"]["image"],
            "environment": {
                "MDS_API_V1_INTEGRATION": "medical_data_service.api.v1.integrations.disable_auth:DisableAuth",
                "MDS_WS_URL": "http://wsi-service:8080",
                "MDS_SMS_URL": "http://storage-mapper-service:8000",
                "MDS_JS_URL": "http://job-service:8000",
                "MDS_AS_URL": "http://annotation-service:8000",
                "MDS_CDS_URL": "http://clinical-data-service:8000",
                "MDS_ES_URL": "http://examination-service:8000",
                "MDS_ROOT_PATH": "/mds-api",
                "NO_PROXY": "wsi-service,storage-mapper-service,job-service,annotation-service,"
                + "clinical-data-service,examination-service",
            },
            "command": ["uvicorn", "--host=0.0.0.0", "--port=8000", "--workers=2", "medical_data_service.app:app"],
            "ports": {},
        },
        {
            "name": "marketplace-service-mock",
            "image": docker_compose_dict["services"]["marketplace-service-mock"]["image"],
            "environment": {
                "MPSM_API_INTEGRATION": "marketplace_service_mock.api.integrations.disable_auth:DisableAuth",
                "MPSM_ROOT_PATH": "/mps-api",
                "MPSM_DISABLE_API_V0": "True",
                "MPSM_ENABLE_API_V1": "True",
            },
            "command": ["uvicorn", "--host=0.0.0.0", "--port=8000", "marketplace_service_mock.app:app"],
            "ports": {},
            "volume": {
                "name": "marketplace-service-mock-vol",
                "mount": "/data",
            },
        },
        {
            "name": "aaa-service-mock",
            "image": docker_compose_dict["services"]["aaa-service-mock"]["image"],
            "environment": {
                "AAAM_API_V1_INTEGRATION": "aaa_service_mock.api.v1.integrations.disable_auth:DisableAuth",
                "AAAM_ROOT_PATH": "/aaa-api",
            },
            "command": ["uvicorn", "--host=0.0.0.0", "--port=8000", "aaa_service_mock.app:app"],
            "ports": {},
            "volume": {
                "name": "aaa-service-mock-vol",
                "mount": "/data",
            },
        },
        {
            "name": "job-execution-service",
            "image": docker_compose_dict["services"]["job-execution-service"]["image"],
            "environment": {
                "JES_DATABASE_URL": "mongodb://eats-mongo-db:27017",
                "JES_DOCKER_NETWORK": EATS_NET,
                "JES_DOCKER_GPU_DRIVER": gpu_driver,
                "JES_JOB_RUNNER": "EVENTED",
                "JES_MAX_NUMBER_OF_JOBS": 1,
                "JES_ENABLE_RECEIVER_AUTH": "False",
                "JES_DOCKER_ALWAYS_PULL": "False",
                "JES_MPS_URL": "http://marketplace-service-mock:8000",
                "JES_MPS_USE_V1_ROUTES": "True",
                "JES_ROOT_PATH": "/jes-api",
                "NO_PROXY": "eats-mongo-db,marketplace-service-mock",
            },
            "command": [],
            "ports": {},
            "volume": {
                "name": "/var/run/docker.sock",
                "mount": "/var/run/docker.sock",
            },
        },
        {
            "name": "workbench-daemon",
            "image": docker_compose_dict["services"]["workbench-daemon"]["image"],
            "environment": {
                "WBS_MEDICAL_DATA_SERVICE_URL": "http://medical-data-service:8000",
                "WBS_JOB_EXECUTION_SERVICE_URL": "http://job-execution-service:8000",
                "WBS_APP_SERVICE_URL": "http://app-service:8000",
                "WBS_ORGANIZATION_ID": STATIC_ORGANIZATION_ID,
                "NO_PROXY": "medical-data-service,job-execution-service",
            },
            "command": ["wbd"],
            "ports": {},
        },
        {
            "name": "workbench-service",
            "image": docker_compose_dict["services"]["workbench-service"]["image"],
            "environment": {
                "WBS_ENABLE_EATS_MODE": "True",
                "WBS_AAA_SERVICE_URL": "http://aaa-service-mock:8000",
                "WBS_MEDICAL_DATA_SERVICE_URL": "http://medical-data-service:8000",
                "WBS_APP_SERVICE_URL": "http://app-service:8000",
                "WBS_JOB_EXECUTION_SERVICE_URL": "http://job-execution-service:8000",
                "WBS_MARKETPLACE_SERVICE_URL": "http://marketplace-service-mock:8000",
                "WBS_CORS_ALLOW_ORIGINS": '["*"]',
                "WBS_API_V1_INTEGRATION": "workbench_service.api.v1.integrations.disable_auth:DisableAuth",
                "WBS_API_V2_INTEGRATION": "workbench_service.api.v2.integrations.disable_auth:DisableAuth",
                "WBS_ORGANIZATION_ID": STATIC_ORGANIZATION_ID,
                "WBS_FRONTEND_TOKEN_EXP": frontend_token_exp,
                "WBS_ROOT_PATH": "/wbs-api",
                "WBS_APP_UI_FRAME_ANCESTORS": app_ui_frame_ancestors,
                "WBS_APP_UI_CONNECT_SRC": app_ui_connect_src,
                "NO_PROXY": "aaa-service-mock,medical-data-service,app-service,job-execution-service,"
                + "marketplace-service-mock",
                "WBS_FRONTEND_CSP_URL": f"http://localhost:{nginx_port}",
            },
            "command": ["run.sh", "--host=0.0.0.0", "--port=8000"],
            "ports": {},
            "extra_hosts": {"host.docker.internal": "host-gateway"},
        },
        {
            "name": "workbench-client",
            "image": docker_compose_dict["services"]["workbench-client"]["image"],
            "environment": {
                "WBC_WBS_SERVER_API_URL": wbs_url,
                "WBC_WBS_USER_ID": STATIC_USER_ID,
                "NO_PROXY": "NO_PROXY",
            },
            "ports": {},
            "command": [],
        },
        {
            "name": "workbench-client-v2",
            "image": docker_compose_dict["services"]["workbench-client-v2"]["image"],
            "environment": {
                "WBC_WBS_SERVER_API_URL": wbs_url,
                "WBC_WBS_USER_ID": STATIC_USER_ID,
                "NO_PROXY": "localhost,127.0.0.1",
            },
            "ports": {},
            "command": [],
        },
        {
            "name": "workbench-client-v2-sample-ui",
            "image": docker_compose_dict["services"]["workbench-client-v2-sample-ui"]["image"],
            "environment": {
                "NO_PROXY": "localhost,127.0.0.1",
            },
            "command": [],
        },
        {
            "name": "nginx",
            "environment": {},
            "path": str(pathlib.Path(path_to_services, "nginx")),
            "dockerfile_path": "Dockerfile",
            "ports": {"80": nginx_port},
            "command": [],
        },
    ]

    # check for isyntax sdk
    isyntax_sdk_path = os.path.join(
        path_to_services,
        "wsi-service-plugin-isyntax/isyntax_backend",
        "philips-pathologysdk-2.0-ubuntu18_04_py36_research.zip",
    )
    if isyntax_sdk:
        shutil.copy(isyntax_sdk, isyntax_sdk_path)
        services.append(
            {
                "name": "isyntax-backend",
                "environment": {},
                "ports": {},
                "command": [],
                "path": str(pathlib.Path(path_to_services, "wsi-service-plugin-isyntax/isyntax_backend")),
            }
        )

    for service in services:
        if "path" not in service:
            service["path"] = str(pathlib.Path(path_to_services, service["name"]))

        if "image" not in service:
            pyproject_file = pathlib.Path(service["path"], "pyproject.toml")
            version = default_version
            if pyproject_file.exists():
                version = toml.load(pyproject_file)["tool"]["poetry"]["version"]
            service["image"] = "eats-" + service["name"] + ":" + version

    return services
