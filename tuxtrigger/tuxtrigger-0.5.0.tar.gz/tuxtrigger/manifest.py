#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import json
import logging
from pathlib import Path
import tempfile
import gzip

from tuxtrigger.request import requests_get
from tuxtrigger.exceptions import TuxtriggerException

LOG = logging.getLogger("tuxtrigger")


def git_manifest_download() -> bytes:
    url = "https://git.kernel.org/manifest.js.gz"
    manifest_request = requests_get(url)

    if manifest_request.status_code != 200:
        LOG.warning(f"*manifest error code {manifest_request.status_code}")
        raise TuxtriggerException(
            f"*** TuxTrigger not able to download manifest {manifest_request.status_code}"
        )

    LOG.debug(f"*manifest response {manifest_request.status_code}")

    with tempfile.TemporaryDirectory() as manifest_temp:
        Path(f"{manifest_temp}/manifest.js.gz").write_bytes(manifest_request.content)

        with gzip.open(f"{manifest_temp}/manifest.js.gz", "rb") as gz_file:
            json_output = gz_file.read()
        LOG.debug(json_output)

    return json_output


def git_repository_fingerprint(json_data, repo_url):
    json_parser = json.loads(json_data)
    if repo_url not in json_parser:
        raise KeyError(f"Tracked Repository does not exist in manifest {repo_url}")
    return json_parser[repo_url]["fingerprint"]


def manifest_changed(repo_url, fingerprint, archive_data) -> bool:
    if archive_data is None:
        LOG.warning("\t*** Data Input is none, not able to compare fingerprint")
        LOG.debug(f"\t-> fingerprint: {fingerprint}")
        return False
    if isinstance(archive_data, dict) and "fingerprint" not in archive_data[repo_url]:
        LOG.warning("\t*** Fingerprint not found in yaml file")
        LOG.debug(f"\t*** Repo name: {repo_url}")
        return False
    if isinstance(archive_data, dict):
        old_fingerprint = archive_data[repo_url]["fingerprint"]
    if isinstance(archive_data, str):
        old_fingerprint = archive_data
    if not fingerprint == old_fingerprint:
        LOG.info(
            f"\t-> fingerprint: {fingerprint} vs \
        previous fingerprint {old_fingerprint}"
        )
        return True
    LOG.info(f"\t-> fingerprint: {fingerprint}")
    LOG.info("\t-> no changes")
    return False
