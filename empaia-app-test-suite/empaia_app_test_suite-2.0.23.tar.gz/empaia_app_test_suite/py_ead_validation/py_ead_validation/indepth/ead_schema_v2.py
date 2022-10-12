from ..exceptions import ConfigValidationError, EadContentValidationError
from .common import _validate_class_value, _validate_reference_type


def validate_ead(ead, namespaces):
    io_mode_refs = set()
    for mode_name, mode_spec in ead["modes"].items():
        _validate_mode(ead, mode_name, mode_spec, io_mode_refs)
        for io_key, io_spec in ead["io"].items():
            _validate_io_item_recursive(ead, mode_spec, io_key, io_spec, namespaces)
    for io_key in ead["io"]:
        if io_key not in io_mode_refs:
            raise EadContentValidationError(f"Unreferenced item in io section: io.{io_key} is not used by any mode")


def validate_config(config, ead):
    config = config if config else {}
    for section_name, config_item in config.items():
        if section_name not in ("customer", "global"):
            raise ConfigValidationError(
                "Please store configurations to validate in the corresponding sections 'global' and 'customer'"
            )
        config_spec = ead.get("configuration", {}).get(section_name, {})
        for key, entry_spec in config_spec.items():
            if not entry_spec.get("optional", False) and key not in config_item:
                raise ConfigValidationError(f"Parameter {key} is missing in given configuration")
            if key in config_item:
                # str[ing], int[eger], bool, float
                if not entry_spec["type"].startswith(type(config_item[key]).__name__):
                    raise ConfigValidationError(f"Parameter {key} has wrong type in given configuration")
        for key in config_item.keys():
            if key not in config_spec:
                raise ConfigValidationError(f"Parameter {key} is not part of the configuration specification")


def _validate_mode(ead, mode_name, mode_spec, io_mode_refs):
    for i_or_o in ("inputs", "outputs"):
        for io_key in mode_spec[i_or_o]:
            if io_key not in ead["io"]:
                raise EadContentValidationError(
                    f"Unresolved {i_or_o} for mode {mode_name}: {io_key} not found in io section"
                )
            other_i_or_o = "inputs" if i_or_o == "outputs" else "outputs"
            if io_key in mode_spec[other_i_or_o]:
                raise EadContentValidationError(f"Mode {mode_name} defines non-disjoint inputs and outputs: {io_key}")
            io_mode_refs.add(io_key)
    if mode_name == "standalone" or mode_name == "preprocessing":
        if not mode_spec.get("containerized", True):
            raise EadContentValidationError(f"{mode_name} mode must not be uncontainerized")
    else:  # postprocessing
        if "containerized" not in mode_spec:
            raise EadContentValidationError("postprocessing mode must specify containerized flag")
    if mode_name == "preprocessing":
        if len(mode_spec["inputs"]) != 1 or ead["io"][mode_spec["inputs"][0]]["type"] != "wsi":
            raise EadContentValidationError("Mode preprocessing requires exactly one input of type wsi")


def _validate_io_item_recursive(ead, mode_spec, io_key, io_spec, namespaces):
    if "reference" in io_spec:
        _validate_reference(ead, mode_spec, io_key, io_spec)
    if "classes" in io_spec:
        _validate_classes(ead, mode_spec, io_key, io_spec, namespaces)
    if io_spec["type"] == "collection":
        _validate_io_item_recursive(ead, mode_spec, io_key + ".items", io_spec["items"], namespaces)


def _validate_reference(ead, mode_spec, io_key, io_spec):
    _, ref_key, *ref_tail = io_spec["reference"].split(".")
    if io_key in mode_spec["inputs"] and ref_key in mode_spec["outputs"]:
        raise EadContentValidationError(f"Inputs must not reference outputs (io.{io_key} -> {io_spec['reference']})")
    reference = ead["io"]
    for node in [ref_key] + ref_tail:
        if node not in reference:
            raise EadContentValidationError(f"{io_spec['reference']} referenced by io.{io_key} not found")
        reference = reference[node]
    _validate_reference_type(io_spec["type"], reference["type"])


def _validate_classes(ead, mode_spec, io_key, io_spec, namespaces):
    if io_key in mode_spec["outputs"]:
        raise EadContentValidationError("Outputs must not have class constraints")
    for class_value in io_spec["classes"]:
        _validate_class_value(ead, class_value, namespaces)
