#
# Copyright 2022-present Linaro Limited
#
# SPDX-License-Identifier: MIT

import os
import shutil
import subprocess
import json
import logging
import tempfile
from tuxtrigger.exceptions import (
    SquadException,
    TuxtriggerException,
    TuxsuiteException,
)

from urllib.parse import urlparse
from tuxtrigger.request import get_session, requests_post


LOG = logging.getLogger("tuxtrigger")
TIMEOUT = 60

squad_config = {
    "plugins": "linux_log_parser,ltp",
    "wait_notif_timeout": "600",
    "notif_timeout": "28800",
    "force_finish_timeout": "False",
    "metadata_keys": "build-url,git_ref,git_describe,git_repo,kernel_version",
    "user_treshold": "build/*-warnings",
    "data_retention": "0",
}


def tux_console_build(git_repo, git_ref, target_arch, kconfig, toolchain):
    with tempfile.NamedTemporaryFile(suffix=".json") as json_temp:
        build = subprocess.run(
            [
                "tuxsuite",
                "build",
                "--git-repo",
                git_repo,
                "--git-ref",
                git_ref,
                "--target-arch",
                target_arch,
                "--kconfig",
                kconfig,
                "--toolchain",
                toolchain,
                "--json-out",
                json_temp.name,
                "--no-wait",
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if build.returncode != 0:
            LOG.warning(f"*build stdout {build.stdout}")
            LOG.warning(f"*build stderr {build.stderr}")
            raise TuxsuiteException(f"*** Tuxsuite not build repo {build.stderr}")

        LOG.debug(build.stdout)
        json_output = json.load(json_temp)
        LOG.debug(f'\t*** Build UID: {json_output["uid"]}')
        return json_output["uid"]


def tux_console_plan(
    json_data, plan_file, squad_group, squad_project, json_out, fingerprint
) -> int:
    if json_data is None:
        LOG.warning("\t** Not able to submit plan -> json output is None")
        raise TuxtriggerException("*** Not able to submit plan -> json output is None")
    with tempfile.NamedTemporaryFile(suffix=".json") as json_temp:
        plan = subprocess.run(
            [
                "tuxsuite",
                "plan",
                "--git-repo",
                json_data["git_repo"],
                "--git-ref",
                json_data["git_ref"],
                "--name",
                json_data["git_describe"],
                "--no-wait",
                plan_file,
                "--json-out",
                json_temp.name,
            ]
        )
        if plan.returncode != 0:
            LOG.warning(
                f'\t** Submiting Plan for {squad_project}_{json_data["git_describe"]} failed'
            )
            raise TuxsuiteException(
                f'*** Submiting Plan for {squad_project}_{json_data["git_describe"]} failed'
            )
        if json_out:
            try:
                shutil.copy(
                    json_temp.name,
                    json_out / f'{squad_project}_{json_data["git_describe"]}.json',
                )

                LOG.info(
                    f'\t*** Json file for git_describe: {json_data["git_describe"]} saved'
                )
            except TuxtriggerException as exc:
                LOG.warning(
                    f'*** Json file for git_describe: {json_data["git_describe"]} not saved: {str(exc)}'
                )
        LOG.info(f'\t-> Submiting Plan for {json_data["git_describe"]}')
        squad_submit(json_data, squad_group, squad_project, json_temp.name, fingerprint)
        return 0


def build_result(uid):
    if uid is None:
        return None
    build = subprocess.run(
        ["tuxsuite", "build", "get", uid, "--json"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    if build.returncode != 0:
        LOG.warning(f"\t** Build result for UID:{uid} failed")
        raise TuxsuiteException(f"*** Build result for UID:{uid} failed")
    json_output = json.loads(build.stdout)
    LOG.debug(f"\t ** JSON OUTPUT: {json_output}")
    LOG.info(
        f'\t-> Build {json_output["uid"]} state: {json_output["state"]}, result: {json_output["result"]}, git describe: {json_output["git_describe"]}'
    )
    return json_output


def check_squad_project(squad_group, squad_project):
    base_url = os.getenv("SQUAD_HOST")
    session = get_session(retries=10)
    squad_response = session.get(
        url=f"{base_url}/api/projects/?slug={squad_project}&full_name={squad_group}",
        timeout=TIMEOUT,
    )
    if squad_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get project id) {squad_response.status_code}"
        )
        raise SquadException(
            f"SQUAD response error - (get project id) {squad_response.status_code}"
        )
    json_output = json.loads(squad_response.content)
    if json_output["count"] != 0:
        LOG.info(
            f'*Project {squad_project} Exists!, parsing id {json_output["results"][0]["id"]}'
        )
        return json_output["results"][0]["id"]

    LOG.debug(f"*Project {squad_project} is empty or not created in SQUAD")
    LOG.info(f"*Creating Project - {squad_project}")
    squad_create = subprocess.run(
        [
            "squad-client",
            "create-or-update-project",
            "--group",
            squad_group,
            "--slug",
            squad_project,
            "--name",
            squad_project,
            "--is-public",
            "--plugins",
            squad_config["plugins"],
            "--wait-before-notification-timeout",
            squad_config["wait_notif_timeout"],
            "--notification-timeout",
            squad_config["notif_timeout"],
            "--force-finishing-builds-on-timeout",
            squad_config["force_finish_timeout"],
            "--important-metadata-keys",
            squad_config["metadata_keys"],
            "--threshold",
            squad_config["user_treshold"],
            "--data-retention",
            squad_config["data_retention"],
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if squad_create.returncode != 0:
        LOG.warning(f"*build stdout {squad_create.stdout}")
        LOG.warning(f"*build stderr {squad_create.stderr}")
        raise SquadException(
            f"*** squad-client not able to create project {squad_create.stderr}"
        )

    squad_output = squad_create.stdout.split(" ")
    squad_url = urlparse(squad_output[-1])
    project_id = squad_url.path.split("/")
    return project_id[-2]


def squad_submit(json_data, squad_group, squad_project, plan_json, fingerprint):
    if squad_group is None or squad_project is None:
        LOG.warn("** SQUAD config is not available! Unable to process **")
        raise TuxtriggerException(
            "** SQUAD config is not available! Unable to process **"
        )

    headers = {"Auth-Token": os.getenv("SQUAD_TOKEN")}
    url = f'{os.getenv("SQUAD_HOST")}/api/submit/{squad_group}/{squad_project}/{json_data["git_describe"]}/{json_data["git_describe"]}'
    data = {
        "metadata": json.dumps(
            {
                "fingerprint": fingerprint,
                "git_sha": json_data["git_sha"],
            }
        )
    }
    result = requests_post(url=url, headers=headers, data=data)
    if not result.ok:
        print(f"Error submitting to qa-reports: {result.reason}: {result.text}")

    squad = subprocess.run(
        [
            "squad-client",
            "submit-tuxsuite",
            "--group",
            squad_group,
            "--project",
            squad_project,
            "--build",
            json_data["git_describe"],
            "--backend",
            "tuxsuite.com",
            "--json",
            plan_json,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if squad.returncode != 0:
        LOG.warning(f"*build stdout {squad.stdout}")
        LOG.warning(f"*build stderr {squad.stderr}")
        raise SquadException(f"*** squad-client not able to pass data {squad.stderr}")

    LOG.debug(squad.stdout)
    LOG.info(f'\t-> Plan submitted to SQUAD git describe: {json_data["git_describe"]}')
    return 0


def squad_metadata_request(squad_project_id, squad_project):
    if squad_project_id is None or squad_project is None:
        LOG.debug(f"SQUAD project {squad_project}")
        LOG.warning("** SQUAD Project is not available!")
        return (None, None)

    base_url = os.getenv("SQUAD_HOST")
    session = get_session(retries=10)

    build_response = session.get(
        url=f"{base_url}/api/projects/{squad_project_id}/builds/?ordering=-datetime",
        timeout=TIMEOUT,
    )
    if build_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get latest build) {build_response.status_code}"
        )
        raise SquadException(
            f"SQUAD response error - (get latest build) {build_response.status_code}"
        )
    build_json = json.loads(build_response.content)
    if build_json["count"] == 0:
        LOG.warning("**git sha not available in SQUAD metadata")
        return ("", "")

    lastest_version_url = build_json["results"][0]["metadata"]

    metadata_response = session.get(url=lastest_version_url, timeout=TIMEOUT)
    if metadata_response.status_code != 200:
        LOG.warning(
            f"*SQUAD response error - (get build metadata) {metadata_response.status_code}"
        )
        raise SquadException(
            f"SQUAD response error - (get build metadata) {metadata_response.status_code}"
        )
    metadata_json = json.loads(metadata_response.content)
    if "git_sha" not in metadata_json.keys():
        LOG.warning("**git sha not available in SQUAD metadata")
        return ("", "")
    git_sha = metadata_json["git_sha"]
    fingerprint = metadata_json["fingerprint"]
    LOG.debug(f"git sha found - {git_sha}")
    LOG.debug(f"fingerprint found - {fingerprint}")
    return fingerprint, git_sha


def compare_squad_sha(squad_project_id, squad_project, current_sha_value) -> bool:
    if squad_project_id is None or squad_project is None:
        LOG.warning("\t** Previous SHA from SQUAD is not available")
        return True
    previous_sha_from_squad = squad_metadata_request(squad_project_id, squad_project)[1]
    if previous_sha_from_squad != current_sha_value:
        LOG.info(
            f"\t-> sha: {current_sha_value} vs \
        previous sha {previous_sha_from_squad}"
        )
        return True
    LOG.info(f"\t-> sha: {current_sha_value}")
    LOG.info("\t-> no changes")
    return False
