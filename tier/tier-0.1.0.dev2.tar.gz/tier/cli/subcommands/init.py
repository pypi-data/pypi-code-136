# std

# internal
from tier.internal.logging import log
from tier.internal.configs.pyproject import PyProject
from tier.internal.tier import Tier


def init(
        recursive: bool,
        commit: bool,
        tag: bool,
):
    log.debug('tier init')

    if tag:
        commit = True

    log.debug(f'{recursive = }')
    log.debug(f'{commit = }')
    log.debug(f'{tag = }')

    if recursive:
        tier = Tier()
        tier.initialize(commit=commit, tag=tag)
    else:
        project = PyProject.from_dirpath(auto_write=True)
        Tier.initialize_project(project=project, commit=commit, tag=tag)
