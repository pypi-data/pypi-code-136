
from itertools import chain

from generallibrary import deco_cache, flatten

from generalpackager.api.localrepo.base.localrepo_target import Targets


class Packages(Targets):
    """ Purpose is to easily see if name is general and what target it has.
        Todo: Generate Python file in generalpackager containing general packages. """
    python = [
        "generalimport",
        "generallibrary",
        "generalfile",
        "generalvector",
        "generalgui",
        "generalbrowser",
        "generalpackager",
    ]
    node = [
        "genlibrary",
        "genvector",
    ]
    django = [

    ]
    exe = [
        "generalmainframe",
    ]

    @classmethod
    @deco_cache()
    def all_packages(cls):
        return flatten(cls.field_values_defaults())

