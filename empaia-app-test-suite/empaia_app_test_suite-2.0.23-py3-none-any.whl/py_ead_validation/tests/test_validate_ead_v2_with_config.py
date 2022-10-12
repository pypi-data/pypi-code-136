import re

import pytest

from py_ead_validation.ead_validator import validate_ead_with_config
from py_ead_validation.exceptions import ConfigValidationError, EadValidationError


def test_ead_is_validated():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.wrong_reference",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    config = {}
    with pytest.raises(EadValidationError):
        validate_ead_with_config(ead, config)


def test_allow_none_config_for_eads_without_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead_with_config(ead, config=None)


def test_allow_empty_config_for_eads_without_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead_with_config(ead, config={})


def test_allow_none_config_for_eads_with_empty_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {"global": {}},
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead_with_config(ead, config=None)


def test_allow_empty_config_for_eads_with_empty_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {"customer": {}},
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead_with_config(ead, config={})


def test_only_validate_existing_configs_sections():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {"customer": {}, "global": {"something": {"type": "integer"}}},
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead_with_config(ead, config={"customer": {}})
    validate_ead_with_config(ead, config={"global": {"something": 42}})


def test_missing_non_optional_entry():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "param": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                    "optional": False,
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    config = {"global": {"param": True}}
    with pytest.raises(ConfigValidationError, match="Parameter url is missing in given configuration"):
        validate_ead_with_config(ead, config)


def test_unspecified_optional_means_mandatory():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "customer": {
                "param": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    config = {"customer": {"param": True}}
    with pytest.raises(ConfigValidationError, match="Parameter url is missing in given configuration"):
        validate_ead_with_config(ead, config)


def test_unspecified_entry():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "param": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                    "optional": False,
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    config = {"global": {"url": "http://api.example.com", "something": "wrong"}}
    with pytest.raises(
        ConfigValidationError, match="Parameter something is not part of the configuration specification"
    ):
        validate_ead_with_config(ead, config)


def test_entry_of_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "customer": {
                "param": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                    "optional": False,
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    config = {"customer": {"url": 42}}
    with pytest.raises(ConfigValidationError, match="Parameter url has wrong type in given configuration"):
        validate_ead_with_config(ead, config)


def test_matching_config():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "flag": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                    "optional": False,
                },
            },
            "customer": {
                "threshold": {
                    "type": "float",
                    "optional": False,
                },
                "count": {
                    "type": "integer",
                    "optional": False,
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }

    config = {
        "global": {
            "url": "http://api.example.com",
            "flag": True,
        },
        "customer": {
            "threshold": 0.75,
            "count": 42,
        },
    }
    validate_ead_with_config(ead, config)

    config = {
        "global": {
            "url": "http://api.example.com",
            "flag": True,
        }
    }
    validate_ead_with_config(ead, config)  # only validate global

    config = {
        "customer": {
            "threshold": 0.75,
            "count": 42,
        }
    }
    validate_ead_with_config(ead, config)  # only validate customer


def test_empty_config_with_configuration_with_non_optionals():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "flag": {
                    "type": "bool",
                    "optional": True,
                },
                "url": {
                    "type": "string",
                    "optional": False,
                },
            },
            "customer": {
                "threshold": {
                    "type": "float",
                    "optional": False,
                },
                "count": {
                    "type": "integer",
                    "optional": False,
                },
            },
        },
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    config = {"global": {"url": "some-url"}, "customer": {}}
    with pytest.raises(ConfigValidationError):
        validate_ead_with_config(ead, config)

    config = {"customer": {"threshold": 3.14, "count": 42}, "customer": {}}
    with pytest.raises(ConfigValidationError):
        validate_ead_with_config(ead, config)

    config = {
        "customer": {"threshold": 3.14, "count": 42},
        "global": {"url": "some-url"},
    }
    validate_ead_with_config(ead, config)
