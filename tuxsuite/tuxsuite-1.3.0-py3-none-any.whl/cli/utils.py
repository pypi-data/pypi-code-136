# -*- coding: utf-8 -*-

import os
import sys
import tuxsuite.download
import tuxsuite.cli.colors as colors

from itertools import chain
from tuxsuite.cli.requests import get
from urllib.parse import urlparse
from tuxsuite.utils import (
    ResultState,
    result_states,
)


LIMIT = 50


def error(msg):
    sys.stderr.write(f"Error: {msg}\n")
    sys.exit(1)


def datediff(one, two):
    if one is None:
        return two

    if one == two:
        return f"{colors.white}{two}{colors.reset}"

    index = 0
    for (o, t) in zip(one, two):
        if o != t:
            break
        index += 1

    return f"{colors.white}{two[0:index]}{colors.reset}{two[index:]}"


def fetch_next(cmd_cls, cfg, url, next_token, limit):
    ret = get(cfg, url, params={"start": next_token})
    cmd_name = url.split("/")[-1]
    next_token = ret.json()["next"]
    res = [cmd_cls.new(**r) for r in ret.json()["results"][:limit]]
    if next_token:
        input(f"\nPress [ENTER] to see next list of {cmd_name}, or Ctrl-C to quit:\n")
    else:
        sys.exit(0)
    return (res, next_token)


def key_value(s):
    if s.count("=") != 1:
        error(f"Key Value pair not valid: {s}")
    parts = s.split("=")
    return (parts[0], "=".join(parts[1:]))


def file_or_url(path):
    """Validate if path is a file/directory or an URL and check its existence"""
    if urlparse(path).scheme in ["http", "https"]:
        return path
    elif os.path.exists(path):
        return path
    error(f"{path} does not exist or invalid")


def wait_for_object(build_object):
    result = True
    for state in build_object.watch():
        print_state(state)
        if state.status in ["error", "fail"] or state.state == "error" and state.final:
            result = False
    return result


def print_state(state, prefix=""):
    msg = f"{prefix}{state.icon} {state.message}: " + str(state.build)
    if state.status == "fail" or state.state == "error" or state.warnings:
        print(msg)  # warning(msg)
    else:
        print(msg)  # info(msg)


def format_result(result_json, tuxapi_url=None, prefix=""):
    state = result_states.get(result_json["state"], None)
    result = result_json["result"]
    result_msg = get_result_msg(result_json, tuxapi_url)
    if state is None:
        errors = 0
        warnings = 0

        if result == "pass":
            warnings = result_json.get("warnings_count", 0)
            if warnings == 0:
                icon = "🎉"
                message = "Pass"
                cli_color = "green"
            else:
                icon = "👾"
                cli_color = "yellow"
                if warnings == 1:
                    message = "Pass (1 warning)"
                else:
                    message = "Pass ({} warnings)".format(warnings)
        elif result == "fail":
            icon = "👹"
            cli_color = "bright_red"
            errors = result_json.get("errors_count", 0)
            if errors == 1:
                message = "Fail (1 error)"
            else:
                message = "Fail ({} errors)".format(errors)
            if "tests" in result_json:
                errors = [
                    name
                    for name in result_json["results"]
                    if result_json["results"][name] == "fail"
                ]
                message = "Fail ({})".format(", ".join(errors))
                errors = len(errors)
        else:
            icon = "🔧"
            cli_color = "bright_red"
            message = result_json.get("status_message", "error")
        state = ResultState(
            state=state,
            status=result_json["state"],
            final=True,
            message=message,
            icon=icon,
            cli_color=cli_color,
            warnings=warnings,
            errors=errors,
        )
    msg = prefix + f"{state.icon} {state.message}: " + result_msg
    if result == "fail" or result == "error":
        print(msg)  # warning(msg)
    else:
        print(msg)  # info(msg)


def get_result_msg(result_json, tuxapi_url):
    result_msg = ""
    if "build_name" in result_json:
        if (
            result_json.get("target_arch")
            and result_json.get("kconfig")
            and result_json.get("toolchain")
        ):
            result_msg = (
                f"{result_json['target_arch']} "
                f"({','.join(result_json['kconfig'])}) "
                f"with {result_json['toolchain']} @ {tuxapi_url}"
            )
    elif "sources" in result_json:
        if (
            result_json["sources"].get("repo")
            or result_json["sources"].get("git_trees")
        ) and (
            result_json.get("container")
            and result_json.get("machine")
            and result_json.get("targets")
        ):
            result_msg = (
                f"with container: {result_json['container']}, "
                f"machine: {result_json['machine']} and "
                f"targets: {result_json['targets']}  @ {tuxapi_url}"
            )
        elif result_json["sources"].get("kas") and result_json.get("container"):
            result_msg = (
                f"with container: {result_json['container']}, "
                f"kas: {result_json['sources']['kas']} @ {tuxapi_url}"
            )

    elif "tests" in result_json:
        result_msg = (
            f"[{','.join(result_json['tests'])}] "
            f"{result_json['device']} @ {tuxapi_url}"
        )
    return result_msg


def show_log(build, download, output_dir):
    if not build.warnings_count and not build.errors_count:
        return
    print("📄 Logs for {}:".format(build), file=sys.stderr)
    sys.stderr.flush()
    if download:
        for line in open(os.path.join(output_dir, build.uid, "build.log")):
            print(line.strip(), file=sys.stderr)
    else:
        tuxsuite.download.download_file(
            os.path.join(build.status["download_url"], "build.log"), sys.stderr.buffer
        )


def format_build(build, icon, color, msg):
    prefix = build.uid + " " + f"{icon} {msg}"
    builds = ""
    # key: string, value: list ( list can't be empty)
    build_type_map = {
        "Build": ["toolchain", "target_arch"],
        "Bitbake": ["container", "machine", "targets"],
    }
    # respective build type classnames for kernel or bake builds
    build_type = build.__class__.__name__
    if build_type == "Bitbake":
        build = build.build_definition

    if build_type in build_type_map:
        for config in build_type_map[build_type]:
            if config in build.__dict__:
                builds += " " + config + ": " + str(getattr(build, config))

    return (prefix + " with" + builds) if builds else prefix


def format_plan_result(build, tests):
    fail = False
    if build.status["result"] == "pass":
        if build.status["warnings_count"] == 0:
            icon = "🎉"
            message = "Pass"
            cli_color = "green"
        else:
            icon = "👾"
            cli_color = "yellow"
            if build.status["warnings_count"] == 1:
                message = "Pass (1 warning)"
            else:
                message = "Pass ({} warnings)".format(build.status["warnings_count"])
    elif build.status["result"] == "fail":
        fail = False
        icon = "👹"
        cli_color = "bright_red"
        if build.status["errors_count"] == 1:
            message = "Fail (1 error)"
        else:
            message = "Fail ({} errors)".format(build.status["errors_count"])
    elif build.status["result"] == "error":
        fail = False
        icon = "🔧"
        cli_color = "bright_red"
        message = build.status["status_message"]
    else:
        raise NotImplementedError()

    builds = format_build(build, icon, cli_color, message)

    tests_str = ""
    tests_pass = sorted(
        set(
            chain.from_iterable(
                [t.tests for t in tests if t.status["result"] == "pass"]
            )
        )
    )
    tests_fail = sorted(
        set(
            chain.from_iterable(
                [t.tests for t in tests if t.status["result"] == "fail"]
            )
        )
    )
    tests_error = sorted(
        set(
            chain.from_iterable(
                [t.tests for t in tests if t.status["result"] == "error"]
            )
        )
    )

    if tests_pass:
        tests_str += " 🎉 " + f"Pass: {','.join(tests_pass)}"
    if tests_fail:
        tests_str += " 👹 " + f"Fail: {','.join(tests_fail)}"
    if tests_error:
        tests_str += " 🔧 " + f"Error: {','.join(tests_error)}"

    if fail or tests_fail or tests_error:
        print(builds + tests_str)
    else:
        print(builds + tests_str)
