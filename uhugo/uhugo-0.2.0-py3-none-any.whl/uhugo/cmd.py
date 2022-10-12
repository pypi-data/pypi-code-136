import logging
import os
from typing import Text, Union

import click
from packaging import version
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from . import __version__
from .checks import check_hugo, get_latest_version_api
from .download import download_hugo_zip
from .install import install_hugo
from .post_install.detect_providers import check_hugo_file, check_providers_fs

log = logging.getLogger(__name__)
console = Console()


@click.group(name="uhugo",
             help="uhugo is a Hugo binary helper that downloads and set ups the environment.")
@click.option('--debug', help="Use debug mode", default=False, is_flag=True)
@click.version_option(__version__, package_name="uHugo", prog_name="uHugo")
@click.pass_context
def cli(ctx: click.core.Context, debug: bool):
    ctx.ensure_object(dict)
    ctx.obj['debug'] = debug

    if debug:
        logging.basicConfig(level='DEBUG',
                            format="%(asctime)s %(name)s - %(levelname)s:'%(message)s'",
                            datefmt='%d-%b-%y %H:%M:%S')


@cli.command(help="Install latest Hugo binary files")
@click.option('--version', '-v', 'ver', default=None, help="Hugo version to download")
@click.option('--force', is_flag=True, default=False, help="Reinstall Hugo")
def install(ver: Text, force: bool):
    hugo = check_hugo()
    if hugo.exists and not force:
        click.echo(console.print("Hugo has already been installed. Use 'uhugo update' to update.",
                                 style="red"))
        return 

    if force:
        log.debug(f"Deleting existing Hugo at {hugo.path}")
        os.remove(hugo.path)

    with console.status("Fetching latest version", spinner="dots"):
        _ver = get_latest_version_api(ver)
    click.echo(console.print(f"- Latest version is v{_ver}", style="yellow bold"), color=True)

    download_path = download_hugo_zip(_ver)

    with console.status(f"Installing Hugo {_ver}", spinner="dots"):
        installed_path = install_hugo(download_path)

    console.print("\nHugo installed! :tada:\n", style='green bold')

    console.print(Panel.fit(f"[bold green]Make sure {installed_path!r} is in your $PATH", title="Note"))


@cli.command(help="Updates Hugo binary files and any associated configurations")
@click.option("--to", default=None, help="Updates to a specified version")
@click.option("--only-hugo", is_flag=True, help="Updates only Hugo binary while ignoring providers")
@click.option("--only-cloud", is_flag=True, help="Updates only cloud providers while ignoring Hugo")
def update(to: Union[Text, None], only_hugo: bool, only_cloud: bool) -> None:
    hugo = check_hugo()
    if not hugo.exists:
        click.echo(console.print("Hugo is not installed. Use 'uhugo install' to install.",
                                 style="red"))
        return

    with console.status("Fetching latest version", spinner="dots"):
        _ver = get_latest_version_api(to)
        log.debug(f"Latest version is {_ver}")

    if (hugo.version >= version.Version(_ver)) and not to and not only_cloud:
        console.print("Hugo is up to date :tada:", style="green")
        return

    if not to and not (hugo.version >= version.Version(_ver)):
        console.print(Panel.fit(f"New version available, v{hugo.version} -> v{_ver}", title=f"Hugo v{_ver}"), style="green")

    if not only_cloud:

        download_path = download_hugo_zip(_ver)

        with console.status(f"Installing Hugo {_ver}", spinner="dots"):
            install_hugo(download_path)

        console.print("\nLocal Hugo updated! :tada:\n", style='green bold')

    if only_cloud:
        console.print("Updating only the cloud :sun_behind_cloud:", style="yellow")

    # ignore cloud provider updates with --only-hugo flag
    if only_hugo:
        return

    with console.status("Checking providers") as s:
        provider = check_hugo_file()
        if not provider.name:
            provider = check_providers_fs()
            if not provider.name:
                return

        s.update(f"{provider.name.title()} found")

        # checks for "env" value and sets the appropriate key with the environment value
        for key, val in provider.dict().items():
            if val and val.startswith("env"):
                try:
                    setattr(provider, key, os.environ[val.split(":")[1]])
                except KeyError as e:
                    log.debug(e)
                    console.print(f"Environment variable '{val.split(':')[1]}' not found", style="bold red")
                    exit(1)

        if provider.name == "cloudflare":
            from .post_install.providers.cloudflare import Cloudflare
            cf = Cloudflare(provider.api_key, provider.email_address, provider.account_id, _ver)
            projects = cf.get_projects(provider.project).json()
            if projects['success'] and isinstance(projects['result'], list):
                names = [name['name'] for name in projects['result']]
                name = Prompt.ask("Enter project name", choices=names)
            elif not projects['success']:
                console.print("There was an error fetching your Cloudflare project", style="bold red")
                log.debug(projects)
                exit(1)
            else:
                name = provider.project

            current_version = cf.current_version(name)
            if current_version:
                console.print(f"Current Hugo version in Cloudflare: v{current_version}")

            response = cf.update_api(name).json()
            if not response['success']:
                console.print("There was an error updating your Cloudflare environment")
                log.debug(response)
                exit(1)
            console.print(f"\nCloudflare updated with Hugo v{_ver} :tada:", style="green bold")


def main():
    cli(obj={})
