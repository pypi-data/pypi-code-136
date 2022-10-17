# Copyright (c) 2021-2022 Mario S. Könz; License: MIT
from ._components import CiMixin
from ._components import CoverageMixin
from ._components import DependencyMixin
from ._components import DockerMixin
from ._components import DocsMixin
from ._components import ExecutablesMixin
from ._components import GitIgnoreMixin
from ._components import GitlabMixin
from ._components import MypyMixin
from ._components import PackageMixin
from ._components import PipMixin
from ._components import PrecommitMixin
from ._components import ProjectMixin
from ._components import PylintMixin
from ._components import PytestMixin
from ._components import SentinelMixin
from ._extra_and_renderer import MetaMixin

__all__ = ["AllRenderer"]


class AllRenderer(  # pylint: disable=too-many-ancestors
    SentinelMixin,
    PipMixin,
    DocsMixin,
    CiMixin,
    DockerMixin,
    PackageMixin,
    ExecutablesMixin,
    PylintMixin,
    MypyMixin,
    PrecommitMixin,
    CoverageMixin,
    PytestMixin,
    DependencyMixin,
    GitlabMixin,
    GitIgnoreMixin,
    ProjectMixin,
    MetaMixin,
):
    pass
