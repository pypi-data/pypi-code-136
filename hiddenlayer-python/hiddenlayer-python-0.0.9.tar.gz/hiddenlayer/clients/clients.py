import os
import requests
import numpy as np
import base64
import gzip

from typing import List, Union
from io import BytesIO

from hiddenlayer.config import config


class HiddenLayerClient(object):

    filterKeys={
        "sensor_id", "requester_id", "group_id", 
        "input_layer_exponent_sha256", 
        "input_layer_byte_size", "input_layer_dtype", 
        "output_layer_byte_size", "output_layer_dtype", 
        "event_time_start", "event_time_stop"
    }

    def __init__(self, token: str = None, api_host: str = None, version: int = None, proto: str = None):
        """HiddenLayer API Client

        :param token: api token for auth
        :param api_host: alternate hiddenlayer api host
        :param version: version number of api

        :return None
        """
        self.version = version or config.api_version() or 1
        self.token = token or config.api_token()
        self.api_host = api_host or config.api_host() or "api.hiddenlayer.com"
        self.proto = proto or config.api_proto() or "https"
        self.api_url = f"{self.proto}://{self.api_host}/caml/api/v{self.version}"

        if self.token is None:
            raise AttributeError("API token must be set via HL_API_TOKEN environment variable or passed to the client.")

        if self.api_url is None:
            raise AttributeError("API url must be set VIA HL_API_URL environment variable or passed to the client.")

        # setup session
        self.session = requests.Session()
        self.session.headers = {"token": self.token}

    def health(self) -> dict:
        """get endpoint health

        :return: response dictionary
        """
        resp = self.session.get(f"{self.api_url}/health")
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(
                f"Failed to get endpoint health. Status code: {resp.status_code}, Detail: {resp.content}"
            )

    def get_event_count(self, params: dict = None) -> int:
        if(not params.keys() <= HiddenLayerClient.filterKeys):
            raise ValueError("illegal parameter")
        resp = self.session.get(f"{self.api_url}/events",params=params)
        if resp.ok:
            data = resp.json()
            count = data.get("total", None)
            if count is not None:
                return count
            else:
                raise ValueError("Error retrieving event count. Key 'total' not found in response.")
        else:
            raise requests.HTTPError(
                f"Failed to get event count. Status code: {resp.status_code}, Detail: {resp.content}"
            )

    def get_alert_count(self, params: dict = None) -> int:
        if(not params.keys() <= HiddenLayerClient.filterKeys):
            raise ValueError("illegal parameter")
        resp = self.session.get(f"{self.api_url}/alerts",params=params)
        if resp.ok:
            data = resp.json()
            count = data.get("total", None)
            if count is not None:
                return count
            else:
                raise ValueError("Error retrieving event count. Key 'total' not found in response.")
        else:
            raise requests.HTTPError(
                f"Failed to get alert count. Status code: {resp.status_code}, Detail: {resp.content}"
            )

    def get_event(self, event_id: str) -> dict:
        """get event by id

        :param event_id: event id to retrieve
        :return: response dictionary
        """
        resp = self.session.get(f"{self.api_url}/events/{event_id}")
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"Failed to get event. Status code: {resp.status_code}, Detail: {resp.content}")

    def get_events(
        self,
        page: int = 0,
        sensor_id: str = None,
        requester_id: str = None,
        group_id: str = None,
        input_layer_exponent_sha256: str = None,
        input_layer_byte_size: int = None,
        input_layer_dtype: str = None,
        output_layer_byte_size: str = None,
        output_layer_dtype: str = None,
        event_time_start: str = None,
        event_time_stop: str = None,
        max_results: int = 1000,
    ) -> List[dict]:
        """Get list of events

        :param page: page number
        :param sensor_id: filter by sensor_id
        :param requester_id: filter by requester_id
        :param group_id: filter by group_id
        :param input_layer_exponent_sha256: filter by input_layer exponent sha256
        :param input_layer_byte_size: filter by input_layer size in bytes
        :param input_layer_dtype: filter by input_layer data type
        :param output_layer_byte_size: filter by output_layer size in bytes
        :param output_layer_dtype: filter by output_layer dtype
        :param event_time_start: start date for filtering by event_time
        :param event_time_stop: stop date for filtering by event_time
        :param max_results: max number of results to retrieve
        :return: list of events
        """
        params = {"page": page}
        if sensor_id is not None:
            params.update({"sensor_id": sensor_id})
        if requester_id is not None:
            params.update({"requester_id": requester_id})
        if group_id is not None:
            params.update({"group_id": group_id})
        if input_layer_exponent_sha256 is not None:
            params.update({"input_layer_exponent_sha256": input_layer_exponent_sha256})
        if input_layer_byte_size is not None:
            params.update({"input_layer_byte_size": input_layer_byte_size})
        if input_layer_dtype is not None:
            params.update({"input_layer_dtype": input_layer_dtype})
        if output_layer_byte_size is not None:
            params.update({"output_layer_byte_size": output_layer_byte_size})
        if output_layer_dtype is not None:
            params.update({"output_layer_dtype": output_layer_dtype})
        if event_time_start is not None:
            params.update({"event_time_start": event_time_start})
        if event_time_stop is not None:
            params.update({"event_time_stop": event_time_stop})

        url = f"{self.api_url}/events"
        results = []
        resp = self.session.get(url, params=params)
        if resp.ok:
            content = resp.json()
            results.extend(content["results"])
            if content["next"]:
                url = content["next"]
            else:
                url = None

            if len(results) < max_results and url:
                while url:
                    resp = self.session.get(url)
                    if resp.ok:
                        content = resp.json()
                        results.extend(content["results"])

                        if content["next"]:
                            url = content["next"]
                        else:
                            url = None

                        if len(results) >= max_results:
                            break
                    else:
                        raise requests.HTTPError(
                            f"Failed to retrieve events page. "
                            f"Status code: {resp.status_code}, Page: {page}, Detail: {resp.content}"
                        )
        else:
            raise requests.HTTPError(
                f"Failed to retrieve events page. "
                f"Status code: {resp.status_code}, Page: {page}, Detail: {resp.content}"
            )

        return results[:max_results] if max_results else results

    def get_alert(self, alert_id: str) -> dict:
        """get alert by id

        :param alert_id: id of alert to retrieve
        :return: response dictionary
        """
        resp = self.session.get(f"{self.api_url}/alerts/{alert_id}")
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"Failed to get alert. Status code: {resp.status_code}, Detail: {resp.content}")

    def get_alerts(
        self,
        page: int = 0,
        sensor_id: str = None,
        requester_id: str = None,
        group_id: str = None,
        category: str = None,
        tactic: int = None,
        risk: str = None,
        event_time_start: str = None,
        event_time_stop: str = None,
        max_results: int = 1000,
    ) -> List[dict]:
        """Get list of events

        :param page: page number
        :param sensor_id: filter by sensor_id
        :param requester_id: filter by requester_id
        :param group_id: filter by group_id
        :param category: filter by category of alerts
        :param tactic: filter by mitre tactic for alerts
        :param risk: filter by risk of alerts
        :param event_time_start: start date for filtering by event_time
        :param event_time_stop: stop date for filtering by event_time
        :param max_results: max number of results to retrieve
        :return: list of events
        """
        params = {"page": page}
        if sensor_id is not None:
            params.update({"sensor_id": sensor_id})
        if requester_id is not None:
            params.update({"requester_id": requester_id})
        if group_id is not None:
            params.update({"group_id": group_id})
        if category is not None:
            params.update({"category": category})
        if tactic is not None:
            params.update({"tactic": tactic})
        if risk is not None:
            params.update({"risk": risk})
        if event_time_start is not None:
            params.update({"event_time_start": event_time_start})
        if event_time_stop is not None:
            params.update({"event_time_stop": event_time_stop})

        url = f"{self.api_url}/alerts"
        results = []
        resp = self.session.get(url, params=params)
        if resp.ok:
            content = resp.json()
            results.extend(content["results"])
            if content["next"]:
                url = content["next"]
            else:
                url = None

            if len(results) < max_results and url:
                while url:
                    resp = self.session.get(url)
                    if resp.ok:
                        content = resp.json()
                        results.extend(content["results"])

                        if content["next"]:
                            url = content["next"]
                        else:
                            url = None

                        if len(results) >= max_results:
                            break
                    else:
                        raise requests.HTTPError(
                            f"Failed to retrieve alerts page. "
                            f"Status code: {resp.status_code}, Page: {page}, Detail: {resp.content}"
                        )
        else:
            raise requests.HTTPError(
                f"Failed to retrieve alerts page. "
                f"Status code: {resp.status_code}, Page: {page}, Detail: {resp.content}"
            )

        return results[:max_results] if max_results else results

    def get_vector(self, vector_sha256: str) -> requests.Response:
        """get vector by sha256

        :param vector_sha256: sha256 of vector to retrieve
        :return: Vector as a list
        """
        resp = self.session.get(f"{self.api_url}/vectors/{vector_sha256}")
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(f"Failed to get vector. Status code: {resp.status_code}, Detail: {resp.content}")

    def submit(
        self,
        model_id: str,
        requester_id: str,
        input_layer: Union[List[List[Union[float]]], np.ndarray],
        output_layer: Union[List[List[Union[float]]], np.ndarray],
        predictions: Union[None, List[Union[float]], np.ndarray] = None,
        compress: bool = True,
    ):
        if len(input_layer) != len(output_layer):
            raise ValueError(F"length of input_layer is not equal to length of output_layer. "
                             F"input_layer: {len(input_layer)}, output_layer: {len(output_layer)}")

        input_layer_buffer = BytesIO()
        np.save(input_layer_buffer, input_layer, allow_pickle=True)

        output_layer_buffer = BytesIO()
        np.save(output_layer_buffer, output_layer, allow_pickle=True)

        if compress:
            input_layer_enc = base64.b64encode(gzip.compress(input_layer_buffer.getvalue())).decode()
            output_layer_enc = base64.b64encode(gzip.compress(output_layer_buffer.getvalue())).decode()
        else:
            input_layer_enc = base64.b64encode(input_layer_buffer.getvalue()).decode()
            output_layer_enc = base64.b64encode(output_layer_buffer.getvalue()).decode()

        if isinstance(predictions, np.ndarray):
            predictions = predictions.tolist()
        elif predictions is None:
            predictions = []

        payload = {
            "model_id": model_id,
            "requester_id": requester_id,
            "input_layer": input_layer_enc,
            "output_layer": output_layer_enc,
            "predictions": predictions,
        }

        resp = self.session.post(f"{self.api_url}/submit", json=payload)
        if resp.ok:
            return resp.json()
        else:
            raise requests.HTTPError(
                f"Failed to submit to api. Status code: {resp.status_code}, Detail: {resp.content}"
            )
