# Copyright (c) 2021-2022 Mario S. Könz; License: MIT
import io
import pprint
from pathlib import Path

from ._components import AllRenderer
from ._components._extra_and_renderer import Renderer
from ._gitlab import GitlabSetter
from ._tick import TickSetter


class LazyVersionStr:
    def __str__(self) -> str:
        # pylint: disable=import-outside-toplevel,cyclic-import
        import adaux

        return adaux.__version__


class CliMixin(Renderer):  # pylint: disable=too-many-ancestors
    def __init__(self, target: Path, silent: bool = False) -> None:
        super().__init__()
        self.verbose = not silent
        self.target = Path(target).resolve()

        if str(Path.cwd()) in str(self.target):
            self.target = self.target.relative_to(Path.cwd())
        self.auxcon_file = self.target.parent / "auxilium.cfg"
        if self.auxcon_file.exists():
            self.load_auxcon()

        self._print(
            f"administratum.auxilium {LazyVersionStr()} at your service", fg="blue"
        )

    @property
    def target_custom(self) -> Path:
        return self.target / "custom"

    def demo(self: "CliMixin") -> None:
        self.clear_to_demo()
        out = io.StringIO()
        self.save_auxcon_to_stream(out)
        self._print(out.getvalue())

    def show(self: "CliMixin") -> None:
        ppr = pprint.PrettyPrinter(indent=4, sort_dicts=False)
        self._print(ppr.pformat(self.auxcon))

    def init(
        self: "CliMixin",
        project_name: str,
        project_slug: str,
        python_version: str,
        author: str,
        force: bool = False,
    ) -> None:

        self.clear_to_template(
            project_name=project_name,
            project_slug=project_slug,
            python_version=python_version,
            author=author,
        )

        self.target.mkdir(parents=True, exist_ok=True)
        dest = self.auxcon_file
        over, fg_col = "", "green"

        if dest.exists():
            assert force
            over, fg_col = "over", "yellow"

        self.save_auxcon()

        # pylint: disable=protected-access
        self._print(f"{over}written template to {dest}", fg=fg_col)

    def sync(self: "CliMixin") -> None:
        proj = self.auxcon.project
        clean = self.type_wo_disabled(discard_before="SentinelMixin")()

        clean.clear_to_template(
            project_name=proj.name,
            project_slug=proj.slug,
            python_version=proj.minimal_version,
            author=proj.author,
        )
        self.update_to_template(clean.auxcon)
        self.save_auxcon()

    def bake(self: "CliMixin") -> None:
        if not self.auxcon_file.exists():
            raise RuntimeError(f"{self.auxcon_file} does not exists! use 'aux init'")
        super().bake()

    def gitlab(self: "CliMixin", token: str) -> None:
        gls = GitlabSetter(self, token)
        with self.extra():
            gls.bake()

    def pipeline(self: "CliMixin", token: str, show_success: bool) -> bool:
        gls = GitlabSetter(self, token)
        with self.extra():
            return gls.pipeline(show_success)

    def tick(
        self: "CliMixin", release_message: str, major: bool = False, minor: bool = False
    ) -> None:
        if major and minor:
            raise RuntimeError("cannot set major and minor tick at the same time!")
        if len(release_message) < 16:
            raise RuntimeError("message cannot be shorter than 16 char")
        ticker = TickSetter(self, release_message, major, minor)
        with self.extra():
            ticker.bake()

    def release(self: "CliMixin", token: str) -> None:
        gls = GitlabSetter(self, token)
        with self.extra():
            return gls.release()


class CliRenderer(CliMixin, AllRenderer):  # pylint: disable=too-many-ancestors
    pass
