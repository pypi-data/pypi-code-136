import csv
import gzip
from typing import Dict

from ._phenomizer import TermPair


def read_ic_mica_data(fpath: str) -> Dict[TermPair, float]:
    """Read a CSV table with information contents of most informative common ancestors from given `fpath`.

    The file is uncompressed on the fly if the file name ends with `.gz`.
    """
    with _open_file(fpath) as fh:
        comments, header = _parse_header(fh, comment_char='#')
        fieldnames = header.split(",")
        reader = csv.DictReader(fh, fieldnames=fieldnames)

        # Read the lines
        mica = {}
        for row in reader:
            pair = TermPair.of(row['term_a'], row['term_b'])
            mica[pair] = float(row['ic_mica'])

        return mica


def _parse_header(fh, comment_char):
    """Parse header into a list of comments and a header line. As a side effect, the `fh` is set to the position where
    CSV parser can take over and read the records.

    :return: a tuple with a list of comment lines and the header line
    """
    comments = []
    header = None
    for line in fh:
        if line.startswith(comment_char):
            comments.append(line.strip())
        else:
            header = line.strip()
            break
    return comments, header


def _open_file(fpath: str):
    if fpath.endswith(".gz"):
        return gzip.open(fpath, 'rt', newline='')
    else:
        return open(fpath, newline='')
