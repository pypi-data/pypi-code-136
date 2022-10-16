#!/usr/bin/env python3
#===============================================================================
# var_to_hg19.py
#===============================================================================

# Imports ======================================================================

import itertools
import pyhg19
import re
import sys

from argparse import ArgumentParser



# Constants ====================================================================

RSID_REGEX = re.compile('rs[1-9][0-9]+$')




# Functions ====================================================================

def generate_vars_from_file(file):
	  with open(file) as f:
		    yield from f.read().splitlines()


def var_to_hg19(*variants):
    for r in variants:
        try:
            coord = pyhg19.coord(r)
            yield ('chr'+ str(coord.chr), coord.pos-1, coord.pos, r, sys.stdout)
        except:
            yield (r, sys.stderr)


def parse_arguments():
    parser = ArgumentParser(description='vars to hg19')
    parser.add_argument(
        'variants',
        metavar='<rsid or file>',
        nargs='+',
        help='Variants or list of variants'
    )
    args = parser.parse_args()
    args.variants = list(
        itertools.chain.from_iterable(
            (v,) if RSID_REGEX.match(v) else generate_vars_from_file(v)
            for v in args.variants
        )
    )
    return args


def main():
    args = parse_arguments()
    for *r, f in var_to_hg19(*args.variants):
        print('\t'.join(r), file=f)




# Execute ======================================================================

if __name__ == '__main__':
    main()
