# Copyright (c) 2021-2022 Mario S. Könz; License: MIT
import dataclasses as dc
import typing as tp
from pathlib import Path

from ._proto_namespace import _ProtoNamespace

__all__ = ["TickSetter"]


@dc.dataclass
class TickSetter:

    ns: _ProtoNamespace
    release_message: str
    major: bool
    minor: bool

    def _print(self, msg: str, **kwgs: tp.Any) -> None:
        # pylint: disable=protected-access
        self.ns._print(msg, **kwgs)

    def bake(self) -> None:
        data = self.ns.auxcon.project
        version, lines = self.ns.get_current_version_and_lines()

        parts = version.split(".")
        if self.major:
            idx = 0
        elif self.minor:
            idx = 1
        else:
            idx = 2
        parts[idx] = str(int(parts[idx]) + 1)
        new_version = ".".join(parts)

        init = Path(data.module_dir) / "__init__.py"
        with init.open("r", encoding="utf8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "__version__" in line:
                    lines[i] = line.replace(version, new_version)

        self._print(f"{version}->{new_version}")
        with init.open("w", encoding="utf8") as f:
            f.writelines(lines)

        release_notes = Path(data.source_dir) / "release-notes.txt"
        with release_notes.open("r", encoding="utf8") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith(new_version):
                raise RuntimeError(f"{new_version} already found in {release_notes}")
        lines.insert(0, f"{new_version} {self.release_message}\n")
        with release_notes.open("w", encoding="utf8") as f:
            f.writelines(lines)
