import argparse
import pickle
import json
import sys
import os
import stat
import shutil
import tarfile
import logging
import importlib
import pandas as pd
from io import BytesIO

# logging.basicConfig(level=logging.INFO)
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def copytree(src, dst, symlinks=False, ignore=None):
    if not os.path.exists(dst):
        os.makedirs(dst)
        shutil.copystat(src, dst)
    lst = os.listdir(src)
    if ignore:
        excl = ignore(src, lst)
        lst = [x for x in lst if x not in excl]
    for item in lst:
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if symlinks and os.path.islink(s):
            if os.path.lexists(d):
                os.remove(d)
            os.symlink(os.readlink(s), d)
            try:
                st = os.lstat(s)
                mode = stat.S_IMODE(st.st_mode)
                os.lchmod(d, mode)
            except:
                pass  # lchmod not available
        elif os.path.isdir(s):
            copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)


def copy_local_file(source, file):
    if isinstance(source, str):
        if os.path.exists(source):
            dest = os.path.dirname(file)
            if os.path.isdir(source):
                copytree(source, dest)
            elif os.path.isfile(source):
                shutil.copy(source, dest)

            with open(f"{file}.data", "w") as f:
                json.dump({"value": source}, f)
            return True
    return False


def save_file(data, file):
    if not copy_local_file(data, file):
        if isinstance(data, pd.DataFrame):
            data.to_parquet(f"{file}.parquet.gzip", compression="gzip")
        else:
            with open(f"{file}.pkl", "wb") as f:
                pickle.dump(data, f)


def load_file(file):
    def load(filename, f):
        basename = os.path.basename(filename)
        if basename.endswith(".csv"):
            return pd.read_csv(BytesIO(f.read()))
        elif basename.endswith(".csv.gzip") or basename.endswith(".csv.gz"):
            return pd.read_csv(BytesIO(f.read()), compression="gzip")
        elif basename.endswith(".json"):
            return json.load(f)
        elif (
            basename.endswith(".parquet")
            or basename.endswith(".parquet.gzip")
            or basename.endswith(".parquet.gz")
        ):
            return pd.read_parquet(BytesIO(f.read()))
        else:
            return pickle.load(f)

    if os.path.basename(file).endswith(".tar.gz"):
        with tarfile.open(file, "r:gz") as tar:
            filename = tar.getnames()[0]
            f = tar.extractfile(filename)
            return load(filename, f)
    else:
        with open(file, "rb") as f:
            return load(file, f)


def get_first_file_name(path):
    return os.listdir(path)[0]


def parse_unknown_args(args):
    arguments = iter(args)
    return {
        arg[0].replace("--", "").replace("-", "_"): arg[1]
        for arg in zip(arguments, arguments)
    }


def extract(dic, keys):
    attrs = {k: getattr(dic, k) for k in dir(dic) if k in keys}
    self = {}
    for attr in attrs:
        setattr(self, attr, attrs[attr])
    return self


if __name__ == "__main__":
    config = load_file(os.path.join(os.environ["SM_CHANNEL_CONFIG"], "config.pkl"))
    logger.info(f"config: {config}")

    # Parse command line arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--output-data-dir", type=str, default=os.environ.get("SM_OUTPUT_DATA_DIR")
    )
    parser.add_argument("--model-dir", type=str, default=os.environ.get("SM_MODEL_DIR"))
    parser.add_argument("--config", type=str, default=os.environ["SM_CHANNEL_CONFIG"])
    parser.add_argument(
        "--code", type=str, default=os.environ.get("SM_CHANNEL_CODE", "/opt/ml/code")
    )
    parser.add_argument("--module", type=str)

    for i in range(config["num_inputs"]):
        parser.add_argument(
            f"--input-{i+1}", type=str, default=os.environ[f"SM_CHANNEL_INPUT_{i+1}"]
        )

    args, remaining = parser.parse_known_args()

    logger.info(f"Received arguments {args}")
    logger.info(f"Additional received arguments {remaining}")

    data = [
        load_file(
            os.path.join(
                getattr(args, f"input_{i+1}"),
                get_first_file_name(getattr(args, f"input_{i+1}")),
            )
        )
        for i in range(config["num_inputs"])
    ]

    # Each job could be executed using multiple EC2 instances, and in order to be able to manage what is executed on each instance,
    # SageMaker provides us the following configuration file in which we can find the number of hosts the cluster has, as well as
    # the current host numbuer on which the script is being executed
    resourceconfig_file = "/opt/ml/input/config/resourceconfig.json"
    if os.path.exists(resourceconfig_file):
        with open(resourceconfig_file) as f:
            resourceconfig = json.load(f)

        logger.info(f"hosts:{resourceconfig['hosts']}")
        num_hosts = len(resourceconfig["hosts"])
        current_host = int(resourceconfig["current_host"].split("-")[-1])
        logger.info(f"num hosts: {num_hosts}")
        logger.info(f"current host: {current_host}")
    else:
        num_hosts = 1
        current_host = 1

    # Set some usefull variables and functions as attributes of self object
    # This way we could access or use them on the scripts with the logic that we are going to execute  using SageMaker jobs
    """
    data['args'] = args
    data['remaining_args'] = remaining
    data['extract'] = extract
    data['num_hosts'] = num_hosts
    data['current_host'] = current_host
    """

    # Import Python script provided with the logic to execute
    sys.path.insert(1, "/opt/ml/processing/dependencies")
    sys.path.insert(1, args.code)
    script = importlib.import_module(args.module)

    os.chdir("/opt/ml")
    num_outputs = 0

    remaining = parse_unknown_args(remaining)

    # Cast each argument to original data type
    if "argument_types" in config:
        logger.info(f"data_types = {config['argument_types']}")

        for attr in config["argument_types"]:
            if config["argument_types"][attr] is dict:
                remaining[attr] = json.loads(remaining[attr])
            else:
                remaining[attr] = config["argument_types"][attr](remaining[attr])

    output = getattr(script, args.module)(*tuple(data), **remaining)

    # Check if the code is running in a Training Job
    if "TRAINING_JOB_ARN" in os.environ:
        if isinstance(output, tuple):
            for idx, output in enumerate(output):
                output_file = (
                    f"output_{idx+1}"
                    if num_hosts == 1
                    else f"output_{idx+1}_{current_host}"
                )
                save_file(output, os.path.join(args.model_dir, output_file))
        else:
            output_file = "model" if num_hosts == 1 else f"model_{current_host}"
            save_file(output, os.path.join(args.model_dir, output_file))
    else:
        if isinstance(output, tuple):
            # Save one file per output
            for idx, output in enumerate(output):
                output_file = (
                    f"output_{idx+1}"
                    if num_hosts == 1
                    else f"output_{idx+1}_{current_host}"
                )
                save_file(
                    output, os.path.join(args.model_dir, f"output_{idx+1}", output_file)
                )
        else:
            # Save just one file
            output_file = "output_1" if num_hosts == 1 else f"output_1_{current_host}"
            save_file(output, os.path.join(args.model_dir, "output_1", output_file))
