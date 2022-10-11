import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from twlib.environment import ROOT_DIR

_log = logging.getLogger(__name__)

SOURCE_HOME = "/Users/Q187392"
DEST_HOME = "/Users/tw"
SOURCE_VIMWIKI_PATH = "/Users/Q187392/vimwiki"
DEST_VIMWIKI_PATH = "/Users/tw/vimwiki"


@dataclass
class Link:
    link: Path
    target: Path


def read_bkp_file(path: str) -> Iterable[str]:
    lines = Path(path).read_text().splitlines()
    return lines


# noinspection PyPep8Naming
def extract_link_data(line: str, prefix_to_replace: str = None) -> Link:
    HOME = str(Path.home())
    if prefix_to_replace is not None:
        HOME = prefix_to_replace
    pattern = re.compile(rf"^.*?(?P<source>/\S+) -> (?P<destination>\S+)$")
    # pattern = re.compile(r"^.*?(?=/)(?P<source>/\S+) -> (?P<destination>\S+)$", re.VERBOSE | re.MULTILINE)

    m = re.match(pattern, line)
    return Link(link=Path(m.group("source")), target=Path(m.group("destination")))


def transform_link(link: Link) -> Link:
    relpath = link.link.relative_to(SOURCE_VIMWIKI_PATH)
    source = Path(DEST_VIMWIKI_PATH) / relpath

    destination = (
        source.parent / link.target if not link.target.is_absolute() else link.target
    )
    try:
        destination = Path.home() / destination.relative_to(SOURCE_HOME)
    except ValueError:
        pass
    return Link(source, destination)


def create_link(link: Link) -> None:
    if link.target.exists():
        if not link.link.is_symlink():
            _log.info(f"Creating {link=}")
            link.link.symlink_to(link.target)
    else:
        _log.warning(f"{link.target=} does not exist. No action.")


if __name__ == "__main__":
    log_fmt = (
        r"%(asctime)-15s %(levelname)s %(name)s %(funcName)s:%(lineno)d %(message)s"
    )
    datefmt = "%Y-%m-%d %H:%M:%S"
    logging.basicConfig(format=log_fmt, level=logging.DEBUG, datefmt=datefmt)

    lines = read_bkp_file(f"{ROOT_DIR}/tests/resources/bkp_vimwiki_links.bkp")

    for line in lines:
        link = extract_link_data(line, prefix_to_replace="/Users/Q187392")
        print(link)
        link = transform_link(link)
        print(link)
        # create_link(link)
        # print(link)
