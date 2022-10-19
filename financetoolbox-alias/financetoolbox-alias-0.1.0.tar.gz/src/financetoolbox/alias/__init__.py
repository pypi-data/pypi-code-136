import os
import sys
import logging
import functools
from typing import Dict, Optional
from types import ModuleType

FTBX_MODULE_ORIGINAL_NAME = os.environ.get("FTBX_MODULE_ORIGINAL_NAME")
FTBX_MODULE_ALIAS_NAME = os.environ.get("FTBX_MODULE_ALIAS_NAME")
FTBX_MODULE_ALIAS_CONFIG_ON_IMPORT_FLAG = os.environ.get("FTBX_MODULE_ALIAS_CONFIG_ON_IMPORT_FLAG", "off")\
    .lower().startswith("on")


logger = logging.getLogger(__name__)


def validate_module_arguments(function):
    @functools.wraps
    def wrapper(**kwargs):
        if not all([kwargs.get("module_original_name"), kwargs.get("module_alias_name")]):
            raise ValueError(
                "Need to specify the following env.vars: FTBX_MODULE_ORIGINAL_NAME, FTBX_MODULE_ALIAS_NAME"
            )
        return function(**kwargs)
    return wrapper


@validate_module_arguments
def get_module_items(
        module_reference_name: str,
        parent: str = "",
        module_original_name: Optional[str] = FTBX_MODULE_ORIGINAL_NAME,
        module_alias_name: Optional[str] = FTBX_MODULE_ALIAS_NAME,
) -> Dict:
    # Import module
    module_import_pattern = f"{module_reference_name}" if not parent else f"{parent}.{module_reference_name}"
    module_instance = __import__(module_import_pattern, fromlist=["*"])
    # Inspect module and detect candidate items
    module_items = {
        item_key: [
            submodule_instance,
            f"{module_import_pattern}.{item_key}".replace(
                module_original_name or "",
                module_alias_name or ""
            )
        ]
        for item_key in (
            module_instance.__dict__["__all__"]
            if "__all__" in module_instance.__dict__
            else dir(module_instance)  # Maybe we should only allow "__all__" inspection
        )
        if not item_key.startswith("_")
        for submodule_instance in [getattr(module_instance, item_key)]
        if isinstance(submodule_instance, ModuleType)
    }
    relative_top_level_names = [*module_items.keys()]
    for module_item in relative_top_level_names:
        module_items.update(
            get_module_items(
                module_reference_name=module_item,
                parent=module_import_pattern,
                module_original_name=module_original_name,
                module_alias_name=module_alias_name,
            )
        )
    return module_items


@validate_module_arguments
def get_module_aliases(
        module_reference_name: str,
        module_original_name: Optional[str] = FTBX_MODULE_ORIGINAL_NAME,
        module_alias_name: Optional[str] = FTBX_MODULE_ALIAS_NAME,
) -> Dict:
    return {
        module_alias: module_instance
        for module_instance, module_alias in get_module_items(
            module_reference_name=module_reference_name,
            module_original_name=module_original_name,
            module_alias_name=module_alias_name,
        ).values()
    }


@validate_module_arguments
def set_alias(
        module_original_name: Optional[str] = FTBX_MODULE_ORIGINAL_NAME,
        module_alias_name: Optional[str] = FTBX_MODULE_ALIAS_NAME,
):
    aliases = get_module_aliases(
        module_reference_name=f"financetoolbox.{module_original_name}",
        module_original_name=module_original_name,
        module_alias_name=module_alias_name
    )
    globals().update(aliases)  # Do we really need this?
    sys.modules.update(aliases)


def set_aliases(**kwargs):
    for module_original_name, module_alias_name in kwargs.items():
        set_alias(
            module_original_name=module_original_name,
            module_alias_name=module_alias_name,
        )


if FTBX_MODULE_ALIAS_CONFIG_ON_IMPORT_FLAG:
    logger.warning(
        f"Module Alias Autoconfig feature is enabled: {FTBX_MODULE_ORIGINAL_NAME} -> {FTBX_MODULE_ALIAS_NAME}"
    )
    set_alias()
