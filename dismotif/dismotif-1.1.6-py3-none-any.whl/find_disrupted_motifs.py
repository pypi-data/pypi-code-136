#!/usr/bin/env python3
#===============================================================================
# find_disrupted_motifs.py
#===============================================================================

"""find disrupted motifs"""




# Imports ======================================================================

import os
import sys
import math

from argparse import ArgumentParser




# Constants ====================================================================

COMBINED_MOTIFS_DIR = os.environ.get('DISMOTIF_COMBINED_MOTIFS')




# Functions ====================================================================

def parse_arguments():
    parser = ArgumentParser(description='find disrupted motifs')
    parser.add_argument('infile', help='input file')
    return parser.parse_args()


def load_motif(motif):
    motif_file = os.path.join(COMBINED_MOTIFS_DIR, f'{motif}.db')
    pwm = {}
    with open(motif_file) as mf:
        ls = mf.read().splitlines()
        for i,l in enumerate(ls):
            n = i+1
            bases = list(map(float, l.split(' ')))
            pwm[n] = {'A':bases[0], 'C':bases[1], 'G':bases[2], 'T':bases[3]} 
    return pwm


def calc_entropy(pwm, vpos):
    entropy = 0
    for freq in pwm[vpos].values():
        if freq > 0:
            entropy += freq * math.log2(freq)
    if entropy < 0:
        entropy *= -1
    return entropy


def generate_disrupted_motifs(fields_iter):
    for fields in fields_iter:
        mstart, mend = int(fields[5]) + 1, int(fields[6]) + 1
        mname = fields[7]
        mstrand = fields[9]
        vpos = int(fields[2])
        pwm = load_motif(mname)
        if mstrand == '+':
            vmpos = vpos - mstart + 1
        elif mstrand == '-':
            vmpos = mend - vpos
        entropy = calc_entropy(pwm, vmpos)
        fields.append(str(entropy))
        yield fields


def main():
    args = parse_arguments()
    with open(args.infile) as f:
        for fields in generate_disrupted_motifs(
            line.rstrip('\n').split('\t') for line in f
        ):
            print('\t'.join(fields))




# Execute ======================================================================

if __name__ == '__main__':
    main()
