import re

import pytest

from py_ead_validation.ead_validator import validate_ead
from py_ead_validation.exceptions import (
    EadContentValidationError,
    EadSchemaMissingError,
    EadSchemaNotAvailableError,
    EadSchemaValidationError,
)


def test_schema_missing():
    ead = {
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {},
        "outputs": {},
    }
    with pytest.raises(EadSchemaMissingError):
        validate_ead(ead)


def test_schema_not_available():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-0.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {},
        "outputs": {},
    }
    with pytest.raises(EadSchemaNotAvailableError):
        validate_ead(ead)


def test_not_compliant_to_schema():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_minimum_compliant_ead():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {},
        "outputs": {},
    }
    validate_ead(ead)


def test_input_reference_not_existing():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {"type": "rectangle", "reference": "inputs.non_existing"},
        },
        "outputs": {},
    }
    with pytest.raises(
        EadContentValidationError, match=re.escape("inputs.non_existing referenced by inputs.my_rectangle not found")
    ):
        validate_ead(ead)


def test_input_references_output():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_class": {"type": "class", "reference": "outputs.my_rectangle"}},
        "outputs": {"my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Inputs must not reference outputs (inputs.my_class -> outputs.my_rectangle)"),
    ):
        validate_ead(ead)


def test_collection_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_collection": {"type": "collection", "items": {"type": "integer"}, "reference": "inputs.my_collection"},
        },
        "outputs": {"my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
    }
    with pytest.raises(EadContentValidationError, match="Collections may only reference WSIs or annotations"):
        validate_ead(ead)


def test_primitive_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_primitive": {"type": "integer", "reference": "inputs.my_primitive"}},
        "outputs": {"my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
    }
    with pytest.raises(
        EadContentValidationError, match="Primitives may only reference WSIs, collections or annotations"
    ):
        validate_ead(ead)


def test_annotation_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
        "outputs": {"my_tumor": {"type": "point", "reference": "inputs.my_rectangle"}},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_class_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
        "outputs": {"my_classification": {"type": "class", "reference": "inputs.my_wsi"}},
    }
    with pytest.raises(EadContentValidationError, match="Classes must reference annotations"):
        validate_ead(ead)


def test_wrong_reference_from_collection_items():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {
                "type": "wsi",
            },
            "my_rectangles": {
                "type": "collection",
                "items": {"type": "rectangle", "reference": "inputs.my_rectangles"},
                "reference": "inputs.my_wsi",
            },
        },
        "outputs": {},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_wrong_reference_into_nested_collection():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsis": {"type": "collection", "items": {"type": "wsi"}},
            "my_params": {"type": "collection", "items": {"type": "float"}},
            "my_wsi_rois": {
                "type": "collection",
                "items": {"type": "collection", "items": {"type": "rectangle", "reference": "inputs.my_params.items"}},
            },
        },
        "outputs": {},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_correct_reference_into_nested_collection():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsis": {"type": "collection", "items": {"type": "wsi"}},
            "my_params": {"type": "collection", "items": {"type": "float"}},
            "my_wsi_rois": {
                "type": "collection",
                "items": {"type": "collection", "items": {"type": "rectangle", "reference": "inputs.my_wsis.items"}},
            },
        },
        "outputs": {},
    }
    validate_ead(ead)


def test_correct_references():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
        "outputs": {
            "my_classification": {"type": "class", "reference": "inputs.my_rectangle"},
            "my_cells": {
                "type": "collection",
                "reference": "inputs.my_rectangle",
                "items": {"type": "point", "reference": "inputs.my_wsi"},
            },
            "my_score": {"type": "float", "reference": "outputs.my_cells"},
            "my_unrelated_collection": {"type": "collection", "items": {"type": "integer"}},
        },
    }
    validate_ead(ead)


def test_output_class_constraints():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {"my_wsi": {"type": "wsi"}, "my_rectangle": {"type": "rectangle", "reference": "inputs.my_wsi"}},
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "classes": ["org.empaia.global.v1.classes.roi"],
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(EadContentValidationError, match="Outputs must not have class constraints"):
        validate_ead(ead)


def test_input_class_constraint_using_wrong_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.other.something.v42.classes.nothing"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Namespace not valid for class value org.empaia.other.something.v42.classes.nothing"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_global_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.global.v1.classes.roi"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_wrong_local_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.wrong.v1.classes.foo"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Namespace not valid for class value org.empaia.vendor_name.wrong.v1.classes.foo"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_nonexisting_global_namespace_version():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.global.v42.classes.roi"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Global namespace not found for class value org.empaia.global.v42.classes.roi"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_malformed_class_value_which_passes_schema():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.global.v1.klasses.roi"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(
        EadContentValidationError, match=re.escape("Class value org.empaia.global.v1.klasses.roi is malformed")
    ):
        validate_ead(ead)


def test_input_class_constraint_using_local_namespace_with_missing_class():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.baz"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Class value org.empaia.vendor_name.ta.v1.classes.baz not found in class hierarchy"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_local_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_top_level_classes():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_top_level_global_classes():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.global.v1.classes"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_inner_class_node():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"baz": {"name": "Baz"}}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_leaf_class_node():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"baz": {"name": "Baz"}}},
        "inputs": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar.baz"],
            },
        },
        "outputs": {
            "my_rectangle": {
                "type": "rectangle",
                "reference": "inputs.my_wsi",
            },
            "my_classification": {"type": "class", "reference": "outputs.my_rectangle"},
        },
    }
    validate_ead(ead)


def test_wrong_configuration_spec():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-app-schema-draft-3.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "param": {
                "type": "string",
                "storage": "moon",
                "optional": False,
            }
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
    with pytest.raises(
        EadContentValidationError, match="Only global storage is supported for the configuration entries"
    ):
        validate_ead(ead)


def test_correct_configuration_spec():
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
    validate_ead(ead)
