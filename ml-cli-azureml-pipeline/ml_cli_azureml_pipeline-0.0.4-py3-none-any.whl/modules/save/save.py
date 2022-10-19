import argparse
from pathlib import Path
from azureml.core import Run, Dataset

from aggregate_output import create_summary
from azureml.core.datastore import Datastore
from azureml.data.datapath import DataPath

# Get parameters
parser = argparse.ArgumentParser()
parser.add_argument(
    '--img_dir', type=str, help='Directory where images to save are stored'
)
parser.add_argument('--save_datastore_name', type=str, help='save datastore name')
parser.add_argument('--save_datastore_path', type=str, help='save datastore path')

parser.add_argument('--save_dataset', type=str, help='save dataset')
parser.add_argument('--chunk_index', type=str, help='index of the current chunk')


# Get arguments from parser
args = parser.parse_args()
img_dir = args.img_dir
# datastore_name = args.datastore_name
chunk_index = args.chunk_index
save_datastore_name = args.save_datastore_name
save_datastore_path = args.save_datastore_path

# Get the experiment run context
run = Run.get_context()
workspace = run.experiment.workspace

# Load data
print("Loading Data...")
data_output_dir_path = Path(img_dir)

summary_filename = "summary_chunk" + str(chunk_index) + ".json"
chunk_name = "chunk" + str(chunk_index)
json_chunk_name = "json" + chunk_name
output_jsons = str(data_output_dir_path / json_chunk_name)
create_summary(output_jsons, str(data_output_dir_path / summary_filename))


dstore = Datastore.get(workspace, save_datastore_name)
dataset = Dataset.File.upload_directory(
    src_dir=str(data_output_dir_path), target=DataPath(dstore, save_datastore_path), pattern="*.json", show_progress=True,
    overwrite=True
)


# End the run
run.complete()
