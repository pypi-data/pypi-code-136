import re
from collections import defaultdict
from sh import git
from git_jira.config import Config

class GitBranch:
    def __init__(self, issue_key=None, issue_summary=None, name_format='issue_key-issue_summary'):
        if issue_key and issue_summary:
            issue_summary = re.sub('[^a-zA-Z\d]','-', issue_summary).lower()
            issue_summary = re.sub('-{2,}', '-', issue_summary)
            self.name = name_format.replace('issue_key', issue_key).replace('issue_summary', issue_summary)
            self.issue_key = issue_key
        else:
            self.name = str(git.branch("--show-current"))[:-1] #Find a better way
            try:
                self.issue_key = re.search(f'{Config().jira["default_project_key"]}-[0-9]*', self.name).group(0)
            except:
                self.issue_key = None

    def create(self):
        git.checkout("-b", self.name)

class GitRepo:
    def __init__(self):
        pass

    def get_branches(self):
        return [b for b in git("--no-pager", "branch", "--all", "--format='%(refname:short)'").stdout.decode().replace("'", "").split('\n') if len(b)>0]

    def get_branches_issue_keys(self):
        branches = defaultdict(lambda: list())
        for branch in self.get_branches():
            try:
                issue_key = re.search(f'{Config().jira["default_project_key"]}-[0-9]*', branch).group(0)
                existing_branches = branches[issue_key]
                existing_branches.append(branch)
                branches.update({issue_key: existing_branches})
            except:
                pass
        return branches
