import argparse
import logging
import os
import sys
import textwrap

import polars as pl

import pgscatalog_utils.config as config
from pgscatalog_utils.match.filter import filter_scores
from pgscatalog_utils.match.label import label_matches
from pgscatalog_utils.match.log import make_logs
from pgscatalog_utils.match.match import get_all_matches
from pgscatalog_utils.match.read import read_target, read_scorefile
from pgscatalog_utils.match.write import write_out, write_log

logger = logging.getLogger(__name__)


def match_variants():
    args = _parse_args()
    config.set_logging_level(args.verbose)

    config.POLARS_MAX_THREADS = args.n_threads
    os.environ['POLARS_MAX_THREADS'] = str(config.POLARS_MAX_THREADS)
    # now the environment variable, parsed argument args.n_threads, and threadpool should agree
    logger.debug(f"Setting POLARS_MAX_THREADS environment variable: {os.getenv('POLARS_MAX_THREADS')}")
    logger.debug(f"Using {config.POLARS_MAX_THREADS} threads to read CSVs")
    logger.debug(f"polars threadpool size: {pl.threadpool_size()}")

    with pl.StringCache():
        scorefile: pl.LazyFrame = read_scorefile(path=args.scorefile)
        target_paths = list(set(args.target))
        n_target_files = len(target_paths)
        matches: pl.DataFrame

        if n_target_files == 0:
            logger.critical("No target genomes found, check the path")
            sys.exit(1)

        if n_target_files == 1 and not args.fast:
            low_memory: bool = True
            match_mode: str = 'single'
        elif n_target_files > 1 and not args.fast:
            low_memory: bool = True
            match_mode: str = 'multi'
        elif args.fast:
            low_memory: bool = False
            match_mode: str = 'fast'

        match match_mode:
            case "single":
                logger.debug(f"Match mode: {match_mode}")
                # _fast_match with low_memory = True reads one target in chunks
                matches: pl.LazyFrame = _fast_match(target_paths, scorefile, args, low_memory)
            case "multi":
                logger.debug(f"Match mode: {match_mode}")  # iterate over multiple targets, in chunks
                matches: pl.LazyFrame = _match_multiple_targets(target_paths, scorefile, args, low_memory)
            case "fast":
                logger.debug(f"Match mode: {match_mode}")
                # _fast_match with low_memory = False just read everything into memory for speed
                matches: pl.LazyFrame = _fast_match(target_paths, scorefile, args, low_memory)
            case _:
                logger.critical(f"Invalid match mode: {match_mode}")
                raise Exception

        dataset = args.dataset.replace('_', '-')  # underscores are delimiters in pgs catalog calculator
        valid_matches, filter_summary = filter_scores(scorefile=scorefile, matches=matches, dataset=dataset,
                                                      min_overlap=args.min_overlap)

        if valid_matches.fetch().is_empty():  # this can happen if args.min_overlap = 0
            logger.error("Error: no target variants match any variants in scoring files")
            raise Exception

        big_log, summary_log = make_logs(scorefile, matches, filter_summary, args.dataset)

        write_log(big_log, prefix=dataset)
        summary_log.collect().write_csv(f"{dataset}_summary.csv")
        write_out(valid_matches, args.split, args.outdir, dataset)


def _check_target_chroms(target: pl.LazyFrame) -> None:
    chroms: list[str] = target.select(pl.col("#CHROM").unique()).collect().get_column("#CHROM").to_list()
    if len(chroms) > 1:
        logger.critical(f"Multiple chromosomes detected: {chroms}. Check input data.")
        raise Exception
    else:
        logger.debug("Split target genome contains one chromosome (good)")


def _fast_match(target_paths: list[str], scorefile: pl.LazyFrame,
                args: argparse.Namespace, low_memory: bool) -> pl.LazyFrame:
    # fast match is fast because:
    #   1) all target files are read into memory without batching
    #   2) matching occurs without iterating through chromosomes
    # when low memory is true and n_targets = 1, fast match is the same as "single" match mode
    params: dict[str, bool] = _make_params_dict(args)
    target: pl.LazyFrame = read_target(paths=target_paths, low_memory=low_memory)
    return (get_all_matches(scorefile=scorefile, target=target, low_memory=low_memory)
            .pipe(label_matches, params=params))


def _match_multiple_targets(target_paths: list[str], scorefile: pl.LazyFrame, args: argparse.Namespace,
                            low_memory: bool) -> pl.LazyFrame:
    matches = []
    params: dict[str, bool] = _make_params_dict(args)
    for i, loc_target_current in enumerate(target_paths):
        logger.debug(f'Matching scorefile(s) against target: {loc_target_current}')
        target: pl.LazyFrame = read_target(paths=[loc_target_current], low_memory=low_memory)
        _check_target_chroms(target)
        matches.append(get_all_matches(scorefile=scorefile, target=target, low_memory=low_memory))
    return (pl.concat(matches)
            .pipe(label_matches, params=params))


def _description_text() -> str:
    return textwrap.dedent('''\
    Match variants from a combined scoring file against a set of
    target genomes from the same fileset, and output scoring files
    compatible with the plink2 --score function.
    
    A combined scoring file is the output of the combine_scorefiles
    script. It has the following structure:
    
        | chr_name | chr_position | ... | accession |
        | -------- | ------------ | --- | --------- |
        | 1        | 1            | ... | PGS000802 |
    
    The combined scoring file is in long format, with one row per
    variant for each scoring file (accession). This structure is
    different to the PGS Catalog standard, because the long format
    makes matching faster and simpler.
    
    Target genomes can be in plink1 bim format or plink2 pvar
    format. Variant IDs should be unique so that they can be specified
    in the scoring file as: variant_id|effect_allele|[effect_weight column(s)...] 
    
    Only one set of target genomes should be matched at a time. Don't
    try to match target genomes from different plink filesets. Matching 
    against a set of chromosomes from the same fileset is OK (see --split). 
   ''')


def _epilog_text() -> str:
    return textwrap.dedent('''\
    match_variants will output at least one scoring file in a
    format compatible with the plink2 --score function. This
    output might be split across different files to ensure each
    variant ID, effect allele, and effect type appears only once
    in each file. Output files have the pattern:

        {dataset}_{chromosome}_{effect_type}_{n}.scorefile.

    If multiple chromosomes are combined into a single file (i.e. not
    --split), then {chromosome} is replaced with 'ALL'. Once the
    scorefiles are used to calculate a score with plink2, the .sscore
    files will need to be aggregated to calculate a single polygenic
    score for each dataset, sample, and accession (scoring file). The
    PGS Catalog Calculator does this automatically.
    ''')


def _parse_args(args=None):
    parser = argparse.ArgumentParser(description=_description_text(), epilog=_epilog_text(),
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-d', '--dataset', dest='dataset', required=True,
                        help='<Required> Label for target genomic dataset')
    parser.add_argument('-s', '--scorefiles', dest='scorefile', required=True,
                        help='<Required> Combined scorefile path (output of read_scorefiles.py)')
    parser.add_argument('-t', '--target', dest='target', required=True, nargs='+',
                        help='<Required> A list of paths of target genomic variants (.bim format)')
    parser.add_argument('-f', '--fast', dest='fast', action='store_true',
                        help='<Optional> Enable faster matching at the cost of increased RAM usage')
    parser.add_argument('-n', dest='n_threads', default=1, help='<Optional> n threads for matching', type=int)
    parser.add_argument('--split', dest='split', default=False, action='store_true',
                        help='<Optional> Split scorefile per chromosome?')
    parser.add_argument('--outdir', dest='outdir', required=True,
                        help='<Required> Output directory')
    parser.add_argument('-m', '--min_overlap', dest='min_overlap', required=True,
                        type=float, help='<Required> Minimum proportion of variants to match before error')
    parser.add_argument('--keep_ambiguous', dest='remove_ambiguous', action='store_false',
                        help='''<Optional> Flag to force the program to keep variants with
                        ambiguous alleles, (e.g. A/T and G/C SNPs), which are normally
                        excluded (default: false). In this case the program proceeds
                        assuming that the genotype data is on the same strand as the
                        GWAS whose summary statistics were used to construct the score.
                                ''')
    parser.add_argument('--keep_multiallelic', dest='remove_multiallelic', action='store_false',
                        help='<Optional> Flag to allow matching to multiallelic variants (default: false).')
    parser.add_argument('--ignore_strand_flips', dest='skip_flip', action='store_true',
                        help='''<Optional> Flag to not consider matched variants that may be reported 
                        on the opposite strand.  Default behaviour is to flip/complement unmatched variants and check if
                        they match.''')
    parser.add_argument('--keep_first_match', dest='keep_first_match', action='store_true',
                        help='''<Optional> If multiple match candidates for a variant exist that can't be prioritised,
                         keep the first match candidate (default: drop all candidates)''')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='<Optional> Extra logging information')
    return parser.parse_args(args)


def _make_params_dict(args) -> dict[str, bool]:
    """ Make a dictionary with parameters that control labelling match candidates """
    return {'keep_first_match': args.keep_first_match,
            'remove_ambiguous': args.remove_ambiguous,
            'skip_flip': args.skip_flip,
            'remove_multiallelic': args.remove_multiallelic}


if __name__ == "__main__":
    match_variants()
