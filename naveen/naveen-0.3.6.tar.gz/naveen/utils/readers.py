from typing import Iterator, Tuple
import json
import sys
from tqdm import tqdm
import pathlib
from logging import Logger


def jsonlreader(filename: str, logger: Logger = None) -> Iterator[Tuple[int, dict]]:  # noqa E501
    msg = "You can only use jsonl reader w/ json file"
    assert pathlib.Path(filename).suffix == ".jsonl", msg
    with open(filename, "r") as inf:
        desc_ = "reading {}".format(filename)
        for linenumber, line in tqdm(enumerate(inf), desc=desc_):
            try:
                yield (linenumber, json.loads(line))
            except json.decoder.JSONDecodeError as e:
                msg = "[*] Decode error on line {} of file {}".format(
                    linenumber, filename)
                sys.stderr.write(msg)
                if logger is not None:
                    logger.error(e)


if __name__ == "__main__":

    for linenumber, line in jsonlreader("test/fixtures/data/oren.jsonl"):
        print(line)
