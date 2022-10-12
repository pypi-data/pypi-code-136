from typing import Any, Mapping, Optional, cast

from .running_in_ipython import running_in_ipython


def find_corresponding_top_level_variable_name(
    value: Any,
) -> Optional[str]:
    if not running_in_ipython():
        return None

    from IPython import (  # pylint: disable=undeclared-dependency, nested-import
        get_ipython,
    )

    top_level_variables: Mapping[str, Any] = cast(Any, get_ipython()).user_ns

    for variable_name, variable_value in top_level_variables.items():
        is_regular_variable = not variable_name.startswith("_")
        if is_regular_variable and variable_value is value:
            return variable_name

    return None
