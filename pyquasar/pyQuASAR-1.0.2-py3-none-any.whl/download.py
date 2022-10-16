#===============================================================================
# download.py
#===============================================================================

# Imports ======================================================================

import gzip
import os
import os.path

from argparse import ArgumentParser
from git import Git
from urllib.request import urlopen
from shutil import copyfileobj

from pyQuASAR.env import DIR, SNPS_BED_PATH




# Constants ====================================================================

QUASAR_GITHUB_REPO = 'https://github.com/piquelab/QuASAR.git'
SNP_FILE_URL = (
    'http://genome.grid.wayne.edu/centisnps/files/1KG_SNPs_filt.bed.gz'
)




# Functions ====================================================================

def download(
    quasar_dir: str = DIR,
    snps_bed_path: str = SNPS_BED_PATH,
    quiet: bool = False
):
    if not quiet:
        print(
            f"Cloning QuASAR repository to {os.path.join(quasar_dir, 'QuASAR')}"
        )
    Git(quasar_dir).clone(QUASAR_GITHUB_REPO)

    if not quiet:
        print(f'Downloading SNP data to {snps_bed_path}.gz')
    with urlopen(SNP_FILE_URL) as (
        response
    ), open(f'{snps_bed_path}.gz', 'wb') as (
        f
    ):
        copyfileobj(response, f)
    
    if not quiet:
        print(f'Decompressing SNP data to {snps_bed_path}')
    with gzip.open(f'{snps_bed_path}.gz', 'rb') as f_comp:
        with open(snps_bed_path, 'wb') as f_decomp:
            copyfileobj(f_comp, f_decomp)
    os.remove(f'{snps_bed_path}.gz')


def parse_arguments():
    parser = ArgumentParser(
        description='download components for a QuASAR pipeline'
    )
    parser.add_argument(
        '--QuASAR-dir',
        metavar='<path/to/dir/>',
        default=DIR,
        help=f'directory in which to download QuASAR data [{DIR}]'
    )
    parser.add_argument(
        '--snps-file',
        metavar='<dest/for/snps.bed>',
        default=SNPS_BED_PATH,
        help=(
            'destination for downloaded SNPs file in BED format '
            f'[{SNPS_BED_PATH}]'
        )
    )
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='suppress status updates'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    download(
        quasar_dir=args.QuASAR_dir,
        snps_bed_path=args.snps_file,
        quiet=args.quiet
    )
