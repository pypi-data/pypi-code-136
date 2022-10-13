"""
Common mappings for MYSTRAN and FEMAP
for each self.flavor, describe vectors in terms of (<vector>, <axis>)
"""
import json
from collections import defaultdict
from importlib import resources

import pkg_resources

from femap_neutral_parser.utils import CaseInsensitiveDict

with resources.open_text("femap_neutral_parser.data", "neutral_flavors.json") as fh:
    _headers_to_neutral = json.loads(fh.read())
# due to json restrictions, we cannot save it wit(vector, axis) keys
# hence, we need to 'compact' it:
HEADERS_TO_NEUTRAL = {}
for vector, data in _headers_to_neutral.items():
    for axis, titles in data.items():
        HEADERS_TO_NEUTRAL[(vector, axis)] = titles
# =============================================================================
# the following boilerplate is purely cosmetcis and ensure that
# engineering high-level functions will get t1 before r1
# =============================================================================
HEADERS_TO_NEUTRAL = list(HEADERS_TO_NEUTRAL.items())
# tercery key
HEADERS_TO_NEUTRAL = sorted(HEADERS_TO_NEUTRAL, key=lambda x: x[0][1], reverse=False)
# secondary key: sort by <axis> first letter, "t" before "r"
HEADERS_TO_NEUTRAL = sorted(HEADERS_TO_NEUTRAL, key=lambda x: x[0][1][0], reverse=True)
# primary key: sort by <vector>
HEADERS_TO_NEUTRAL = sorted(HEADERS_TO_NEUTRAL, key=lambda x: x[0][0], reverse=False)
# and go back to dict...
HEADERS_TO_NEUTRAL = dict(HEADERS_TO_NEUTRAL)


# ALIASES are used to restrict `get_vectors` returned values
ALIASES = {
    "cbar_force": {
        "axial_b": "axial",
        "axial_a": "axial",
        "torque_b": "torque",
        "torque_a": "torque",
        "shear_a2": "shear2",
        "shear_a1": "shear1",
        "shear_b2": "shear2",
        "shear_b1": "shear1",
    },
    "cbeam_force": {
        "axial_b": "axial",
        "axial_a": "axial",
        "torque_b": "torque",
        "torque_a": "torque",
        "shear_a2": "shear2",
        "shear_a1": "shear1",
        "shear_b2": "shear2",
        "shear_b1": "shear1",
    },
}

REVERTED_ALIASES = {}
for vector, merges in ALIASES.items():
    REVERTED_ALIASES[vector] = {v: k for k, v in merges.items()}


# -----------------------------------------------------------------------------
# prepare reversed search
# "RSS translation" -> ("displacements", "t_total")  # as pynastran
NEUTRAL_TO_HEADERS = CaseInsensitiveDict()
for headers, titles in HEADERS_TO_NEUTRAL.items():
    for title in titles:
        if title:
            if title in NEUTRAL_TO_HEADERS and headers != NEUTRAL_TO_HEADERS[title]:
                raise ValueError(
                    f"CaseInsensitiveDict cannot handle a different {title=}\nAlready stored {NEUTRAL_TO_HEADERS[title]}\nWant to add {headers}"
                )
            NEUTRAL_TO_HEADERS[title] = headers


class Flavor:
    """Mixin handling neutral self.flavor

    >>> f = Flavor()
    >>> f.title_to_headers("T1 translation")
    ('displacements', 't1')
    >>> f.title_to_headers("t1 TrAnslation")
    ('displacements', 't1')
    """

    def title_to_headers(self, key, merge_aliases=False):
        """Convert Neutral title to headers tuple:

        >>> f = Flavor()
        >>> f.title_to_headers("T1 translation")
        ('displacements', 't1')
        >>> f.title_to_headers("BAR EndA Torque")
        ('cbar_force', 'torque_a')
        >>> f.title_to_headers("BAR EndA Torque", merge_aliases=True)
        ('cbar_force', 'torque')
        """
        headers = NEUTRAL_TO_HEADERS.get(key)
        if not headers:
            # return initial FEMAP/MYSTRAN title
            return key
        vector, axis = headers
        if merge_aliases:
            # check if an alias esits
            aliases = ALIASES.get(vector)
            if aliases:
                axis = aliases.get(axis, axis)
        return (vector, axis)

    def headers_to_title(self, key):
        """search for `key` in `self.flavor` dict
        >>> f = Flavor()
        >>> f.headers_to_title(("displacements", "t1"))
        'T1 translation'
        >>> f.headers_to_title("displacements::t1")
        'T1 translation'
        >>> f.headers_to_title(('cbar_force', 'torque_a'))
        'BAR EndA Torque'
        >>> f.headers_to_title(('cbar_force', 'torque_a'))
        'BAR EndA Torque'
        >>> f.headers_to_title(('cbar_force', 'torque'))
        'BAR EndA Torque'
        """
        if isinstance(key, str):
            vector, axis = key.split("::")
        else:
            # assumed a correct tuple was passed
            vector, axis = key
        try:
            axis = REVERTED_ALIASES[vector][axis]
        except KeyError:
            pass  # no alias
        title = HEADERS_TO_NEUTRAL[(vector, axis)][0]
        return title

    @classmethod
    def get_vectors(self, what=None, merge_aliases=False):
        """
        return a list of relevant vectors
        >>> f = Flavor()
        >>> f.get_vectors("cbar_force") == [
        ... 'cbar_force::torque_a',
        ... 'cbar_force::torque_b',
        ... 'cbar_force::shear_a1',
        ... 'cbar_force::shear_a2',
        ... 'cbar_force::shear_b1',
        ... 'cbar_force::shear_b2',
        ... 'cbar_force::bending_moment_a1',
        ... 'cbar_force::bending_moment_a2',
        ... 'cbar_force::bending_moment_b1',
        ... 'cbar_force::bending_moment_b2',
        ... 'cbar_force::axial_a',
        ... 'cbar_force::axial_b']
        True

        If merge_aliases is `True`::
        >>> f.get_vectors("cbar_force", merge_aliases=True) == [
        ... 'cbar_force::bending_moment_a1',
        ... 'cbar_force::bending_moment_a2',
        ... 'cbar_force::bending_moment_b1',
        ... 'cbar_force::bending_moment_b2',
        ... 'cbar_force::axial',
        ... 'cbar_force::shear1',
        ... 'cbar_force::shear2',
        ... 'cbar_force::torque']
        True

        Ommitting key will give access to available vectors families::
        >>> sorted(list(f.get_vectors()))
        ['applied_gpf', 'cbar_force', ..., 'spc_forces', 'summed_gpf']

        """
        dic = defaultdict(list)
        for (vector, axis), initial_title in HEADERS_TO_NEUTRAL.items():
            dic[vector].append(axis)
        dic = dict(dic)
        # -> {..., 'cbar_force': ['torque_a', 'torque_b',...], ...}
        if merge_aliases:
            for vector, merges in ALIASES.items():
                dic[vector] = [axis for axis in dic[vector] if axis not in merges]
                dic[vector] += sorted(list(set(merges.values())))
        if what is not None:
            return [f"{what}::{t}" for t in dic[what]]
        return set(dic.keys())


if __name__ == "__main__":
    import doctest

    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
