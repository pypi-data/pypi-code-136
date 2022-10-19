from datacite_api import Dois
import click

import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('run.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

print("Working on a DOI ...")
print("Registering")
@click.command()
@click.argument('password_file', type=click.File('r'))
@click.option("-do", "--doi", help="creating a DOI")
@click.option("-y", "--yaml_data", help="updating a DOI")
@click.option("-c", "--create", is_flag=True, help="creating a DOI")
@click.option("-u", "--update", is_flag=True, help="updating a DOI")
@click.option("-d", "--delete", is_flag=True, help="deleting a DOI")
@click.option("-r", "--register", is_flag=True, help="registering a DOI")
@click.option("-f", "--findable", is_flag=True, help="making a DOI findable")
@click.option("-h", "--hide", is_flag=True, help="hiding a DOI")
def run(password_file,yaml_data,doi,create,update,delete,register,findable,hide):
    dc = Dois(password_file,yaml_data,doi)
    if create:
        dc.create_doi()
    elif update:
        dc.update_doi()
        logger.debug(password_file)
    elif register:
        logger.debug("Registering")
        dc.register_doi()

    elif findable:
        dc.set_findable()
    elif hide:
        dc.hide_doi()
    elif delete:
        dc.delete_doi()
run()
