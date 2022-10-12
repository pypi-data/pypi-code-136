"""
llvm_snapshot_builder.actions provides classes to interact with Copr.
"""

from .build_all_packages import CoprActionBuildAllPackages
from .build_packages import CoprActionBuildPackages
from .cancel_builds import CoprActionCancelBuilds
from .delete_builds import CoprActionDeleteBuilds
from .delete_project import CoprActionDeleteProject
from .fork_project import CoprActionForkProject
from .make_or_edit_packages import CoprActionMakeOrEditPackages
from .make_or_edit_project import CoprActionMakeOrEditProject
from .project_exists import CoprActionProjectExists
from .action import CoprAction
from .regenerate_repos import CoprActionRegenerateRepos
