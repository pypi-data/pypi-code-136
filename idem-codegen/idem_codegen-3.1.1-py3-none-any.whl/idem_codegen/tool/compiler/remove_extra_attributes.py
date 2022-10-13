import copy
import inspect
from collections import ChainMap
from typing import Any
from typing import Dict


def remove_extra_attributes_from_sls_data(hub, sls_data_original: Dict[str, Any]):
    sls_data = copy.deepcopy(sls_data_original)
    for item in sls_data:
        resource_attributes = list(sls_data[item].values())[0]
        dict(ChainMap(*resource_attributes))
        resource_type = list(sls_data[item].keys())[0]
        func_obj = get_func(hub, resource_type)
        parameters = list(inspect.signature(func_obj).parameters.values())
        params_names = [params_obj.name for params_obj in parameters]
        resource_attributes_copy = copy.deepcopy(resource_attributes)

        for resource_attribute in resource_attributes_copy:
            resource_attribute_copy = copy.deepcopy(resource_attribute)
            for resource_attribute_key in resource_attribute_copy:
                if resource_attribute_key not in params_names:
                    if len(resource_attribute) > 1:
                        for resource_attribute_key_1 in resource_attribute_copy:
                            if (
                                resource_attribute_key_1 not in params_names
                                and resource_attribute_key_1 in resource_attribute
                            ):
                                resource_attribute.pop(resource_attribute_key_1)
                    else:
                        resource_attributes.remove(resource_attribute)
    return sls_data


def get_func(hub, resource_path):
    """
    Given the function , determine what function
    on the hub that can be run
    """
    func = getattr(hub, "states." + resource_path)
    return func
