import statistics
import sys

from ..util import ArgumentParser
from ..loci_util import Loci, interpolate_random_loci
from ..cov_util import (
    parse_window_setting,
    get_windows_bounds,
    get_window_scale,
    get_coverage_at_loci,
    parse_sample_setting,
    parse_average_setting,
    average_coverage)
from ..io import get_signal_reader, get_signal_writer


def main(raw_args):

    info = '''
normalize genome-wide coverage (bigwig)

arguments:
    -t --target ::: bigwig file path to normalize
                    required
    -l --loci ::::: positive loci path to get reference average signal
                    required
    -w --window ::: coverage window as < center/left/right >
                    required (eg: summit/-2000/2001)
    -s --strand ::: consider strand using information in < column >
                    write strand if input is bed
                    strand not considered by default
    -d --default :: replace missing values (nan) by this value
                    write nan to keep missing values as missing
                    0 by default
    -r --random ::: substract background if flag set
                    don't by default
    -o --output ::: output bigwig file path (will be overwritten if existing)
                    required
'''

    if "-h" in raw_args or "--help" in raw_args:
        sys.stderr.write(info.strip() + "\n")
        return
        
    parser = ArgumentParser()
    parser.add_argument("-t", "--target", required=True)
    parser.add_argument("-l", "--loci", required=True)
    parser.add_argument("-w", "--window", required=True)
    parser.add_argument("-s", "--strand", default=None)
    parser.add_argument("-d", "--default", type=float, default=0)
    parser.add_argument("-r", "--random", action="store_true")
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--bin-size", type=int, default=10)
    args = parser.parse_args(raw_args)

    center, left, right = parse_window_setting(args.window)
    row_count, col_count, sample_method = parse_sample_setting("all/all/nearest")
    window_scale = get_window_scale(left, right, args.bin_size, col_count)
    average_method, average_args = parse_average_setting("mean")
    loci = Loci.from_file(args.loci)
    loci.set_types({center: int})
    chr_ids = loci.get_col("chr")
    centers = loci.get_col(center)
    strands = None if args.strand is None else loci.get_col(args.strand)
    starts, ends = get_windows_bounds(centers, left, right, strands)
    values = get_coverage_at_loci(
        args.target, chr_ids, starts, ends,
        bin_size=args.bin_size,
        default_value=args.default,
        strands=strands)
    profile = average_coverage(values, "rows", average_method, *average_args)
    ref_value = max(profile)
    norm_function = lambda value: value / ref_value

    if args.random:
        rnd_chr_ids, rnd_locs = interpolate_random_loci(chr_ids, centers, 400)
        rnd_starts = [loc - 200 for loc in rnd_locs]
        rnd_ends = [loc + 200 for loc in rnd_locs]
        rnd_values = get_coverage_at_loci(
            args.target, rnd_chr_ids, rnd_starts, rnd_ends,
            bin_size=args.bin_size,
            default_value=args.default)
        rnd_profile = average_coverage(rnd_values, "rows", average_method, *average_args)
        rnd_ref_value = statistics.median(rnd_profile)
        rnd_to_ref_value = ref_value - rnd_ref_value
        norm_function = lambda value: (value - rnd_ref_value) / rnd_to_ref_value

    with get_signal_writer("bigwig")(args.output) as writer:
        for entry in get_signal_reader("bigwig")(args.target):
            entry[3] = norm_function(float(entry[3]))
            writer.add_entry(*entry)

