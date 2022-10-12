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
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
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
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    with pytest.raises(EadSchemaNotAvailableError):
        validate_ead(ead)


def test_not_compliant_to_schema():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_minimum_compliant_ead():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {"standalone": {"inputs": [], "outputs": []}},
    }
    validate_ead(ead)


def test_preprocessing_requires_one_slide():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {"preprocessing": {"inputs": [], "outputs": []}},
    }
    with pytest.raises(EadContentValidationError, match="preprocessing requires exactly one input of type wsi"):
        validate_ead(ead)


def test_standalone_must_not_be_uncontainerized():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {
            "standalone": {"inputs": [], "outputs": [], "containerized": False},
        },
    }
    with pytest.raises(EadContentValidationError, match="standalone mode must not be uncontainerized"):
        validate_ead(ead)


def test_preprocessing_must_not_be_uncontainerized():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {"slide": {"type": "wsi"}},
        "modes": {
            "preprocessing": {"inputs": ["slide"], "outputs": [], "containerized": False},
        },
    }
    with pytest.raises(EadContentValidationError, match="preprocessing mode must not be uncontainerized"):
        validate_ead(ead)


def test_postprocessing_without_preprocessing_forbidden():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {},
        "modes": {"postprocessing": {"inputs": [], "outputs": [], "containerized": False}},
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_postprocessing_must_specify_containerized_flag():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {"slide": {"type": "wsi"}},
        "modes": {
            "preprocessing": {"inputs": ["slide"], "outputs": []},
            "postprocessing": {"inputs": [], "outputs": []},
        },
    }
    with pytest.raises(EadContentValidationError, match="postprocessing mode must specify containerized flag"):
        validate_ead(ead)


def test_postprocessing_with_preprocessing_works():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {"slide": {"type": "wsi"}},
        "modes": {
            "preprocessing": {"inputs": ["slide"], "outputs": []},
            "postprocessing": {"inputs": [], "outputs": [], "containerized": False},
        },
    }
    validate_ead(ead)


def test_all_modes_together_works():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {"slide": {"type": "wsi"}},
        "modes": {
            "standalone": {"inputs": [], "outputs": []},
            "preprocessing": {"inputs": ["slide"], "outputs": []},
            "postprocessing": {"inputs": [], "outputs": [], "containerized": False},
        },
    }
    validate_ead(ead)


def test_unreferenced_io_forbidden():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "slide": {"type": "wsi"},
            "leftover": {"type": "rectangle", "reference": "io.slide"},
            "hotarea": {"type": "rectangle", "reference": "io.slide"},
        },
        "modes": {"standalone": {"inputs": ["slide"], "outputs": ["hotarea"]}},
    }
    with pytest.raises(EadContentValidationError, match="io.leftover is not used by any mode"):
        validate_ead(ead)


def test_mode_io_is_disjoint():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "slide": {"type": "wsi"},
        },
        "modes": {"standalone": {"inputs": ["slide"], "outputs": ["slide"]}},
    }
    with pytest.raises(EadContentValidationError, match="Mode standalone defines non-disjoint inputs and outputs"):
        validate_ead(ead)


def test_input_reference_not_existing():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {"type": "rectangle", "reference": "io.non_existing"},
        },
        "modes": {
            "standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]},
        },
    }
    with pytest.raises(
        EadContentValidationError, match=re.escape("io.non_existing referenced by io.my_rectangle not found")
    ):
        validate_ead(ead)


def test_input_references_output():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_class": {"type": "class", "reference": "io.my_rectangle"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_class"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Inputs must not reference outputs (io.my_class -> io.my_rectangle)"),
    ):
        validate_ead(ead)


def test_collection_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_collection": {"type": "collection", "items": {"type": "integer"}, "reference": "io.my_collection"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_collection"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadContentValidationError, match="Collections may only reference WSIs or annotations"):
        validate_ead(ead)


def test_primitive_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_primitive": {"type": "integer", "reference": "io.my_primitive"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_primitive"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(
        EadContentValidationError, match="Primitives may only reference WSIs, collections or annotations"
    ):
        validate_ead(ead)


def test_annotation_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
            "my_tumor": {"type": "point", "reference": "io.my_rectangle"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_tumor"]}},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_class_references_wrong_type():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
            "my_classification": {"type": "class", "reference": "io.my_wsi"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_classification"]}},
    }
    with pytest.raises(EadContentValidationError, match="Classes must reference annotations"):
        validate_ead(ead)


def test_wrong_reference_from_collection_items():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {
                "type": "wsi",
            },
            "my_rectangles": {
                "type": "collection",
                "items": {"type": "rectangle", "reference": "io.my_rectangles"},
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangles"], "outputs": []}},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_wrong_reference_into_nested_collection():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsis": {"type": "collection", "items": {"type": "wsi"}},
            "my_params": {"type": "collection", "items": {"type": "float"}},
            "my_wsi_rois": {
                "type": "collection",
                "items": {"type": "collection", "items": {"type": "rectangle", "reference": "io.my_params.items"}},
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsis", "my_params", "my_wsi_rois"], "outputs": []}},
    }
    with pytest.raises(EadContentValidationError, match="Annotations must reference WSIs"):
        validate_ead(ead)


def test_correct_reference_into_nested_collection():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsis": {"type": "collection", "items": {"type": "wsi"}},
            "my_params": {"type": "collection", "items": {"type": "float"}},
            "my_wsi_rois": {
                "type": "collection",
                "items": {"type": "collection", "items": {"type": "rectangle", "reference": "io.my_wsis.items"}},
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsis", "my_params", "my_wsi_rois"], "outputs": []}},
    }
    validate_ead(ead)


def test_correct_references():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {"type": "rectangle", "reference": "io.my_wsi"},
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
            "my_cells": {
                "type": "collection",
                "reference": "io.my_rectangle",
                "items": {"type": "point", "reference": "io.my_wsi"},
            },
            "my_score": {"type": "float", "reference": "io.my_cells"},
            "my_unrelated_collection": {"type": "collection", "items": {"type": "integer"}},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification", "my_cells", "my_score", "my_unrelated_collection"],
            }
        },
    }
    validate_ead(ead)


def test_output_class_constraints():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.global.v1.classes.roi"],
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadContentValidationError, match="Outputs must not have class constraints"):
        validate_ead(ead)


def test_input_class_constraint_using_wrong_namespace():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.other.something.v42.classes.nothing"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_classification"]}},
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Namespace not valid for class value org.empaia.other.something.v42.classes.nothing"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_global_namespace():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.global.v1.classes.roi"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_classification"]}},
    }
    validate_ead(ead)


def test_input_class_constraint_using_wrong_local_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.wrong.v1.classes.foo"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_classification"]}},
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Namespace not valid for class value org.empaia.vendor_name.wrong.v1.classes.foo"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_nonexisting_global_namespace_version():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.global.v42.classes.roi"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {"standalone": {"inputs": ["my_wsi", "my_rectangle"], "outputs": ["my_classification"]}},
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Global namespace not found for class value org.empaia.global.v42.classes.roi"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_malformed_class_value_which_passes_schema():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.global.v1.klasses.roi"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    with pytest.raises(
        EadContentValidationError, match=re.escape("Class value org.empaia.global.v1.klasses.roi is malformed")
    ):
        validate_ead(ead)


def test_input_class_constraint_using_local_namespace_with_missing_class():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.baz"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    with pytest.raises(
        EadContentValidationError,
        match=re.escape("Class value org.empaia.vendor_name.ta.v1.classes.baz not found in class hierarchy"),
    ):
        validate_ead(ead)


def test_input_class_constraint_using_local_namespace():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_top_level_classes():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"name": "Bar"}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_top_level_global_classes():
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
                "reference": "io.my_wsi",
                "classes": ["org.empaia.global.v1.classes"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_inner_class_node():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"baz": {"name": "Baz"}}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    validate_ead(ead)


def test_input_class_constraint_using_leaf_class_node():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "classes": {"foo": {"name": "Foo"}, "bar": {"baz": {"name": "Baz"}}},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
                "classes": ["org.empaia.vendor_name.ta.v1.classes.bar.baz"],
            },
            "my_classification": {"type": "class", "reference": "io.my_rectangle"},
        },
        "modes": {
            "standalone": {
                "inputs": ["my_wsi", "my_rectangle"],
                "outputs": ["my_classification"],
            },
        },
    }
    validate_ead(ead)


def test_disallow_empty_root_configuration_spec():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_wrong_configuration_spec():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "something": {
                "param": {
                    "type": "float",
                    "optional": False,
                }
            },
        },
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_wrong_configuration_param_type_spec():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "param": {
                    "type": "complex",
                    "optional": False,
                }
            },
        },
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_correct_global_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "param": {
                    "type": "integer",
                    "optional": False,
                }
            },
        },
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    validate_ead(ead)


def test_correct_customer_configuration():
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
                }
            },
        },
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    validate_ead(ead)


def test_correct_global_and_customer_configuration():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "configuration": {
            "global": {
                "param": {
                    "type": "float",
                    "optional": True,
                }
            },
            "customer": {
                "something": {
                    "type": "string",
                },
                "foo": {"type": "float", "optional": True},
            },
        },
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    validate_ead(ead)


def test_wrong_permission_section():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "permissions": {"something": "unspecified"},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    with pytest.raises(EadSchemaValidationError):
        validate_ead(ead)


def test_correct_permission_section():
    ead = {
        "$schema": "https://developer.empaia.org/schema/ead-schema.v2.json",
        "name": "Test App",
        "name_short": "TestApp",
        "namespace": "org.empaia.vendor_name.ta.v1",
        "description": "EAD for testing purposes",
        "permissions": {"wsi_raw_file_access": True, "data_transmission_to_external_service_provider": False},
        "io": {
            "my_wsi": {"type": "wsi"},
            "my_rectangle": {
                "type": "rectangle",
                "reference": "io.my_wsi",
            },
        },
        "modes": {"standalone": {"inputs": ["my_wsi"], "outputs": ["my_rectangle"]}},
    }
    validate_ead(ead)
