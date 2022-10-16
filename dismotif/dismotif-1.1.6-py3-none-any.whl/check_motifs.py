#===============================================================================
# check_motifs.py
#===============================================================================

"""Check motifs"""




# Imports ======================================================================

import itertools
import os
import os.path
import pyhg19
import re
import subprocess

from argparse import ArgumentParser
from pybedtools import BedTool
from tempfile import TemporaryDirectory

from dismotif.var_to_hg19 import generate_vars_from_file, var_to_hg19
from dismotif.find_disrupted_motifs import generate_disrupted_motifs



# Constants ====================================================================

RSID_REGEX = re.compile('rs[1-9][0-9]+$')
MEME_DB = os.environ.get('DISMOTIF_MEME_DB')




# Functions ====================================================================

def add_buffer(feature, bp: int = 15):
    feature.start -= 15
    feature.end += 15
    return feature


def fimo(seqfn, meme_db=MEME_DB, motif=None):
    with subprocess.Popen(
        ('fimo',) + (bool(motif) * ('--motif', motif)) + (
            '--bgfile', '--motif--',
            '--text',
            '--thresh', '1e-4',
            '--max-strand',
            '--parse-genomic-coord',
            '--verbosity', '1',
            meme_db,
            seqfn
        ),
        stdout=subprocess.PIPE
    ) as p:
        return p.communicate()[0].decode()


def parse_fimo_results(fimo_results: str):
    for line in fimo_results.splitlines()[1:]:
        split_line = line.split('\t')
        yield tuple(split_line[i] for i in (2, 3, 4, 0, 7, 5))


def parse_arguments():
    parser = ArgumentParser(description='disrupted motifs')
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


def check_motifs(*variants):
    v = BedTool(
        r for *r, f in var_to_hg19(*variants) if len(r) == 4
    ).each(add_buffer).sequence(fi=pyhg19.PATH)
    motifs = BedTool(parse_fimo_results(fimo(v.seqfn)))
    with TemporaryDirectory() as temp_dir:
        BedTool(
            r for *r, f in var_to_hg19(*variants) if len(r) == 4
        ).saveas(os.path.join(temp_dir, 'variants.bed'))
        motifs.saveas(os.path.join(temp_dir, 'motifs.bed'))
        vars_motifs = BedTool(os.path.join(temp_dir, 'variants.bed')).intersect(
            BedTool(os.path.join(temp_dir, 'motifs.bed')), wa=True, wb=True
        )
        return BedTool(generate_disrupted_motifs(vars_motifs))


def main():
    args = parse_arguments()
    print(check_motifs(*args.variants), end='')
