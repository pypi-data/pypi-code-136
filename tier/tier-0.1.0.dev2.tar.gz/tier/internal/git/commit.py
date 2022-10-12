# std
from __future__ import annotations
from functools import cached_property
from typing import Optional as Opt, TYPE_CHECKING

# internal
if TYPE_CHECKING:
    from tier.internal.git.git import Git


class Commit:

    def __init__(self, commit_id: str, git: Opt[Git] = None):
        from tier.internal.git.git import Git
        self.hash: str = commit_id
        self.git: Git = git or Git()

    def __repr__(self) -> str:
        return f'Commit<{self.hash}>'

    @cached_property
    def message(self) -> str:
        return self.git.capture('log', '--format=%B', '-n', '1', self.hash)

    def title_line(self) -> str:
        return self.message.splitlines()[0]
