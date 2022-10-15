# Copyright (c) 2021-2022 Mario S. Könz; License: MIT
# pylint: disable=too-many-lines
import collections
import contextlib
import copy
import datetime
import os
import re
import subprocess
import sys
import typing as tp
from pathlib import Path

from .._parser import ConfigParser
from .._parser import Jinja2Parser
from .._parser import YamlParser
from .._proto_namespace import _ProtoNamespace
from ._extra_and_renderer import Renderer


class ProjectMixin(Renderer):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("project", _ProtoNamespace())

    def clear_to_template(self, *, project_name: str, project_slug: str, python_version: str, author: str, **kwgs: str) -> None:  # type: ignore # pylint: disable=arguments-differ
        super().clear_to_template(**kwgs)
        data = self.auxcon.project
        data.name = project_name
        data.slug = project_slug
        data.minimal_version = python_version
        data.supported_versions = [python_version]
        data.author = author
        data.creation_year = self.get_current_year()

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(
            project_name="hallo.world",
            project_slug="hlw",
            python_version=self.deduce_python_version(),
            author="anonymous",
            **kwgs,
        )
        data = self.auxcon.project
        data.license = "MIT"

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.project
            data.minimal_version_slug = data.minimal_version.replace(".", "")
            data.setdefault("source_dir", "source")  # stay sync with aux_ci!
            data.setdefault("license", "Proprietary")
            data.module_dir = data.source_dir + "/" + data.name.replace(".", "/")
            data.namespace_name, data.second_name = "", data.name
            if "." in data.name:
                data.namespace_name, data.second_name = data.name.split(".", 1)
            data.active_years = self.get_active_years()
            data.setdefault("project_urls", _ProtoNamespace())
            data.setup_fields = [
                "name",
                "author",
                "license",
                "description",
                "long_description",
                "project_urls",
            ]
            yield
            del data.module_dir
            del data.minimal_version_slug
            del data.second_name
            del data.active_years
            del data.setup_fields
            del data.namespace_name

    def bake(self) -> None:
        super().bake()
        data = self.auxcon.project
        self.bake_file("install-dev.sh", chmod=0o755)
        self.bake_file("root/_setup.py", "../setup.py")

        srcj = self.root / "root/setup.cfg.jinja2"
        with Jinja2Parser.render_to_tmp(srcj, aux=self.auxcon) as src:
            data.config = ConfigParser.read(src)
            for key in data.setup_fields:
                if key not in data:
                    continue
                val = data[key]
                if val:
                    data.config.metadata[key] = val

        # license
        if data.license != "Proprietary":
            self.bake_file(
                f"license/{data.license}.txt",
                (self.target / ".." / "LICENSE.txt").resolve(),
            )

    def writeout(self) -> None:
        super().writeout()
        dest = self.target / "../setup.cfg"
        written = ConfigParser.write(self.auxcon.project.pop("config"), dest)
        if written:
            self._print(f"baked {dest}", fg="green")

    @classmethod
    def deduce_project_name(cls, path: tp.Optional[Path] = None) -> str:
        proj_name = None
        path = path or (Path.cwd())

        for obj in path.iterdir():
            if obj.is_dir():
                if obj.stem not in ["devops", ".git", "playground", "dist"]:
                    proj_name = obj.stem
        if proj_name is None:
            return "not-found"

        first_init = path / proj_name / "__init__.py"
        if first_init.exists():
            if "__version__" in first_init.open("r", encoding="utf-8").read():
                return proj_name

        subdir = "not-found"
        for guess in [path / proj_name, path / "source"]:
            if guess.exists():
                subdir = cls.deduce_project_name(guess)
                break

        if "." in subdir:
            proj_name = subdir  # we track at most two levels
        elif subdir != "not-found":
            proj_name = f"{proj_name}.{subdir}"
        return proj_name

    @classmethod
    def deduce_project_slug(cls) -> str:
        proj_name = cls.deduce_project_name()
        if "." in proj_name:
            ns, sub = proj_name.split(".")
            return ns[:2] + sub[:3]
        return proj_name[:3]

    @classmethod
    def deduce_python_version(cls) -> str:
        return ".".join(map(str, sys.version_info[:2]))

    @classmethod
    def deduce_user(cls) -> str:
        return os.environ.get("USER", os.environ.get("USERNAME", "unknown"))

    @property
    def python_version_slug(self) -> str:
        return str(self.auxcon.project.minimal_version.replace(".", ""))

    def get_active_years(self) -> str:
        current_year = self.get_current_year()
        creation_year = self.auxcon.project.creation_year
        if creation_year == current_year:
            return f"{creation_year}"

        return f"{creation_year}-{current_year}"

    @classmethod
    def get_current_year(cls) -> str:
        return str(datetime.date.today().year)

    def get_current_version_and_lines(self) -> tp.Tuple[str, tp.List[str]]:
        data = self.auxcon.project
        init = Path(data.module_dir) / "__init__.py"

        with init.open("r", encoding="utf8") as f:
            lines = f.readlines()
            for line in lines:
                if "__version__" in line:
                    version = line.strip().split('"', 2)[1]
                    break
            else:
                raise RuntimeError(f"version not found in {init}")

        return version, lines

    def get_release_notes(self) -> tp.Dict[str, str]:
        data = self.auxcon.project
        notes = Path(data.source_dir) / "release-notes.txt"
        release_note: tp.Dict[str, str] = {}
        with notes.open("r", encoding="utf8") as f:
            for line in f.readlines():
                version, note = line.strip().split(" ", 1)
                release_note[version] = note

        return release_note


class GitIgnoreMixin(ProjectMixin):
    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            self.auxcon.setdefault("git_ignore", _ProtoNamespace())
            self.auxcon.git_ignore.setdefault("root", [])
            self.auxcon.git_ignore.setdefault("source", [])
            yield

    def bake(self) -> None:
        super().bake()
        self.bake_file("gitignore", ".gitignore")

        data = self.auxcon.project

        name1 = "root/gitignore_root"
        name2 = "root/gitignore_source"
        src1 = self.root / f"{name1}.jinja2"
        src2 = self.root / f"{name2}.jinja2"
        dest = self.target / ".." / ".gitignore"
        if data.source_dir != ".":
            self.bake_file(name1, "../.gitignore")
            self.bake_file(name2, f"../{data.source_dir}/.gitignore")

            flip = False
            for key in list(self.auxcon.project.config):
                if flip:
                    self.auxcon.project.config.move_to_end(key)
                if key == "options":
                    flip = True
                    self.auxcon.project.config["options.packages.find"] = dict(
                        where=data.source_dir
                    )

        else:
            tpl1 = Jinja2Parser.read(src1)
            tpl2 = Jinja2Parser.read(src2)
            tpl = f"{tpl1.render(aux=self.auxcon)}\n{tpl2.render(aux=self.auxcon)}"
            written = Jinja2Parser.write(tpl, dest)
            if written:
                self._print(f"baked {dest}", fg="green")


class GitlabMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("gitlab", _ProtoNamespace())

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.gitlab
        data.vip_branches = [
            "develop;push_access_level=40;allow_force_push=True",
            "release",
        ]

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.gitlab.vip_branches[
            0
        ] += ";push_access_level=40,allow_force_push=True"
        self.auxcon.gitlab.default_branch = "develop"
        self.auxcon.gitlab.release_branch = "release"
        self.auxcon.gitlab.remote_user = "administratum"
        self.auxcon.gitlab.remote_url = "gitlab.x.y"

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.gitlab
            data.setdefault("vip_branches", ["release", "develop"])
            vip_branches_og = data.vip_branches
            data.vip_branches = self.list2ns(vip_branches_og)
            vip_branch_name = list(data.vip_branches)
            data.setdefault("default_branch", vip_branch_name[0])
            data.setdefault("release_branch", vip_branch_name[-1])

            # if "remote_user" not in data or "remote_url" not in data:
            #     try:
            #         resp = subprocess.run(
            #             "git remote -v".split(), capture_output=True, check=True
            #         )
            #         out = resp.stdout.decode("utf8")
            #         url = out.split()[1]
            #         match = re.match(r"git@([^:]+):([\w]+)\/([\w]+).git", url)
            #         assert match
            #         data.setdefault("remote_url", match.group(1))
            #         data.setdefault("remote_user", match.group(2))
            #     except subprocess.CalledProcessError:
            #         pass

            if "remote_user" in data and "remote_url" in data:
                self.auxcon.project.project_urls.Source = f"https://{data.remote_url}/{data.remote_user}/{self.auxcon.project.second_name}"

            # https://docs.gitlab.com/ee/api/protected_branches.html
            default = {
                (False, False): dict(
                    allow_force_push=True, push_access_level=30, merge_access_level=30
                ),
                (True, False): dict(push_access_level=0, merge_access_level=30),
                (False, True): dict(push_access_level=0, merge_access_level=40),
            }
            for key, val in data.vip_branches.items():
                mark = (key == data.default_branch, key == data.release_branch)
                for skey, sval in default[mark].items():
                    val.setdefault(skey, sval)

            yield
            data.vip_branches = vip_branches_og


class DependencyMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("dependencies", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.dependencies.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(dependencies=self.__keys()[1:], **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return (
            "default",
            "test",
            "dev",
            "docs",
            "default_apt",
            "test_apt",
            "dev_apt",
            "docs_apt",
        )

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.dependencies
        data.default_apt = ["postgres"]
        data.default = ["numpy"]
        data.dev.pop(-1)

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        super().update_to_template(tpl)
        data = self.auxcon.dependencies
        # add inexisting deps
        for mod in tpl.dependencies:
            if mod not in data:
                data[mod] = tpl.dependencies[mod]
                self._print(f"dependencies.{mod}: added {data[mod]}", fg="green")

        for mod in tpl.dependencies:
            if mod not in ["test", "doc", "dev"]:
                continue
            newer = {}
            for dep in tpl.dependencies[mod]:
                pkg, version = self.parse_dep(dep)
                assert version
                newer[pkg] = version

            dep_list = data.get(mod, [])
            for i, dep in enumerate(dep_list):
                pkg, version = self.parse_dep(dep)
                if version is not None:
                    if pkg in newer and newer[pkg] != version:
                        self._print(
                            f"dependencies.{mod}: updated {pkg} {version}->{newer[pkg]}",
                            fg="green",
                        )
                        dep_list[i] = dep.replace(version, newer[pkg])

    @classmethod
    def parse_dep(cls, dep: str) -> tp.Tuple[str, tp.Optional[str]]:
        if "=" in dep:
            pkg, version = re.split("[=><~]{2}", dep, 1)
        else:
            pkg = dep
            version = None
        return pkg, version

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.dependencies
            for key in self.__keys():  # config loading artefact
                if data[key] == "":
                    data[key] = []
            yield

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config

        for key, deps in self.auxcon.dependencies.items():
            if key.endswith("_apt") or key.endswith("_script"):
                continue
            if key == "default":
                # my config writer will mess up dependencies with environment markers
                # if ' are present, but I need ' in auxilium.cfg for the docker files
                # as some are "${VAR}" and '${VAR}' does not work
                config.options.install_requires = [x.replace("'", '"') for x in deps]
            else:
                if key not in ["docs"] and self.is_enabled(key):
                    config["options.extras_require"][key] = deps


class PytestMixin(DependencyMixin):
    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.dependencies
        data.test.append(self.versions.pytest)

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.setdefault("pytest", _ProtoNamespace())
        data = self.auxcon.pytest
        data.asyncio_mode = "strict"

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            self.auxcon.setdefault("pytest", _ProtoNamespace())
            yield


class CoverageMixin(PytestMixin):
    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.test.append(self.versions.pytest_cov)


class PrecommitMixin(DependencyMixin, ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pre_commit", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pre_commit.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pre_commit=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("hooks", "rev_overwrite")

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.dependencies
        data.dev.append(self.versions.pre_commit)
        data.dev_apt.append("git-core")

        data = self.auxcon.pre_commit
        data.hooks = [
            "check-yaml;exclude=devops/CI",
            "check-toml",
            "check-json",
            "end-of-file-fixer",
            "add-copy-right",
            "trailing-whitespace",
            "black;exclude=devops/CI",
            "blacken-docs",
            "pyupgrade",
            "pycln",
            "reorder-python-imports",
        ]
        if self.is_enabled("mypy"):
            data.hooks.append("mypy")

        if self.is_enabled("pylint"):
            data.hooks.append("pylint")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pre_commit
        data.hooks = list(data.hooks[0:12:5])
        data.hooks += ["pylint-test;files=tests/"]
        data.rev_overwrite = ["black==21.9b0"]

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.pre_commit
            hooks_og = data.hooks
            data.hooks = self.list2ns(hooks_og)
            rev_overwrite_og = data.rev_overwrite
            data.rev_overwrite = {x.split("==", 1)[0]: x for x in rev_overwrite_og}

            # add custom extensions
            custom_config = self.target_custom / "pre-commit" / "config.yaml"
            data.custom = ""
            if custom_config.exists():
                with open(custom_config, encoding="utf-8") as f:
                    data.custom = f.read()

            yield
            data.hooks = hooks_og
            data.rev_overwrite = rev_overwrite_og

    def bake(self) -> None:  # pylint: disable=too-many-branches
        super().bake()

        data = self.auxcon.pre_commit
        # overwrite revs
        self.auxcon.versions.update(data.rev_overwrite)

        srcj = self.root / "pre-commit/config.yaml.jinja2"
        with Jinja2Parser.render_to_tmp(srcj, aux=self.auxcon) as src:
            config = YamlParser.read(src)

        requested_hooks = list(data.hooks.keys())

        self._raise_if_unsupported_hooks(config, requested_hooks)

        multi_hook_repo = ""
        # remove the ones not selected
        for repo in reversed(config.repos):

            def keep_selected(hook: _ProtoNamespace) -> bool:
                return hook.id in requested_hooks

            if len(repo.hooks) > 1:
                multi_hook_repo = repo.repo
            repo.hooks = list(filter(keep_selected, repo.hooks))
            if not repo.hooks:  # remove repo if empty
                config.repos.remove(repo)

            # integrate options
            for hook in repo.hooks:
                for key, val in data.hooks[hook.id].items():
                    if key in ["coverage"]:
                        continue
                    if key not in ["files", "exclude"]:
                        raise NotImplementedError(
                            f"support for option '{key}' of {hook.id} not implemented yet"
                        )
                    if key in hook:
                        hook[key] += "|" + val
                    else:
                        hook[key] = val

        # check if local python files are required from the hook
        for repo in config.repos:
            for hook in repo.hooks:
                entry = hook.get("entry")
                if entry and entry.startswith("devops/") and "custom" not in entry:
                    self.bake_file(entry.replace("devops/", ""), chmod=0o755)

        # order the config according to the requested_hooks
        if multi_hook_repo != "":
            self._print(
                f"pre-commit: cannot sort repos: '{multi_hook_repo}' has multiple hooks",
                fg="red",
            )
        config.repos = sorted(
            config.repos, key=lambda x: requested_hooks.index(x.hooks[0].id)
        )

        dest = self.target / "pre-commit/config.yaml"
        written = YamlParser.write(config, dest)
        if written:
            self._print(f"baked {dest}", fg="green")

    @classmethod
    def _raise_if_unsupported_hooks(
        cls, config: _ProtoNamespace, requested_hooks: tp.Iterable[str]
    ) -> None:
        available_hooks: tp.List[str] = sum(
            ([hook.id for hook in repo.hooks] for repo in config.repos), []
        )
        unknown_hooks = set(requested_hooks) - set(available_hooks)
        if unknown_hooks:
            raise RuntimeError(
                f"pre-commit hooks are not supported by aux: {unknown_hooks}.\n"
                "       Hint: You could add them in the custom directory."
            )


class PylintMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pylint", _ProtoNamespace())
        self.auxcon.setdefault("pylint_test", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pylint.setdefault(key, [])
            self.auxcon.pylint_test.setdefault(key, [])

        if not self.is_enabled("docs"):
            self.auxcon.pylint.setdefault(
                "disable",
                [
                    "missing-class-docstring",
                    "missing-module-docstring",
                    "missing-function-docstring",
                ],
            )

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pylint=self.__keys(), pylint_test=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("disable", "good_names")

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.dev.append(self.versions.pylint)

        if not self.is_enabled("docs"):
            self.auxcon.pylint.disable = [
                "missing-class-docstring",
                "missing-module-docstring",
                "missing-function-docstring",
            ]

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pylint
        data.disable += ["too-few-public-methods", "no-self-use"]
        data.good_names += ["t", "dt"]

    def bake(self) -> None:
        super().bake()
        # ensure python version
        found_version = ".".join(map(str, sys.version_info[:2]))
        if found_version != self.auxcon.project.minimal_version:
            raise RuntimeError(
                f"you are using python {found_version}, please use python {self.auxcon.project.minimal_version} (minimal version)."
            )

        x = subprocess.run(
            ["pylint", "--generate-rcfile"], capture_output=True, check=True
        )
        text = x.stdout.decode()

        hooks = self.auxcon.pre_commit.hooks
        configs = [ConfigParser.read_string(text)]
        keys = ["pylint"]
        writeout = ["pylint" in hooks]

        writeout.append("pylint-test" in hooks)
        if writeout[-1]:
            keys.append("pylint-test")

        for i, key in enumerate(keys):
            config = configs[-1]
            if i > 0:
                config = copy.copy(config)
                configs.append(config)

            key = key.replace("-", "_")
            for key1, key2, key3 in [
                ("MESSAGES CONTROL", "disable", "disable"),
                ("BASIC", "good-names", "good_names"),
                ("SIMILARITIES", "min-similarity-lines", "min_similarity_lines"),
            ]:
                proplist = copy.copy(config[key1][key2])
                data = self.auxcon[key]
                if key2 in ["good-names", "disable"]:
                    for x in data[key3]:
                        proplist[-1] += ","
                        if x in proplist:
                            raise RuntimeError(f"{x} is already marked {key3}")
                        proplist.append(x)
                    config[key1][key2] = proplist
                else:
                    if key3 in data:
                        config[key1][key2] = data[key3]

        config["SIMILARITIES"]["ignore-imports"] = "yes"

        for key, config, wout in zip(keys, configs, writeout):
            if not wout:
                continue
            dest = self.target / f"pre-commit/{key}rc"
            written = ConfigParser.write(config, dest)
            if written:
                self._print(f"baked {dest}", fg="green")


class MypyMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("mypy", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.mypy.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(mypy=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("ignore",)

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.dev.append(self.versions.mypy)

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.mypy.ignore += ["click_help_colors"]

    def bake(self) -> None:
        super().bake()
        src = self.root / "pre-commit/mypy.ini"
        dest = self.target / "pre-commit/mypy.ini"
        config = ConfigParser.read(src)

        # namespace compat
        if "." in self.auxcon.project.name:
            config["mypy"]["namespace_packages"] = True
            config["mypy"]["explicit_package_bases"] = True
            config["mypy"][
                "mypy_path"
            ] = f"$MYPY_CONFIG_FILE_DIR/../../{self.auxcon.project.source_dir}"

        for x in self.auxcon.mypy.ignore:
            config[f"mypy-{x}.*"] = _ProtoNamespace(ignore_missing_imports="True")

        # special django stubs case
        for dep in self.auxcon.dependencies["dev"]:
            if (
                "django-stubs" in dep
                and (Path(self.auxcon.project.source_dir) / "settings.py").exists()
            ):
                config["mypy"]["plugins"] = ["mypy_django_plugin.main"]
                config["mypy.plugins.django-stubs"] = dict(
                    django_settings_module=f"{self.auxcon.project.name}.settings"
                )

        written = ConfigParser.write(config, dest)
        if written:
            self._print(f"baked {dest}", fg="green")


class ExecutablesMixin(DependencyMixin, ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("executables", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.executables.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(executables=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("console_scripts", "scripts")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.executables.scripts += ["scripts/say_hello"]

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.executables
            scripts_og = data.scripts
            data.scripts = copy.copy(scripts_og)
            yield
            data.scripts = scripts_og

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config
        data = self.auxcon.executables

        default_scripts = [
            ("mypy", "mp"),
            ("pylint", "pl"),
            ("coverage", "cov"),
            ("docker", "dcp"),
            ("ci", "ci"),
            ("pre-commit", "pra2"),
            ("project", "pipi"),
            ("package", "sdist"),
            ("docs", "docs"),
        ]

        for key, val in default_scripts:
            if self.is_enabled(key):
                self.bake_file(f"scripts/{val}")
                data.scripts += [f"devops/scripts/{val}"]

        config.options.scripts = data.scripts
        cscr = data.console_scripts
        for i, val in enumerate(cscr):
            if "=" in val:
                continue
            name = val.rsplit(":", 1)[1]
            cscr[i] = f"{name} = {val}"

        config["options.entry_points"].console_scripts = cscr


class PackageMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("package", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.package.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(package=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("include", "exclude")

    def bake(self) -> None:
        super().bake()
        config = self.auxcon.project.config
        data = self.auxcon.package
        name = self.auxcon.project.name

        for dkey, ckey in [
            ("include", "options.package_data"),
            ("exclude", "options.exclude_package_data"),
        ]:
            if not data[dkey]:
                continue
            config.setdefault(ckey, _ProtoNamespace())
            config[ckey][name] = data[dkey]

        config = copy.copy(config)

        def not_devops(x: str) -> bool:
            return "devops" not in x

        config.options = copy.copy(config.options)
        config.options.scripts = list(filter(not_devops, config.options.scripts))
        if not config.options.scripts:
            del config.options.scripts

        extra = copy.copy(config["options.extras_require"])
        del extra["dev"]
        config["options.extras_require"] = extra
        data.config = config

    def writeout(self) -> None:
        super().writeout()
        dest = self.target / "package/setup-dist.cfg"
        written = ConfigParser.write(self.auxcon.package.pop("config"), dest)
        if written:
            self._print(f"baked {dest}", fg="green")


class DockerMixin(DependencyMixin, ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("docker", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.docker.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(docker=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("services",)

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.docker
        vslug = self.python_version_slug
        data.services = [f"python-deps-{vslug}"]
        if self.is_enabled("pre-commit"):
            data.services.append(f"pre-commit-{vslug}")
            data.services.append(f"pre-commit-all-{vslug}")
        if self.is_enabled("pytest"):
            data.services.append(f"pytest-{vslug}")
        if self.is_enabled("coverage"):
            data.services.append(f"pycov-{vslug};coverage=95")
        if self.is_enabled("docs"):
            data.services.append(f"docs-{vslug};extra_req=docs")
        if self.is_enabled("gitlab"):
            data.services += [
                "gitlab-release",
                "pkg-gitlab",
            ]

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.docker
        data.platform = "amd64"

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        super().update_to_template(tpl)

        def job_name(job: str) -> str:
            return job.split(";", 1)[0].strip()

        data = self.auxcon.docker
        old = list(map(job_name, data.services))
        for job in tpl.docker.services:
            name = job_name(job)
            if name not in old:
                data.services.append(job)
                self._print(f"docker.services: added {name}", fg="green")

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.docker
            services_og = data.services
            data.services = self.list2ns(services_og)
            for key, opts in data.services.items():
                if "extra_req" in opts:
                    opts["extra_req"] = opts["extra_req"].split(",")
                res = []
                if "assets" in opts:
                    opts["assets"] = opts["assets"].split(",")
                    for x in opts["assets"]:
                        shortname = x.rsplit("/", 1)[1]
                        url = (
                            "$CI_API_V4_URL/projects/$CI_PROJECT_ID/packages/generic/"
                            + x
                        )
                        res.append(
                            r"{\"name\":\""
                            + shortname
                            + r"\",\"url\":\""
                            + url
                            + r"\"}"
                        )
                opts["assets"] = res
                opts.setdefault("pip_req", [])
                opts.setdefault("script", [])
                opts.setdefault("base", None)

                opts.setdefault("apt_req", [])
                if "-" in key:
                    opts.pure_name, opts.version_slug = key.rsplit("-", 1)
                else:
                    opts.pure_name = key
                    opts.version_slug = "  "

                if opts.version_slug[0] in "3" and opts.version_slug[1:] in [
                    "8",
                    "9",
                    "10",
                    "11",
                    "12",
                    "13",
                ]:
                    opts.version = f"{opts.version_slug[0]}.{opts.version_slug[1:]}"
                else:
                    opts.pure_name = key
                    del opts.version_slug

                opts.full_name = f"{self.auxcon.project.slug}-{key}"
                # we dont duplicate the slug
                if opts.pure_name == self.auxcon.project.slug:
                    opts.full_name = key

                if "mode" in opts:
                    supported = ["django", "django+nginx"]
                    if opts.mode not in supported:
                        raise RuntimeError(
                            f"mode {opts.mode} is not supported {supported}"
                        )

            data.setdefault("platform", None)
            data.project_dir = "../../"
            data.source_dir = f"../../{self.auxcon.project.source_dir}"
            yield
            del data.project_dir
            del data.source_dir
            data.services = services_og

    def bake(self) -> None:
        super().bake()
        data = self.auxcon.docker

        extra_req_default = {
            "python-deps": ["default"],
            "pytest": ["test"],
            "pre-commit": ["test", "dev"],
            "pytest-standalone": ["default", "test"],
            "docs": ["docs"],
            "ansible-deploy": ["deploy"],
        }
        deps = self.auxcon.dependencies
        for opts in data.services.values():
            fallback = extra_req_default.get(opts.pure_name, [])
            needed = opts.get("extra_req", fallback)
            opts.pip_req = self._unique_sum(
                opts.pip_req, *[deps.get(x, []) for x in needed]
            )
            opts.apt_req = self._unique_sum(
                opts.apt_req, *[deps.get(x + "_apt", []) for x in needed]
            )
            opts.script = self._sum(
                opts.script, *[deps.get(x + "_script", []) for x in needed]
            )
            assert all('"' not in x for x in opts.pip_req)

            if self.is_enabled("pip"):
                self.branch_match_and_cred_passing(opts)

        config = _ProtoNamespace([("version", "3.6"), ("services", {})])

        must_be_custom = []
        for opts in data.services.values():
            src_dir = self.root / f"docker/services/{opts.pure_name}"
            # Dockerfile
            src = src_dir / "Dockerfile.jinja2"
            if src.exists():
                self.bake_file(
                    f"docker/services/{opts.pure_name}/Dockerfile",
                    f"docker/{opts.full_name}.dockerfile",
                    opts=opts,
                )

            elif (src_dir / "Dockerfile").exists():
                raise NotImplementedError("plain Dockerfiles")
            # docker-compose.yml
            srcj = src_dir / "docker-compose.yml.jinja2"
            if srcj.exists():
                with Jinja2Parser.render_to_tmp(
                    srcj, aux=self.auxcon, opts=opts
                ) as src:
                    part = YamlParser.read(src).services

                config["services"].update(part)
            else:
                must_be_custom.append(opts.full_name)

        # modifies config!
        self._add_custom_services(must_be_custom, config)

        dest = self.target / "docker/compose.yml"
        written = YamlParser.write(config, dest)
        if written:
            self._print(f"baked {dest}", fg="green")

    def _add_custom_services(
        self, must_be_custom: tp.List[str], config: _ProtoNamespace
    ) -> None:
        data = self.auxcon.docker
        custom_config = self.target_custom / "docker" / "compose.yml"
        if not custom_config.exists():
            return
        custom_config = YamlParser.read(custom_config)
        if list(custom_config.keys()) != ["services"]:
            raise RuntimeError(
                "only services can be defined in custom docker-compose.yml."
            )
        custom_services = custom_config.services
        set1 = set(must_be_custom)
        set2 = set(custom_services.keys())
        if set1 != set2:
            raise RuntimeError(
                f"the service declaration {set2} in custom is not equal to the needed services by aux: {set1}"
            )
        config["services"].update(custom_config.services)
        for service_name in custom_services:
            prefix = f"{self.auxcon.project.slug}-"
            if not service_name.startswith(prefix):
                raise RuntimeError(
                    f"custom service '{service_name}' must start with '{prefix}'"
                )
            candidates = [
                x for x in data.services.values() if x.full_name == service_name
            ]
            assert len(candidates) == 1
            opts = candidates[0]
            name = f"docker/{service_name}.dockerfile"
            self.bake_file(name, custom=True, ignore_absent=True, opts=opts)

    @staticmethod
    def _unique_sum(*args: tp.List[str]) -> tp.List[str]:
        res = []
        for part in args:
            for x in part:
                if x not in res:
                    res.append(x)
        return res

    @staticmethod
    def _sum(*args: tp.List[str]) -> tp.List[str]:
        res = []
        for part in args:
            for x in part:
                res.append(x)
        return res


class CiMixin(DockerMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("ci", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.ci.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(ci=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("jobs",)

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        data = self.auxcon.ci
        vslug = self.python_version_slug
        data.jobs = [f"python-deps-{vslug}      ;default=true"]
        if self.is_enabled("pre-commit"):
            data.jobs += [
                f"pre-commit-{vslug}       ;default=true",
                f"pre-commit-all-{vslug}   ;default=true",
            ]
        if self.is_enabled("pytest"):
            data.jobs += [f"pytest-{vslug}           ;default=true"]
        if self.is_enabled("coverage"):
            data.jobs += [f"pycov-{vslug}            ;default=true"]
        if self.is_enabled("docs"):
            data.jobs += [f"docs-{vslug}                 ;default=true"]
        if self.is_enabled("gitlab"):
            data.jobs += [
                "check-release-notes",
                "gitlab-release",
                "pkg-gitlab",
            ]

    def update_to_template(self, tpl: _ProtoNamespace) -> None:
        super().update_to_template(tpl)

        def job_name(job: str) -> str:
            return job.split(";", 1)[0].strip()

        data = self.auxcon.ci
        old = list(map(job_name, data.jobs))
        for job in tpl.ci.jobs:
            name = job_name(job)
            if name not in old:
                data.jobs.append(job)
                self._print(f"ci.jobs: added {name}", fg="green")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        self.auxcon.ci.runner = "dind-cached"
        self.auxcon.ci.mechanism = "mixed"
        self.auxcon.ci.jobs[3] += ";run=true;service=postgres"

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.ci
            jobs_og = data.jobs
            data.jobs = self.list2ns(jobs_og)

            valid_opts_keys = [
                "default",
                "build",
                "build-deps",
                "build-stage",
                "build-rules",
                "images",
                "run",
                "run-deps",
                "run-stage",
                "run-rules",
                "services",
                "overwrite",
                "rules",
                "files",
                "function",
                "target",  # for release-tag
                "always-build",  # for image
            ]

            for job, val in data.jobs.items():
                self._set_default(job, val)

                val.setdefault("function", "docker")
                self._handle_special(job, val)

                for key in ["build", "run"]:
                    val.setdefault(key, True)
                    if isinstance(val[key], str):
                        val[key] = val[key] in ["true", "True"]

                for key in ["build-stage", "run-stage"]:
                    val.setdefault(key, None)

                for key in [
                    "build-deps",
                    "run-deps",
                    "rules",
                    "build-rules",
                    "run-rules",
                    "services",
                    "images",
                    "overwrite",
                    "files",
                ]:
                    val.setdefault(key, [])
                    if isinstance(val[key], str):
                        val[key] = val[key].split(",")

                # infuse shorthands
                shorthand = dict(push=["push-no-mr", "mr"])
                default_rules: tp.Dict[str, tp.List[str]] = {
                    "rules": shorthand["push"] + ["web", "pipeline"],
                }
                for key in ["rules", "build-rules", "run-rules"]:
                    res = []
                    for rule in val[key]:
                        if rule in shorthand:
                            val[key].remove(rule)
                            res += shorthand[rule]
                        else:
                            res += [rule]
                    if not val["rules"]:
                        res = res or default_rules[key]
                    val[key] = res

                diff = set(val.keys()) - set(valid_opts_keys)
                if diff:
                    raise RuntimeError(f"invalid options: {diff}")

            data.setdefault("mechanism", "monolith")
            data.setdefault("runner", "normal")
            data.setdefault("docker_image", self.versions.ci_docker_image)
            assert data.mechanism in ["monolith", "gitlab", "mixed"]
            assert data.runner in ["dind-cached", "normal"]
            yield
            data.jobs = jobs_og

    @classmethod
    def _set_default(cls, job: str, opts: _ProtoNamespace) -> None:
        if opts.get("default", "false") != "true":
            return

        default_trigger = ["web", "pipeline"]
        version = job.rsplit("-", 1)[1]
        if "pre-commit-all" in job:
            opts.setdefault("build", False)
            opts.setdefault("run-deps", f"pre-commit-{version}")
            opts.setdefault("rules", ["mr"] + default_trigger)
        elif "pre-commit" in job:
            opts.setdefault("files", ["devops/pre-commit/config.yaml"])
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("run-rules", ["push-no-mr"] + default_trigger)
            opts.setdefault("build-rules", ["push-no-mr", "mr"] + default_trigger)
        elif "python-deps" in job:
            opts.setdefault("build-stage", "pre-build")
            opts.setdefault("run", False)
            opts.setdefault("rules", ["push"] + default_trigger)
        elif "pytest-standalone" in job:
            opts.setdefault("rules", ["vip-mr"] + default_trigger)
        elif "image-pytest" in job:
            opts.setdefault("always-build", True)
            opts.setdefault("build-deps", [f"pytest-{version}"])
            opts.setdefault("build-stage", "build")
            opts.setdefault("rules", ["release-mr"] + default_trigger)
        elif "ansible-deploy" in job:
            opts.setdefault("build-stage", "pre-build")
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", ["release-push"] + default_trigger)
        elif "pytest" in job:
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("run-rules", ["push"] + default_trigger)
        elif "pycov" in job:
            opts.setdefault("build", False)
            opts.setdefault("run-deps", [f"pytest-{version}"])
            opts.setdefault("run-rules", ["mr", "vip-push"] + default_trigger)
        elif "image" in job:
            opts.setdefault("always-build", True)
            opts.setdefault("build-deps", [f"python-deps-{version}"])
            opts.setdefault("build-stage", "build")
            opts.setdefault("run", False)
            opts.setdefault("rules", ["release-push"] + default_trigger)

    @classmethod
    def _handle_special(cls, job: str, opts: _ProtoNamespace) -> None:
        if job == "check-release-notes":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-mr")
            opts.function = "spez"
        elif job == "gitlab-release":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
            opts.function = "spez"
        elif job == "pkg-gitlab":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
        elif job == "pkg-pypi":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
        elif job == "release-tag":
            opts.setdefault("build", False)
            opts.setdefault("run-stage", "release")
            opts.setdefault("rules", "release-push")
            if "target" not in opts:
                raise RuntimeError("release-tag must specify the option 'target'")
            opts.function = "spez"

    def bake(self) -> None:  # pylint: disable=too-many-branches,too-many-locals
        super().bake()
        dest_dir = self.target / "CI"
        data = self.auxcon.ci
        base_files = ["00-main.yml", "01-rules.yml"]
        job_files = []
        if data.mechanism in ["monolith", "mixed"]:
            job_files += ["python_ci.py"]
            self.bake_file("../_aux_ci.py", "CI/_aux_ci.py")

        if data.mechanism in ["mixed", "gitlab"]:
            base_files += ["02-template.yml"]
            job_files += ["03-build.yml", "04-run.yml"]

        for filename in base_files:
            self.bake_file(f"CI/{filename}")

        valid_rules = []

        config = YamlParser.read(dest_dir / "01-rules.yml")
        valid_rules += list(x.replace(".r-", "") for x in config)
        ci_rules = self._generate_python_rules(valid_rules, config)

        # validate jobs
        valid_build_deps: tp.List[str] = []
        valid_run_deps: tp.List[str] = []

        def invalid_option_error(key: str, k: str, valid: tp.Sequence[str]) -> None:
            if k not in valid:
                raise RuntimeError(f"{k} is not in valid {key} ({valid})")

        for job, opts in list(data.jobs.items()):
            for key, valid in [
                ("build-deps", valid_build_deps),
                ("run-deps", valid_run_deps),
                ("build-rules", valid_rules),
                ("run-rules", valid_rules),
                ("rules", valid_rules),
            ]:
                if key in opts:
                    for k in opts[key]:
                        invalid_option_error(key, k, valid)

            for key, valid in [
                ("target", valid_build_deps),
            ]:
                if key in opts:
                    invalid_option_error(key, opts[key], valid)

            if opts.build:
                docker_job = self.auxcon.docker.services[job]
                opts.branch_match = docker_job.get("branch_match", [])
                if docker_job.base and docker_job.base not in opts.images:
                    opts.images.append(docker_job.base)
                valid_build_deps.append(job)
            if opts.run:
                base = [job] if opts.build else []
                opts["run-deps"] = base + opts["run-deps"]
                # release-tag special addition
                target = opts.get("target")
                if target:
                    opts["run-deps"].append(target)

                opts["services"] = [job] + opts["services"]
                for service_name in opts["services"]:
                    service = data.jobs.get(service_name)
                    if not service:
                        continue
                    if (
                        service.function == "docker" or service_name == "gitlab-release"
                    ) and service_name not in self.auxcon.docker.services:
                        raise RuntimeError(
                            f"{service_name} is listed in CI but not in docker.services, please fix!"
                        )
                valid_run_deps.append(job)

        for filename in job_files:
            self.bake_file(f"CI/{filename}", ci_rules=ci_rules)

        if "python_ci.py" in job_files:
            self.chmod(dest_dir / "python_ci.py", 0o755)

    def _generate_python_rules(
        self, valid_rules: tp.List[str], config: _ProtoNamespace
    ) -> tp.List[tp.Tuple[str, str]]:
        initial = [(rule, config[".r-" + rule]["if"]) for rule in valid_rules]
        res = []
        for name, form in initial:
            python_form = self._rule_to_python(form)
            res.append((name, python_form))
        return res

    @classmethod
    def _rule_to_python(cls, form: str) -> str:
        x = re.sub(r"\$([A-Z0-9_]+)", r'env("\1")', form)
        x = re.sub(r"\|\|", "or", x)
        x = re.sub(r"\&\&", "and", x)
        x = re.sub("null", '""', x)
        return x


class DocsMixin(ProjectMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("docs", _ProtoNamespace())

    def clear_to_template(self, **kwgs: str) -> None:
        super().clear_to_template(**kwgs)
        self.auxcon.dependencies.docs = [
            self.versions.sphinx,
            self.versions.sphinx_rtd_theme,
            self.versions.sphinx_click,
            self.versions.jupyter_sphinx,
            self.versions.bash_kernel,
        ]

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(docs=self.__keys(), **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return tuple()

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.docs
            data.setdefault(
                "root", f"{self.auxcon.project.source_dir}/docs"
            )  # pylint: disable=pointless-statement
            for key in ["strict"]:
                if key in data:
                    data[key] == data[key] in ["true", "True"]

            gitlab = self.auxcon.gitlab
            if "url" not in data:
                pages_url = gitlab.remote_url.replace("gitlab", "pages")
                data.setdefault(
                    "url",
                    f"https://{gitlab.remote_user}.{pages_url}/{self.auxcon.project.second_name}",
                )

            self.auxcon.project.project_urls.Documentation = data.url
            yield

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.docs
        data.root = "source/docs"

    def bake(self) -> None:
        super().bake()
        data = self.auxcon.docs

        # user docs dir
        dest_rel = f"../{data.root}"
        self.bake_file(
            "docs/user/conf.py", f"{dest_rel}/conf.py", only_if_inexistent=True
        )
        self.bake_file(
            "docs/user/index.rst", f"{dest_rel}/index.rst", only_if_inexistent=True
        )
        self.bake_file("docs/user/gitignore", f"{dest_rel}/.gitignore")

        for name in ["static"]:
            path = self.target / f"{dest_rel}/{name}"
            path.mkdir(parents=True, exist_ok=True)

        # devops docs dir
        dest_rel = "docs"
        for name in ["static", "templates"]:
            path = self.target / f"{dest_rel}/{name}"
            path.mkdir(parents=True, exist_ok=True)

        self.bake_file("docs/default_conf.py")
        self.bake_file("docs/postprocess_html.py")
        self.bake_file("docs/static/git-link-color.css")


class PipMixin(DependencyMixin):
    def set_defaults(self) -> None:
        super().set_defaults()
        self.auxcon.setdefault("pip", _ProtoNamespace())
        for key in self.__keys():
            self.auxcon.pip.setdefault(key, [])

    def cleanup(self, **kwgs: tp.Any) -> None:
        super().cleanup(pip=self.__keys()[1:], **kwgs)

    @classmethod
    def __keys(cls) -> tp.Tuple[str, ...]:
        return ("extra_index_url", "branch_match")

    def clear_to_demo(self, **kwgs: str) -> None:
        super().clear_to_demo(**kwgs)
        data = self.auxcon.pip
        data.extra_index_url = [
            "demo=https://gitlab-ci-token:$CI_JOB_TOKEN@gitlab.x.y/api/v4/projects/118/packages/pypi/simple"
        ]
        data.branch_match = ["demo=https://gitlab.x.y/user/demo.git"]

    @contextlib.contextmanager
    def extra(self) -> tp.Iterator[None]:
        with super().extra():
            data = self.auxcon.pip

            for key in self.__keys():
                if data[key] == "":
                    data[key] = []

            extra_index_url_og = data.extra_index_url
            branch_match_og = data.branch_match
            data.extra_index_url = collections.OrderedDict(
                tuple(val.split("=", 1)) for val in extra_index_url_og  # type: ignore
            )
            data.branch_match = collections.OrderedDict(
                tuple(val.split("=", 1)) for val in branch_match_og  # type: ignore
            )

            wo_creds = collections.OrderedDict()
            creds = collections.OrderedDict()

            for key, url in data.extra_index_url.items():
                if "@" in url:
                    pre, url = url.split("@", 1)
                    proto, cred = pre.split("//", 1)
                    url = f"{proto}//{url}"
                    token, var_cred = cred.split(":", 1)
                    assert "$" == var_cred[0]
                    creds[key] = var_cred[1:]
                    assert "$" not in token

                wo_creds[key] = url

            data.extra_index_url_wo_creds = wo_creds
            data.creds = creds
            yield
            del data.extra_index_url_wo_creds
            data.branch_match = branch_match_og
            data.extra_index_url = extra_index_url_og

    def bake(self) -> None:
        super().bake()

        # we rely on .netrc for the credentials
        name = "pip/pip.conf"
        self.bake_file(name)

        # venv = os.environ.get("VIRTUAL_ENV")
        # if venv is None:
        # return
        # venv_path = Path(venv)
        # self.copy_file(self.target / name, venv_path / "pip.conf")

    def branch_match_and_cred_passing(self, opts: _ProtoNamespace) -> None:
        opts.pip_extra_url = self._collect_extra_url(opts.pip_req)
        opts.pip_cred_vars = self._collect_cred_vars(opts.pip_req)
        for i, dep in enumerate(opts.pip_req):
            pkg, _ = self.parse_dep(dep)
            match = self.auxcon.pip.branch_match.get(pkg)
            if match is None:
                continue
            # skip matching these branches
            skip = [self.auxcon.gitlab.release_branch]
            var = f'{pkg.upper().replace(".", "_")}_MATCHING_REPO'
            opts.pip_req[i] = f"${{{var}:-{dep}}}"
            opts.pip_cred_vars.append(var)
            opts.setdefault("branch_match", [])
            opts.branch_match.append((pkg, var, match, skip))  # variable used by CI

    def _collect_extra_url(self, deps: tp.List[str]) -> tp.List[str]:
        extra_url = set()

        for dep in deps:
            pkg, _ = self.parse_dep(dep)
            url = self.auxcon.pip.extra_index_url.get(pkg)
            if url is not None:
                extra_url.add(url)

        return list(sorted(extra_url))

    def _collect_cred_vars(self, deps: tp.List[str]) -> tp.List[str]:
        cred_vars = set()

        for dep in deps:
            pkg, _ = self.parse_dep(dep)
            cred = self.auxcon.pip.creds.get(pkg)
            if cred is not None:
                cred_vars.add(cred)

        return list(sorted(cred_vars))


class SentinelMixin(Renderer):
    def bake(self) -> None:
        with self.extra():
            super().bake()
        self.writeout()
