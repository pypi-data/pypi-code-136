from collections.abc import Iterator

import gitlab
from decouple import config
from gitlab.v4.objects import ProjectIssue

from requirements_extractor.gitlab_models import GitlabIssue


class GitlabConnector:
    ENV_TOKEN_NAME = 'PRIVATE_TOKEN'
    ENV_PROJECT_ID = 'PROJECT_ID'

    def __init__(self, personal_api_token: str, project_id: str):
        """
        Create Gitlab instance with token and project
        :param personal_api_token:
        :param project_id:
        """
        assert personal_api_token
        assert project_id
        self.project_id = project_id
        self.__gitlab = gitlab.Gitlab(private_token=personal_api_token)

    @property
    def project(self):
        return self.__gitlab.projects.get(self.project_id)

    @staticmethod
    def factory() -> "GitlabConnector":
        personal_api_token = config(GitlabConnector.ENV_TOKEN_NAME)
        project_id = config(GitlabConnector.ENV_PROJECT_ID, default=False)
        if not project_id:
            # if project is not defined, assume current project
            project_id = config('CI_PROJECT_ID')
        return GitlabConnector(personal_api_token, project_id)

    def get_all_issues(self) -> set[GitlabIssue]:
        issues = self.project.issues.list(get_all=True)
        return self._convert_issues(issues)

    def get_issues(self, state: str = None, labels: list[str] = None, order_by="created_at", sort="desc"):
        """
        Get filtered list of issues
        implements #31
        :param state: "opened", "closed", None
        :param labels: list or None = all
        :param order_by:
        :param sort:
        :return:
        """
        args = {'order_by': order_by, 'sort': sort, 'iterator': True}
        if state:
            args['state'] = state
        if labels:
            args['labels'] = labels
        issues_iter = self.project.issues.list(**args)
        return self._convert_issues(issues_iter)

    @staticmethod
    def _convert_issues(issue_json: Iterator[ProjectIssue]) -> set[GitlabIssue]:
        result = set()
        for raw_req in issue_json:
            result.add(GitlabIssue.from_project_issue(raw_req))
        return result

    @staticmethod
    def _convert_issues_from_dict(issue_json: list[dict]) -> set[GitlabIssue]:
        result = set()
        for raw_req in issue_json:
            result.add(GitlabIssue(**raw_req))
        return result

    def link_issues(self, parent_id: int, child_issue: ProjectIssue):
        """

        :param parent_id: iid of parent issue
        :param child_issue: the issue itself, created by get_project().issues.create(args)
        :return: (raw) gitlab issues - do not use
        """
        data = {
            'target_project_id': child_issue.project_id,
            'target_issue_iid': child_issue.iid
        }
        parent_issue = self.project.issues.get(id=parent_id)
        return parent_issue.links.create(data)

    def get_linked_issues(self, parent_issue: int) -> dict[int, str]:
        issue = self.project.issues.get(parent_issue)
        linked = {}
        for li in issue.links.list():
            gi = GitlabIssue.from_project_issue(li)
            linked[gi.iid] = gi.title
        return linked

    def append_label(self, label: str, issue: GitlabIssue):
        handled_issue = self.project.issues.get(issue.iid)
        labels = issue.labels
        labels.append(label)
        handled_issue.labels = labels
        handled_issue.save()
