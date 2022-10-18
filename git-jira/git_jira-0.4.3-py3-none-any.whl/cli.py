import click

from git_jira.commands.branch import branch
from git_jira.commands.configure import configure
from git_jira.commands.issue import issue
from git_jira.commands.list import list


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    )

def cli():
    """A git addon to manage jira from git.
    For more info visit: https://github.com/rloredo/git-jira
    """
    pass

cli.add_command(configure)
cli.add_command(branch)
cli.add_command(issue)
cli.add_command(list)
