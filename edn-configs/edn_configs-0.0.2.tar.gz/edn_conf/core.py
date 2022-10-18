"""TODO."""

import edn_format as edn
import os

from . import eval as e


def load(
    filename: str,
    basefolder: str,
    tags_filename: str = f"{os.path.dirname(os.path.abspath(__file__))}/tags",
    relative: bool = False,
    extension: bool = False,
):
    """Load an edn file with the reader macro defined in tags.edn."""
    with open(f"{tags_filename}.edn", "r") as f:
        tags = e.clojure_eval(edn.loads("".join(f.readlines())))
        for name, f in tags.items():
            edn.add_tag(name, f)
    extension = ".edn" if not extension else ""
    path = (
        f"./{basefolder}/{filename}{extension}"
        if relative
        else f"{basefolder}/{filename}{extension}"
    )

    with open(path, "r") as f:
        return edn.loads("".join(f.readlines()))


def load_and_resolve(
    filename: str,
    basefolder: str = "resources",
    tags_filename: str = f"{os.path.dirname(os.path.abspath(__file__))}/tags",
    relative: bool = False,
    extension: bool = False,
):
    """Load and resolve an edn file."""
    return e.clojure_eval(
        load(filename, basefolder, tags_filename, relative, extension)
    )
