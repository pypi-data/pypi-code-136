from ctypes import Union
from cerebrium.models import (
    PickleModel,
    ClassifierPickleModel,
    XGBRegressorModel,
    XGBClassifierModel,
    TorchModel,
    TorchPickleModel,
)
from cerebrium.errors import CerebriumRequestError

from pipeline import Pipeline, PipelineFile, Variable, PipelineCloud
import requests
import json
import re
import os
from numpy import ndarray
from torch import Tensor
from typing import Union, Tuple

env = os.getenv("DEVELOPMENT_ENV", "prod")
if env == "dev":
    print("Using development environment")
    BASE_CEREBRIUM_URL = "https://dev-inference.cerebrium.ai"
else:
    BASE_CEREBRIUM_URL = "https://inference.cerebrium.ai"

SUPPORTED_MODELS = (
    "xgb_classifier",
    "xgb_regressor",
    "torch",
    "sklearn",
    "sklearn_classifier",
)
REGEX_NAME_PATTERN = "^[A-Za-z0-9-]*$"


def _check_auth_request(api_key: str) -> bool:
    """
    Check that the user is authenticated, returning the pipeline token if they are.

    Args:
        api_key (str): The API key for the Cerebrium account.
    Returns:
        dict ('status_code': int, 'data': dict): The response code and data. 'data' contains the pipeline token if successful.
    """

    url = f"{BASE_CEREBRIUM_URL}/getExternalApiKey"
    payload = {}
    headers = {"Authorization": api_key}

    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload), timeout=10
    )
    data = {} if not response.text else json.loads(response.text)
    return {"status_code": response.status_code, "data": data}


def _generate_pipeline(pipeline_name, model_type, model_filepath) -> Pipeline:
    """
    Generate a pipeline for the given model type.

    Args:
        pipeline_name (str): The name of the pipeline.
        model_type (str): The type of model to generate a pipeline for.
            One of ["xgb_classifier", "xgb_regressor", "torch", "sklearn", "sklearn_classifier"].
        model_filepath (str): The path to the model file.

    Returns:
        Pipeline: The generated pipeline.
    """
    if model_filepath.endswith(".pkl"):
        if model_type == "torch":
            print("Loading Torch Model from cloudpickle")
            with Pipeline(pipeline_name) as pipeline:
                input_list = Variable(type_class=list, is_input=True)
                model_file = PipelineFile(path=model_filepath)

                pipeline.add_variables(input_list, model_file)

                model = TorchPickleModel()
                model.load(model_file)

                output = model.predict(input_list)
                pipeline.output(output)
            return Pipeline.get_pipeline(pipeline_name)
        elif model_type == "sklearn_classifier" or model_type == "xgb_classifier":
            print("Loading Classifier Pickle Model")
            with Pipeline(pipeline_name) as pipeline:
                input_list = Variable(type_class=list, is_input=True)
                model_file = PipelineFile(path=model_filepath)

                pipeline.add_variables(input_list, model_file)

                model = ClassifierPickleModel()
                model.load(model_file)

                output = model.predict(input_list)
                pipeline.output(output)
            return Pipeline.get_pipeline(pipeline_name)
        else:
            print("Loading Pickle Model")
            with Pipeline(pipeline_name) as pipeline:
                input_list = Variable(type_class=list, is_input=True)
                model_file = PipelineFile(path=model_filepath)

                pipeline.add_variables(input_list, model_file)

                model = PickleModel()
                model.load(model_file)

                output = model.predict(input_list)
                pipeline.output(output)
            return Pipeline.get_pipeline(pipeline_name)
    elif model_type == "xgb_classifier":
        print("Loading XGB Classifier from JSON")
        with Pipeline(pipeline_name) as pipeline:
            input_list = Variable(type_class=list, is_input=True)
            model_file = PipelineFile(path=model_filepath)

            pipeline.add_variables(input_list, model_file)

            model = XGBClassifierModel()
            model.load(model_file)

            output = model.predict(input_list)
            pipeline.output(output)
        return Pipeline.get_pipeline(pipeline_name)
    elif model_type == "xgb_regressor":
        print("Loading XGB Regressor from JSON")
        with Pipeline(pipeline_name) as pipeline:
            input_list = Variable(type_class=list, is_input=True)
            model_file = PipelineFile(path=model_filepath)

            pipeline.add_variables(input_list, model_file)

            model = XGBRegressorModel()
            model.load(model_file)

            output = model.predict(input_list)
            pipeline.output(output)
        return Pipeline.get_pipeline(pipeline_name)
    elif model_type == "torch":
        print("Loading Torch from Torchscript JIT compiled model")
        with Pipeline(pipeline_name) as pipeline:
            input_list = Variable(type_class=list, is_input=True)
            model_file = PipelineFile(path=model_filepath)

            pipeline.add_variables(input_list, model_file)

            model = TorchModel()
            model.load(model_file)

            output = model.predict(input_list)
            pipeline.output(output)
        return Pipeline.get_pipeline(pipeline_name)


def _register_model_request(
    name: str, pipeline_id: str, model_type: str, description: str, api_key: str
) -> str:
    """
    Register a model with Cerebrium.

    Args:
        pipeline_id (str): The ID of the pipeline to register.
        model_type (str): The type of model to register. One of ["xgb_classifier", "xgb_regressor", "torch", "sklearn"].
        api_key (str): The API key for the Cerebrium account.

    Returns:
        dict ('status_code': int, 'data': dict): The response code and data. 'data' contains the endpoint of the registered model if successful.
    """

    url = f"{BASE_CEREBRIUM_URL}/models"
    payload = {
        "arguments": {
            "name": name,
            "externalId": pipeline_id,
            "modelType": model_type,
        }
    }
    if description != "":
        payload["description"] = description
    headers = {"Authorization": api_key}

    response = requests.request(
        "POST", url, headers=headers, data=json.dumps(payload), timeout=30
    )
    return {"status_code": response.status_code, "data": json.loads(response.text)}


def _convert_input_data(data: Union[list, ndarray, Tensor]) -> list:
    """
    Convert the input data to a list.

    Args:
        data (Union[list, ndarray, Tensor]): The data to convert.

    Returns:
        list: The converted data as a python list.
    """

    if isinstance(data, ndarray) or isinstance(data, Tensor):
        return data.tolist()
    else:
        return data


def model_api_request(
    model_endpoint: str,
    data: Union[list, ndarray, Tensor],
    api_key: str,
) -> dict:
    """
    Make a request to the Cerebrium model API.

    Args:
        model_endpoint (str): The endpoint of the model to make a request to.
        data (list): The data to send to the model.

    Returns:
        dict ('status_code': int, 'data': dict): The response code and data.
    """

    payload = _convert_input_data(data)
    headers = {"Authorization": api_key}
    response = requests.request(
        "POST", model_endpoint, headers=headers, data=json.dumps(payload), timeout=30
    )
    return {"status_code": response.status_code, "data": json.loads(response.text)}


def deploy(
    model_filepath: str,
    model_type: str,
    pipeline_name: str,
    api_key: str,
    description: str = "",
    dry_run=False,
) -> Tuple[str, str]:
    """
    Deploy a model to Cerebrium.

    Args:
        model_filepath (str): The filepath of the saved model to deploy.
        model_type : The type of model to instantiate.
            One of ["xgb_classifier", "xgb_regressor", "torch", "sklearn"].
        pipeline_name (str): The name to deploy the pipeline under.
        api_key (str): The API key for the Cerebrium account.
        description (str): An optional description of the model or pipeline.
        dry_run (bool): Whether to run the deployment in dry-run mode.
            If True, the model will not be deployed, and deploy will return a pipeline function which can be used to test with.

    Returns:
        str: The newly deployed REST endpoint.
    """

    # Check that the model type is supported
    if model_type not in SUPPORTED_MODELS:
        raise ValueError(f"model_type must be one of {SUPPORTED_MODELS}")

    # Check that the pipeline name is valid
    if len(pipeline_name) > 20:
        raise ValueError("Pipeline name must be less than 20 characters")
    if not bool(re.match(REGEX_NAME_PATTERN, pipeline_name)):
        raise ValueError(
            "Pipeline name can only contain alphanumeric characters and hyphens"
        )

    # Check that the user is authenticated
    if not dry_run:
        check_auth_response = _check_auth_request(api_key)
        if check_auth_response["status_code"] != 200:
            raise CerebriumRequestError(
                check_auth_response["status_code"],
                "getExternalApiKey",
                check_auth_response["data"],
            )
        else:
            pipeline_token = check_auth_response["data"]["apiKey"]
    # Create the pipeline
    pipeline = _generate_pipeline(pipeline_name, model_type, model_filepath)

    if not dry_run:
        # Deploy the pipeline to PipelineAI and register the model with Cerebrium
        pipeline_cloud = PipelineCloud(token=pipeline_token, verbose=False)
        print("Uploading pipeline...")
        uploaded_pipeline = pipeline_cloud.upload_pipeline(pipeline)
        print("Registering with Cerebrium...")
        model_response = _register_model_request(
            pipeline_name, uploaded_pipeline.id, model_type, description, api_key
        )
        if model_response["status_code"] != 200:
            raise CerebriumRequestError(
                model_response["status_code"], "models", model_response["data"]
            )
        else:
            endpoint = model_response["data"]["internalEndpoint"]
            print(f"Model {pipeline_name} deployed at {endpoint}")
            return endpoint
    else:
        print("Dry run complete")

        def run_function(input_data):
            return pipeline.run(_convert_input_data(input_data))

        return run_function
