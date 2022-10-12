"""Evaluate list of changes matched with rule glob pattern

Examples
--------
glob_patterns : list[str]
    List of pattern to evaluate
facts : list[str]
    List of changes
"""
from fnmatch import fnmatch


def is_changes_match_glob(glob_patterns: list[str], facts: list[str]) -> bool:
    """Validate fact match at lease one glob pattern

    This function will be return True when atleast  pattern match with atleast fact

    Parameters
    ----------
    glob_patterns : list[str]
        List of glob pattern to be verified
    facts : list[str]
        Fact to be verified

    Returns
    -------
    bool
        True if atleast item matched
    """

    if not glob_patterns:
        return True

    for pattern in glob_patterns:
        for fact in facts:
            if fnmatch(fact, pattern):
                return True

    return False
