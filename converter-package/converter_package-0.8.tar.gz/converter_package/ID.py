import time


def generate_k3s_pod_name(appinstanceinfo, component_name, minicloud_id):
    running_component_id = time.time() * 1000
    k3s_pod_name = appinstanceinfo + "." + component_name + "." + str(running_component_id) + "." + minicloud_id
    return k3s_pod_name


def genenerate_k3s_namespace(application_name, application_version, application_id):
    k3s_namespace = "accordion."+application_name + "." + application_version + "." + application_id
    return k3s_namespace
