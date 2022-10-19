import datetime
import logging
import time

import dateutil.parser

from ..api import API
from ..exceptions import DeqartBaseException
from ..lib import circuit_serialization

logger = logging.getLogger("deqart-python-sdk")

_api = API.get_instance()


def search_jobs(run_status=None, limit=100, created_later_than=None):
    if created_later_than is None:
        parsed_created_later_than = None
    elif isinstance(created_later_than, str):
        parsed_created_later_than = dateutil.parser.parse(created_later_than)
        if parsed_created_later_than.tzinfo is None:
            logger.warning(
                "created_later_than is a str object without timezone info, assuming UTC timezone"
            )
            parsed_created_later_than = parsed_created_later_than.replace(
                tzinfo=datetime.timezone.utc
            )
        parsed_created_later_than = parsed_created_later_than.isoformat()
    elif isinstance(created_later_than, datetime.datetime):
        if created_later_than.tzinfo is None:
            raise DeqartBaseException(
                0, "created_later_than is a datetime object without timezone info"
            )
        parsed_created_later_than = created_later_than.isoformat()
    else:
        raise DeqartBaseException(
            0, "created_later_than should be None, str, or datetime.datetime object"
        )

    params = {
        "limit": limit,
        "run_status": run_status,
        "created_later_than": parsed_created_later_than,
    }
    result_dict = {"column_names": [], "data": []}
    while True:
        response = _api.send_request(req_type="GET", path="/jobs", params=params)
        if not response.ok:
            raise DeqartBaseException(
                response.status_code, "Couldn't search jobs " + response.text
            )
        response = response.json()

        result_dict["column_names"] = response["column_names"]
        results = response["data"]
        result_dict["data"] += results
        result_dict["total_count"] = response["total_count"]

        if len(results) < limit:
            break

        params["offset"] = len(result_dict["data"])
    return result_dict


def estimate_job_runtime(circuit):
    encoded_circuit = circuit_serialization.encode_circuit(circuit)
    params = encoded_circuit
    params["estimate_only"] = True
    response = _api.send_request(req_type="POST", path="/jobs", json_req=params)
    if not response.ok:
        raise DeqartBaseException(
            response.status_code, "Couldn't estimate job " + response.text
        )
    return response.json()


def submit_job(circuit):
    encoded_circuit = circuit_serialization.encode_circuit(circuit)
    params = {"circuit": encoded_circuit}
    response = _api.send_request(req_type="POST", path="/jobs", json_req=params)
    if not response.ok:
        raise DeqartBaseException(
            response.status_code, "Couldn't submit job " + response.text
        )
    return response.json()["data"]


def wait_for_job(job_id):
    while True:
        response = _api.send_request(req_type="GET", path=f"/jobs/{job_id}")
        if not response.ok:
            raise DeqartBaseException(
                response.status_code, "Couldn't search jobs " + response.text
            )
        response = response.json()["data"]
        if response["run_status"] != "COMPLETED":
            time.sleep(10.0)
        else:
            return response
