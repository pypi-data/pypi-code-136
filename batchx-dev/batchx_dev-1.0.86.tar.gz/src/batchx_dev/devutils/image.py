from .CTE import DEFAULT_MEMORY_MB, DEFAULT_VCPUS
from .io import load_json


# Rule configuration
def default_rule_parameters(
    name,
    config,
    fallback_timeout_s,
    fallback_vcpus=DEFAULT_VCPUS,
    fallback_memory_mb=DEFAULT_MEMORY_MB,
):
    tool_configuration = config.get("tools", dict())
    configuration = tool_configuration.get(name, dict()).copy()
    resources = configuration.pop("resources", dict())

    parameters = dict(
        name=name,
        configuration=configuration,
        timeout_s=resources.get("timeout", fallback_timeout_s),
        vcpus=resources.get("vcpus", fallback_vcpus),
        memory_mb=resources.get("memory", fallback_memory_mb),
    )
    return parameters


def get_tools(manifest_or_manifest_fp):
    def _get_name(batchx_coords):
        return batchx_coords.split("@")[-1].split(":")[0]

    def _get_canonical_name(batchx_coords):
        image_name = _get_name(batchx_coords)

        n = image_name.replace("/", "-")

        if n.startswith("bioinformatics-"):
            n = n.split("bioinformatics-")[1]

        if n.startswith("pipelines-"):
            n = n.split("pipelines-")[1]

        return n

    if isinstance(manifest_or_manifest_fp, dict):
        # you got the manifest
        manifest = manifest_or_manifest_fp
        return {
            _get_canonical_name(bx_coords): bx_coords
            for bx_coords in manifest.get("pipeline").get("steps")
        }
    else:
        # you got the manifest filepath
        manifest_fp = manifest_or_manifest_fp
        manifest = load_json(manifest_fp)
        return get_tools(manifest)
