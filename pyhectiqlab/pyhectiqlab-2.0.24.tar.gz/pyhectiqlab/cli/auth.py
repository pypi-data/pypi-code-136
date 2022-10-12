import os
import click
import getpass
import pyhectiqlab
import pyhectiqlab.ops as ops
from pyhectiqlab.utils import load_event_manager
from pyhectiqlab.auth import AuthProvider
from pyhectiqlab.mlmodels import download_mlmodel as ops_download_mlmodel
from pyhectiqlab.datasets import download_dataset as ops_download_dataset
from pyhectiqlab.apps import download_app as ops_download_app
from pyhectiqlab.apps import create_app as ops_create_app
import socket

@click.group()
def cli():
    """The official hectiqlab command line client"""
    pass

@cli.command()
def add_profile():
	auth = AuthProvider()
	username = click.prompt('Username ', )
	if auth.profile_exists(username):
		click.echo(f'A profile already exists for {username} at {auth.tokens_path}. Try using the pyhectiqlab or delete the profile before executing add-profile.')
		return

	password = getpass.getpass(prompt='Password: ', stream=None) 
	try:
		api_name = socket.gethostname()
	except:
		api_name = None

	name = click.prompt('Alias for the key: ', default=api_name)
	click.echo("Connecting...")
	success, api_key_uuid = auth.fetch_secret_api_token(username, password, name)

	if success:
		click.echo(f'Added profile [{username}] in {auth.tokens_path}')
		if (auth.profiles and len(auth.profiles)>1):
			click.echo(f"You have multiple profiles in {auth.tokens_path}. Use env var HECTIQLAB_PROFILE to switch between profiles.")
		click.echo('You can now start using hectiqlab 🎉!')
		click.echo('📚 Documentation at https://docs.hectiq.ai')
		click.echo('🚀 Web palteform at https://lab.hectiq.ai')

	else:
		click.echo('😞 Unsuccessful login.')

@cli.command()
def version():
	click.echo(pyhectiqlab.__version__)

@cli.command()
def profiles():
	auth = AuthProvider()
	profiles = list(auth.profiles.keys())
	click.echo(profiles)

@cli.command()
@click.option('-p', '--project', prompt="Project", help='Path of the project (e.g. `hectiqai/project`)', required=True)
@click.option('-n', '--name', prompt='MLModel name', help='Name of the mlmodel', required=True)
@click.option('-v', '--version', help='Version of the mlmodel. If not specified, will download the latest release', required=False)
@click.option('-s', '--save_path', help='Save path [./]', default="./", required=False)
@click.option('-o', '--overwrite', is_flag=True)
def download_mlmodel(project, name, version, save_path, overwrite):
	dir_path = ops_download_mlmodel(mlmodel_name=name, 
						project_path=project, 
						version=version, 
						save_path=save_path, 
						overwrite=overwrite)
	if dir_path is not None:
		click.echo(f'MLModel saved in {dir_path}')

@cli.command()
@click.option('-p', '--project', prompt="Project", help='Path of the project (e.g. `hectiqai/project`)', required=True)
@click.option('-n', '--name', prompt='Dataset name', help='Name of the dataset', required=True)
@click.option('-v', '--version', help='Version of the dataset. If not specified, will download the latest release', required=False)
@click.option('-s', '--save_path', help='Save path [./]', default="./", required=True)
@click.option('-o', '--overwrite', is_flag=True)
def download_dataset(project, name, version, save_path, overwrite):
	dir_path = ops_download_dataset(dataset_name=name, 
						project_path=project, 
						version=version, 
						save_path=save_path, 
						overwrite=overwrite)
	if dir_path is not None:
		click.echo(f'Dataset saved in {dir_path}')

@cli.command()
@click.option('-p', '--project', prompt="Project", help='Path of the project (e.g. `hectiqai/project`)', required=True)
@click.option('-n', '--name', prompt='App name', help='Name of the app', required=True)
@click.option('-s', '--save_path', help='Save path [./]', default="./", required=True)
@click.option('-o', '--overwrite', is_flag=True)
@click.option('-r', '--raw', help='If set, the files are downloaded in save_path without directory', is_flag=True)
def download_app(project, name, save_path, overwrite, raw):
	dir_path = ops_download_app(app_name=name, 
						project_path=project, 
						save_path=save_path, 
						overwrite=overwrite,
						no_dir=raw)
	if dir_path is not None:
		click.echo(f'App saved in {dir_path}')


@cli.command()
@click.option('-p', '--project', prompt="Project", help='Path of the project (e.g. `hectiqai/project`)', required=True)
@click.option('-n', '--name', prompt='App name', help='Name of the app', required=True)
@click.option('-d', '--description', prompt='App description', help='A one-line description of what the app does', required=False)
@click.option('--files_path', type=click.Path(exists=True), prompt='Path to the folder containing the app', help='Path to the files',required=True, autocompletion=os.listdir)
@click.option('--privacy', prompt='Privacy settings (public or private)', type=click.Choice(['public', 'private']), required=True)
@click.option('--app_type', prompt='The app type',  help='The app type', type=click.Choice(['streamlit', 'gradio', 'plotly']), required=True)
def create_app(project, name, description, files_path, privacy, app_type):
	manager = load_event_manager()
	results = manager.add_event("fetch_instance_types", (project,), async_method=False)
	if results.get("status_code")!=200:
		click.echo(results.get("detail", "Something wrong occured."))
		return
	payload = results.get("payload")
	if payload.get("owned_by")=="organization":
		click.echo(f"Showing the instances for {payload.get('owner')}:")
	instance_types = results.get("results")
	choices = click.Choice([r["name"] for r in instance_types if r["selectable"]==True], case_sensitive=True)
	instances_description = "\n\n"
	for r in instance_types:
		available = ""
		if r["selectable"]==False:
			available = "Requies a team membership\n"
		instances_description += f"{available}[{r['name']}] {r['price']}\n  {r['description']}\n  {r['tip']}\n\n"

	instance_type = click.prompt(f"Select your instance type: {instances_description}", type=choices, show_choices=True)
	click.echo("Please wait while we create your app...")

	url = ops_create_app(name=name, 
				project=project,
				app_type=app_type, 
				instance=instance_type, 
				is_private=privacy=="private", 
				dir_path=files_path, 
				description=description)
	click.echo(f"🚀 Your app is not available at {url}")
	click.launch(url)