# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from typing import Any, Dict, Optional, Union

from azureml.train.automl.runtime._many_models.pipeline_parameters import (
    InferencePipelineParameters,
    TrainPipelineParameters,
)
from azureml.train.automl.automlconfig import AutoMLConfig
from azureml._common._error_definition import AzureMLError
from azureml.automl.core.shared.reference_codes import ReferenceCodes
from azureml.automl.core.shared.exceptions import (
    InvalidValueException,
    ValidationException
)
from azureml.automl.core.shared._diagnostics.automl_error_definitions import (
    InvalidParameterSelection,
    RollingForecastMissingTargetColumn
)
from azureml.automl.core.shared.constants import TimeSeriesInternal


class ManyModelsTrainParameters(TrainPipelineParameters):
    """Parameters used for ManyModels train pipelines."""
    PARTITION_COLUMN_NAMES_KEY = "partition_column_names"

    def __init__(
        self,
        automl_settings: Union[AutoMLConfig, Dict[str, Any]],
        partition_column_names: str
    ):
        super(ManyModelsTrainParameters, self).__init__(automl_settings)

        self.partition_column_names = partition_column_names
        self._modify_automl_settings()

    def validate(self, run_invocation_timeout):
        super(ManyModelsTrainParameters, self).validate(run_invocation_timeout)

    def _modify_automl_settings(self):
        self.automl_settings[ManyModelsTrainParameters.PARTITION_COLUMN_NAMES_KEY] = self.partition_column_names


class ManyModelsInferenceParameters(InferencePipelineParameters):

    def __init__(
            self,
            partition_column_names: str,
            time_column_name: Optional[str] = None,
            target_column_name: Optional[str] = None,
            inference_type: Optional[str] = None,
            forecast_mode: Optional[str] = TimeSeriesInternal.RECURSIVE,
            step: Optional[int] = 1,
    ):
        super(ManyModelsInferenceParameters, self).__init__()

        self.partition_column_names = partition_column_names
        self.time_column_name = time_column_name
        self.target_column_name = target_column_name
        self.inference_type = inference_type
        self.forecast_mode = forecast_mode
        self.step = step

    def validate(self):
        super(ManyModelsInferenceParameters, self).validate()
        if self.forecast_mode not in (TimeSeriesInternal.RECURSIVE, TimeSeriesInternal.ROLLING):
            raise InvalidValueException._with_error(
                AzureMLError.create(
                    InvalidParameterSelection,
                    target="forecast_mode",
                    parameter="forecast_mode",
                    values=f"{TimeSeriesInternal.RECURSIVE} or {TimeSeriesInternal.ROLLING}"
                )
            )
        if self.forecast_mode == TimeSeriesInternal.ROLLING and self.target_column_name is None:
            raise ValidationException._with_error(
                AzureMLError.create(
                    RollingForecastMissingTargetColumn,
                    reference_code=ReferenceCodes._ROLLING_FORECAST_MISSING_TARGET_COLUMN
                )
            )
