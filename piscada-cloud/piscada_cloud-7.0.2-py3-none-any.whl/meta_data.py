"""Functions related to the Cloud Meta Data API."""
import os
from typing import Dict, List, Optional, Tuple
from uuid import UUID

import requests

from piscada_cloud.mappings import Tag


def _check_env_vars() -> Tuple[str, str]:
    host = os.getenv("CLOUD_META_DATA_HOST")
    token = os.getenv("CLOUD_META_DATA_TOKEN")
    if not host or not token:
        raise RuntimeError("Both environment variables CLOUD_META_DATA_HOST and CLOUD_META_DATA_TOKEN need to be defined.")
    return host, token


def get_controllers() -> List[Dict]:
    """Get list of accessible controllers.

    Returns
    -------
    List[Dict]
        List of accessible controllers

    Raises
    ------
    RuntimeError
        if response status from Cloud Meta Data API is not 200
    """
    host, token = _check_env_vars()
    response = requests.request("GET", f"https://{host}/v0/controllers", headers={"Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        raise RuntimeError(f"Cloud Meta Data API gave response: {response.status_code}: {response.text}")
    return response.json()


def get_tags(controller_uuid: Optional[UUID] = None, name: Optional[str] = None, path: Optional[str] = None, uuid: Optional[UUID] = None) -> List[Tag]:
    """List accessible tags with filtering.

    Paraneters
    ----------
    controller_uuid: Optional[UUID]
        UUID of the controller the tag(s) are associated with
    name: Optional[str]
        Tag name
    path: Optional[str]
        Tag path
    uuid: Optional[UUID]
        Tag UUID

    Returns
    -------
    List[Tag]
        Tags matching provided filter

    Raises
    ------
    RuntimeError
        if Cloud Meta Data API does not respond with status 200
    """
    host, token = _check_env_vars()
    if not (controller_uuid is None or isinstance(controller_uuid, UUID)):
        raise ValueError("controller_uuid must be of type UUID")
    if not (uuid is None or isinstance(uuid, UUID)):
        raise ValueError("uuid must be of type UUID")
    query_params = [f"{key}={value}" for key, value in {"controller-uuid": controller_uuid, "name": name, "path": path, "uuid": uuid}.items() if value is not None]
    url = f"https://{host}/v0/tags"
    if len(query_params) > 0:
        url += "?" + "&".join(query_params)
    response = requests.request("GET", url, headers={"Authorization": f"Bearer {token}"})
    if response.status_code != 200:
        raise RuntimeError(f"Cloud Meta Data API gave response: {response.status_code}: {response.text}")
    return [Tag(controller_id=meta_data["controller-uuid"], uuid=meta_data["uuid"], name=meta_data["name"], path=meta_data["path"]) for meta_data in response.json()]
