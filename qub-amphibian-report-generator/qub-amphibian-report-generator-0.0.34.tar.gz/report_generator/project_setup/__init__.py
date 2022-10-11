"""# Project Setup.

This package handles initial setup of the project. It creates a directory for project files, configuration files and downloads data required to create locations database utilised in the location_formatter package.

It is made up of the following modules:

- locations_data_setup.py:  Downloads, copies and inserts data into location db.
- locations_db_setup.py: Creates database and tables for locations.
- locations_json_setup.py: Loads data from country and continent csv into json file that will be added to in location formatter.
- new_report_project.py: Provides methods and CLI interface to setup project default settings.
- Project_directory_setup.py: Creates directories and moves files from data directory in package to project directory.

"""
