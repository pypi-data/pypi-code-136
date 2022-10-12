# std
import os
import subprocess
from typing import List, Optional as Opt

# internal
from tier.internal.errors import expect
from tier.internal.git.commit import Commit


class Git:

    def __init__(self, dirpath: Opt[str] = None):
        self.dirpath = dirpath or os.getcwd()

    def is_git(self):
        return self.run('rev-parse', '--is-inside-work-tree')

    def expect_clean(self, path: str = '.'):
        expect(self.is_clean(path), f'{os.path.join(self.dirpath, path)} is expected to be clean')

    def is_staged_changes(self, path: str = '.') -> bool:
        return not self.quiet('diff', '--exit-code', '--staged', path)

    def is_unstaged_changes(self, path: str = '.') -> bool:
        return not self.quiet('diff', '--exit-code', path)

    def is_changes(self, path: str = '.') -> bool:
        return self.is_staged_changes(path) or self.is_unstaged_changes(path)

    def is_clean(self, path: str = '.') -> bool:
        return not self.is_changes(path)

    def commits(self, commit1: str, commit2: str = 'HEAD', path: Opt[str] = None) -> List[Commit]:
        commit_ids = self.commit_ids(commit1, commit2, path)
        return [Commit(commit_id, git=self) for commit_id in commit_ids]

    def commit_ids(self, commit1: str, commit2: str = 'HEAD', path: Opt[str] = None) -> List[str]:
        args = [
            'log',
            f'{commit1}..{commit2}',
            '--pretty=%H',
        ]
        if path:
            args.append(path)
        return self.capture(*args).splitlines()

    def latest_commit_id(self, path: Opt[str] = None) -> str:
        args = ['log', '-n', '1', '--pretty=%H']
        if path:
            args.append(path)
        return self.capture(*args)

    def top_level(self) -> str:
        return self.capture('rev-parse', '--show-toplevel')

    def run(self, *args: str) -> bool:
        return subprocess.run(
            ['git'] + list(args),
            cwd=self.dirpath,
        ).returncode == 0

    def check(self, *args: str):
        subprocess.run(
            ['git'] + list(args),
            check=True,
            cwd=self.dirpath,
        )

    def quiet(self, *args: str) -> bool:
        return subprocess.run(
            ['git'] + list(args),
            capture_output=True,
            cwd=self.dirpath,
            ).returncode == 0

    def capture(self, *args: str, check: bool = True, strip: bool = True) -> str:
        res = subprocess.run(
            ['git'] + list(args),
            capture_output=True,
            check=check,
            cwd=self.dirpath,
        )
        captured = res.stdout.decode()
        if strip:
            captured = captured.strip()
        return captured
