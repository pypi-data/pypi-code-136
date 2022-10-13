import copy


def generate(hub, run_name, idem_resource_id_map, sls_file_data):
    # we process only sls_files and some sls files needs to be ignored

    sls_original_data = copy.deepcopy(sls_file_data)
    if sls_file_data:
        sls_file_data = hub[run_name].generator.argument_binder.default.arg_bind(
            sls_file_data, idem_resource_id_map
        )
        sls_file_data = hub[run_name].generator.parameterizer.default.parameterize(
            sls_file_data
        )
        # add comments
        jinja_dump_data = hub.idem_codegen.generator.jinja.init.execute(
            run_name, sls_file_data, sls_original_data
        )
        return jinja_dump_data


def run(hub, run_name: str, sls_files_directory: str):
    """
    :param hub:
    :param run_name: The state run name
    :param sls_files_directory:
    """

    # if hub.test:
    #     output_dir_path = f"{hub.test.idem_codegen.current_path}/output"
    # else:
    #     output_dir_path = hub.OPT.idem_codegen.output_directory_path

    if not sls_files_directory:
        sls_files_directory = hub.OPT.idem_codegen.get("output_directory_path")

    if "SLS_DATA_WITH_KEYS_ORIGINAL" in hub[run_name].RUNS:
        sls_data = hub[run_name].RUNS["SLS_DATA_WITH_KEYS_ORIGINAL"]
    else:
        sls_data = hub.idem_codegen.tool.utils.get_sls_data_from_directory(
            sls_files_directory
        )
    idem_resource_id_map = hub.idem_codegen.exec.generator.generate.resource_id_map(
        sls_data
    )

    # recursively loop through the given sls files that were grouped in group phase
    # This utility function will iterate recursively from root directory
    sls_data_grouped = hub[run_name].RUNS["SLS_DATA_GROUPED"]
    # generate resource_ids, init and delete files.
    hub[run_name].generator.files.default.create(
        None, sls_files_directory, sls_data_grouped
    )

    sls_data_with_arg_bind_and_parameterization = {}
    for sls_file_path, sls_file_data in sls_data_grouped.items():
        sls_data_with_arg_bind_and_parameterization[
            sls_file_path
        ] = hub.idem_codegen.generator.init.generate(
            run_name, idem_resource_id_map, copy.deepcopy(sls_file_data)
        )

    hub.idem_codegen.tool.utils.dump_jinja_data_to_multiple_files(
        sls_data_with_arg_bind_and_parameterization, sls_files_directory
    )

    # hub.idem_codegen.tool.utils.recursively_iterate_sls_files_directory(
    #     sls_files_directory,
    #     hub.idem_codegen.generator.init.generate,
    #     run_name=run_name,
    #     idem_resource_id_map=idem_resource_id_map,
    # )
