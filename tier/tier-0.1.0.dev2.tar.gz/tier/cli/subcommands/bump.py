# std

# internal
from tier.internal.logging import log
from tier.internal.configs.pyproject import PyProject
from tier.internal.tier import Tier


def bump(
        recursive: bool,
        commit: bool,
        tag: bool,
        major: bool,
        minor: bool,
        patch: bool,
        post: bool,
        rc: bool,
        beta: bool,
        alpha: bool,
        dev: bool,
):
    log.debug('tier bump')

    if recursive:
        tier = Tier()
        tier.bump(
            commit=commit,
            tag=tag,
            major=major,
            minor=minor,
            patch=patch,
            post=post,
            rc=rc,
            beta=beta,
            alpha=alpha,
            dev=dev,
        )
    else:
        project = PyProject.from_dirpath(auto_write=True)
        Tier.bump_project_from_options(
            project=project,
            commit=commit,
            tag=tag,
            major=major,
            minor=minor,
            patch=patch,
            post=post,
            rc=rc,
            beta=beta,
            alpha=alpha,
            dev=dev,
        )
