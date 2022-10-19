from typing import Callable, Any

import pytest

from tests import test_pre_training_validation
from cinnaroll_internal import utils

test_get_infer_func_code_cases = [
    [test_pre_training_validation.pass_infer, """def infer(model_object: Any, input_data: Any) -> None:
    pass
"""],
    [test_pre_training_validation.implemented_infer, """def infer(model_object: Any, input_data: Any) -> None:
    print("some code")
"""]
]


@pytest.mark.parametrize("func, expected_code", test_get_infer_func_code_cases)
def test_function_code(func: Callable[[Any, Any], Any], expected_code: str) -> None:
    got = utils.get_function_code(func)
    assert got == expected_code
