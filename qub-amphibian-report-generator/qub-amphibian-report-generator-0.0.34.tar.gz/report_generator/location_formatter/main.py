"""Script to run the basic location formatter process.

Takes the input_file_name opens it in pandas runs the location_formatter on the
Location column of the inputted dataset and then saves the altered dataset in
the output_file_name

Args:
    input_file_name(str): string input file name
    output_file_name(str): string output file name
"""


import cProfile
import sys
import time
from datetime import datetime

import location_updater
import pandas
from loguru import logger


def main(input_file_name: str, output_file_name: str, inplace=True) -> None:
    """Call location_formatter.

    Operates location formatter on input_file saves as output_file

    Args:
        input_file_name(str): string input file name
        output_file_name(str): string output file name

    """
    # Process start time
    start_time = time.time()
    start_datetime = datetime.now()

    # Create logger file
    logger.add(f"logs/location_finder_{start_datetime}.log")

    # logger start
    logger.info("Started updating location")

    # load Dataframe
    logger.info("Reading Excel Start")
    process_start_time = time.time()

    data_frame = pandas.read_excel(input_file_name)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Reading Excel end: {process_time_taken}s")

    # Update DataFrame with new location information
    logger.info("Updating Dataframe Start")
    process_start_time = time.time()

    updated_location_data_frame = location_updater.update_location(data_frame)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Updating Dataframe end: {process_time_taken}s")

    # Output updated DataFrame to output file
    logger.info(f"Output Dataframe to {output_file_name} Start")
    process_start_time = time.time()

    updated_location_data_frame.to_excel(output_file_name, index=False)

    process_time_taken = time.time() - process_start_time
    logger.info(f"Output to {output_file_name} end: {process_time_taken}s")
    logger.info(f"Finished updating locations end: {time.time() - start_time}s")


if __name__ == "__main__":
    args = sys.argv
    start_time = time.time()
    if len(args) < 3:
        logger.warning("Invalid number of arguments:")
        logger.warning("python3 main.py {input_file} {output_file}")
    else:
        if len(args) == 4:
            cProfile.run("main(args[1], args[2], args[3])", "profile")
        else:
            cProfile.run("main(args[1], args[2])", "profile")
    logger.info(f"Time taken: {time.time() - start_time}s")
