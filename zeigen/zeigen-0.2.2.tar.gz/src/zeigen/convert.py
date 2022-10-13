"""Convert parquet and tsv."""
import sys
from pathlib import Path

import pandas as pd
from loguru import logger

from .common import APP


PARQUET_EXT = ".parquet"
TSV_EXT = ".tsv"


@APP.command()
def parquet_to_tsv(infile: str) -> None:
    """Convert parquet file to TSV."""
    inpath = Path(infile)
    if inpath.suffix != PARQUET_EXT:
        logger.error(f"{infile} does not have {PARQUET_EXT} extension.")
        sys.exit(1)
    if not inpath.exists():
        logger.error(f"{infile} does not exist.")
        sys.exit(1)
    df = pd.read_parquet(inpath)
    outfile = inpath.stem + TSV_EXT
    df.to_csv(outfile, sep="\t")
    logger.info(f"{len(df)} rows x {len(df.columns)} written" + f" to {outfile}.")
