import os

"""
    Grouping mechanism based on resource types
"""


def segregate(hub, run_name: str):
    if hub.test:
        if hub.test.idem_codegen.unit_test:
            output_dir_path = f"{hub.test.idem_codegen.current_path}/unit_test_output"
            os.makedirs(os.path.dirname(output_dir_path), exist_ok=True)
        else:
            output_dir_path = f"{hub.test.idem_codegen.current_path}/output"
    else:
        output_dir_path = hub.OPT.idem_codegen.output_directory_path

    sls_data_with_keys = hub[run_name].RUNS.get("SLS_DATA_WITH_KEYS", {})

    if not sls_data_with_keys:
        hub.log.error("'SLS_DATA_WITH_KEYS' is not present in hub.")
        return

    grouped_sls_data = (
        hub.idem_codegen.tool.group.resource_type.group_sls_data_by_resource_type(
            sls_data_with_keys, os.path.join(output_dir_path, "output")
        )
    )

    hub[run_name].RUNS["SLS_DATA_GROUPED"] = grouped_sls_data
    # hub.idem_codegen.tool.utils.dump_data_to_multiple_files(
    #     grouped_sls_data, os.path.join(output_dir_path, "output", "sls")
    # )
    hub.idem_codegen.tool.group.utils.create_base_directory_structure(
        os.path.join(output_dir_path, "output"), grouped_sls_data
    )
    return output_dir_path
