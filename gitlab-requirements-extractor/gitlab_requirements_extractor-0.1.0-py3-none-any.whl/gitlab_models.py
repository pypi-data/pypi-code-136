import json
import os
import re

from gitlab.v4.objects import ProjectIssue
from pydantic import BaseModel

FULL_IGNORE_LABEL = 'ignore'


class References(BaseModel):
    short: str
    full: str

    def get_project_url(self) -> str:
        return self.full.split('#')[0]


class GitlabIssue(BaseModel):
    id: int
    iid: int
    title: str
    state: str
    labels: list[str]
    references: References
    description: str

    GITLAB_BASE_URL = os.getenv('GITLAB_BASE_URL', 'https://gitlab.com')

    def __hash__(self):
        """
        makes this object hashable
        :return:
        """
        return self.id

    def get_issue_link(self) -> str:
        """

        :return: https://gitlab.com/foo/group/project/-/issues/
        """
        prefix = self.references.get_project_url()
        return f"{self.GITLAB_BASE_URL}/{prefix}/-/issues/{self.iid}"

    def ignore(self) -> bool:
        """Shall this issue be ignored?"""
        return FULL_IGNORE_LABEL in self.labels

    @staticmethod
    def from_project_issue(obj: ProjectIssue):
        return GitlabIssue(**json.loads(obj.to_json()))

    def get_requirements(self) -> list[str]:
        issue_description = self.description
        start, end = _find_requirement_part(issue_description)
        if start == end:
            return []

        result = []
        # convert lines to items
        sub_lines = issue_description[start:end].split("\n")
        for line in sub_lines:
            if line.startswith('-'):
                line = line[1:].strip()
                if len(line) > 5:
                    result.append(line)
        return result


def _find_requirement_part(issue_description: str) -> tuple[int, int]:
    """
    (start_pos, end_pos) of the issue_description where the requirements / acceptance criterias are
    :param issue_description:
    :return:
    """
    req = re.search('((#)+ (requirements|acceptance))', issue_description, flags=re.IGNORECASE)
    if not req:
        return 0, 0

    headline_prefix = req.group(0).split(' ')[0]
    start = issue_description.find('\n', req.end())
    end = issue_description.find(f"\n{headline_prefix} ", start)
    if -1 == end:
        # no next headline, assume end of text
        end = len(issue_description)
    return start, end
