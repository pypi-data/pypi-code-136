import re

import pytest

from py_ead_validation.ead_validator import validate_ead_with_config
from py_ead_validation.exceptions import ConfigValidationError, EadValidationError


def test_ead_is_validated():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.wrong_reference",
            },
        },
    }
    config = {}
    with pytest.raises(EadValidationError):
        validate_ead_with_config(ead, config)


def test_allow_none_config_for_eads_without_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {},
        "outputs": {},
    }
    validate_ead_with_config(ead, config=None)


def test_allow_empty_config_for_eads_without_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {},
        "outputs": {},
    }
    validate_ead_with_config(ead, config={})


def test_allow_none_config_for_eads_with_empty_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {},
        "inputs": {},
        "outputs": {},
    }
    validate_ead_with_config(ead, config=None)


def test_allow_empty_config_for_eads_with_empty_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {},
        "inputs": {},
        "outputs": {},
    }
    validate_ead_with_config(ead, config={})


def test_missing_non_optional_entry():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "param": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
                "optional": False,
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {"param": True}
    with pytest.raises(ConfigValidationError, match="Parameter url is missing in given configuration"):
        validate_ead_with_config(ead, config)


def test_unspecified_optional_means_mandatory():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "param": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {"param": True}
    with pytest.raises(ConfigValidationError, match="Parameter url is missing in given configuration"):
        validate_ead_with_config(ead, config)


def test_unspecified_entry():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "param": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
                "optional": False,
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {"url": "http://api.example.com", "something": "wrong"}
    with pytest.raises(
        ConfigValidationError, match="Parameter something is not part of the configuration specification"
    ):
        validate_ead_with_config(ead, config)


def test_entry_of_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "param": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
                "optional": False,
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {"url": 42}
    with pytest.raises(ConfigValidationError, match="Parameter url has wrong type in given configuration"):
        validate_ead_with_config(ead, config)


def test_matching_config():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "flag": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
                "optional": False,
            },
            "threshold": {
                "type": "float",
                "storage": "global",
                "optional": False,
            },
            "count": {
                "type": "integer",
                "storage": "global",
                "optional": False,
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {
        "url": "http://api.example.com",
        "flag": True,
        "threshold": 0.75,
        "count": 42,
    }
    validate_ead_with_config(ead, config)


def test_empty_config_with_configuration_with_non_optionals():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "flag": {
                "type": "bool",
                "storage": "global",
                "optional": True,
            },
            "url": {
                "type": "string",
                "storage": "global",
                "optional": False,
            },
            "threshold": {
                "type": "float",
                "storage": "global",
                "optional": False,
            },
            "count": {
                "type": "integer",
                "storage": "global",
                "optional": False,
            },
        },
        "inputs": {
            "my_wsi": {"type": "wsi"},
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
        },
    }
    config = {}
    with pytest.raises(ConfigValidationError):
        validate_ead_with_config(ead, config)
