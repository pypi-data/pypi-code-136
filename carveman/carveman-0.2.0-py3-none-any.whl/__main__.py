
import os
import sys
import argparse

from hash_calc.HashCalc import HashCalc

from carveman.Controller import Controller
from carveman.carver.ImageCarver import ImageCarver
from carveman.carver.PDFCarver import PDFCarver

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to carving source (dd, raw)")
    parser.add_argument("--outdir", "-d", type=str, default="carveman-result", help="The default directory to save carved files")
    args = parser.parse_args()

    if(not os.path.isdir(args.outdir)):
        os.mkdir(args.outdir)

    c = Controller()
    hash = HashCalc(args.path)

    c.printHeader(args.path, args.outdir, hash)

    print("")
    print("--> Carving started")
    print("")

    with open(args.path, "rb") as f:
        data = f.read()
        imageCarver = ImageCarver(args.outdir)
        imageCarver.carve(data)
        pdfCarver = PDFCarver(args.outdir)
        pdfCarver.carve(data)

        
    print("")
    print("--> Carving finished")

    c.printExecutionTime()


if __name__ == "__main__":
    sys.exit(main())