import click
from pick import pick

from git_jira.jira import JiraIssue, JiraMetaIssue
from git_jira.git import GitBranch
from git_jira.utils import INDICATOR


def prompt_field(field):
    if field["type"] == "string":
        return click.prompt(field["name"], type=str)
    elif field["type"] == "number":
        return click.prompt(field["name"], type=float)
    elif field["type"] == "option":
        option, _ = pick([opt["value"] for opt in field["options"]], field["name"], indicator=INDICATOR)
        click.echo(f"{field['name']}: {option}")
        return {'value' : option}
    elif field["type"] == "array":
        response = pick([opt['value'] for opt in field['options']], f"{field['name']} (press SPACE to select, ENTER to continue", multiselect=True, min_selection_count=1, indicator=INDICATOR)
        click.echo(f"{field['name']}: {', '.join([option[0] for option in response])}")
        return [{'value' : option[0]} for option in response]

def issue_fields_input():
    meta_issue = JiraMetaIssue()
    fields = dict()
    click.echo("Fill in the required fields")
    fields["project"] = {"key": meta_issue.project_code}
    option, _ = pick(meta_issue.issue_type_names, "Issue type", indicator=INDICATOR)
    fields["issuetype"] = {"name": option}
    click.echo(f"Issue type: {option}")
    fields["summary"] = click.prompt("Summary", type=str)
    fields["description"] = click.prompt("Description", type=str)
    #Iterate if there is any other required
    for field in meta_issue.required_fields(fields["issuetype"]["name"]):
        if field['key'] not in ["project", "issuetype", "summary", "description", "reporter"]:
            fields[field['key']] = prompt_field(field)
    return fields

@click.command()
@click.option('-k', '--issue-key', 'issue_key', help='Create an branch using an existing issue', type=str)
@click.option('-f', '--format', 'branch_format', default = 'issue_key-issue_summary', help='Specify a custom branch name, words issue_key and summary will be replaced with the issue key and summary', type=str)
def branch(issue_key, branch_format):
    if issue_key:
        issue = JiraIssue(issue_key = issue_key)
        msg = f"Branch created! See issue: {issue.url}"
    else:
        issue = JiraIssue(input_fields=issue_fields_input())
        msg = f"{issue.type} created at {issue.url}"
    GitBranch(issue_key=issue.key, issue_summary=issue.summary, name_format=branch_format).create()
    click.echo(msg)
