import glob
import json
import os
import re
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from typing import Callable

from pydantic import BaseModel

from datapac.package.artefact import Artefact
from datapac.package.path import format
from datapac.package.path import parse

_open = open

Loader = Callable[[str], list[Artefact]]


class InvalidPackageError(RuntimeError):
    pass


class Package(BaseModel):
    path: str
    artefacts: list[Artefact] = []

    def add_artefact(self, artefact: Artefact):
        self.artefacts.append(artefact)


@contextmanager
def open(path: str, loaders: list[Loader]):
    validate(path)

    pkg = Package(path=path)

    for loader in loaders:
        pkg.artefacts += loader(path)

    yield pkg


def validate(path: str) -> None:
    config_path = os.path.join(path, "datapac.json")

    # TODO
    # if not os.path.isabs(path):
    #     raise ValueError(f"[{path}] is not absolute path")
    # if not os.path.exists(path):
    #     raise ValueError(f"[{path}] does not exist")

    if not os.path.exists(config_path):
        raise InvalidPackageError("missing datapac.json file")

    with _open(config_path) as f:
        return json.load(f)


@contextmanager
def create(path: str):
    package = Package(path=path)

    yield package

    write(package, path)


def write(package: Package, path: str):
    if not os.path.isabs(path):
        raise ValueError(f"[{path}] is not absolute path")

    if os.path.exists(path):
        raise ValueError(f"[{path}] already exists")

    os.mkdir(path)

    for artefact in package.artefacts:
        abs_path = os.path.join(path, artefact.output_path)

        # make nested dirs
        os.makedirs(
            os.path.dirname(abs_path),
            exist_ok=True,
        )

        artefact.write(abs_path)

    with _open(os.path.join(path, "datapac.json"), "w") as f:
        f.write(json.dumps({}))


def match_str(pattern: str, input: str) -> tuple[bool, dict[str, str]]:
    def compile(name, spec):
        return f"(?P<{name}>.*)" if spec == "/" else f"(?P<{name}>[^/]*)"

    vars = {name: compile(name, spec) for name, spec in parse(pattern).items()}
    regex = format(pattern, **vars)
    result = re.compile(regex).search(input)

    return (True, result.groupdict()) if result else (False, {})


def match_files(path: str, pattern: str):
    for entry in glob.glob(f"{path}/**", recursive=True):
        if not os.path.isfile(entry):
            continue

        match match_str(pattern, entry):
            case True, kwargs:
                yield (entry, kwargs)


@contextmanager
def render(template: Package, variables: dict):
    with TemporaryDirectory() as tmp_dir:
        with create(os.path.join(tmp_dir, "rendered")) as pkg:
            for artefact in template.artefacts:
                pkg.add_artefact(artefact.map(variables))

        yield pkg
