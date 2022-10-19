from pathlib import Path
from azureml.pipeline.steps import PythonScriptStep
from azureml.core.runconfig import RunConfiguration

def save_step(
    compute_target,
    environment,
    img_dir,
    save_datastore_name,
    path_on_datastore,
    chunk_index,
    name="Save"
):
    """
    This step will save images to a DataStore in a specified Dataset,
    creating it if it doesn't exist.

    Args:
        workspace: The current workspace
        compute_target: The compute target to run the step on
        environment: The environment in which to run the script
        img_dir: Reference to the directory containing the raw images
        target_dataset_name: The name of the target dataset
        save_datastore_name: The name of the Datastore to save data on
        path_on_datastore: Path on the datastore
        name: Action name of the node

    Returns:
        The step dictionary
    """

    # Create the run configuration
    run_config = RunConfiguration()
    # Assign the cluster to the run configuration
    run_config.target = compute_target
    # Assign the environment to the run configuration
    run_config.environment = environment
    print("Run configuration created for the images saving step")

    # Step 2, run the data saving script
    step = PythonScriptStep(
        script_name="save.py",
        name=name,
        arguments=[
            "--img_dir",
            img_dir,
            "--chunk_index",
            chunk_index,
            "--save_datastore_name",
            save_datastore_name,
            "--save_datastore_path",
            path_on_datastore,

        ],
        inputs=[img_dir],
        compute_target=compute_target,
        runconfig=run_config,
        source_directory=Path(__file__).resolve().parent,
        allow_reuse=True,
    )

    return step
