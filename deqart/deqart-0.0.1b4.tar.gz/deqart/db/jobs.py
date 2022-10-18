import logging
import time

from ..api import API
from ..exceptions import DeqartBaseException
from ..lib import circuit_serialization

logger = logging.getLogger("deqart-python-sdk")

_api = API.get_instance()

SINGLE_REQUEST_LIMIT = 10


def search_jobs():
    params = {"limit": SINGLE_REQUEST_LIMIT}
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

        if len(results) < SINGLE_REQUEST_LIMIT:
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
