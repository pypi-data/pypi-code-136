import argparse
from pathlib import Path
import shutil
import sys

from tcsa import welcome, __version__
from .prequisite import create_parser, handle_dicom, handle_single_nifti
from .pipeline import full_pipeline

parser = create_parser()

if len(sys.argv)==1:
    parser.print_usage()
    sys.exit(0)

args = parser.parse_args()

if args.version:
    welcome()
    sys.exit(0)

args.images = args.images.resolve(strict=True) # check if the path exist
args.output = args.output.resolve(strict=False)

if args.dicom:
    handle_dicom(args, verbosity=False)

if args.images.is_file() and not args.dicom:
    handle_single_nifti(args)

def main() -> None:
    """
    Run the full script.
    """
    # welcome()
    full_pipeline(input_path=args.images, output_path=args.output, delete=args.delete, both_sides=args.both_sides)
    shutil.rmtree(str(Path('temp_images').resolve()), ignore_errors=True)