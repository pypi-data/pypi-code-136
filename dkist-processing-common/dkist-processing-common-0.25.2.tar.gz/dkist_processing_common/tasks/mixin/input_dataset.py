"""Mixin for a WorkflowDataTaskBase subclass which implements input data set access functionality."""
import json
from dataclasses import dataclass
from datetime import datetime
from itertools import chain
from pathlib import Path
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

from dkist_processing_common.models.tags import Tag
from dkist_processing_common.tasks.base import tag_type_hint


frames_part_type_hint = Union[List[Dict[str, Union[str, List[str]]]], None]


@dataclass
class InputDatasetParameterValue:
    """Data structure for a de-serialized input dataset parameter value."""

    parameter_value_id: int
    parameter_value: Any = None
    parameter_value_start_date: Optional[datetime] = None


@dataclass
class InputDatasetFrame:
    """Data structure for a de-serialized input dataset frame."""

    bucket: str
    object_key: str


class InputDatasetMixin:
    """Mixin for WorkflowDataTaskBase that accesses downloaded input dataset part documents."""

    def _input_dataset_part_document(self, tags: tag_type_hint):
        """Get the input dataset document part and deserialize it."""
        paths: List[Path] = list(self.read(tags=tags))
        if not paths:
            return
        if len(paths) > 1:
            raise ValueError(
                f"There are more than one input dataset part documents to parse for {tags=}"
            )
        p = paths[0]
        with p.open(mode="rb") as f:
            return json.load(f)

    @property
    def input_dataset_observe_frames_part_document(self) -> frames_part_type_hint:
        """Get the 'observe frames' part of the input dataset."""
        return self._input_dataset_part_document(tags=Tag.input_dataset_observe_frames())

    @property
    def input_dataset_calibration_frames_part_document(self) -> frames_part_type_hint:
        """Get the 'calibration frames' part of the input dataset."""
        return self._input_dataset_part_document(tags=Tag.input_dataset_calibration_frames())

    @property
    def input_dataset_parameters_part_document(
        self,
    ) -> Union[List[Dict[str, Union[str, List[Dict[str, Union[int, str]]]]]], None]:
        """Get the 'parameters' part of the input dataset."""
        return self._input_dataset_part_document(tags=Tag.input_dataset_parameters())

    @property
    def input_dataset_frames(self) -> List[InputDatasetFrame]:
        """Get the list of frames for this input dataset."""
        result = []
        observe_frames = self.input_dataset_observe_frames_part_document or []
        calibration_frames = self.input_dataset_calibration_frames_part_document or []
        for frame_set in chain(observe_frames, calibration_frames):
            for key in frame_set.get("object_keys", list()):
                result.append(InputDatasetFrame(bucket=frame_set["bucket"], object_key=key))
        return result

    @property
    def input_dataset_parameters(self) -> Dict[str, List[InputDatasetParameterValue]]:
        """Get the input dataset parameters."""
        parameters = self.input_dataset_parameters_part_document or []
        result = dict()
        for p in parameters:
            result.update(self._input_dataset_parse_parameter(p))
        return result

    def _input_dataset_parse_parameter(
        self, parameter: dict
    ) -> Dict[str, List[InputDatasetParameterValue]]:
        name: str = parameter["parameterName"]
        raw_values: List[dict] = parameter["parameterValues"]
        values = self._input_dataset_parse_parameter_values(raw_values=raw_values)
        return {name: values}

    def _input_dataset_parse_parameter_values(
        self, raw_values: List[Dict[str, Any]]
    ) -> List[InputDatasetParameterValue]:
        values = list()
        for v in raw_values:
            parsed_value = InputDatasetParameterValue(parameter_value_id=v["parameterValueId"])
            parsed_value.parameter_value = self._input_dataset_parse_parameter_value(
                raw_parameter_value=v["parameterValue"]
            )
            if d := v.get("parameterValueStartDate"):
                parsed_value.parameter_value_start_date = datetime.fromisoformat(d)
            else:
                parsed_value.parameter_value_start_date = datetime(1, 1, 1)
            values.append(parsed_value)
        return values

    @staticmethod
    def _input_dataset_parse_parameter_value(raw_parameter_value: str) -> Any:
        return json.loads(raw_parameter_value)
