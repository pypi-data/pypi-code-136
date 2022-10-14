import click
from git_jira.jira import JiraProject
from git_jira.git import GitRepo
from git_jira.utils import print_table

columns = ['key', 'type', 'summary', 'branches', 'assignee']

def classify_issues(status):
    issues = dict()
    for issue in JiraProject().get_issues(status=status):
        issues.update({issue.key:{"type":issue.type, "summary":issue.summary, "assignee":issue.assignee, "branches": "No branches"}})
    branches = GitRepo().get_branches_issue_keys()
    for issue_key in branches.keys():
         try:
            issues[issue_key].update({"branches":', '.join(branches[issue_key])})
         except:
            pass    
    return [[issue_key, issues[issue_key]['type'], issues[issue_key]['summary'], issues[issue_key]['branches'], issues[issue_key]['assignee']]  for issue_key in issues.keys()]


@click.command()
@click.option('-s', '--status', help='List issues with this status', default='Planned', type=str)
def list(status):
    click.echo("Getting available issues...")
    issues = classify_issues(status=status)
    click.echo(print_table(columns, issues))
    