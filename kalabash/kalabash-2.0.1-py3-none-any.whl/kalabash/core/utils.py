"""Utility functions."""

from pkg_resources import parse_version

from django.utils.translation import ugettext as _

from kalabash.core.extensions import exts_pool
from kalabash.lib.api_client import KalmonakAPIClient
from . import models


def parse_map_file(path):
    """Parse a postfix map file and return values."""
    content = {}
    with open(path) as fp:
        for line in fp:
            if not line or line.startswith("#"):
                continue
            name, value = line.split("=", 1)
            content[name.strip()] = value.strip()
    return content


def check_for_updates():
    """Check if a new version of Kalabash is available."""
    local_config = models.LocalConfig.objects.first()
    client = KalmonakAPIClient()
    extensions = exts_pool.list_all()
    extensions = [{
        "label": "Kalabash",
        "name": "kalabash",
        "description": _("The core part of Kalabash"),
        "version": client.local_core_version
    }] + extensions
    update_avail = False
    for extension in extensions:
        pkgname = extension["name"].replace("_", "-")
        for api_extension in local_config.api_versions:
            if api_extension["name"] != pkgname:
                continue
            extension["last_version"] = api_extension["version"]
            if (
                parse_version(api_extension["version"]) >
                parse_version(extension["version"])
            ):
                extension["update"] = True
                extension["changelog_url"] = api_extension["url"]
                update_avail = True
                break
    return update_avail, extensions
