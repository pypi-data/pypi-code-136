import argparse
from pathlib import Path
from azureml.core import Run
from ml_cli import run_ml_cli

parser = argparse.ArgumentParser()
parser.add_argument(
    "--raw-data-dir",
    type=str,
    dest="raw_data_dir",
    help="raw data folder",
)
parser.add_argument(
    "--data-output-dir",
    type=str,
    dest="data_output_dir",
    help="data output directory",
)
parser.add_argument(
    "--json-output-dir",
    type=str,
    dest="json_output_dir",
    help="json output directory"
)
parser.add_argument(
    "--chunk-index",
    type=str,
    dest="chunk_index",
    help="index of the current chunk"
)
parser.add_argument(
    "--ml_cli_azureml_pipeline-template",
    type=str,
    dest="mlcli_template",
    help="template configuration of ml-cli"
)


# Get arguments from parser
args, unknown = parser.parse_known_args()
raw_data_dir = args.raw_data_dir
data_output_dir = args.data_output_dir
chunk_index = args.chunk_index
mlcli_template = args.mlcli_template

data_output_dir_path = Path(data_output_dir)
data_output_dir_path.mkdir(exist_ok=True)

# Get the experiment run context
run = Run.get_context()
parent_run_id = run.parent.id

chunk_name = "chunk" + str(chunk_index)
json_chunk_name = "json" + chunk_name
output_jsons = str(data_output_dir_path / json_chunk_name)

run_ml_cli(str(Path(raw_data_dir) / chunk_name), output_jsons, mlcli_template)

run.complete()
