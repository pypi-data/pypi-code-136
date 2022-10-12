import json
from datetime import datetime
from uuid import uuid4

import requests

from .constants import STATIC_ORGANIZATION_ID
from .print_helpers import PrintStep
from .py_ead_validation.py_ead_validation.ead_validator import validate_ead, validate_ead_with_config
from .py_ead_validation.py_ead_validation.exceptions import (
    ConfigValidationError,
    EadSchemaValidationError,
    EadValidationError,
)
from .shared import ValidationError, get_service_url


def get_mps_apps_list(client):
    headers = {"organization-id": STATIC_ORGANIZATION_ID}
    mps_url = get_service_url(client=client, service_name="marketplace-service-mock")
    r = requests.put(f"{mps_url}/v1/customer/portal-apps/query", json={}, headers=headers)
    r.raise_for_status()
    return r.json()


def apps_register(client, ead, docker_image, config_file=None, app_ui_url=None, app_ui_config_file=None):
    mps_url = get_service_url(client=client, service_name="marketplace-service-mock")
    aaa_url = get_service_url(client=client, service_name="aaa-service-mock")

    with PrintStep("Validate EAD"):
        _validate_ead(ead)
    with PrintStep("Validate configuration"):
        config = _validate_configuration_parameters(ead, config_file)
    if len(client.images.list(name=docker_image)) == 0:
        with PrintStep(f"Pull image {docker_image}"):
            client.images.pull(docker_image)
    else:
        with PrintStep("Image found on host system"):
            pass
    with PrintStep("Register app"):
        aaa_orga = _generate_organization_json(name="placeholder", organization_id=1)
        _aaa_post_organization(aaa_url, aaa_orga)
        mps_app = _generate_app_json(ead, docker_image, aaa_orga, app_ui_url)
        _mps_post_app(mps_url, mps_app)
        app_id = mps_app["active_preview"]["app"]["id"]
    if config_file:
        with PrintStep("Register configuration"):
            _register_configuration_parameters(app_id, config_file, config, mps_url)
    if app_ui_config_file:
        with PrintStep("Register app-ui configuration"):
            with open(app_ui_config_file, "r", encoding="utf-8") as f:
                app_ui_config = json.load(f)
            _register_app_ui_configuration(app_id, app_ui_config_file, app_ui_config, mps_url)

    return mps_app


def _generate_app_json(ead: dict, docker_registry: str, organization: dict, app_ui_url: str):
    now = str(datetime.now())

    data = {
        "id": str(uuid4()),
        "organization_id": organization["keycloak_id"],
        "status": "LISTED",
        "active_preview": {
            "version": ead["namespace"].split(".")[-1],
            "details": {
                "name": ead["namespace"],
                "description": [
                    {"lang": "EN", "text": ead["description"]},
                    {"lang": "DE", "text": ead["description"]},
                ],
                "marketplace_url": "http://url.to/store",
            },
            "media": {
                "peek": [
                    {
                        "index": 0,
                        "caption": [
                            {"lang": "EN", "text": "Peek caption"},
                            {"lang": "DE", "text": "Titel Übersichtsbild"},
                        ],
                        "alt_text": [
                            {"lang": "EN", "text": "Peek alternative text"},
                            {"lang": "DE", "text": "Alternativtext Übersichtsbild"},
                        ],
                        "internal_path": "/internal/path/to",
                        "content_type": "image/jpeg",
                        "presigned_media_url": "https://url.to/image",
                        "id": str(uuid4()),
                    }
                ]
            },
            "tags": {
                "tissues": [
                    {
                        "name": "SKIN",
                        "tag_translations": [{"lang": "EN", "text": "Skin"}, {"lang": "DE", "text": "Haut"}],
                    }
                ],
                "stains": [],
                "indications": [],
                "analysis": [],
            },
            "id": str(uuid4()),
            "non_functional": False,
            "portal_app_id": str(uuid4()),
            "organization_id": organization["keycloak_id"],
            "status": "APPROVED",
            "app": {
                "ead": ead,
                "registry_image_url": docker_registry,
                "app_ui_url": app_ui_url,
                "id": str(uuid4()),
                "version": "v1.2",
                "status": "APPROVED",
                "has_frontend": bool(app_ui_url),
                "portal_app_id": str(uuid4()),
                "creator_id": str(uuid4()),
                "created_at": now,
                "updated_at": now,
            },
            "creator_id": str(uuid4()),
            "created_at": now,
            "review_comment": "Test comment",
            "reviewer_id": str(uuid4()),
            "reviewed_at": now,
        },
        "creator_id": str(uuid4()),
        "created_at": now,
        "updated_at": now,
    }

    return data


def _generate_organization_json(name: str, organization_id: int):
    now = str(datetime.now())
    data = {
        "organization_id": organization_id,
        "keycloak_id": str(uuid4()),
        "name": name,
        "normalized_name": name,
        "street_name": "string",
        "street_number": "string",
        "zip_code": "string",
        "place_name": "string",
        "country_code": "string",
        "department": "string",
        "email": "string",
        "phone_number": "string",
        "fax_number": "string",
        "website": "string",
        "picture": "https://upload.wikimedia.org/wikipedia/commons/c/ca/Microscope_icon_%28black_OCL%29.svg",
        "organization_role": "AI_VENDOR",
        "account_state": "ACTIVE",
        "date_created": now,
        "date_last_change": now,
        "contact_person_user_id": 0,
        "clientGroups": [
            {
                "client_group_id": 0,
                "group_organization_id": 0,
                "group_type": "AAA_SERVICE",
                "group_namespace": "string",
                "group_authorization_from": [
                    {"client_group_authorization_id": 0, "authorization_from": 0, "authorization_for": 0}
                ],
                "group_authorization_for": [
                    {"client_group_authorization_id": 0, "authorization_from": 0, "authorization_for": 0}
                ],
                "clients": [
                    {
                        "client_id": "string",
                        "name": "string",
                        "url": "string",
                        "group_id": 0,
                        "keycloak_id": "string",
                        "description": "string",
                        "token_lifetime_in_seconds": 0,
                        "redirect_uris": ["string"],
                    }
                ],
            }
        ],
        "solutions": [{"organization_id": 0, "solution_id": 0}],
        "user_count": 0,
    }
    return data


def _register_configuration_parameters(app_id: str, config_file: str, config: dict, mps_url):
    if config_file:
        url = f"{mps_url}/v1/custom-mock/apps/{app_id}/config"
        r = requests.post(url, json=config)
        r.raise_for_status()


def _register_app_ui_configuration(app_id: str, app_ui_config_file: str, app_ui_config: dict, mps_url):
    if app_ui_config_file:
        url = f"{mps_url}/v1/custom-mock/apps/{app_id}/app-ui-config"
        r = requests.post(url, json=app_ui_config)
        r.raise_for_status()


def _validate_ead(ead: dict):
    try:
        validate_ead(ead)
    except EadSchemaValidationError as e:
        error = "Validation of EAD failed: EAD does not match schema."
        raise ValidationError(error) from e
    except EadValidationError as e:
        error = f"Validation of EAD failed: {e}"
        raise ValidationError(error) from e


def _validate_configuration_parameters(ead: dict, config_file: str):
    config = None
    if config_file is not None:
        with open(config_file, "r", encoding="utf-8") as f:
            config = json.load(f)

    try:
        validate_ead_with_config(ead, config=config)
        return config
    except EadValidationError as e:
        error = f"Validation of EAD failed: {e}"
        raise ValidationError(error) from e
    except ConfigValidationError as e:
        error = f"Validation of APP configuration failed: {e}"
        raise ValidationError(error) from e


def _mps_post_app(mps_url, data):
    url = f"{mps_url}/v1/custom-mock/app"
    r = requests.post(url, json=data)
    return r


def _aaa_post_organization(sss_url, data):
    url = f"{sss_url}/api/custom-mock/organization"
    r = requests.post(url, json=data)
    return r
