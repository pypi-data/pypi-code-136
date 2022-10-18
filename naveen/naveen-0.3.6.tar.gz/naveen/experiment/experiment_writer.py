import json
import os
import time
from typing import List

import pandas as pd  # type: ignore

from naveen.experiment.config.abstract_config import (  # type: ignore # noqa: E501
    AbstractConfig,
)
from naveen.logger import get_logger


class ExperimentWriter(object):
    def __init__(
        self,
        config: AbstractConfig,
        output_directory: str = None,  # type: ignore
    ) -> None:
        self.config = config
        if output_directory is None:
            output_directory = "results/{}".format(int(time.time()))

            self.output_directory = output_directory
        else:
            self.output_directory = output_directory

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        logger = get_logger()

        logger.info(
            "[*] Writing experiment to {}".format(self.output_directory)
        )

    def write_results(self, results: List[dict]) -> None:
        df = pd.DataFrame(results)

        outpath = os.path.join(self.output_directory, self.config.name + ".csv")
        df.to_csv(outpath, index=False)
        outconfigpath = os.path.join(self.output_directory, "config.json")
        with open(outconfigpath, "w") as of:
            of.write(self.config.to_json())
