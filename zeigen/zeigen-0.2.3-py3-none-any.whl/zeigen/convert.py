"""Convert parquet and tsv."""
import sys
from pathlib import Path
from typing import Optional

import pandas as pd
from loguru import logger

from .common import APP
from .common import ID_FIELD
from .common import SUB_FIELD


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


@APP.command()
def list_columns(parquetfile: str) -> None:
    """Print column names in parquet file."""
    inpath = Path(parquetfile)
    if inpath.suffix != PARQUET_EXT:
        logger.error(f"{parquetfile} does not have {PARQUET_EXT} extension.")
        sys.exit(1)
    if not inpath.exists():
        logger.error(f"{parquetfile} does not exist.")
        sys.exit(1)
    df = pd.read_parquet(inpath)
    for col in df.columns:
        print(col)


@APP.command()
def print_columns(
    parquetfile: str, col_list: list[str], first_n: Optional[int] = 0
) -> None:
    """Print columns in parquet file."""
    inpath = Path(parquetfile)
    if inpath.suffix != PARQUET_EXT:
        logger.error(f"{parquetfile} does not have {PARQUET_EXT} extension.")
        sys.exit(1)
    if not inpath.exists():
        logger.error(f"{parquetfile} does not exist.")
        sys.exit(1)
    df = pd.read_parquet(inpath)
    if first_n > 0:
        df = df.head(first_n)
    for col in col_list:
        if col not in df.columns:
            logger.error(f"No column named '{col}' in file")
            sys.exit(1)
    query_list = [ID_FIELD, SUB_FIELD] + col_list
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)
    pd.set_option("display.max_colwidth", None)
    print(df[query_list])
