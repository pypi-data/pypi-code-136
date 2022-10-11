import importlib
import importlib.util
import os
import sys
from typing import Optional, Tuple

from prefect.flows import Flow


def import_prefect_flow_from_file(
    pipeline_path: str, flow_cb: str = "main"
) -> Tuple[str, Flow]:
    """Import a prefect flow from a file path.

    Args:
        pipeline_path: Path to `.py`-file containing flow, or a directory. If a directory is specified, then the flow is assumed to be in `flow.py` within the specified directory
        flow_cb: Name of function with the `@flow`-decorator

    Returns:
        Imported flow

    Raises:
        ImportError: Failed to import flow for some reason
    """

    _, ext = os.path.splitext(pipeline_path)
    if ext != ".py":
        module_path = os.path.join(pipeline_path, "flow.py")
    else:
        module_path = pipeline_path

    if not os.path.exists(module_path):
        raise ImportError(f"The module '{module_path}' does not exist")

    module_name, _ = os.path.splitext(os.path.split(module_path)[-1])

    spec = importlib.util.spec_from_file_location(f"flows.{module_name}", module_path)
    if not spec or not spec.loader:
        raise ImportError(f"Failed to import flow from file '{module_path}'")

    sys.path.append(os.path.abspath(pipeline_path))
    flow_module = importlib.util.module_from_spec(spec)
    if not flow_module:
        raise ImportError(f"Failed to import flow from module spec '{spec.name}'")

    spec.loader.exec_module(flow_module)

    flow_module_name = ".".join(flow_module.__name__.split(".")[:-1])
    return flow_module_name, getattr(flow_module, flow_cb)
