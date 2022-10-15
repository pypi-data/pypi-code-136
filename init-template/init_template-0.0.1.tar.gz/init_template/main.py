#!/usr/bin/env python3
import os
import click

EXEC_PATH = os.getcwd()
TEMPLATE_REPO = "https://github.com/EliasOlie/ts-setup.git"

PATH_HELP_MESSAGE = """
(pt-BT) O caminho onde você deseja criar o projeto.

EX ".", "./repo"

"""

TEMPLATE_HELP_MESSAGE = """
(pt-BR) Qual template você deseja, o valor padrão é um projeto minimalista de TS
"""
# @click.option("--initialize-git", "--git", default=False, prompt=True)


@click.group()
def cli():
  pass

@cli.command()# ✔
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
def setup_no_git(path, template):
  click.echo(click.style("Inicializando...", fg="blue"))
  
  os.system(f"git clone {template} {path}")
   
  os.system("rm -rf ./.git")
  click.echo(click.style("Feito", fg="green"))

@cli.command()# ✔
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
def setup_git(path, template):
  click.echo(click.style("Inicializando...", fg="blue"))
  
  os.system(f"git clone {template} {path}")
  
  click.echo(click.style("Preparando repositório", fg="yellow"))
  os.system("rm -rf ./.git")
  os.system("git init")
    
  click.echo(click.style("Feito", fg="green"))

@cli.command()
@click.option("--path", "-p", default=EXEC_PATH, help=PATH_HELP_MESSAGE)
@click.option("--template", "-t", default=TEMPLATE_REPO, help=TEMPLATE_HELP_MESSAGE)
@click.option("--remote-origin", "--origin", prompt=True)
def setup_git_origin(path, template, remote_origin):
  click.echo(click.style("Inicializando...", fg="blue"))
  
  os.system(f"git clone {template} {path}")
  
  click.echo(click.style("Preparando repositório", fg="yellow"))
  os.system("rm -rf ./.git")
  os.system("git init")
  click.echo(click.style("Adicionando origem remota", fg="yellow"))
  os.system(f"git remote add origin {remote_origin}")  
  click.echo(click.style("Feito", fg="green"))

if __name__ == '__main__':
  cli()