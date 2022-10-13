import os

import pytest

from requirements_extractor.gitlab_connector import GitlabConnector


def need_token(func):
    @pytest.mark.skipif(os.getenv(GitlabConnector.ENV_TOKEN_NAME) is None,
                        reason="Need gitlab private token %s" % GitlabConnector.ENV_TOKEN_NAME)
    def myfunc(*args, **kwargs):
        return func(*args, **kwargs)

    return myfunc


def gc():
    return GitlabConnector.factory()


@need_token
def test_issues():
    issues = gc().get_all_issues()
    for issue in issues:
        assert issue.iid


@need_token
def test_issues_by_label():
    # tests #31
    labels = ['story']
    issues = gc().get_issues(labels=labels)
    assert len(issues) == 1


@need_token
def test_issues_by_state():
    state = 'closed'
    issues = gc().get_issues(state=state)
    assert len(issues) == 1


@need_token
def test_create_dependend_issue():
    project = gc().project
    args = {'title': 'whatsoever this ticket is called', 'description': 'derived from #1 by an automated test'}
    issue = project.issues.create(args)
    issue.labels = ['requirement']
    issue.save()

    src_issue, dest_issue = gc().link_issues(1, issue)
    assert src_issue.iid == 1
    assert dest_issue.labels == ['requirement']

    issue.delete()


@need_token
def test_get_linked_issues():
    linked = gc().get_linked_issues(1)
    assert isinstance(linked, dict)
    assert len(linked) == 3
