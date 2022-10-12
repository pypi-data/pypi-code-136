import json
import os
from copy import deepcopy
from pathlib import Path
from typing import List
from uuid import uuid4

import requests
from pydantic import ValidationError as PydanticValidationError
from requests import HTTPError

from .constants import ALLOWED_ANNOTATION_TYPES, ALLOWED_PRIMITIVE_TYPES, STATIC_CASE_ID, STATIC_USER_ID
from .custom_models import ApiDataType, InputParameter, WsiInput, extend_type_inplace, parse_input_item
from .shared import ValidationError, get_collection, post_collection


def create_static_case_if_not_exists(mds_url):
    # create / get case
    r = requests.get(f"{mds_url}/v1/cases/{STATIC_CASE_ID}")
    if r.status_code == 400:
        data = {
            "description": "A very interesting example case",
            "id": STATIC_CASE_ID,
            "creator_id": STATIC_USER_ID,
            "creator_type": "USER",
        }
        r = requests.post(f"{mds_url}/v1/cases", json=data, params={"external_ids": True})
        r.raise_for_status()


def get_or_create_examination_if_none_open(mds_url):
    # get open examination on that case, create if none exists
    query = {"cases": [STATIC_CASE_ID]}
    r = requests.put(f"{mds_url}/v1/examinations/query", json=query)
    r.raise_for_status()
    examinations = r.json()["items"]
    open_exs = []
    for ex in examinations:
        if ex["state"] == "OPEN":
            open_exs.append(ex)
    if len(open_exs) == 0:
        data = {"case_id": STATIC_CASE_ID, "creator_id": STATIC_USER_ID, "creator_type": "USER"}
        r = requests.post(f"{mds_url}/v1/examinations", json=data)
        r.raise_for_status()
        ex = r.json()
    else:
        ex = open_exs[0]
    return ex


def get_or_create_scope(mds_url, ex_id, app_id):
    # create or get scope
    data = {"examination_id": ex_id, "app_id": app_id, "user_id": STATIC_USER_ID}
    try:
        r = requests.post(f"{mds_url}/v1/scopes", json=data)
        r.raise_for_status()
        return r.json()["id"]
    except HTTPError:
        r = requests.put(f"{mds_url}/v1/scopes", json=data)
        r.raise_for_status()
        return r.json()["id"]


def add_app_to_examination(mds_url, app_id, ex_id):
    # add app to examination
    r = requests.put(f"{mds_url}/v1/examinations/{ex_id}/apps/{app_id}/add")
    if r.status_code <= 299 or r.status_code == 405:
        pass
    else:
        r.raise_for_status()


def add_job_to_examination(mds_url, app_id, job_id, ex_id):
    # add job to examination
    r = requests.put(f"{mds_url}/v1/examinations/{ex_id}/apps/{app_id}/jobs/{job_id}/add")
    r.raise_for_status()


def validate_input_parameters_files(ead, input_dir):
    # validate file exists for each input
    for input_key, input_data in ead["inputs"].items():
        input_file = os.path.join(input_dir, f"{input_key}.json")
        if not os.path.isfile(input_file):
            raise ValidationError(f"Validating [{input_key}] failed: No input file found")
        try:
            # pydantic model validation
            parse_input_item(input_data["type"], input_file)
        except PydanticValidationError as e:
            raise ValidationError(f"Validating [{input_key}] failed: \n{e.json()}") from e


def _is_ead_input_or_class(ead, input_key, data):
    if input_key in ead["inputs"]:
        return True
    if "value" in data and "reference_id" in data:
        return True
    if "item_type" in data:
        if data["item_type"] == "class":
            return True
        if data["item_type"] == "collection":
            return _is_ead_input_or_class(ead, input_key, data["items"][0])
    return False


def parse_input_parameters_files(ead, input_dir, v1, scope_id):
    # semantic validation and data extension
    inputs_to_register = []
    wsis_to_register = []
    job_inputs = {}
    for path in Path(input_dir).glob("*.json"):
        with open(path, "rb") as data_file:
            data = json.loads(data_file.read())
            extend_type_inplace(data)
            input_key = path.stem
            if _is_ead_input_or_class(ead, input_key, data):
                # single wsi
                if is_single_wsi_input(data):
                    input_type = _get_type(data)
                    extend_id_inplace(data)
                    append_wsis_in_input_dict_to_list(data, wsis_to_register)
                # wsi collection
                elif is_wsi_collection(data):
                    input_type = _get_type(data)
                    # check if either all collection items (incl. collection) either dont have ID or all do have
                    _check_collections_and_items_id(path, data)
                    # recursive add missing ids
                    extend_id_inplace(data)
                    data_copy = deepcopy(data)
                    append_wsis_in_input_dict_to_list(data_copy, wsis_to_register)
                    # recursive add creator_type and creator_id
                    _extend_creator_inplace(data, v1, scope_id)
                    # for wsi collections, the leafs only have "id"
                    _strip_wsi_collection(input_key, data)
                    reference_ids = []
                    entry = InputParameter(
                        input_key=input_key, post_data=data, api_data_type=input_type, reference_ids=reference_ids
                    )
                    inputs_to_register.append(entry)
                # rest
                else:
                    input_type = _get_type(data)
                    # configuration file residing in inputs folder might be None
                    if input_type is not None:
                        # check if either all collection items (incl. collection) either dont have ID or all do have
                        _check_collections_and_items_id(path, data)
                        # check if classes and annotations have reference_id
                        _check_reference_id(path, data)
                        # recursive add creator_type and creator_id
                        _extend_creator_inplace(data, v1, scope_id)
                        # recursive add missing ids
                        extend_id_inplace(data)
                        # recursive get all reference_ids
                        reference_ids = _get_reference_ids(data)
                        entry = InputParameter(
                            input_key=input_key, post_data=data, api_data_type=input_type, reference_ids=reference_ids
                        )
                        inputs_to_register.append(entry)
                # for all
                # classes, e.g. rois, are not listed in the ead/job!
                if input_key in ead["inputs"]:
                    job_inputs[input_key] = data["id"]

    return inputs_to_register, wsis_to_register, job_inputs


def remove_already_existing_inputs(inputs_to_register: List[InputParameter], mds_url: str):
    inputs_to_register_new = []
    input_ids_already_registered = []
    for input_param in inputs_to_register:
        # input id does not exist
        if not _check_input_with_id_exist(input_param, mds_url):
            inputs_to_register_new.append(input_param)
        # input id already exists AND data has not changed
        else:
            input_ids_already_registered += _get_ids(input_param.post_data)
    return inputs_to_register_new, input_ids_already_registered


def register_wsis(wsis_to_register: List[WsiInput], mds_url: str):
    url_cds = f"{mds_url}/v1/slides"
    url_storage = f"{mds_url}/v1/slides/storage"
    for wsi_info in wsis_to_register:
        # CDS
        post_data_cds = {
            "tissue": wsi_info.tissue,
            "stain": wsi_info.stain,
            "block": wsi_info.block,
            "id": wsi_info.id,
            "case_id": STATIC_CASE_ID,
        }
        r = requests.post(url_cds, json=post_data_cds, params={"external_ids": True})
        r.raise_for_status()
        if r.status_code in [200, 201]:
            # SMS
            post_data_storage = {
                "slide_id": wsi_info.id,
                "storage_type": "fs",
                "storage_addresses": [
                    {
                        "storage_address_id": str(uuid4()),
                        "slide_id": wsi_info.id,
                        "address": str(wsi_info.path),
                        "main_address": True,
                    }
                ],
            }
            r = requests.post(url_storage, json=post_data_storage)
            r.raise_for_status()
    wsi_ids = [wsi.id for wsi in wsis_to_register]
    return wsi_ids


def validate_wsis_with_existing_wsis(wsis_to_register: List[WsiInput], mds_url: str):
    new_wsis = []
    existing_wsis = []
    for wsi_info in wsis_to_register:
        # check values equal in CDS
        r = requests.get(f"{mds_url}/v1/slides/{wsi_info.id}")
        wsi = wsi_info.dict()
        if r.status_code != 400:  # Not "Not found" (= already exists)
            existing_slide_cds = r.json()
            for p in ["tissue", "stain", "block"]:
                if existing_slide_cds[p] != wsi[p]:
                    error_msg = (
                        f"Slide with id [{wsi_info.id}] already exists but with a different value for {p}: [{wsi[p]}]."
                    )
                    raise Exception(error_msg)
            existing_wsis.append(wsi_info)
        else:
            new_wsis.append(wsi_info)
        # check values equal in SMS
        r = requests.get(f"{mds_url}/v1/slides/{wsi_info.id}/storage")
        if r.status_code != 404:  # Not "Not found" (= already exists)
            existing_slide_sms = r.json()
            for address in existing_slide_sms["storage_addresses"]:
                if address["main_address"]:
                    if address["address"] != wsi_info.path:
                        error_msg = (
                            f"Slide with id [{wsi_info.id}] already exists "
                            f"but with a different path: {address['address']}"
                        )
                        raise Exception(error_msg)
    return new_wsis, existing_wsis


def validate_wsis_current_job_inputs(wsis_to_register: List[WsiInput]):
    no_duplicate_wsis = []
    duplicate_wsis = []
    wsis = {}
    for wsi_info in wsis_to_register:
        wsi_1 = wsi_info.dict()
        if "id" in wsi_1:
            if wsi_1["id"] in wsis:
                wsi_2 = wsis[wsi_1["id"]]
                for key in wsi_1:
                    if key in wsi_2:
                        if wsi_1[key] != wsi_2[key]:
                            error_msg = (
                                f"Slide with id [{wsi_1['id']}] already in input wsis "
                                f"but with a different value for {key}: [{wsi_1[key]}]."
                            )
                            raise Exception(error_msg)
                duplicate_wsis.append(wsi_info)
            else:
                no_duplicate_wsis.append(wsi_info)
        wsis[wsi_1["id"]] = wsi_1
    return no_duplicate_wsis, duplicate_wsis


def register_input_parameters(
    inputs_to_register: List[InputParameter], input_ids_already_registered: List[str], wsi_ids: List[str], mds_url: str
):
    # needed to check whether all required ids exist for inputs with reference_id
    input_ids_persisted = wsi_ids
    input_ids_persisted += input_ids_already_registered

    input_keys = [p.input_key for p in inputs_to_register]
    input_keys_persisted = []
    new_inputs_persisted_last_run = True
    # loop until no more new items were posted in last loop
    while new_inputs_persisted_last_run:
        new_inputs_persisted_last_run = False
        for input_param in inputs_to_register:
            if (
                # assure references exist at DADS
                set(input_param.reference_ids).issubset(input_ids_persisted)
                # no double post
                and input_param.input_key not in input_keys_persisted
            ):
                try:
                    params = {"external_ids": True}
                    if input_param.api_data_type == ApiDataType.COLLECTIONS:
                        return_data = post_collection(input_param.post_data, mds_url, params)

                    else:
                        r = requests.post(
                            f"{mds_url}/v1/{input_param.api_data_type.value}", json=input_param.post_data, params=params
                        )
                        r.raise_for_status()
                        return_data = r.json()
                    input_ids_persisted += _get_ids(return_data)
                    new_inputs_persisted_last_run = True
                    input_keys_persisted.append(input_param.input_key)
                except requests.HTTPError as e:
                    error_msg = f"Could not register input [{input_param.input_key}]. Service Error: {e}"
                    raise Exception(error_msg) from e

    if len(inputs_to_register) > len(input_keys_persisted):
        input_key_not_persisted = list(set(input_keys) - set(input_keys_persisted))
        error_msg = (
            f"Could not register the following inputs: {input_key_not_persisted}. "
            "Check if their [reference_id]s are valid [id]s of other inputs."
        )
        raise Exception(error_msg)


def register_configuration_parameters(app_id: str, config_file: str, config: dict, vsm_url):
    if config_file:
        url = f"{vsm_url}/api/v1/admin/{app_id}"
        r = requests.post(url, json=config)
        r.raise_for_status()


def register_ead(app_id: str, ead: dict, mds_url: str):
    try:
        r = requests.put(f"{mds_url}/v1/apps/{app_id}/ead", json=ead)
        r.raise_for_status()
    except HTTPError as e:
        r_json = r.json()
        if r.status_code == 400:
            if "detail" in r_json:
                if "cause" in r_json["detail"]:
                    if "already exists" in r_json["detail"]["cause"]:
                        return
        raise e


def register_job(app_id: str, mds_url: str, v1: bool = False, scope_id: str = None):
    job = {
        "app_id": app_id,
        "creator_id": scope_id if scope_id and not v1 else STATIC_USER_ID,
        "creator_type": "SCOPE" if scope_id and not v1 else "USER",
    }
    r = requests.post(f"{mds_url}/v1/jobs", json=job)
    r.raise_for_status()
    data = r.json()
    job_id = data["id"]
    r = requests.get(f"{mds_url}/v1/jobs/{job_id}/token")
    r.raise_for_status()
    data = r.json()
    return job_id, data["access_token"]


def register_job_inputs(job_id: str, job_inputs: dict, mds_url: str):
    for input_key, input_id in job_inputs.items():
        r = requests.put(f"{mds_url}/v1/jobs/{job_id}/inputs/{input_key}", json={"id": input_id})
        r.raise_for_status()


def set_job_statuses(job_id: str, mds_url: str, statuses: List[str]):
    for s in statuses:
        try:
            r = requests.put(f"{mds_url}/v1/jobs/{job_id}/status", json={"status": s})
            r.raise_for_status()
        except requests.HTTPError as e:
            msg = r.text
            if s in ["READY", "RUNNING"]:
                error_msg = f"Could not change job status to '{s}'. Job was started already. Error: {msg}"
                raise Exception(error_msg) from e
            else:
                raise e


def append_wsis_in_input_dict_to_list(input_dict: dict, wsi_infos: List[WsiInput]):
    if input_dict["type"] == "wsi":
        wsi = WsiInput.parse_obj(input_dict)
        wsi.id = wsi.id if wsi.id is not None else str(uuid4)
        wsi_infos.append(wsi)
    elif input_dict["type"] == "collection":
        for item in input_dict["items"]:
            append_wsis_in_input_dict_to_list(item, wsi_infos)
    else:
        raise ValidationError("No WSI input.")


def _get_reference_ids(data: dict) -> List[str]:
    reference_ids = []
    if "reference_id" in data:
        reference_ids.append(data["reference_id"])
    if "items" in data:
        for item in data["items"]:
            reference_ids += _get_reference_ids(item)
    return reference_ids


def _get_ids(data: dict) -> List[str]:
    ids = []
    if "id" in data:
        ids.append(data["id"])
    if "items" in data:
        for item in data["items"]:
            ids += _get_ids(item)
    return ids


def is_single_wsi_input(input_data):
    if "type" in input_data:
        if input_data["type"] == "wsi":
            return True
    return False


def _strip_wsi_collection(file_path, data):
    if "type" in data:
        if data["type"] == "wsi":
            if "id" not in data:
                raise Exception("NO ID IN WSI COLLECTION")
            del data["creator_type"]
            del data["creator_id"]
            del data["path"]
    if "items" in data:
        for item in data["items"]:
            _strip_wsi_collection(file_path, item)


def _extend_creator_inplace(data, v1, scope_id):
    creator_id = scope_id if scope_id and not v1 else STATIC_USER_ID
    creator_type = "scope" if scope_id and not v1 else "user"
    # if "creator_id" not in data:
    data["creator_id"] = creator_id
    # if "creator_type" not in data:
    data["creator_type"] = creator_type
    if "items" in data:
        for item in data["items"]:
            _extend_creator_inplace(item, v1, scope_id)


def extend_id_inplace(data):
    if "id" not in data:
        data["id"] = str(uuid4())
    if "items" in data:
        for item in data["items"]:
            extend_id_inplace(item)


def _check_collections_and_items_id(file_path, data):
    has_id = "id" in data
    if "item_type" in data:
        for item in data["items"]:
            item_has_id = "id" in item
            leafs_have_id = _check_collections_and_items_id(file_path, item)
            if item_has_id != has_id or leafs_have_id != has_id:
                error_msg = (
                    f"Check file [{file_path}]. If assigning [id]s to input collections or its items, "
                    "then all items and the collection itself must have an [id] assigned."
                )
                raise ValidationError(error_msg)
    return has_id


def _check_reference_id(file_path, data):
    # classes
    if "type" not in data and "items" not in data and "value" in data:
        if "reference_id" not in data:
            error_msg = f"Please check the file {file_path}. " "At least one class is missing [reference_id]."
            raise ValidationError(error_msg)
    # annotations
    if "type" in data:
        if data["type"] in ALLOWED_ANNOTATION_TYPES:
            if "reference_id" not in data:
                error_msg = f"Please check the file {file_path}. " "At least one annotation is missing [reference_id]."
                raise ValidationError(error_msg)
    if "items" in data:
        for item in data["items"]:
            item = _check_reference_id(file_path, item)
    return data


def is_wsi_collection(input_data: dict):
    if "item_type" in input_data:
        if input_data["item_type"] == "wsi":
            return True
        elif input_data["item_type"] == "collection":
            for item in input_data["items"]:
                return is_wsi_collection(item)
    return False


def _get_type(data: dict):
    if "type" in data:
        if data["type"] in ALLOWED_ANNOTATION_TYPES:
            return ApiDataType.ANNOTATIONS
        elif data["type"] in ALLOWED_PRIMITIVE_TYPES:
            return ApiDataType.PRIMITIVES
        elif data["type"] == "wsi":
            return ApiDataType.SLIDES
        elif data["type"] == "collection":
            return ApiDataType.COLLECTIONS
        elif data["type"] == "class":
            return ApiDataType.CLASSES
    elif "items" in data:
        return ApiDataType.COLLECTIONS
    elif "value" in data:
        return ApiDataType.CLASSES
    return None


def _check_input_with_id_exist(input_param: InputParameter, mds_url: str):
    input_id = input_param.post_data["id"]
    r = requests.get(f"{mds_url}/v1/{input_param.api_data_type.value}/{input_id}?shallow=true")
    if r.status_code == 404:
        return False
    else:
        if input_param.api_data_type == ApiDataType.COLLECTIONS:
            return_data = get_collection(input_id, mds_url)
        else:
            r.raise_for_status()
            return_data = r.json()
        _check_data_changed(input_param.input_key, input_param.post_data, return_data)
        return True


def _check_data_changed(input_key: str, input_data: dict, return_data: dict):
    for key in input_data:
        if key != "items":
            if input_data[key] != return_data[key]:
                error_msg = (
                    f"Value of [{key}] of input parameter [{input_key}] with [id] [{input_data['id']}] changed. "
                    f"If [{input_key}] is a (nested) collection, this might also be an item of this collection. "
                    "Delete volumes of the EMPAIA Test Suite <docker volume rm $(eats services volumes)>. "
                    f"Or if you want to preserve old job data, assign new IDs to the collection [{input_key}] "
                    "and to all of its (nested) items."
                )
                raise Exception(error_msg)
        else:
            if len(input_data["items"]) != return_data["item_count"]:
                error_msg = (
                    f"Number of items in collection [{input_key}] changed. "
                    "Delete volumes of the EMPAIA Test Suite <docker volume rm $(eats services volumes)>. "
                    f"Or if you want to preserve old job data, assign new IDs to the collection [{input_key}] "
                    "and to all of its (nested) items."
                )
                raise Exception(error_msg)
            for item in input_data["items"]:
                item_id = item["id"]
                item_found = False
                for r_item in return_data["items"]:
                    r_item_id = r_item["id"]
                    if item_id == r_item_id:
                        _check_data_changed(input_key, item, r_item)
                        item_found = True
                        break
                if not item_found:
                    error_msg = (
                        f"Number of items in collection [{input_key}] changed. "
                        "Delete volumes of the EMPAIA Test Suite <docker volume rm $(eats services volumes)>. "
                        f"Or if you want to preserve old job data, assign new IDs to the collection [{input_key}] "
                        "and to all of its (nested) items."
                    )
                    raise Exception(error_msg)
