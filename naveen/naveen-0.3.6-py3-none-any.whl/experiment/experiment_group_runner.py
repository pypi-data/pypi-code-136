import json
import os
import sys
import time
from pathlib import Path
from typing import List

from naveen.experiment.config.experiment_group_parser import (  # noqa: E501
    ExperimentGroupParser,
)
from naveen.experiment.experiment_runner import (  # type: ignore # noqa: E501
    ExperimentRunner,
)


class ExperimentGroupRunner(object):
    def __init__(
        self, config_path: str, group_directory=None  # type: ignore
    ) -> None:  # type: ignore
        assert config_path.endswith("yaml") or config_path.endswith(
            "yml"
        ), "Experiment group config must be yaml"
        self.group_config_path = config_path
        self.group_config = ExperimentGroupParser(
            group_config_filename=self.group_config_path
        )
        self.experiment_configs = self.group_config.parse_experiment_configs()
        group_name = self.group_config.get_group_name()
        if group_directory is None:
            self.group_directory = group_name + str(int(time.time()))
        else:
            self.group_directory = group_directory

    def get_path_to_results(self, outputdir: str) -> str:
        path_to_results = os.path.join(outputdir, self.group_directory)
        return path_to_results

    def prepare_path_to_results(self, path_to_results: str) -> None:
        Path(path_to_results).mkdir(parents=True, exist_ok=True)
        # write group config to root directory
        os.system("cp {} {}".format(self.group_config_path, path_to_results))

    def _read_reshaped(self, path_to_reshaped: Path) -> List[dict]:
        experiments = []
        try:
            for child in path_to_reshaped.iterdir():
                if child.is_dir():
                    with open((child / "config.json").as_posix(), "r") as inf:
                        config = json.load(inf)
                        config["path"] = (child / "config.json").as_posix()
                    with open((child / "reshaped.json").as_posix(), "r") as inf:
                        results = json.load(inf)
                    config["results"] = results
                experiments.append(config)
        except FileNotFoundError:
            print("[*] Could not find reshaped.json or config.json")
            print(
                "- If you use these conventional names naveen can automatically make a json blob of your results"  # noqa:E501
            )
        finally:
            return experiments

    def _post_process_reshaped_files(self, outputdir: str) -> None:

        path_to_reshaped: Path = Path(outputdir, self.group_directory)

        path_to_group_results = Path(
            outputdir, self.group_directory, "reshaped.json"
        )

        experiments = self._read_reshaped(path_to_reshaped=path_to_reshaped)
        with open(path_to_group_results.as_posix(), "w") as of:
            of.write(json.dumps(experiments))

    def run(self, outputdir: str, package_name: str) -> None:

        path_to_results = self.get_path_to_results(outputdir)
        self.prepare_path_to_results(path_to_results=path_to_results)

        for ex_no, experiment_config in enumerate(self.experiment_configs):
            path_to_result = os.path.join(
                outputdir, self.group_directory, str(ex_no)
            )
            runner = ExperimentRunner(
                experiment_config,
                package_name=package_name,
                output_directory=path_to_result,
            )
            runner.run()

        self._post_process_reshaped_files(outputdir=outputdir)


if __name__ == "__main__":
    runner = ExperimentGroupRunner("config/experiment_groups/demo.yaml")
    package_name = "naveen"
    sys.path.append(package_name)
    runner.run(outputdir="tmp", package_name=package_name)
    # rm -rf tmp/demogroup
