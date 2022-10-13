import os

import yaml


def create_base_directory_structure(hub, output_dir_path, grouped_sls_data):
    os.makedirs(
        os.path.dirname(f"{output_dir_path}/params/init.sls"),
        exist_ok=True,
    )
    os.makedirs(
        os.path.dirname(f"{output_dir_path}/params/resource_ids.sls"),
        exist_ok=True,
    )
    os.makedirs(
        os.path.dirname(f"{output_dir_path}/params/variables.sls"),
        exist_ok=True,
    )

    with open(f"{output_dir_path}/params/init.sls", "w") as file1:
        yaml.dump(
            {"include": ["resource_ids", "variables"]}, file1, default_flow_style=False
        )
    unique_folders = set()
    file_names_map = {}
    for file_name in grouped_sls_data.keys():
        folder = file_name.split("/")[-2]
        filename = file_name.split("/")[-1]
        unique_folders.add(folder)
        if folder not in file_names_map:
            file_names_map[folder] = ["sls." + filename]
        else:
            file_names_map[folder].append("sls." + filename)

    for unique_folder in unique_folders:
        os.makedirs(
            os.path.dirname(f"{output_dir_path}/{unique_folder}/"),
            exist_ok=True,
        )
        os.makedirs(
            os.path.dirname(f"{output_dir_path}/init.sls"),
            exist_ok=True,
        )
        with open(f"{output_dir_path}/init.sls", "w") as _file:
            yaml.dump(
                {"include": sorted(list(file_names_map[unique_folder]))},
                _file,
                default_flow_style=False,
            )
