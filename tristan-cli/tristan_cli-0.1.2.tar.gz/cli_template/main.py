import typer


app = typer.Typer()


@app.callback()
def callback():
    """
    Setup git-leaks automatically
    """


@app.command()
def initialize():
    """
    Setup Git-Leaks
    """
    typer.echo("Git-Leaks setup successfully, we can all go home")

