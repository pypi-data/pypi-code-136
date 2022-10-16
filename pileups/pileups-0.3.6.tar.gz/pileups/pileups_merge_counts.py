#!/usr/bin/env python3
#===============================================================================
# pileups_merge_counts.py
#===============================================================================

"""Merge counts files"""




# Imports ======================================================================

import argparse
from pileups.pileups import merge_counts




# Functions ====================================================================

def parse_arguments():
    parser = argparse.ArgumentParser(description='Merge counts files')
    parser.add_argument('tsv', nargs='+', help='Paths to counts files')
    parser.add_argument('--header', help='Add a header to the output')
    parser.add_argument(
        '--het-filter',
        metavar='<int>',
        type=int,
        help='apply het filter'
    )
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    for row in merge_counts(
        *args.tsv,
        header=(args.header.split() if args.header else None),
        het_filter=args.het_filter
    ):
        print('\t'.join(row), end='\n')
