#===============================================================================
# clean_bed12.py
#===============================================================================

"""Generate a 'clean' bed12 file from a 'full' file by removing non-chromosome
sequences"""

from argparse import ArgumentParser
from itertools import chain
import gzip

def parse_arguments():
    parser = ArgumentParser(
        description='Generate a "clean" bed12 file from a "full" file by removing non-chromosome sequences')
    parser.add_argument('bed')
    parser.add_argument('output')
    parser.add_argument('--mouse', action='store_true')
    return parser.parse_args()


def generate_rows(f_in, chromosomes):
    for line in f_in:
        chrom, *_ = line.split()
        if chrom in chromosomes:
            yield line


def main():
    args = parse_arguments()
    chromosomes = {f'chr{x}' for x in chain(range(1, 20 if args.mouse else 23), 'X', 'Y')}
    with gzip.open(args.bed, 'rt') as f_in, gzip.open(args.output, 'w') as f_out:
        f_out.write(''.join(generate_rows(f_in, chromosomes)).encode())


if __name__ == '__main__':
    main()
