import json
from typing import Tuple
import numpy as np
from trojsdk.client import TrojClient
from trojsdk.config.base import BaseTrojConfig
from trojsdk.config.nlp import NLPTrojConfig
from trojsdk.config.tabular import TabularTrojConfig
from trojsdk.config.vision import VisionTrojConfig
from trojsdk.core import data_utils, troj_logging
from pathlib import Path

log = troj_logging.getLogger(__file__)

"""
The troj job handler class wraps the client and stores all details relevant to a given job or session
"""

def submit_evaluation(path_to_config:str = None, config:dict = None, docker_metadata=None) -> "TrojJobHandler":
    if path_to_config is not None:
        config = data_utils.load_json_from_disk(Path(path_to_config))
        log.info("JSON loaded from disk.")

    config, docker_metadata = config_from_dict(config, docker_metadata)
    tjh = TrojJobHandler()
    response = tjh.post_job_to_endpoint(config, docker_metadata)
    log.info("Config posted to endpoint")
    log.info("Response: " + str(response))

    return tjh

def config_from_dict(config:dict, docker_metadata:dict=None) -> Tuple[BaseTrojConfig, dict]:
    if config.get("docker_metadata"):
        dm = config.pop("docker_metadata")
        if docker_metadata is None:
            docker_metadata = dm
    if config["task_type"] == "nlp":
        config = NLPTrojConfig.config_from_dict(config)
    elif config["task_type"] == "tabular":
        config = TabularTrojConfig.config_from_dict(config)
    elif config["task_type"] == "vision":
        config = VisionTrojConfig.config_from_dict(config)

    return config, docker_metadata


class TrojJobHandler:
    def __init__(self) -> None:
        self.client = None
        self.post_response = None
        self.status_response = None

    def post_job_to_endpoint(
        self, config: BaseTrojConfig, docker_metadata: dict = None
    ) -> dict:
        """

        This function posts any given config to the endpoint supplied, can be used via command line or programmatically

        *Params*
        config: dict
            The main configuration for the project.
        docker_metadata: dict
            A dictionary with the following two values;
            "docker_image_url": A Docker Hub image id for any engine type.
                Ex. value: "trojai/troj-engine-base-tabular:tabluar-shawn-latest"
            "docker_secret_name": The name of the environment secret containing the credentials for Docker Hub access. This is defined in the TrojAI helm repo in the _setup.sh_ script.

        *Return*
        dict
            Contains job_name under key "data", under key "job_name". (Dict within dict)

        *Raises*
        Exception
            If docker_metadata is not defined, and the config does not contain a valid task type. (tabular, nlp, vision, ...)

        """

        self.client = TrojClient(auth_config=config.auth_config)
        res = self.client.post_job(config, docker_metadata)
        self.post_response = res
        return res

    def check_job_status(self, response: dict = None, format_pretty: bool = True):
        """ """
        try:
            if response is None:
                response = self.post_response
                job_name = response.get("data").get("job_name")
        except Exception as e:
            raise e

        if self.client is None:
            print(
                "No jobs have been submitted yet! Call the post_job_to_endpoint and pass the required config first."
            )
        else:

            res = self.client.get_job_status(job_name)
            if format_pretty:
                mess = res["data"]["Message"]
                mess = str(mess).replace("\\n", "\n").replace("'", "").replace('"', "")
            else:
                mess = str(mess).replace("\n", "")
            self.status_response = res
            return res

    def stream_job_logs(self, job_id):
        """
        this function will stream all the prints/logs from the evaluation pod as its running
        I believe it will use prometheus to some effect
        """
        pass


class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)
