import json
import os

import yaml

from idem_codegen.idem_codegen.tool.utils import MyDumperNoBlankLines


def read_json(path):
    _file = open(path)  # Open the json file
    json_data = json.loads(_file.read())  # Read the data from json file
    _file.close()
    return json_data


def get_idem_resource_id(hub, tf_instance, attribute_to_export):
    tf_attributes = (
        tf_instance["attributes_flat"]
        if "attributes_flat" in tf_instance
        else tf_instance["attributes"]
    )
    return (
        tf_attributes[attribute_to_export]
        if attribute_to_export in tf_attributes
        else ""
    )


def init(hub):
    tf_state_file_path = hub.OPT.idem_codegen.tf_state_file_path
    output_file_path = hub.OPT.idem_codegen.output_directory_path
    tf_state_data = read_json(tf_state_file_path)
    resource_ids_map = {}
    attribute_to_export = hub.OPT.idem_codegen.type
    if attribute_to_export:
        for tf_state_resource in tf_state_data["resources"]:
            count = 0
            if tf_state_resource.get("module"):
                module = tf_state_resource.get("module").replace("module.", "")
            else:
                # TODO: Add a better name instead of no-module.
                module = "no-module"
            tf_resource_type = tf_state_resource.get("type")
            if module not in resource_ids_map:
                resource_ids_map[module] = {}
            tf_instances = tf_state_resource.get("instances", [])

            for tf_instance in tf_instances:
                resource_id_value = (
                    ""
                    if tf_resource_type == "aws_security_group_rule"
                    else get_idem_resource_id(hub, tf_instance, attribute_to_export)
                )
                if resource_id_value:
                    if len(tf_instances) > 1:
                        resource_ids_map[module][
                            f"{tf_resource_type}.{tf_state_resource.get('name')}-{count}"
                        ] = resource_id_value
                    else:
                        resource_ids_map[module][
                            f"{tf_resource_type}.{tf_state_resource.get('name')}.{attribute_to_export}"
                        ] = resource_id_value
                    count = count + 1

    for module, module_resource_map in resource_ids_map.items():
        if module_resource_map:
            output_file_name = os.path.join(
                output_file_path, attribute_to_export + "_" + module + ".sls"
            )
            os.makedirs(os.path.dirname(output_file_name), exist_ok=True)
            with open(output_file_name, "w") as file:
                file.truncate(0)
                yaml.dump(module_resource_map, file, Dumper=MyDumperNoBlankLines)
