import pytest
from blockutils.exceptions import SupportedErrors, UP42Error, catch_exceptions
from blockutils.logging import get_logger


# pylint: disable=redefined-outer-name
@pytest.fixture()
def mock_logger():
    logger = get_logger("mock")
    return logger


@pytest.fixture()
def mock_function_with_catch(mock_logger):
    @catch_exceptions(mock_logger)
    def run(exc):
        raise exc

    return run


@pytest.mark.parametrize(
    "error",
    [
        SupportedErrors.INPUT_PARAMETERS_ERROR,
        SupportedErrors.NO_INPUT_ERROR,
        SupportedErrors.WRONG_INPUT_ERROR,
        SupportedErrors.API_CONNECTION_ERROR,
        SupportedErrors.NO_OUTPUT_ERROR,
        SupportedErrors.ERR_INCORRECT_ERRCODE,
    ],
)
def test_exit_supported_error(mock_function_with_catch, error):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mock_function_with_catch(UP42Error(error))
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == error.value


def test_exit_memory_error(mock_function_with_catch):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mock_function_with_catch(MemoryError())
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 137


def test_exit_other(mock_function_with_catch):
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        mock_function_with_catch(TypeError())
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 1
