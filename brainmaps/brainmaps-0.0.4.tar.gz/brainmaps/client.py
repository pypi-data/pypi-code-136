from itertools import chain
import click
import requests
import json
import secrets


API_URL = "https://api.brainmaps.io/graphql"
API_KEY_LENGTH=64

logo = """
    /$$$$$$$                      /$$           /$$      /$$                              
    | $$__  $$                    |__/          | $$$    /$$$                              
    | $$  \ $$  /$$$$$$   /$$$$$$  /$$ /$$$$$$$ | $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$$
    | $$$$$$$  /$$__  $$ |____  $$| $$| $$__  $$| $$ $$/$$ $$ |____  $$ /$$__  $$ /$$_____/
    | $$__  $$| $$  \__/  /$$$$$$$| $$| $$  \ $$| $$  $$$| $$  /$$$$$$$| $$  \ $$|  $$$$$$ 
    | $$  \ $$| $$       /$$__  $$| $$| $$  | $$| $$\  $ | $$ /$$__  $$| $$  | $$ \____  $$
    | $$$$$$$/| $$      |  $$$$$$$| $$| $$  | $$| $$ \/  | $$|  $$$$$$$| $$$$$$$/ /$$$$$$$/
    |_______/ |__/       \_______/|__/|__/  |__/|__/     |__/ \_______/| $$____/ |_______/ 
                                                                    | $$                
                                                                    | $$                
                                                                    |__/                
    """

@click.group(chain=True)
def cli():
    """BrainMaps command-line client."""
    print(logo)



@cli.command("register")
@click.option("--name", default="John Smith", prompt="Enter your full name", help="Your full name")
@click.option("--username", default="@johnsmith", prompt="Enter your BrainMaps username", help="Your username on BrainMaps")
def register(name, username):
    click.echo(f"Hello, {name}!")
    if username:
        click.echo(f"Your username is {username}")


@cli.command("create")
@click.option("--dataset", default="Default Dataset", prompt="Enter your full name", help="Your full name")
def create(dataset):
    click.echo(f"Creating {dataset}...")
    if dataset:
        click.echo(f"Your dataset has been created successfully.")
    else:
        click.echo("No dataset name provided!")


@cli.command("generate_api_key")
def generate():
    generated_key = secrets.token_urlsafe(API_KEY_LENGTH)
    click.echo(f"Your API Key is: {generated_key} . Please keep this safe, it will not be shown again.")


@cli.command("upload")
@click.option("--dataset", default="", prompt="Enter a dataset ID", help="Dataset ID to upload")
def upload(dataset):
    # click.echo(f"Hello, {name}!")
    if dataset:
        click.echo(f"Dataset to upload: {dataset}")
    else:
        click.echo("Please enter a dataset ID to upload.")


@cli.command("download")
@click.option("--dataset", default="", prompt="Enter a dataset ID", help="Dataset ID to download")
def download(dataset):
    # click.echo(f"Hello, {name}!")
    if dataset:
        click.echo(f"Dataset to upload: {dataset}")
    else:
        click.echo(f"Please enter a dataset ID to download")

cli.add_command(register)
cli.add_command(generate)
cli.add_command(create)
cli.add_command(upload)
cli.add_command(download)

if __name__ == "__client__":
    print(logo)
    cli()

if __name__ == "__main__":
    print(logo)
    cli()
