import argparse
import utils as utils
from run import run

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Tool to generate and evaluate mathematical models from GNSS satellites u-center csv files.')

    dir_or_file = parser.add_mutually_exclusive_group(required=False)
    dir_or_file.add_argument('-file', type=utils.file_path, help='CSV file to analyze')
    dir_or_file.add_argument('-dir', type=utils.dir_path,
                             help='Directory which contains all CSV files to analyze (default is current directory)')

    parser.add_argument('-sat', type=int, help='Satellite number to analyze (default is all satellites)',
                        required=False)
    parser.add_argument('-save', type=utils.dir_path,
                        help='Directory where results will be saved (default is current directory', required=False)

    args = parser.parse_args()

    run(vars(args))
