#===============================================================================
# download.py
#===============================================================================

# Imports ======================================================================

from argparse import ArgumentParser
from urllib.request import urlopen
from shutil import copyfileobj

from picardtools.env import JAR



# Constants ====================================================================

PICARD_JAR_URL = 'https://github.com/broadinstitute/picard/releases/download/2.20.3/picard.jar'




# Functions ====================================================================

def parse_arguments():
    parser = ArgumentParser(description='download picard.jar')
    parser.add_argument(
        '--quiet',
        action='store_true',
        help='suppress status updates'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    if not args.quiet:
        print(f'downloading picard.jar from {PICARD_JAR_URL} to {JAR}')
    with urlopen(PICARD_JAR_URL) as (
        response
    ), open(JAR, 'wb') as (
        f
    ):
        copyfileobj(response, f)
    if not args.quiet:
        print('download complete')
