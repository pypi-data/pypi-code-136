import click
from git_jira.config import Config

def jira_config_input():
    config = dict()
    config["server_url"] = click.prompt("Jira server url", type=str)
    config["username"] = click.prompt("Jira username", type=str)
    config["api_token"] = click.prompt("Jira API token", type=str)
    config["default_project_key"] = click.prompt("Default project", type=str)
    return config

@click.command()
def configure():
    click.echo("Welcome to git-jira. Let's generate your config file...")
    config = {"jira": jira_config_input()}
    click.echo(
        f"A config file with the following params will be created at {Config().path} \n"
    )
    click.echo(f"{Config().str_content(config)}")
    if click.confirm("Do you want to continue?"):
        Config().change(config)
        click.echo(f"Config file successfully created.")
        click.echo("Thanks for using git-jira!")
    else:
        click.echo(f"Configuration aborted.")
