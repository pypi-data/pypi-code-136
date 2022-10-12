# std
import re

# internal
from tier.internal.git.commit import Commit
from tier.internal.versioning.bump_type import BumpType


class CommitAnalyzer:
    MAJOR_PATTERN_1 = re.compile(r'\w+(\(\w+\))?!: .*(\n\n(.*\n)*BREAKING[ -]CHANGE: .*\n(.*\n)*)?')
    MAJOR_PATTERN_2 = re.compile(r'\w+(\(\w+\))?!?: .*\n\n(.*\n)*BREAKING[ -]CHANGE: .*(\n(.*\n)*)?')
    MINOR_PATTERN = re.compile(r'(feat|minor)(\(\w+\))?: .*(\n\n(.*\n)*)?', flags=re.IGNORECASE)
    PATCH_PATTERN = re.compile(r'(fix|patch)(\(\w+\))?: .*(\n\n(.*\n)*)?', flags=re.IGNORECASE)

    def analyze_commit(self, commit: Commit) -> BumpType:
        return self.analyze_message(commit.message)

    def analyze_commits(self, *commits: Commit) -> BumpType:
        return self.analyze_messages(*(c.message for c in commits))

    def analyze_message(self, message: str) -> BumpType:
        bump_type = BumpType.NULL
        if self.is_major(message):
            bump_type += BumpType.MAJOR
        if self.MINOR_PATTERN.match(message):
            bump_type += BumpType.MINOR
        if self.PATCH_PATTERN.match(message):
            bump_type += BumpType.PATCH
        return bump_type

    def analyze_messages(self, *messages: str) -> BumpType:
        bump_type = BumpType.NULL
        for message in messages:
            bump_type += self.analyze_message(message)
        return bump_type

    @staticmethod
    def is_major(commit_message: str) -> bool:
        return (
            bool(CommitAnalyzer.MAJOR_PATTERN_1.match(commit_message))
            or
            bool(CommitAnalyzer.MAJOR_PATTERN_2.match(commit_message))
        )
