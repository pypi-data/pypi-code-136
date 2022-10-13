import os


def group_sls_data_by_resource_type(hub, sls_data_with_keys, output_files_directory):
    grouped_sls_data = {}
    for idem_resource_key, idem_resource_state in sls_data_with_keys.items():
        for key in list(idem_resource_state):
            if "." in key:
                comps = key.split(".")
                resource_type = ".".join(comps[1:-1])
                if "." in resource_type:
                    resource_type = resource_type.replace(".", "_")
                key_name = os.path.join(
                    os.path.abspath(output_files_directory), "sls", str(resource_type)
                )
                if key_name not in grouped_sls_data:
                    grouped_sls_data[key_name] = {}
                grouped_sls_data[key_name][idem_resource_key] = idem_resource_state

    return grouped_sls_data
