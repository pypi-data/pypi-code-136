from trojsdk.core import data_utils
from trojsdk.core import client_utils
from trojsdk.core.client_utils import TrojJobHandler
import logging


def test_sdk_fail():
    # config = load_json_from_disk(Path("./trojsdk/examples/testing_config.json"))

    docker_metadata = {
        "docker_image_url": "trojai/trojai-engine-master:10ba6f109b9843e2be008db01465de9e40fc2dc0",
        "docker_secret_name": "trojaicreds",
    }

    # troj_job_handler = submit_evaluation("./trojsdk/configs/tabular_test/tabular_test_main.json", docker_metadata=docker_metadata)
    troj_job_handler = TrojJobHandler()
    failure = False
    try:
        troj_job_handler.check_job_status()
    except:
        failure = True

    assert failure


def test_sdk_pass_tabular():
    # config = load_json_from_disk(Path("./trojsdk/examples/testing_config.json"))

    docker_metadata = {
        "docker_image_url": "trojai/trojai-engine-master:10ba6f109b9843e2be008db01465de9e40fc2dc0",
        "docker_secret_name": "trojaicreds",
    }
    troj_job_handler = client_utils.submit_evaluation(
        path_to_config="trojsdk/examples/tabular_medical_insurance_config.json",
        # docker_metadata=docker_metadata,
    )
    import time

    time.sleep(2)
    troj_job_handler.check_job_status()

    assert troj_job_handler.status_response["data"]["status"] == "success"

def test_sdk_pass_nlp():
    # config = load_json_from_disk(Path("./trojsdk/examples/testing_config.json"))
    # config = load_json_from_disk(Path("./trojsdk/examples/s3_test/s3_classification_config.json"))

    troj_job_handler = client_utils.submit_evaluation("./trojsdk/examples/nlp_test_main.json")
    import time

    time.sleep(2)
    troj_job_handler.check_job_status()

    assert troj_job_handler.status_response["data"]["status"] == "success"
