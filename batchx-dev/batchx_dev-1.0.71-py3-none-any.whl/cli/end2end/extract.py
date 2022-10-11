"""
Functions to preprocess/extract useful information for MFI and RMI
"""


def get_steps_urls_dict(
    steps_dict: dict, categories: tuple[str] = ("input", "output", "docs")
):
    steps_urls_dict = dict(input=dict(), output=dict(), docs=dict())
    for k, v in steps_dict.items():
        steps_urls_dict["docs"][k.capitalize()] = v.get("urls").get("docs")

        key = "**`{k}`**".format(k=k)
        for category in categories:
            steps_urls_dict[category][key] = v.get("urls").get(category)
    return steps_urls_dict


def bx_coords_and_version(mf, bx_environment: str = "batchx"):
    bx_coords = "{env}@{n}".format(env=bx_environment, n=mf.name)
    return bx_coords, mf.version
