"""# Report Generator.

Application to create report based on parameters passed into it.

@Params:
        data_source         - Data source for report creation
        report_name         - Title of the report and the file name
        report_author       - Author of the report
        university_name     - Name of the university
        university_school   - Name of the university school

"""
import time

from loguru import logger

import report_generator.config
import report_generator.project_setup.new_report_project as new_project
import report_generator.report_generator_cli.create_report as create_report


def main(arguments: dict = {}) -> None:
    """Command line interface main method.

    The main method for the command line interface.

    Checks if project already exists. If it does loads config data and
    proceeds to run create_report method with data from config and options.
    If it does not have config settings it will run the create_new_project
    process.

    Args:
        arguments (dict)    A dictionary passed from the cli with options
                            selected by the user.
    """
    startTime = time.time()
    config = None

    config = report_generator.config.load_config()

    if config is None:
        new_project.create_new_project()
        config = report_generator.config.load_config()

    data_source = config["data_set"]

    if arguments["--output"] is not False:
        report_name = arguments["--output"].upper()
    else:
        report_name = config["report_name"].upper()

    report_author = config["author_name"].upper()
    university_name = config["uni_name"].upper()
    university_school = config["school_name"].upper()

    logger.info(f"Creating Report: {report_name}.pdf")
    create_report.create_report(
        data_source,
        arguments,
        report_name,
        report_author,
        university_name,
        university_school,
    )
    logger.info(f"Report Complete: {report_name}.pdf")

    executionTime = time.time() - startTime
    logger.info("Report creation time in seconds: " + str(executionTime))


if __name__ == "__main__":
    main()
