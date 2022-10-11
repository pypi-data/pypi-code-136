import json
from datetime import datetime
from typing import Any
from typing import List
from typing import Tuple
from uuid import uuid4

import pytest

from dkist_processing_common.models.tags import Tag


def input_dataset_frames_part_factory(bucket_count: int = 1) -> List[dict]:
    return [
        {"bucket": uuid4().hex[:6], "object_keys": [uuid4().hex[:6] for _ in range(3)]}
        for _ in range(bucket_count)
    ]


def flatten_frame_parts(frame_parts: List[dict]) -> List[Tuple[str, str]]:
    result = []
    for frame_set in frame_parts:
        for key in frame_set["object_keys"]:
            result.append((frame_set["bucket"], key))
    return result


def input_dataset_parameters_part_factory(
    parameter_count: int = 1, has_date: bool = False
) -> List[dict]:
    result = [
        {
            "parameterName": uuid4().hex[:6],
            "parameterValues": [{"parameterValueId": i, "parameterValue": json.dumps(uuid4().hex)}],
        }
        for i in range(parameter_count)
    ]
    if has_date:
        for data in result:
            data["parameterValueStartDate"] = datetime(2022, 9, 14).isoformat()[:10]
    return result


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param((None, Tag.input_dataset_observe_frames()), id="empty"),
        pytest.param(
            (input_dataset_frames_part_factory(), Tag.input_dataset_observe_frames()),
            id="single_bucket",
        ),
        pytest.param(
            (input_dataset_frames_part_factory(bucket_count=2), Tag.input_dataset_observe_frames()),
            id="multi_bucket",
        ),
    ],
)
def test_input_dataset_observe_frames_part_document(
    task_with_input_dataset, input_dataset_parts: Tuple[Any, str]
):
    """
    Given: A task with an input dataset observe frames part document tagged as such
    When: Accessing the document via the InputDatasetMixIn
    Then: The contents of the file are returned
    """
    doc_part, _ = input_dataset_parts
    task = task_with_input_dataset
    assert task.input_dataset_observe_frames_part_document == doc_part


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param((None, Tag.input_dataset_calibration_frames()), id="empty"),
        pytest.param(
            (input_dataset_frames_part_factory(), Tag.input_dataset_calibration_frames()),
            id="single_bucket",
        ),
        pytest.param(
            (
                input_dataset_frames_part_factory(bucket_count=2),
                Tag.input_dataset_calibration_frames(),
            ),
            id="multi_bucket",
        ),
    ],
)
def test_input_dataset_calibration_frames_part_document(
    task_with_input_dataset, input_dataset_parts: Tuple[Any, str]
):
    """
    Given: A task with an input dataset calibration frames part document tagged as such
    When: Accessing the document via the InputDatasetMixIn
    Then: The contents of the file are returned
    """
    doc_part, _ = input_dataset_parts
    task = task_with_input_dataset
    assert task.input_dataset_calibration_frames_part_document == doc_part


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param((None, Tag.input_dataset_parameters()), id="empty"),
        pytest.param(
            (input_dataset_parameters_part_factory(), Tag.input_dataset_parameters()),
            id="single_param_no_date",
        ),
        pytest.param(
            (
                input_dataset_parameters_part_factory(parameter_count=2),
                Tag.input_dataset_parameters(),
            ),
            id="multi_param_no_date",
        ),
        pytest.param(
            (input_dataset_parameters_part_factory(has_date=True), Tag.input_dataset_parameters()),
            id="single_param_with_date",
        ),
        pytest.param(
            (
                input_dataset_parameters_part_factory(parameter_count=2, has_date=True),
                Tag.input_dataset_parameters(),
            ),
            id="multi_param_with_date",
        ),
    ],
)
def test_input_dataset_parameters_part_document(
    task_with_input_dataset, input_dataset_parts: Tuple[Any, str]
):
    """
    Given: A task with an input dataset parameters part document tagged as such
    When: Accessing the document via the InputDatasetMixIn
    Then: The contents of the file are returned
    """
    doc_part, _ = input_dataset_parts
    task = task_with_input_dataset
    assert task.input_dataset_parameters_part_document == doc_part


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param(
            [
                (input_dataset_frames_part_factory(), Tag.input_dataset_observe_frames()),
                (input_dataset_frames_part_factory(), Tag.input_dataset_calibration_frames()),
            ],
            id="observe1_cal1_single_bucket",
        ),
        pytest.param(
            [
                (input_dataset_frames_part_factory(), Tag.input_dataset_observe_frames()),
                (None, Tag.input_dataset_calibration_frames()),
            ],
            id="observe1_cal0_single_bucket",
        ),
        pytest.param(
            [
                (None, Tag.input_dataset_observe_frames()),
                (input_dataset_frames_part_factory(), Tag.input_dataset_calibration_frames()),
            ],
            id="observe0_cal1_single_bucket",
        ),
        pytest.param(
            [
                (None, Tag.input_dataset_observe_frames()),
                (None, Tag.input_dataset_calibration_frames()),
            ],
            id="observe0_cal0_single_bucket",
        ),
        pytest.param(
            [
                (
                    input_dataset_frames_part_factory(bucket_count=2),
                    Tag.input_dataset_observe_frames(),
                ),
                (
                    input_dataset_frames_part_factory(bucket_count=2),
                    Tag.input_dataset_calibration_frames(),
                ),
            ],
            id="observe1_cal1_multi_bucket",
        ),
        pytest.param(
            [
                (
                    input_dataset_frames_part_factory(bucket_count=2),
                    Tag.input_dataset_observe_frames(),
                ),
                (None, Tag.input_dataset_calibration_frames()),
            ],
            id="observe1_cal0_multi_bucket",
        ),
        pytest.param(
            [
                (None, Tag.input_dataset_observe_frames()),
                (
                    input_dataset_frames_part_factory(bucket_count=2),
                    Tag.input_dataset_calibration_frames(),
                ),
            ],
            id="observe0_cal1_multi_bucket",
        ),
        pytest.param(
            [
                (None, Tag.input_dataset_observe_frames()),
                (None, Tag.input_dataset_calibration_frames()),
            ],
            id="observe0_cal0_multi_bucket",
        ),
    ],
)
def test_input_dataset_frames(task_with_input_dataset, input_dataset_parts: List[Tuple[Any, str]]):
    """
    Given: a task with the InputDatasetMixin
    When: getting the frames in the input dataset
    Then: it matches the frames used to create the input dataset
    """
    doc_parts = [part for part, _ in input_dataset_parts]
    task = task_with_input_dataset
    expected = []
    for part in doc_parts:
        if part:
            expected.extend(flatten_frame_parts(part))
    expected_set = set(expected)
    actual = [(frame.bucket, frame.object_key) for frame in task.input_dataset_frames]
    actual_set = set(actual)
    assert len(actual) == len(actual_set)
    assert actual_set.difference(expected_set) == set()


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param((None, Tag.input_dataset_parameters()), id="empty"),
        pytest.param(
            (input_dataset_parameters_part_factory(), Tag.input_dataset_parameters()),
            id="single_param_no_date",
        ),
        pytest.param(
            (
                input_dataset_parameters_part_factory(parameter_count=2),
                Tag.input_dataset_parameters(),
            ),
            id="multi_param_no_date",
        ),
        pytest.param(
            (input_dataset_parameters_part_factory(has_date=True), Tag.input_dataset_parameters()),
            id="single_param_with_date",
        ),
        pytest.param(
            (
                input_dataset_parameters_part_factory(parameter_count=2, has_date=True),
                Tag.input_dataset_parameters(),
            ),
            id="multi_param_with_date",
        ),
    ],
)
def test_input_dataset_parameters(
    task_with_input_dataset, input_dataset_parts: List[Tuple[Any, str]]
):
    """
    Given: a task with the InputDatasetMixin
    When: getting the parameters in the input dataset
    Then: the names of the parameters match the keys in the returned dictionary
    """
    task = task_with_input_dataset
    doc_part, _ = input_dataset_parts
    doc_part = doc_part or []  # None case parsing of expected values
    expected_parameters = {p["parameterName"]: p["parameterValues"] for p in doc_part}
    for key, values in task.input_dataset_parameters.items():
        assert key in expected_parameters
        for value in values:
            expected_values = expected_parameters[key]
            expected_value = [
                v for v in expected_values if value.parameter_value_id == v["parameterValueId"]
            ]
            assert len(expected_value) == 1
            expected_value = expected_value[0]
            assert value.parameter_value == json.loads(expected_value["parameterValue"])
            expected_date = expected_value.get("parameterValueStartDate", datetime(1, 1, 1))
            assert value.parameter_value_start_date == expected_date


@pytest.mark.parametrize(
    "input_dataset_parts",
    [
        pytest.param(
            [
                (input_dataset_frames_part_factory(), Tag.input_dataset_observe_frames()),
                (input_dataset_frames_part_factory(), Tag.input_dataset_observe_frames()),
            ],
            id="observe",
        ),
        pytest.param(
            [
                (input_dataset_frames_part_factory(), Tag.input_dataset_calibration_frames()),
                (input_dataset_frames_part_factory(), Tag.input_dataset_calibration_frames()),
            ],
            id="calibration",
        ),
        pytest.param(
            [
                (input_dataset_frames_part_factory(), Tag.input_dataset_parameters()),
                (input_dataset_frames_part_factory(), Tag.input_dataset_parameters()),
            ],
            id="params",
        ),
    ],
)
def test_multiple_input_dataset_parts(
    task_with_input_dataset, input_dataset_parts: List[Tuple[Any, str]]
):
    """
    Given: a task with the InputDatasetMixin and multiple tagged input datasets
    When: reading the input dataset document
    Then: an error is raised
    """
    task = task_with_input_dataset
    with pytest.raises(ValueError):
        task.input_dataset_parameters_part_document
        task.input_dataset_observe_frames_part_document
        task.input_dataset_calibration_frames_part_document
