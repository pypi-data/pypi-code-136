import json
import os

from typing import Any

from cinnaroll_internal.environment_check import API_KEY_ENV_VAR_NAME
from cinnaroll_internal.rollout_config import RolloutConfig
from cinnaroll_internal.constants import KERAS
from cinnaroll_internal.rollout import rollout

from tests.unit.test_simple_nn_models import create_model_object, generate_random_data

import numpy as np


class MyRolloutConfig(RolloutConfig):
    @staticmethod
    def train_eval() -> None:
        num_samples = 10
        X, Y = generate_random_data(num_samples, input_dim)
        model_object.fit(X, Y, epochs=5)

    @staticmethod
    def infer(model_object: Any, input_data: str) -> str:
        X = np.array(json.loads(input_data))
        Y = model_object.predict(X)
        output = {"output": int(Y.argmax())}

        return json.dumps(output)


if __name__ == "__main__":
    os.environ[API_KEY_ENV_VAR_NAME] = "my_api_key"

    input_dim = np.random.randint(5, 10)

    # generate random input to the model
    model_input_sample = generate_random_data(1, input_dim)[0]
    infer_func_input_sample = json.dumps(model_input_sample.tolist())

    framework = KERAS

    dense_layers = (8, 4)
    model_object = create_model_object(framework, input_dim, dense_layers)

    rollout_config = MyRolloutConfig(
        project_id="my_project_id",
        model_object=model_object,
        model_input_sample=model_input_sample,
        infer_func_input_format="json",
        infer_func_output_format="json",
        infer_func_input_sample=infer_func_input_sample,
        metrics={},
    )

    print("\nCall infer():")
    output = rollout_config.infer(model_object, infer_func_input_sample)
    print(output)

    print("\nRoll out!")
    rollout(rollout_config)
