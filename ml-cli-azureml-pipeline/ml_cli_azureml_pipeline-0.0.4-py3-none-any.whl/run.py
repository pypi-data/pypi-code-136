import json
from .environment import (
    load_workspace,
    get_datastore,
    create_cluster,
    create_environment,
)
from .pipelines.train_pipeline import train_pipeline
from azureml.core import Experiment

def run_ml_cli_pipeline(args, config_path, ml_cli_template_path):
    # Build Information (when running from AzureDevOps)
    build_id = args.build_id
    build_tags_string = args.build_tags
    config_aml_path = args.config_aml_path
    skip_train_execution = args.skip_train_execution

    build_tags = {}
    if build_tags_string != "":
        build_tags = json.loads(build_tags_string)

    # #################### LOAD CONFIGURATION #####################

    with open(config_path) as config_file:
        config = json.load(config_file)

    with open(ml_cli_template_path) as mlcli_file:
        mlcli_template = mlcli_file.read()

    # Experiment
    experiment_name = config["experiment_name"]

    # #################### ENVIRONMENT CREATION #####################
    # Load the workspace
    workspace = load_workspace(config_aml_path)

    # Load a datastore
    datastore = get_datastore(workspace, config["datastore_name"])

    # Create or get compute clusters
    cfg_cluster_cpu = config["cluster"]["cluster_cpu"]
    cluster_cpu = create_cluster(
        workspace,
        cluster_name=cfg_cluster_cpu["cluster_name"],
        vm_size=cfg_cluster_cpu["vm_size"],
        max_nodes=cfg_cluster_cpu["max_nodes"],
        vnet_resourcegroup_name=cfg_cluster_cpu["vnet_resourcegroup_name"],
        vnet_name=cfg_cluster_cpu["vnet_name"],
        subnet_name=cfg_cluster_cpu["subnet_name"],
    )
    clusters = [cluster_cpu]

    # Create and register Python environments for the experiment
    cfg_light_env = config["environment"]["light_env"]
    light_env = create_environment(
        workspace,
        cfg_light_env["env_name"],
        cfg_light_env["version"],
        cfg_light_env["conda_dependencies_file"],
    )
    cfg_ml_cli_env = config["environment"]["ml-cli_env"]
    ml_cli_env = create_environment(
        workspace,
        cfg_ml_cli_env["env_name"],
        cfg_ml_cli_env["version"],
        cfg_ml_cli_env["conda_dependencies_file"],
        dockerfile=cfg_ml_cli_env["dockerfile"]
    )
    environments = [light_env, ml_cli_env]

    dataset_dict = config["datasets"]

    # #################### PIPELINE CREATION AND SUBMISSION #####################

    # Create the pipeline
    pipeline = train_pipeline(
        workspace, datastore, clusters, environments, dataset_dict, mlcli_template
    )

    if skip_train_execution is False:
        experiment = Experiment(workspace=workspace, name=experiment_name)

        # Run the pipeline
        pipeline_run = experiment.submit(
            pipeline, regenerate_outputs=False, tags=build_tags
        )
        print("Pipeline submitted for execution.", pipeline_run.id)
    else:
        pipeline.validate()

        published_pipeline = pipeline.publish(
            name=experiment_name,
            description="Model training/retraining pipeline",
            version=build_id,
        )

        build_data = {
            "pipeline_id": published_pipeline.id,
            "experiment_name": experiment_name,
            "model_name": "",
        }

        print(f"Published pipeline name: {published_pipeline.name}")
        print(f"Published pipeline id: {published_pipeline.id}")
        print(f"for build {published_pipeline.version}")
        # Save the Pipeline Info for other AzDO jobs after script is complete
        with open("pipeline_info.json", "w+") as out_file:
            out_file.write(json.dumps(build_data))