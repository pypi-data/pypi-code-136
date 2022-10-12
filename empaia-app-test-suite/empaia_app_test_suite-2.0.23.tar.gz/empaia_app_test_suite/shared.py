import json
import os

import requests

from .constants import ALLOWED_ANNOTATION_TYPES, ALLOWED_PRIMITIVE_TYPES, SERVICE_API_MAPPING
from .settings import get_services


class ValidationError(Exception):
    pass


def get_service_url(client, service_name):
    services = get_services()
    nginx = {}
    for service in services:
        if service["name"] == "nginx":
            nginx = service
    for service in services:
        if service["name"] != service_name:
            continue
        if service["name"] in SERVICE_API_MAPPING:
            container = client.containers.get("nginx")
            internal_port = list(nginx["ports"].keys())[0]
            container_info = client.api.port(container.id, internal_port)
            host_port = container_info[0]["HostPort"]
            return f"http://127.0.0.1:{host_port}/{SERVICE_API_MAPPING[service_name]}"

        return None


def save_output_parameters(job, mds_url, output_dir):
    ead = job["ead"]
    for output_key, output_id in job["outputs"].items():
        output_type = ead["outputs"][output_key]["type"]
        return_data = {}
        file_name_ext = ""
        if output_type in ALLOWED_ANNOTATION_TYPES:
            r = requests.get(f"{mds_url}/v1/annotations/{output_id}")
            r.raise_for_status()
            return_data = r.json()
        elif output_type in ALLOWED_PRIMITIVE_TYPES:
            r = requests.get(f"{mds_url}/v1/primitives/{output_id}")
            r.raise_for_status()
            return_data = r.json()
        elif output_type == "collection":
            return_data = get_collection(output_id, mds_url)
        elif output_type == "class":
            r = requests.get(f"{mds_url}/v1/classes/{output_id}")
            r.raise_for_status()
            return_data = r.json()
        else:
            raise Exception("Unknown output type {output_type} for output key {output_key}.")

        with open(os.path.join(output_dir, f"{output_key}{file_name_ext}.json"), "w", encoding="utf-8") as f:
            f.write(json.dumps(clean_dict(return_data), indent=4))


def clean_dict(d):
    if not isinstance(d, (dict, list)):
        return d
    elif isinstance(d, list):
        return [v for v in (clean_dict(v) for v in d) if v is not None]
    else:
        return {k: v for k, v in ((k, clean_dict(v)) for k, v in d.items()) if v is not None}


def post_collection(data: str, mds_url: str, params: dict):
    empty_collection = {}
    for key in data:
        if key == "items":
            empty_collection[key] = []
        else:
            empty_collection[key] = data[key]
    r = requests.post(f"{mds_url}/v1/collections", json=empty_collection, params=params)
    r.raise_for_status()
    empty_collection = r.json()
    collection = extend_collection(empty_collection, data["items"], mds_url, params)
    return collection


def extend_collection(empty_collection: dict, items: dict, mds_url: str, params: dict, batch_size: int = 1000):
    inner_type = empty_collection["item_type"]
    skip = 0
    while skip < len(items):
        batch = {"items": []}
        if inner_type == "collection":
            for item in items[skip : skip + batch_size]:
                inner_collection = {}
                for key in item:
                    if key == "items":
                        inner_collection[key] = []
                    else:
                        inner_collection[key] = item[key]
                batch["items"].append(inner_collection)
            r = requests.post(f"{mds_url}/v1/collections/{empty_collection['id']}/items", json=batch, params=params)
            r.raise_for_status()
            posted_collections = r.json()
            for collection in posted_collections["items"]:
                for orig_collection in items:
                    if orig_collection["id"] == collection["id"]:
                        collection = extend_collection(collection, orig_collection["items"], mds_url, params)
            if "items" not in empty_collection:
                empty_collection["items"] = []
            empty_collection["items"] += posted_collections["items"]
        else:
            batch["items"] += items[skip : skip + batch_size]
            r = requests.post(f"{mds_url}/v1/collections/{empty_collection['id']}/items", json=batch, params=params)
            r.raise_for_status()
            posted_items = r.json()
            if "items" not in empty_collection:
                empty_collection["items"] = []
            empty_collection["items"] += posted_items["items"]
        skip += batch_size
    return empty_collection


def get_collections_items(collection: dict, mds_url, batch_size: int = 1000):
    if collection["item_type"] == "collection":
        for inner in collection["items"]:
            inner = get_collections_items(inner, mds_url, batch_size)
    else:
        skip = 0
        limit = batch_size
        if "items" not in collection:
            collection["items"] = []
        while skip < collection["item_count"]:
            params = {"skip": skip, "limit": limit}
            r = requests.put(f"{mds_url}/v1/collections/{collection['id']}/items/query", json={}, params=params)
            r.raise_for_status()
            batch = r.json()["items"]
            collection["items"] += batch
            skip += batch_size
    return collection


def get_collection(collection_id: str, mds_url: str, batch_size: int = 1000):
    try:
        r = requests.get(f"{mds_url}/v1/collections/{collection_id}")
        r.raise_for_status()
        collection = r.json()
    except requests.exceptions.HTTPError as error:
        if "Request Entity Too Large" not in str(error):
            raise error
        r = requests.get(f"{mds_url}/v1/collections/{collection_id}?shallow=true")
        r.raise_for_status()
        collection = r.json()
        collection = get_collections_items(collection, mds_url, batch_size)
    return collection


def get_annotation(annotation_id: str, mds_url: str):
    url = f"{mds_url}/v1/annotations/{annotation_id}"
    params = {"with_classes": True}
    raw_annotation = requests.get(url, params=params)
    return raw_annotation.json()
