from ..exceptions import ConfigValidationError, EadContentValidationError
from .common import _validate_class_value, _validate_reference_type


def validate_ead(ead, namespaces):
    for io in ("inputs", "outputs"):
        for key, spec in ead[io].items():
            _validate_recursive(ead, io, key, spec, namespaces)
    _validate_config_spec(ead)


def validate_config(config, ead):
    config_spec = ead.get("configuration", {})
    config = config if config else {}
    for key, entry_spec in config_spec.items():
        if not entry_spec.get("optional", False) and key not in config:
            raise ConfigValidationError(f"Parameter {key} is missing in given configuration")
        if key in config:
            # str[ing], int[eger], bool, float
            if not entry_spec["type"].startswith(type(config[key]).__name__):
                raise ConfigValidationError(f"Parameter {key} has wrong type in given configuration")
    for key in config.keys():
        if key not in config_spec:
            raise ConfigValidationError(f"Parameter {key} is not part of the configuration specification")


def _validate_recursive(ead, io, key, spec, namespaces):
    if "reference" in spec:
        _validate_reference(ead, io, key, spec)
    if "classes" in spec:
        _validate_classes(ead, io, spec, namespaces)
    if spec["type"] == "collection":
        _validate_recursive(ead, io, key + ".items", spec["items"], namespaces)


def _validate_reference(ead, io, key, spec):
    if io == "inputs" and spec["reference"].startswith("outputs."):
        raise EadContentValidationError(f"Inputs must not reference outputs (inputs.{key} -> {spec['reference']})")
    head, *tail = spec["reference"].split(".")
    reference = ead[head]
    for node in tail:
        if node not in reference:
            raise EadContentValidationError(f"{spec['reference']} referenced by {io}.{key} not found")
        reference = reference[node]
    _validate_reference_type(spec["type"], reference["type"])


def _validate_classes(ead, io, spec, namespaces):
    if io == "outputs":
        raise EadContentValidationError("Outputs must not have class constraints")
    for class_value in spec["classes"]:
        _validate_class_value(ead, class_value, namespaces)


def _validate_config_spec(ead):
    if "configuration" in ead:
        for entry in ead["configuration"].values():
            if entry["storage"] != "global":
                raise EadContentValidationError("Only global storage is supported for the configuration entries")
