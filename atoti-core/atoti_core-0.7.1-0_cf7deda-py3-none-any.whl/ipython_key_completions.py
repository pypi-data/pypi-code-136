from typing import Any, List, Mapping, Tuple, Union

IPythonKeyCompletions = List[Union[str, Tuple[str, str]]]


def get_ipython_key_completions_for_mapping(
    mapping: Union[Mapping[str, Any], Mapping[Tuple[str, ...], Any]]
) -> IPythonKeyCompletions:
    """Return IPython key completions for mapping."""
    return sorted({key if isinstance(key, str) else key[-1] for key in mapping})
