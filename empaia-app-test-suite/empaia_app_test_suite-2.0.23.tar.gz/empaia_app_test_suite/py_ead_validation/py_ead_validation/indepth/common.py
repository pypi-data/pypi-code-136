from ..exceptions import EadContentValidationError

ANNOTATION_TYPES = ("point", "line", "arrow", "rectangle", "polygon", "circle")
PRIMITIVE_TYPES = ("bool", "integer", "float", "string")


def _validate_class_value(ead, class_value, namespaces):
    split_target = ".classes."
    if class_value.endswith(".classes"):
        split_target = ".classes"
    if split_target not in class_value:
        raise EadContentValidationError(f"Class value {class_value} is malformed")
    class_namespace, class_suffix = class_value.split(split_target)
    if class_namespace.startswith("org.empaia.global."):
        for namespace_id, namespace in namespaces.items():
            if namespace_id == class_namespace:
                class_node = namespace["classes"]
                break
        else:
            raise EadContentValidationError(f"Global namespace not found for class value {class_value}")
    elif class_namespace == f"{ead['namespace']}":
        class_node = ead.get("classes", {})
    else:
        raise EadContentValidationError(f"Namespace not valid for class value {class_value}")

    if class_suffix:  # empty if class value is the classes root
        for item in class_suffix.split("."):
            if item not in class_node:
                raise EadContentValidationError(f"Class value {class_value} not found in class hierarchy")
            class_node = class_node[item]


def _validate_reference_type(source_type, target_type):
    if source_type == "collection":
        if target_type != "wsi" and target_type not in ANNOTATION_TYPES:
            raise EadContentValidationError("Collections may only reference WSIs or annotations")
    if source_type in PRIMITIVE_TYPES:
        if target_type != "wsi" and target_type != "collection" and target_type not in ANNOTATION_TYPES:
            raise EadContentValidationError("Primitives may only reference WSIs, collections or annotations")
    if source_type in ANNOTATION_TYPES:
        if target_type != "wsi":
            raise EadContentValidationError("Annotations must reference WSIs")
    if source_type == "class":
        if target_type not in ANNOTATION_TYPES:
            raise EadContentValidationError("Classes must reference annotations")
