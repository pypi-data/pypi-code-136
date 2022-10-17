# Copyright (c) 2021-2022 Mario S. Könz; License: MIT
import collections
import contextlib
import copy
import filecmp
import os
import shutil
import typing as tp
from pathlib import Path

from .._base_parser import FileOpsConvenience
from .._parser import ConfigParser
from .._parser import Jinja2Parser
from .._proto_namespace import _ProtoNamespace


class Extra(FileOpsConvenience, _ProtoNamespace):
    def __init__(self) -> None:
        super().__init__()
        self.root = Path(__file__).resolve().parent.parent / "src"
        self.verbose = True

        self.versions = _ProtoNamespace(
            pytest="pytest>=6.2",
            pytest_cov="pytest-cov~=3.0",
            pre_commit="pre-commit>=2.10",
            mypy="mypy==0.931",
            pylint="pylint==2.12.2",
            black="black==22.6.0",
            sphinx="sphinx>=4.3",
            sphinx_rtd_theme="sphinx-rtd-theme>=1.0.0",
            sphinx_click="sphinx-click>=3.1",
            jupyter_sphinx="jupyter-sphinx>=0.3",
            bash_kernel="bash_kernel>=0.7",
            ci_docker_image="docker:20.10.17",
            blacken_docs="blacken-docs==v1.12.1",
            pre_commit_hooks="pre-commit-hooks==v4.3.0",
            pyupgrade="pyupgrade==v2.37.3",
            pycln="pycln==v2.1.1",
            reorder_python_imports="reorder_python_imports==v3.8.2",
            encryption_check="encryption_check==v1.0.0",
            docstr_coverage="docstr-coverage==v2.1.1",
        )

    @classmethod
    def _print(
        cls, msg: str, **kwgs: tp.Any  # pylint: disable=unused-argument
    ) -> None:
        print(msg)

    def load_auxcon(self) -> None:
        # pylint: disable=attribute-defined-outside-init
        self.auxcon = ConfigParser.read(self.auxcon_file)
        self.set_defaults()

    def save_auxcon(self) -> None:
        self.cleanup()
        ConfigParser.write(self.auxcon, self.auxcon_file)

    def save_auxcon_to_stream(self, ost: tp.TextIO) -> None:
        ConfigParser.write_stream(self.auxcon, ost)

    @classmethod
    def list2ns(cls, list_w_opt: tp.List[str]) -> _ProtoNamespace:
        res = _ProtoNamespace()
        for item in list_w_opt:
            parts = item.split(";")
            id_ = parts[0].strip()
            res[id_] = _ProtoNamespace()
            for opt in parts[1:]:
                key, val = opt.split("=", 1)
                res[id_][key.strip()] = val.strip()
        return res

    @classmethod
    def compose(cls, *types: type) -> "Renderer":
        if cls not in types:
            types = (cls,) + types
        bases = tuple(reversed(types))
        return type("DynRenderer", bases, {})  # type: ignore

    def copy_file(
        self,
        name: tp.Union[str, Path],
        dest_name: tp.Union[str, Path] = "",
        chmod: tp.Optional[int] = None,
        custom: bool = False,
    ) -> None:
        if isinstance(name, str):
            if custom:
                src = self.target_custom / name
            else:
                src = self.root / name
        else:
            src = name
            assert dest_name != ""

        dest_name = dest_name or name
        if isinstance(name, str):
            dest = self.target / dest_name
        else:
            dest = dest_name

        self.ensure_parent(dest)

        if dest.exists() and filecmp.cmp(src, dest):
            return

        shutil.copyfile(src, dest)
        if chmod:
            self.chmod(dest, chmod)
        if self.verbose:
            self._print(f"copied {dest}", fg="blue")

    def bake_file(  # pylint: disable=too-many-arguments
        self,
        name: str,
        dest_name: str = "",
        chmod: tp.Optional[int] = None,
        only_if_inexistent: bool = False,
        custom: bool = False,
        ignore_absent: bool = False,
        **kwgs: tp.Any,
    ) -> None:
        dest_name = dest_name or name
        src_dir = self.target_custom if custom else self.root
        dest = self.target / dest_name
        if only_if_inexistent and dest.exists():
            return

        src = src_dir / name
        if src.exists():
            self.copy_file(name, dest_name, chmod=chmod, custom=custom)
            return

        jinja_src = src_dir / (name + ".jinja2")
        if not jinja_src.exists() and ignore_absent:
            return
        written = Jinja2Parser.render_to_dest(jinja_src, dest, aux=self.auxcon, **kwgs)
        if written:
            if chmod:
                self.chmod(dest, chmod)
            self._print(f"baked {dest}", fg="green")

    def combine_files(self, *names: str, dest_name: str) -> None:
        tmp_combo = self.root / "temp-combination"
        if tmp_combo.exists():
            tmp_combo.unlink()
        with open(tmp_combo, "a", encoding="utf-8") as tmp:
            for name in names:
                src = self.root / name
                with open(src, encoding="utf-8") as in_:
                    tmp.writelines(in_.readlines())
                    if name != names[-1]:
                        tmp.write("\n")

        self.copy_file(tmp_combo.name, dest_name)
        tmp_combo.unlink()

    @classmethod
    def chmod(cls, dest: Path, chmod: int) -> None:
        os.chmod(dest, chmod)

    def copy_many_files(self, *names: str) -> None:
        for name in names:
            self.copy_file(name)


class Renderer(Extra):
    def __init__(self) -> None:
        super().__init__()
        self.set_defaults()

    def set_defaults(self) -> None:
        self.setdefault("auxcon", _ProtoNamespace())

    def clear_to_demo(self, **kwgs: tp.Any) -> None:
        self.clear_to_template(**kwgs)

    def cleanup(self, **kwgs: tp.Any) -> None:
        for component, keys in kwgs.items():
            for key in keys:
                if not self.auxcon[component][key]:
                    del self.auxcon[component][key]

        for key in copy.copy(self.auxcon):
            if not self.auxcon[key]:
                del self.auxcon[key]

    def clear_to_template(self, **kwgs: str) -> None:
        assert not kwgs
        self.auxcon.clear()
        self.set_defaults()

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        pass

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        self.auxcon.versions = copy.copy(self.versions)
        yield

    def bake(self) -> None:
        pass

    def writeout(self) -> None:
        pass


class MetaMixin(Renderer):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("meta", _ProtoNamespace())
        self.auxcon.meta.setdefault("disabled", ["docs"])

    def clear_to_demo(self, **kwgs: tp.Any) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.meta.disabled = ["some_module"]

    def is_enabled(self, component_name: str) -> bool:
        return component_name not in self.auxcon.meta.disabled

    def type_wo_disabled(
        self,
        disabled_list: tp.Optional[tp.List[str]] = None,
        *,
        discard_before: str = "",
        check_absence: bool = True,
    ) -> "Renderer":
        disabled_list = disabled_list or self.auxcon.meta.disabled
        res: tp.List[type] = []
        for part in self.__class__.__mro__:
            if part.__name__ == discard_before:
                res.clear()
            if part.__name__ in ["AllRenderer", "DynRenderer"]:
                continue
            if not any(
                part.__name__.lower().startswith(x.replace("-", ""))
                for x in disabled_list
            ):
                res.append(part)

        res_type = Renderer.compose(*reversed(res))

        # check if disabled did not get added by enabled
        if check_absence:
            compare_to = self.type_wo_disabled(
                discard_before="SentinelMixin", check_absence=False
            )
            parents: tp.MutableMapping[
                type, tp.Sequence[type]
            ] = collections.defaultdict(list)
            for part in compare_to.__mro__[1:]:  # remove bottom dyn
                parents[part] = part.__mro__[1:]  # remove self == part
                if any(
                    part.__name__.lower().startswith(x.replace("-", ""))
                    for x in disabled_list
                ):
                    used_by = [
                        key.__name__ for key, val in parents.items() if part in val
                    ]
                    raise RuntimeError(
                        f"{part.__name__} cannot be disabled, as it is used by {', '.join(used_by)}"
                    )

        return res_type
