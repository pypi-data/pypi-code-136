#!/usr/bin/env python3
#===============================================================================
# write_table.py
#===============================================================================

"""Write a data table from luciferase input data"""




# Imports ======================================================================

import argparse
import json
import pandas as pd

from luciferase.luciferase import load_data, remove_batch_effect




# Constants ====================================================================

JSON_EXAMPLE = """Example of luciferase reporter data in JSON format:
{
  "Ref, untreated": [33.2, 30.3, 33.3],
  "Alt, untreated": [19.7, 16.2, 18.3],
  "Empty, untreated": [1.0, 1.0, 1.0],
  "Ref, dex": [149.4, 99.7, 124.5],
  "Alt, dex": [44.6, 37.6, 37.7],
  "Empty, dex": [1.1, 1.0, 0.9]
}

The number of entries in the input JSON should be a multiple of 3
"""




# Functions ====================================================================

def parse_arguments():
    parser = argparse.ArgumentParser(
        description=(
            'Plot and compare the ref / alt ratios of two luciferase reporter '
            'assays'
        ),
        epilog=JSON_EXAMPLE,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        'data',
        metavar='<path/to/data.{csv,tsv,json,xls,xlsx}>',
        help='path to a file containing luciferase reporter data'
    )
    parser.add_argument(
        'output',
        metavar='<path/to/output.{csv,tsv}>',
        help='path to output file'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    luc_data = load_data(args.data)
    if isinstance(luc_data, dict):
        luc_data = pd.DataFrame.from_dict(luc_data).transpose()
    if 'Batch' in luc_data.index:
        luc_data = remove_batch_effect(luc_data)
    if args.output.endswith('tsv'):
        luc_data.transpose().to_csv(args.output, sep='\t', index=False)
    elif args.output.endsiwth('csv'):
        luc_data.transpose().to_csv(args.output, index=False)
    else:
        raise RuntimeError('Output should be a CSV or TSV file')
