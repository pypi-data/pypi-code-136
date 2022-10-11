"""# Clean Data.

Script to clean data from dataset and create new excel sheet with data.

Can be ran from command line:

    python3 clean_data.py {input_file} {output_file}

Or import clean_data function:

    from clean_data import clean_data

"""

import os
import re
import sys

import pandas
from loguru import logger


def create_data_frame(path_to_dataset: str):
    """Create data frame.

    Loads excel file and returns Pandas DataFrame obj

    Args:
        path_to_data_set(str): file path string

    Returns:
        data_frame(object): Pandas DataFrame object
    """
    data_frame = None
    try:
        data_frame = pandas.read_excel(path_to_dataset)

    except FileNotFoundError as e:
        logger.error(f"Cleaning Data - Failed to open excel file: {e}")

    return data_frame


def clean_data(data_frame: object) -> object:
    """Clean data.

    Takes data_frame object and cleans data by using 'applymap' to apply a
    lamda function to all DataFrame values

    1st Lambda function converts values to strings, replaces instances of ND
    with empty string, and strips whitespace and quotation marks.

    2nd Lambda function converts values that should be numeric back to
    numeric values.

    Args:
        data_frame(object): Pandas DataFrame object

    Returns:
        clean_data_frame(object) Pandas DataFrame object

    """
    clean_data_frame = data_frame.applymap(
        lambda x: re.sub(r'^\s*["]*ND["]*\s*$', "", str(x)).strip().strip('"')
    )
    clean_data_frame = clean_data_frame.applymap(
        lambda x: pandas.to_numeric(x, errors="coerce")
        if x.replace(".", "").isdigit()
        else x
    )
    return clean_data_frame


def main(input_file_name, output_file_name) -> None:
    """Clean data main.

    Takes input_file_name and output_file_name.
    Loads data from input_file
    Cleans data
    Saves as output_file

    Args:
        input_file_name:
        output_file_name:

    """
    # Get filepaths
    cur_dir = os.getcwd()
    path_to_dataset = os.path.join(cur_dir, input_file_name)
    path_to_output_file = os.path.join(cur_dir, output_file_name)

    # load df
    try:
        data_frame = create_data_frame(path_to_dataset)
        # print(data_frame["RangeSize"].head(5))

        # clean df
        clean_data_frame = clean_data(data_frame)
        # print(clean_data_frame["RangeSize"].head())

        # output to new file
        clean_data_frame.to_excel(path_to_output_file, index=False)

    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    args = sys.argv

    if len(args) < 3:
        print("Not enough args")

    else:
        main(args[1], args[2])
