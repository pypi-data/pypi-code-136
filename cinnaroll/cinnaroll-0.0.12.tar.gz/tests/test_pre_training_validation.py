import json
from unittest import mock

import pytest
from typing import Callable, Any, Optional, List

from cinnaroll_internal import pre_training_validation, io_formats, rollout_config
from tests import utils


class TestClassWithImplementedInfer:
    @staticmethod
    def infer(model_object: Any, input_data: Any) -> None:
        print("some code")


class TestClassWithPassInfer:
    @staticmethod
    def infer(model_object: Any, input_data: Any) -> None:
        pass


class TestClassWithDotInfer:
    @staticmethod
    def infer(model_object: Any, input_data: Any) -> None:
        ...


class TestClassWithSameLineDotInfer:
    @staticmethod
    def infer(model_object: Any, input_data: Any) -> None: ...  # noqa: E704


implemented_infer = TestClassWithImplementedInfer.infer
pass_infer = TestClassWithPassInfer.infer
dot_infer = TestClassWithDotInfer.infer
same_line_dot_infer = TestClassWithSameLineDotInfer.infer


def test_verify_infer_func_is_implemented_returns_none_if_infer_is_implemented() -> None:
    err = pre_training_validation.find_infer_func_not_implemented_error(implemented_infer)
    assert err is None


@pytest.mark.parametrize("infer_func", (pass_infer, dot_infer, same_line_dot_infer))
def test_verify_infer_func_is_implemented_returns_error_if_infer_is_empty(infer_func: Callable[[Any, Any], Any]) -> None:
    err: Optional[Exception] = pre_training_validation.find_infer_func_not_implemented_error(infer_func)
    assert isinstance(err, pre_training_validation.InferFunctionNotImplementedError)
    assert err.args == ("Infer function is not implemented. Implement it.", )


class TestConfig(rollout_config.RolloutConfig):
    @staticmethod
    def train_eval() -> None:
        ...

    @staticmethod
    def infer(model_object: Any, input_data: Any) -> Any:
        ...


test_find_config_none_value_errors_cases = [
    (TestConfig(
        project_id="something",
        model_object="something",
        infer_func_input_format="something",
        infer_func_output_format="something",
        model_input_sample="something",
        infer_func_input_sample="something",
        metrics=None,
    ), []),
    (TestConfig(
        project_id=None,  # type: ignore
        model_object=None,
        infer_func_input_format=None,  # type: ignore
        infer_func_output_format=None,  # type: ignore
        model_input_sample=None,
        infer_func_input_sample=None,
        metrics=None,
    ), [
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter project_id is undefined (its value is None)."
        ),
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter model_object is undefined (its value is None)."
        ),
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter infer_func_input_format is undefined (its value is None)."
        ),
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter infer_func_output_format is undefined (its value is None)."
        ),
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter model_input_sample is undefined (its value is None)."
        ),
        pre_training_validation.ConfigParameterUndefinedError(
            "Required config parameter infer_func_input_sample is undefined (its value is None)."
        )
    ])
]


@pytest.mark.parametrize("config, expected_errors", test_find_config_none_value_errors_cases)
def test_find_config_none_value_errors(config: rollout_config.RolloutConfig, expected_errors: List[Exception]) -> None:
    got = pre_training_validation.find_config_none_value_errors(config)
    assert len(got) == len(expected_errors)
    utils.assert_contains_exceptions(expected_errors, got)


# PROJECT_ID = "123123123"
# test_find_project_id_error_when_response_arrives_cases = [
#     (requests.codes.ok, "", None),
#     (requests.codes.unauthorized, "", environment_check.WrongAPIKeyError()),
#     (requests.codes.forbidden, "", pre_training_validation.ProjectIDError(
#         f"Project with ID {PROJECT_ID} doesn't exist. "
#         f"Ensure you've pasted project ID correctly.")),
#     (requests.codes.not_found, "", pre_training_validation.ProjectIDError(
#         f"Project with ID {PROJECT_ID} doesn't exist. "
#         f"Ensure you've pasted project ID correctly.")),
#     (requests.codes.internal_server_error, "There was an error processing the request.",
#      pre_training_validation.ProjectIDError(
#          f"Project ID validation returned status code {requests.codes.internal_server_error} "
#          f"and message: There was an error processing the request.")),
# ]


# @mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": "abc123"})
# @mock.patch("cinnaroll_internal.pre_training_validation.requests.get")
# @pytest.mark.parametrize("status_code, text, expected", test_find_project_id_error_when_response_arrives_cases)
# def test_find_project_id_error_when_response_arrives(
#         mock_get: mock.MagicMock, status_code: int, text: str, expected: Optional[Exception]) -> None:
#     mock_get.return_value.status_code = status_code
#     mock_get.return_value.text = text
#     got = pre_training_validation.find_project_id_error(PROJECT_ID)
#     utils.assert_optional_exception_equals(expected, got)
#
#
# @mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": "abc123"})
# @mock.patch("cinnaroll_internal.pre_training_validation.requests.get")
# def test_find_project_id_error_when_request_errors_out(mock_get: mock.MagicMock) -> None:
#     mock_get.side_effect = requests.ConnectTimeout()
#     got = pre_training_validation.find_project_id_error(PROJECT_ID)
#     utils.assert_optional_exception_equals(requests.RequestException(), got)


test_find_disallowed_io_format_cases = [
    ("json", "img", []),
    ("foo", "json", [
        io_formats.DisallowedInferFuncInputFormatError(
            f"foo is not an allowed infer func input format. "
            f"You can choose from one of: {io_formats.ALLOWED_INFER_FUNC_INPUT_FORMATS}")]),
    ("file", "baz", [
        io_formats.DisallowedInferFuncOutputFormatError(
            f"baz is not an allowed infer func output format. "
            f"You can choose from one of: {io_formats.ALLOWED_INFER_FUNC_OUTPUT_FORMATS}")]),
    ("foo", "baz", [
        io_formats.DisallowedInferFuncOutputFormatError(
            f"baz is not an allowed infer func output format. "
            f"You can choose from one of: {io_formats.ALLOWED_INFER_FUNC_OUTPUT_FORMATS}"),
        io_formats.DisallowedInferFuncInputFormatError(
            f"foo is not an allowed infer func input format. "
            f"You can choose from one of: {io_formats.ALLOWED_INFER_FUNC_INPUT_FORMATS}")
    ]),
]


@pytest.mark.parametrize("infer_func_input_format, infer_func_output_format, expected",
                         test_find_disallowed_io_format_cases)
def test_find_disallowed_io_format_errors(infer_func_input_format: str, infer_func_output_format: str,
                                          expected: List[Exception]) -> None:
    got = io_formats.find_disallowed_io_format_errors(infer_func_input_format, infer_func_output_format)
    assert len(expected) == len(got)
    if len(expected):
        utils.assert_contains_exceptions(expected, got)


test_find_infer_func_input_format_mismatch_error_when_input_is_json_cases = [
    (json.dumps({'number': 3}), None),
    ("invalid json", io_formats.InferFuncInputFormatMismatchError(
        "Input in json format needs to be a string containing valid JSON "
        "that can be decoded with json.loads(). Here is the error encountered "
        "while trying to json.loads() provided input: "
    ))
]


@pytest.mark.parametrize("input_sample, expected",
                         test_find_infer_func_input_format_mismatch_error_when_input_is_json_cases)
def test_find_infer_func_input_format_mismatch_error_when_input_is_json(input_sample: str,
                                                                        expected: Optional[Exception]) -> None:
    got = io_formats.find_infer_func_input_format_mismatch_error(input_sample, "json")
    utils.assert_optional_exception_like(expected, got)


test_find_infer_func_input_format_mismatch_error_when_input_is_file_type_cases = [
    ("file", None, None),
    ("img", None, None),
    ("file", PermissionError(), io_formats.InferFuncInputFormatMismatchError(
        "Input in file format needs to be path to a file that can be opened. "
        "Here is the error encountered while trying to open provided file: "
    )),
    ("img", PermissionError(), io_formats.InferFuncInputFormatMismatchError(
        "Input in img format needs to be path to a file that can be opened. "
        "Here is the error encountered while trying to open provided file: "
    ))
]


@pytest.mark.parametrize("input_format, side_effect, expected",
                         test_find_infer_func_input_format_mismatch_error_when_input_is_file_type_cases)
def test_find_infer_func_input_format_mismatch_error_when_input_is_file_type(
        input_format: str, side_effect: Optional[Exception], expected: Optional[Exception]) -> None:
    with mock.patch('builtins.open', mock.mock_open()) as mock_file:
        mock_file.side_effect = side_effect
        got = io_formats.find_infer_func_input_format_mismatch_error("~/.somefile", input_format)
        utils.assert_optional_exception_like(expected, got)


# @mock.patch.dict(os.environ, {"CINNAROLL_API_KEY": "abc123"})
# @mock.patch("cinnaroll_internal.pre_training_validation.requests.get")
# def test_find_config_pre_training_errors_when_it_should_return_multiple_errors(mock_get: mock.MagicMock) -> None:
#     config = TestConfig(
#         project_id="abc321",
#         model_object=None,
#         infer_func_input_format="unimplemented format",
#         infer_func_output_format="unimplemented format",
#         model_input_sample=None,
#         infer_func_input_sample=None,
#         metrics=None)
#
#     mock_get.return_value.status_code = requests.codes.not_found
#     got = pre_training_validation.find_config_pre_training_errors(config)
#     assert len(got)
