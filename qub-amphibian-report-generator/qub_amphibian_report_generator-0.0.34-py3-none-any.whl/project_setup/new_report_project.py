"""# New Report Project.

Setup configuration files and directories for report project.

Will have more info soon

"""

import os
import pathlib
import time

import yaml
from loguru import logger

import report_generator.excel_extraction.excel_to_sql
import report_generator.project_setup.locations_data_setup
import report_generator.project_setup.locations_db_setup
import report_generator.project_setup.locations_json_setup
import report_generator.project_setup.project_directory_setup


def create_new_project(settings_dict: dict = None) -> None:
    """Create new report project.

    Creates a new report project.

    Examples:
        Example of use.

    """
    HOME_DIR = pathlib.Path.home()
    logger.info("Starting new Project")
    try:
        settings = get_project_settings(settings_dict)
        dir_path = report_generator.project_setup.project_directory_setup.create_dirs(
            HOME_DIR, settings["project_name"]
        )
        settings["dir_path"] = dir_path
        create_project_config_file(settings)

        report_generator.project_setup.locations_data_setup.insert_default_data(
            dir_path
        )
        # dir_path = os.path.join(HOME_DIR, "c",)
        time.sleep(5)
        report_generator.project_setup.locations_db_setup.locations_database_setup(
            os.path.join(dir_path, "data", "locations")
        )
        time.sleep(5)
        report_generator.project_setup.locations_json_setup.locations_json_setup(
            os.path.join(dir_path, "data", "locations")
        )

        database_path = os.path.join(dir_path, "data", "database", "species.db")

        report_generator.excel_extraction.excel_to_sql.export_to_database(
            settings["data_set"], database_path
        )

        logger.info("Report Project set up complete!")
    except FileExistsError as e:
        logger.error(e)
    except FileNotFoundError as e:
        logger.error(e)
    except KeyboardInterrupt as e:
        logger.error(e)
        logger.error("Quitting Application...")


def get_project_settings(settings: dict = None) -> None:
    """CLI to query project setup from user.

    Gets a series of user inputs to set up the config
    files for the project.

    Examples:
        Example of use.

    Args:
        Settings (dict): Settings dict that is provided if user doing set up
                         from the GUI application rather than the CLI.

    """
    if settings is None:

        print("\nCreating new project")
        project_name = input("Please enter project name: ")
        report_name = input("Please enter report name: ")
        author_name = input("Please enter author name: ")
        school_name = input("Please enter School name: ")
        uni_name = input("Please enter uni name: ")
        data_set = input("Please enter path to data_set file: ")

        settings = {
            "project_name": project_name,
            "report_name": report_name,
            "author_name": author_name,
            "school_name": school_name,
            "uni_name": uni_name,
            "data_set": data_set,
            "fonts": {
                "header_colour": "Black",
                "header_font": "Helvetica",
                "header_size": 48,
                "paragraph_colour": "Black",
                "paragraph_font": "Helvetica",
                "paragraph_size": 10,
                "title_colour": "Red",
                "title_font": "OpenSans-Bold",
                "title_size": 56,
                "title_sub": "OpenSans",
            },
        }
    else:
        settings["fonts"] = {
            "header_colour": "Black",
            "header_font": "Helvetica",
            "header_size": 48,
            "paragraph_colour": "Black",
            "paragraph_font": "Helvetica",
            "paragraph_size": 10,
            "title_colour": "Red",
            "title_font": "OpenSans-Bold",
            "title_size": 56,
            "title_sub": "OpenSans",
        }
    return settings


def create_project_config_file(settings: dict) -> None:
    """Create the project config file.

    Creates a Yaml file containing all project's
    basic settings.

    Examples:
        Example of use.

    """
    with open("config.yaml", "w", encoding="utf-8") as file:
        yaml.dump(settings, file)


def main():
    """Create new Report.

    Main method for module.

    Example:
        Example use case.
    """
    create_new_project()


if __name__ == "__main__":
    main()
