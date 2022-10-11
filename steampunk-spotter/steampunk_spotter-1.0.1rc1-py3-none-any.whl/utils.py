import sys

import pkg_resources


def get_current_cli_version() -> str:
    """
    Retrieve current version of Steampunk Spotter CLI (steampunk-spotter Python package)
    :return: Version string
    """
    try:
        return pkg_resources.get_distribution("steampunk-spotter").version
    except pkg_resources.DistributionNotFound as e:
        print(f"Error when retrieving current steampunk-spotter version: {e}")
        sys.exit(1)
