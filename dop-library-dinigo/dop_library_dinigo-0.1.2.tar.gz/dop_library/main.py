"""
When running several dbt commands it generates an output file called
`run_results.json`. Being able to interact with this file is useful for
observability.
"""
import json
import logging
from pathlib import Path
from typing import Dict, Union

import yaml
from airflow.configuration import conf as airflow_conf
from airflow.hooks.subprocess import SubprocessHook
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from dagfactory import DagFactory


def run_results_to_bq(
    run_results_path: str,
    dest_dataset_id: Union[str, Dict],
    dest_table_id: Union[str, Dict],
    conn_id: str = None,
    project_id: str = None,
):
    """
    Load run_results json file in BigQuery. As a first step is checked if the
    table
    already exists in the schema and if not, it's created.

    To fit BQ schema, the field 'metadata.env' (JSON object) must be serialised
    and 'results.message' converted to string,
    because depending on the task it can be an integer or a string
    """

    # get the json file with a cloud storage hook if the run results schema
    # starts with gs:// and get it from local storage otherwise
    logging.info(f'Getting run results from {run_results_path}')
    if run_results_path.startswith('gs://'):
        with GCSHook().provide_file(object_url=run_results_path) as blob:
            run_results_json = blob.read()
    else:
        with open(run_results_path, 'r') as local_file:
            run_results_json = local_file.read()

    run_results = json.loads(run_results_json)

    # Serialise 'metadata.env' field if it's a dict or remove if it's empty
    logging.info('Formatting run results')
    metadata_env = run_results['metadata'].get('env')
    if isinstance(metadata_env, dict):
        run_results["metadata"]["env"] = json.dumps(metadata_env)
    elif 'env' in run_results['metadata'].keys():
        del run_results["metadata"]["env"]

    # Convert results.message to string if it's an integer
    for item in run_results["results"]:
        item["message"] = str(item["message"])

    logging.info(f'Inserting run results in {dest_table_id}')
    # allows for the default auth method, without conn_id, to work too
    if conn_id is None:
        hook = BigQueryHook()
    else:
        hook = BigQueryHook(gcp_conn_id=conn_id)

    hook.insert_all(
        project_id=project_id,
        dataset_id=dest_dataset_id,
        table_id=dest_table_id,
        rows=[run_results],
        ignore_unknown_values=True,
        fail_on_error=True,
    )


def load_yaml_dags(dags_folder: str = airflow_conf.get("core", "dags_folder")):
    """
    This script tries to load all the YAML DAGs in the DAGs folder recursively
    and ignores those that fail. Ideally you want to be much more restrictive
    with the YAML DAGs you try to load. So create a better filter for the
    yaml files you load if you are going to have mixed config yaml files from
    several tools/modules/functionalities.
    """
    for config_file_path in Path(dags_folder).rglob('*.yaml'):
        with open(config_file_path) as config_file:
            try:
                dag_config = yaml.unsafe_load(config_file)
                DagFactory(config=dag_config).generate_dags(globals())
                logging.info(f'* DAG loaded: {config_file_path}')
            except Exception as err:
                logging.error(f"* Failed to load {config_file_path} — {err}")


def compress_file_callback(source_path: str, compressed_file_path: str):
    """Uploads the dbt test results to GCS"""
    return lambda *_: SubprocessHook().run_command(
        command=['tar', '-czvf', compressed_file_path, source_path],
        cwd=str(Path(source_path).parent.absolute())
    )


def remove_local_file_callback(source_path: str):
    """Removes the local dbt test results"""
    return lambda *_: Path(source_path).unlink()
