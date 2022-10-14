import os
import argparse
import io

import pytest
from ts_sdk.cli.__put_cmd import __ensure_args, __namespace_type


def test_ensure_args():
    os.environ.update({"TS_ORG": "env-org", "TS_API_URL": "env-api-url"})
    args = argparse.Namespace(
        org="arg-org",
        ignore_ssl=False,
        config=io.StringIO(
            '{"org": "cfg-org", "auth_token": "cfg-token", "ignore_ssl": true}'
        ),
    )
    __ensure_args(args)
    assert args.api_url == "env-api-url"
    assert args.org == "arg-org"
    assert args.auth_token == "cfg-token"
    assert args.ignore_ssl == True


@pytest.mark.parametrize(
    "namespace",
    [
        # valid namespaces
        "private-123",
        "private-a-b-c-1",
        "private-my-namespace-123",
        "private-Test-Namespace",
        "private-my-123-namespace",
    ],
)
def test_namespace_type_valid(namespace):
    validated_namespace = __namespace_type(namespace)
    assert validated_namespace == namespace


@pytest.mark.parametrize(
    "namespace",
    [
        # invalid namespaces
        "nonprivate-test-namespace",
        "common-org-123",
        "private-t3st-n@m3sp@ce",
        "private-a-b-c-",
        "private---a-b",
        "private-my--namespace",
        "-private-namespace",
        "private-my-123-namespace-" "-private-namespace-",
    ],
)
def test_namespace_type_invalid(namespace):
    with pytest.raises(argparse.ArgumentTypeError):
        __namespace_type(namespace)
