"""
Utils that are useful in dev notebooks when building an image.
"""
import json
import pprint
from pathlib import Path

from ..cli.bx_readme import run_bx_readme
from .debug import debug_print
from .run import run_command
from .io import download_resource, save_json, load_json


# datastructs
def get_fs(
    rdp: Path | None = None, tool: str = "biotool", verbose: bool = True
) -> dict:
    # fix root directory
    if rdp is None:
        rdp = Path().absolute().parent

    debug_print("Root directory path", rdp, verbose=verbose)

    # fix other directories
    fs = dict(
        rdp=rdp,
        ddp=rdp / "dev",
        mdp=rdp / "manifest",
        adp=rdp / "dev" / "assets",
        bdp=Path("bx://test/") / tool,
    )

    if fs.get("adp").exists():
        pass
    else:
        print("/assets subdirectory does not exist, making it for you.")
        fs.get("adp").mkdir(parents=True, exist_ok=True)

    # fix filepaths
    fs["mffp"] = fs.get("mdp") / "manifest.json"
    fs["rmfp"] = fs.get("mdp") / "readme.md"
    fs["dockerfile_fp"] = fs.get("rdp") / "Dockerfile"
    fs["dockerdemo_fp"] = fs.get("adp") / "Dockerdemo"
    fs["ifn"] = fs.get("adp") / "input.json"

    debug_print("Filesystem", fs, verbose=verbose)
    return fs


def get_resources(fs: dict, remote_resources: dict, verbose: bool = True) -> dict:
    local_resources = {
        k: (fs.get("adp") / Path(v).name) for k, v in remote_resources.items()
    }
    relative_local_resources = {
        k: v.relative_to(fs.get("rdp")) for k, v in local_resources.items()
    }

    bx_resources = {
        k: str(fs.get("bdp") / Path(v).name).replace("bx:/", "bx://")
        for k, v in remote_resources.items()
    }

    resources = dict(
        remote=remote_resources,
        local=local_resources,
        relative_local=relative_local_resources,
        bx=bx_resources,
    )

    debug_print("Resources", resources, verbose=verbose)

    return resources


def dl_resources(resources: dict, verbose: bool = True):
    debug_print("\n\nStarting download(s) of local resources", None, verbose=verbose)

    for n, u in resources.get("remote").items():
        f = resources.get("local").get(n)
        msg = """
        Obtaining resource {n}
        FROM: {u}
        TO:   {f}
        """.format(
            n=n, u=u, f=f
        )
        debug_print(msg, None, verbose=verbose)

        download_resource(url=u, fp=f)
    return


# commands
def get_docker_build_command(
    dockerfile_fp: Path = Path("Dockerfile"),
    tag: str = "biotool",
    cwd: Path | None = None,
    verbose: bool = True,
):
    # fix cwd
    if cwd is None:
        cwd = Path().absolute().parent
        debug_print("cwd", cwd, verbose=verbose)

    # build command
    cmd = "docker build . -f {f} -t {t}".format(f=dockerfile_fp.relative_to(cwd), t=tag)

    debug_print(
        "docker build command",
        cmd,
        verbose=verbose,
    )
    return cmd


def get_bx_run_local_command(
    input_dict_fp: Path = Path("input.json"),
    tag: str = "tool",
    cwd: Path | None = None,
    short: bool = True,
    verbose: bool = True,
):
    # fix cwd
    if cwd is None:
        cwd = Path().absolute().parent
        debug_print("cwd", cwd, verbose=verbose)

    if short:
        cmd_input_part = "$(cat {fp})".format(fp=input_dict_fp.relative_to(cwd))
    else:
        input_dict = load_json(input_dict_fp)
        cmd_input_part = "{ip}".format(ip=input_dict).replace("'", '"')

    cmd = "bx run-local {t} '{input_part}'".format(t=tag, input_part=cmd_input_part)

    debug_print(
        "bx run-local command",
        cmd,
        verbose=verbose,
    )
    return cmd


# setup of experiments
def get_and_run_docker_build_command(
    dockerfile_fp: Path = Path("Dockerfile"),
    tag: str = "biotool",
    cwd: Path | None = None,
    verbose: bool = True,
):
    # fix cwd
    if cwd is None:
        cwd = Path().absolute().parent
        debug_print("cwd", cwd, verbose=verbose)

    docker_build_command = get_docker_build_command(
        dockerfile_fp=dockerfile_fp, tag=tag, cwd=cwd, verbose=verbose
    )
    run_command(
        docker_build_command, identifier="Docker build", cwd=cwd, verbose=verbose
    )
    return


def setup_bx_run_local(
    resources: dict = {},
    input_dict_fp: Path = "input.json",
    tag: str = "tool",
    cwd: Path | None = None,
    short: bool = True,
    verbose: bool = True,
    **kwargs
):

    input_dict = get_input_dict(
        resources=resources,
        input_dict_fp=input_dict_fp,
        cwd=cwd,
        verbose=verbose,
        **kwargs
    )

    bx_run_local_command = get_bx_run_local_command(
        input_dict_fp=input_dict_fp, tag=tag, cwd=cwd, verbose=verbose, short=short
    )
    return input_dict, bx_run_local_command


def get_input_dict(
    resources: dict = {},
    input_dict_fp: Path | None = None,
    cwd: Path | None = None,
    verbose: bool = True,
    **kwargs
):
    def _make_paths_relative_recursively(d: dict, cwd: Path):
        for k, v in d.items():
            if isinstance(v, Path):
                d[k] = v.relative_to(cwd)
            elif isinstance(v, list | tuple | set):
                d[k] = [e.relative_to(cwd) if isinstance(v, Path) else e for e in v]
            elif isinstance(v, dict):
                d[k] = _make_paths_relative_recursively(v, cwd=cwd)
            else:
                pass
        return d

    if cwd is not None:
        resources = _make_paths_relative_recursively(resources, cwd=cwd)

    input_dict = {**resources, **kwargs}
    debug_print("input_dict", input_dict, verbose=verbose)

    if input_dict_fp is not None:
        save_json(input_dict, fp=input_dict_fp, verbose=verbose)
    return input_dict
