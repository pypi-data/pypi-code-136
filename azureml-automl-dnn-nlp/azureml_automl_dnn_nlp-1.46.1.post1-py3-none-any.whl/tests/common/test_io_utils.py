from unittest.mock import ANY, Mock, patch

import os
import pandas as pd
import unittest

from azureml.automl.core.shared import constants
from azureml.automl.dnn.nlp.common.constants import OutputLiterals, SystemSettings
from azureml.automl.dnn.nlp.common.io.utils import save_model_wrapper
from ..mocks import MockRun


class TestIOUtils(unittest.TestCase):
    @patch('azureml.train.automl.runtime._azureautomlruncontext.AzureAutoMLRunContext.batch_save_artifacts')
    def test_save_model_wrapper_mlflow(self,
                                       mock_batch_save_artifacts):
        model = Mock()
        mock_run = MockRun()
        input_sample_str = "pd.DataFrame({\"text\": pd.Series([\"example_value\"], dtype=\"object\")})"
        output_sample_str = "np.array([\"example_value\"])"
        save_model_wrapper(run=mock_run, model=model, save_mlflow=True,
                           input_sample_str=input_sample_str, output_sample_str=output_sample_str)

        mock_batch_save_artifacts.assert_called_once_with(
            os.getcwd(),
            input_strs={constants.RUN_ID_OUTPUT_PATH: mock_run.id},
            model_outputs={os.path.join(OutputLiterals.OUTPUT_DIR, OutputLiterals.MODEL_FILE_NAME): model},
            save_as_mlflow=True,
            mlflow_options={constants.MLFlowLiterals.LOADER: SystemSettings.NAMESPACE,
                            constants.MLFlowLiterals.SCHEMA_SIGNATURE: ANY,
                            constants.MLFlowLiterals.INPUT_EXAMPLE: ANY}
        )  # Correctly route request to batch save artifacts with necessary MLflow settings populated.

        self.assertEqual("inputs: \n  ['text': string]\noutputs: \n  [Tensor('str', (-1,))]\n",
                         str(mock_batch_save_artifacts.call_args[1]["mlflow_options"]["signature"]))
