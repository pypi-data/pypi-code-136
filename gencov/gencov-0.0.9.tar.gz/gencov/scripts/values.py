from os.path import basename, splitext
import sys

from ..util import arr_to_bin
from ..util import ArgumentParser
from ..loci_util import Loci
from ..cov_util import (
    parse_window_setting,
    get_windows_bounds,
    get_window_scale,
    get_coverage_at_loci,
    parse_sample_setting,
    sample_coverage)
from ..io import read_loci_signal


def main(raw_args):

    info = '''
get coverage values at loci

arguments:
    -l --loci ::::: path to loci files (tsv, csv, bed or excel)
                    required
    -t --targets :: path to coverage files (bigwig or indexed bam)
                    required
    -w --window ::: coverage window as < center/left/right >
                    required (eg: summit/-2000/2001)
    --clean-chr ::: remove non standard chromosomes (mitochondrial, unlocalized
                    and unplaced sequences) using chromosomes ids
    -s --strand ::: consider strand using information in < column >
                    write strand if input is bed
                    strand not considered by default
    -b --bin-size : coverage bin size in base pairs (report one every x values)
                    binning is done before sampling
                    10 by default
    -d --default :: replace missing values (nan) by this value
                    write nan to keep missing values as missing
                    0 by default
    --sample :::::: output size as < row_count/column_count(/method) >
                    with row_count and column_count as all, integer
                    and method as nearest, area
                    all/all/nearest by default
    -o --output ::: output file path (append to file if existing)
                    /dev/stdout by default
    --header :::::: include loci name, coverage name and window scale in output
    --bin-out ::::: output in binary format (incompatible with header)
'''

    if "-h" in raw_args or "--help" in raw_args:
        sys.stderr.write(info.strip() + "\n")
        return
        
    parser = ArgumentParser()
    parser.add_argument("-l", "--loci", nargs="+", required=True)
    parser.add_argument("-t", "--targets", nargs="+", required=True)
    parser.add_argument("-w", "--window", required=True)
    parser.add_argument("--clean-chr", action="store_true")
    parser.add_argument("-s", "--strand", default=None)
    parser.add_argument("-b", "--bin-size", type=int, default=10)
    parser.add_argument("-d", "--default", type=float, default=0)
    parser.add_argument("--sample", default="all/all/nearest")
    parser.add_argument("-o", "--output", default="/dev/stdout")
    parser.add_argument("--header", action="store_true")
    parser.add_argument("--bin-out", action="store_true")
    args = parser.parse_args(raw_args)

    center, left, right = parse_window_setting(args.window)
    row_count, col_count, sample_method = parse_sample_setting()
    window_scale = get_window_scale(left, right, args.bin_size, col_count)
    result = []
    for loci_path in args.loci:
        loci = Loci.from_file(loci_path)
        if args.clean_chr:
            loci.clean_chr()
        loci.set_types({center: int})
        chr_ids = loci.get_col("chr")
        centers = loci.get_col(center)
        strands = None if args.strand is None else loci.get_col(args.strand)
        starts, ends = get_windows_bounds(centers, left, right, strands)
        for target_path in args.targets:
            values = read_loci_signal(
                target_path, chr_ids, starts, ends,
                bin_size=args.bin_size,
                default_value=args.default,
                strands=strands)
            values = sample_coverage(values, row_count, col_count, sample_method)
            result.append([loci_path, target_path, values])

    if args.bin_out and args.header:
        raise ValueError("incompatible options: --header and --bin-out")
    if args.bin_out:
        with open(args.output, "ab") as file:
            for _, _, values in result:
                file.write(arr_to_bin(values))
    else:
        with open(args.output, "a") as file:
            if args.header:
                file.write("loci\ttarget\t" + "\t".join(str(value) for value in window_scale) + "\n")
            for loci_path, target_path, values in result:
                for row in values:
                    if args.header:
                        file.write(splitext(basename(loci_path))[0] + "\t")
                        file.write(splitext(basename(target_path))[0] + "\t")
                    file.write("\t".join(str(value) for value in row) + "\n")

    return result
