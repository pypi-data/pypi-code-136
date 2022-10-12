import enum


class PackageType(enum.Enum):
    """An enum representing the types of possible packages."""

    PYTHON_PACKAGE = "PYTHON_PACKAGE"
    LINUX_SHARED_OBJECT = "LINUX_SHARED_OBJECT"
    DOCKER_BUILD_TRITON = "DOCKER_BUILD_TRITON"
    ONNXRUNTIME_CUSTOM_OPERATOR_LINUX = "ONNXRUNTIME_CUSTOM_OPERATOR_LINUX"
