import re
import subprocess
import webbrowser
from typing import Optional

import typer

app = typer.Typer(name="git-open")


def extract_url(url: str) -> str:
    https_pattern = re.compile(r".*://(.*@)?(.*?)(:\d+)?/(.*)")
    ssh_pattern = re.compile(r"(.*@)?(.*?)(:\d+)?/(.*)")
    match = https_pattern.match(url)
    if match is None:
        match = ssh_pattern.match(url)
    if match is None:
        typer.secho(
            f"Could not extract http url from {url}", err=True, fg=typer.colors.RED
        )
        raise typer.Abort()
    user = match.group(1)
    host = match.group(2)
    port = match.group(3)
    path = match.group(4)
    return f"https://{host}/{path}"


def get_git_url(path: Optional[str] = ".") -> str:
    cmd = f"pushd {path} > /dev/null 2>&1; git remote -v | awk '/fetch/{{print $2}}'; popd > /dev/null 2>&1"
    result = subprocess.run(cmd, capture_output=True, shell=True)
    url = result.stdout.decode().strip("\n")
    return url


@app.command()
def git_open(
    path: str = typer.Argument(".", help="path in directory of the desired repo."),
):
    """Opens the remote github/gitlab repository belonging to this local repo

    Add to path, then git CLI will pick it up automatically: `git open .`
    """
    url = get_git_url(path)
    git_url = extract_url(url)
    typer.secho(f"{git_url}", err=False, fg=None)
    webbrowser.open(git_url, new=2)


if __name__ == "__main__":
    app()
