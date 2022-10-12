# internal
from tier.internal.logging import log
from tier.internal.configs.pyproject import PyProject
from tier.internal.tier import Tier


def update(
        recursive: bool,
        commit: bool,
        tag: bool,
):
    log.debug('tier update')

    if tag:
        commit = True

    log.debug(f'{recursive = }')
    log.debug(f'{commit = }')
    log.debug(f'{tag = }')

    if recursive:
        tier = Tier()
        tier.update(commit=commit, tag=tag)
    else:
        project = PyProject.from_dirpath(auto_write=True)
        Tier.update_project(project=project, commit=commit, tag=tag)
