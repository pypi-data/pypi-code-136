import typer

from .project_models import project_models_app

app = typer.Typer()
app.add_typer(project_models_app, name="project-models")


def main():
    app()
