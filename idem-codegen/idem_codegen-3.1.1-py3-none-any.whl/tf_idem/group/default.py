import os

"""
    Default group mechanism for tf_idem to group based on resources available in TF files
"""
__contracts__ = ["group"]


def segregate(hub, run_name: str):
    git_dict = {}
    # Process all the terraform files in the terraform_directory_path.
    input_dir_path = hub.OPT.idem_codegen.terraform_directory_path
    hub[run_name].RUNS["SLS_DATA_GROUPED"] = {}
    if hub.test and hub.test.idem_codegen.unit_test:
        output_dir_path = f"{hub.test.idem_codegen.current_path}/expected_output"
    else:
        output_dir_path = hub.OPT.idem_codegen.output_directory_path

    for file in os.listdir(input_dir_path):
        # TODO: Ignoring subdirectories here. Modify the below if condition to process subdirectories as well.
        if not file.endswith(".tf"):
            continue
        tf_file_data = hub.tf_idem.tool.utils.parse_tf_data(
            os.path.join(input_dir_path, file), None
        )
        # Perform tf to sls conversion for each module
        for module in tf_file_data.get("module", {}):
            module_name = list(module.keys())[0]
            if "git::git@gitlab" in module.get(module_name).get("source"):
                # assuming there will be only files to process and not directories or sub-directories.
                (
                    git_dict["tf_files"],
                    git_dict["git_file_path"],
                    git_dict["project"],
                ) = hub.tf_idem.tool.utils.fetch_gitlab_tf_files(
                    module.get(module_name).get("source"),
                    hub.OPT.idem_codegen.private_token,
                    hub.OPT.idem_codegen.gitlab_link,
                    hub.OPT.idem_codegen.project_branch,
                )
                git_dict["name_of_files_in_module"] = set()
                for tf_file in git_dict["tf_files"]:
                    if not tf_file["name"].endswith(".tf"):
                        continue
                    filepath = git_dict["git_file_path"] + "/" + tf_file["name"]
                    count = filepath.count("/")
                    hub.tf_idem.exec.group.segregate.generate_sls_files_for_tf_files_in_dir(
                        filepath, count, output_dir_path, run_name, git_dict
                    )
            else:
                absolute_path_of_module_source = os.path.abspath(
                    module.get(module_name).get("source")
                )
                count = absolute_path_of_module_source.count("/")
                for root, _, _ in os.walk(absolute_path_of_module_source):
                    hub.tf_idem.exec.group.segregate.generate_sls_files_for_tf_files_in_dir(
                        root, count, output_dir_path, run_name, None
                    )
        # Perform tf to sls conversion of current file
        count = os.path.abspath(input_dir_path).count("/")
        hub.tf_idem.exec.group.segregate.generate_sls_files_for_tf_files_in_dir(
            os.path.abspath(input_dir_path), count, output_dir_path, run_name, None
        )
