import pytest

from .constants import ACCESS_DENIED_ERROR_CODE
from .error import JsonRpcError, raise_for_error


def test_json_rpc_error__is_access_denied():
    any_message = {"hello": "world"}

    # no access denied
    another_code = ACCESS_DENIED_ERROR_CODE + 1
    error_msg = {"code": another_code}
    error = JsonRpcError(message=any_message, error=error_msg)
    assert not error.is_access_denied

    # access denied
    error_msg = {"code": ACCESS_DENIED_ERROR_CODE}
    error = JsonRpcError(message=any_message, error=error_msg)
    assert error.is_access_denied


def test_raise_for_error():
    any_message = {"hello": "world"}

    # no error
    response = {"everything is": "OK"}
    raise_for_error(any_message, response)

    # error
    response = {"error": "Houston, we have a problem"}
    with pytest.raises(JsonRpcError):
        raise_for_error(any_message, response)
