import argparse

from azureml.core import Dataset, Run
from chunk_files import chunk_files
import shutil

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument("--dataset_name", type=str, help="Dataset name")
parser.add_argument("--dataset_version", type=str, help="Dataset version")
parser.add_argument(
    "--raw_data_dir", type=str, help="Directory to store raw pdf,png,jpeg,tiff"
)
parser.add_argument("--number_chunk", type=int, help="Number of chunk")
parser.add_argument("--chunk_index", type=int, help="Chunk index")

# Get arguments from parser
args = parser.parse_args()
dataset_name = args.dataset_name
dataset_version = args.dataset_version
raw_data_dir = args.raw_data_dir
number_chunk = args.number_chunk
chunk_index = args.chunk_index

# Get the experiment run context
run = Run.get_context()
workspace = run.experiment.workspace

# Get raw data
raw_dataset = Dataset.get_by_name(workspace, dataset_name, version=dataset_version)
print(
    f"Retrieve raw data in dataset: {raw_dataset.name} - version: {raw_dataset.version}"
)

raw_dataset.as_mount("/mnt/ged_cni")

chunk_files(raw_dataset, raw_data_dir, number_chunk, shutil.copy, [chunk_index])


