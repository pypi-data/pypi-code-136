import datetime
import os
import sys
from typing import List

import click
import json

from rich import print, get_console
from rich.prompt import Confirm
from rich.traceback import install
from rich.table import Table
from fagus import Fagus, Fil, CFil
import re
import shlex
import readline

install()

COMMANDS = {
    "list": "(l), lists available devices",
    "help": "(h), shows this help text",
    "select": (
        "(s), select the following device(s) as shown in list. E.g. TeleStar_R1 or TS_R1 or 3. The id's can also be "
        "selected as ranges, e.g. 3-5 or 4-9. To select all devices leave the parameter empty, defaults to all devices."
    ),
    "config": (
        '(c), shows all commands in the configuration starting with the provided prefix, e.g. "interface f/." '
        "If no parameter is provided, the whole startup configuration is shown."
    ),
    "edit": (
        "(e) Like c, but now the selected configuration can be edited in a file called tmp_gns3.txt in the "
        "current working directory"
    ),
    "reload": "(r), reloads all the router's startup config files from disk",
    "exit": "or quit, ends the shell",
}
EDIT_FILE = "tmp_gns3.txt"
EDIT_LINE_LENGTH = 80
EDIT_ROUTER_LINE = EDIT_LINE_LENGTH * "#"


@click.command()
@click.option(
    "-d",
    "--directory",
    help="GNS3 project directory to inspect, default .",
    type=click.Path(exists=True, file_okay=False, dir_okay=True),
    # default=(
    #     "/mnt/hgfs/data/Users/Lukas/OneDrive - NTNU/studier/2022 HØST/TTM4240 Advanced Network Control/"
    #     "labs/lab 1/lab1_ipv4 (kopi)/"  # None,
    # )
    default=".",
)
def main(directory: str):
    gns3_files = tuple(f for f in os.listdir(directory) if f.endswith(".gns3"))
    if len(gns3_files) != 1:
        print("[red]The provided directory is no GNS3-project", file=sys.stderr)
        exit(1)
    with open(f"{directory}/{gns3_files[0]}") as f:
        config = Fagus(json.load(f), fagus=True)
    process_commands(
        Fagus(
            {
                router.node_id: router()
                for _, router in sorted(
                    config.iter(
                        0, filter_=Fil(..., (..., CFil("symbol", lambda x: "router" in x))), path="topology nodes"
                    ),
                    key=lambda x: x[1].name,
                )
            },
            fagus=True,
        ),
        directory,
    )


def process_commands(routers: Fagus, directory: str):
    router_lookup = router_lookup_list(routers)
    selected = tuple(routers)
    while True:
        try:
            command = shlex.split(input(">>> "))
            if not command:
                pass
            elif command[0] in ("exit", "quit"):
                raise KeyboardInterrupt
            elif command[0] in ("h", "help"):
                print(
                    f"Help for the commands available in this command-line (shortcuts for commands in parantesis):\n"
                    f"{'%(linebreak)s'.join(f'{k}: {v}' for k, v in COMMANDS.items())}" % {"linebreak": "\n"}
                )
            elif command[0] in ("l", "list"):
                list_routers(routers)
            elif command[0] in ("s", "select"):
                selected = select_routers(routers, router_lookup, command[1:])
            elif command[0] in ("c", "config"):
                show_config(routers, get_configs(routers, selected, directory, command[1:]))
            elif command[0] in ("e", "edit"):
                edit_config_files(
                    routers, get_configs(routers, selected, directory, command[1:]), router_lookup, directory
                )
            elif command[0] in ("r", "reload"):
                reload_config_files(routers, directory)
            else:
                print(
                    "[red]Invalid command, type help to see a list of valid commands or quit to exit", file=sys.stderr
                )
        except KeyboardInterrupt as e:
            raise e
        except:
            get_console().print_exception()


def edit_config_files(routers: Fagus, configs: dict, router_lookup: dict, directory: str):
    if (
        Confirm.ask(
            f"{EDIT_FILE} already exists. Would you like to overwrite it from the current configuration (o), or keep "
            "the current file (k)?",
            show_default=False,
            choices=["o", "k"],
        )
        if os.path.exists("tmp_gns3.txt")
        else True
    ):
        generate_edit_file(configs, routers)
    if Confirm.ask(f"Hit y when you're done editing {EDIT_FILE}, or n to cancel."):
        apply_edit_file(configs, routers, router_lookup, directory)
    elif Confirm.ask(f"Would you like to keep (k) or delete (d) {EDIT_FILE}", choices=["d", "k"]):
        os.remove(EDIT_FILE)


def generate_edit_file(configs: dict, routers: Fagus):
    with open(EDIT_FILE, "w") as f:
        for r_id, r_configs in (x for x in configs.items() if x[1]):
            router = routers[r_id]
            f.write(
                f"{EDIT_LINE_LENGTH * '#'}\n##### BEGIN ROUTER %s %s #####\n{EDIT_LINE_LENGTH * '#'}\n\n"
                % (r := f"{router.name} {router.abbreviation} ({router.id})", (EDIT_LINE_LENGTH - len(r) - 26) * " ")
            )
            for i, config in enumerate(Fagus.values(r_configs, "configs", fagus=True)):
                f.write(
                    f"##### BEGIN CONFIG {i} line {config.start} until {config.start + len(config.orig_lines) - 1} "
                    f"#####\n%s\n##### END CONFIG {i} line {config.start} until "
                    f"{config.start + len(config.orig_lines) - 1} #####\n" % "\n".join(config.orig_lines)
                )
            f.write(
                f"\n{EDIT_LINE_LENGTH * '#'}\n##### END ROUTER %s %s #####\n{EDIT_LINE_LENGTH * '#'}\n\n"
                % (r := f"{router.name} {router.abbreviation} ({router.id})", (EDIT_LINE_LENGTH - len(r) - 24) * " ")
            )
    print(
        f"Created {EDIT_FILE} in your current working directory. You can now edit tmp_gns3.txt to edit the config. "
        f"Do not touch the lines starting with #####. [red]Make sure that all the devices you would like to edit are "
        f"turned off in GNS3 before continuing!"
    )


def apply_edit_file(configs: dict, routers: Fagus, router_lookup: dict, directory: str):
    with open(EDIT_FILE) as f:
        lines = f.read().splitlines()
    r_end = None
    r_id = None
    config = None
    c_end = None
    i = 0
    while i < len(lines) - 1:
        i += 1
        line = lines[i]
        if len(line) == EDIT_LINE_LENGTH:
            if r_id and line == r_end and lines[i - 1] == EDIT_ROUTER_LINE and lines[i + 1] == EDIT_ROUTER_LINE:
                r_end = None
                configs[r_id]["valid"] = True
                r_id = None
                i += 1
                continue
            elif (
                bool(match := re.match("##### BEGIN ROUTER (.*?) (.*?) \\((\\d+)\\) +#####", line))
                and lines[i - 1] == EDIT_ROUTER_LINE
                and lines[i + 1] == EDIT_ROUTER_LINE
            ):
                if match[3] in router_lookup:
                    r_id = router_lookup[match[3]]
                    r_end = "##### END ROUTER %s %s #####" % (
                        r := f"{match[1]} {match[2]} ({match[3]})",
                        (EDIT_LINE_LENGTH - len(r) - 24) * " ",
                    )
                    i += 1
                else:
                    print(f"[red]A router with the id {match[3]} currently doesn't exist, skip it", file=sys.stderr)
                continue
        if r_end and bool(match := re.match("##### BEGIN CONFIG (\\d+) line (\\d+) until (\\d+) #####", line)):
            if int(match[1]) > Fagus.count(configs, (r_id, "configs")):
                print(
                    f"[red]A config with the id {match[1]} does not exist for router {routers[(r_id, 'name')]}",
                    file=sys.stderr,
                )
                continue
            config = configs[r_id]["configs"][int(match[1])]
            if int(match[2]) != config["start"] or int(match[3]) != config["start"] + len(config["orig_lines"]) - 1:
                config = None
                print(
                    f"[red]A config with the id {match[1]} from line {match[2]} to {match[3]} does not exist for "
                    f"router {routers[(r_id, 'name')]}",
                    file=sys.stderr,
                )
            c_end = f"##### END CONFIG {match[1]} line {match[2]} until {match[3]} #####"
        elif config:
            if line == c_end:
                config["valid"] = True
                config = None
            else:
                Fagus.append(config, line, "new_lines")
    update_config_files(routers, configs, directory)


def update_config_files(routers: Fagus, configs: dict, directory: str):
    valid, invalid = Fagus.split(configs, Fil(..., CFil("valid", True), ..., CFil("valid", True)), copy=True)
    show_config(routers, valid, False)
    if invalid:
        if invalid_routers := set(invalid) - set(valid):
            print(
                f"[red]The config of the router%s {', '.join(routers[(r, 'name')] for r in invalid_routers)} %s not "
                f"terminated properly and thus skipped" % (("s", "were") if len(invalid_routers) > 1 else ("", "was")),
                file=sys.stderr,
            )
        for r_id, r_data in invalid.items():
            if r_id not in invalid_routers and r_data["configs"]:
                invalid_configs = tuple(str(i) for i, c in enumerate(configs[r_id]["configs"]) if not c.get("valid"))
                print(
                    f"[red]For {routers[(r_id, 'name')]}, the config%s {', '.join(invalid_configs)} %s not terminated "
                    f"properly and thus skipped" % (("s", "were") if len(invalid_configs) > 1 else ("", "was")),
                    file=sys.stderr,
                )
    if Confirm.ask("Apply the changes as shown above? The indicated lines will be overwritten."):
        for r_id, r_data in (r for r in valid.items() if r[1]["configs"]):
            if any(c["new_lines"] != c["orig_lines"] for c in r_data["configs"]) and (
                os.path.exists((path := f"{directory.rstrip('/')}/project-files/dynamips/{r_id}/configs/"))
                and len(r_cfg := tuple(f for f in os.listdir(path) if f.endswith("startup-config.cfg"))) == 1
            ):
                cfg = routers[(r_id, "cfg")].splitlines()
                for i, line in enumerate(cfg):
                    if "Last configuration change at" in line:
                        cfg[i] = cfg[i][: cfg[i].index("change at ") + 10] + datetime.datetime.utcnow().strftime(
                            "%H:%M:%S UTC %a %b %-d %Y"
                        )
                for config in r_data["configs"]:
                    cfg[config["start"] - 1 : config["start"] + len(config["orig_lines"]) - 1] = config.get(
                        "new_lines", ()
                    )
                with open(f"{path}{r_cfg[0]}", "w") as f:
                    f.writelines("\n".join(cfg))
                print(f"Updated startup configuration file for {routers[(r_id, 'name')]}")
    reload_config_files(routers, directory)
    if Confirm.ask(f"Would you like to keep (k) or delete (d) {EDIT_FILE}", choices=["d", "k"]):
        os.remove(EDIT_FILE)


def reload_config_files(routers: Fagus, directory: str):
    for r_id, router in routers.items():
        if (
            os.path.exists((path := f"{directory.rstrip('/')}/project-files/dynamips/{r_id}/configs/"))
            and len(r_cfg := tuple(f for f in os.listdir(path) if f.endswith("startup-config.cfg"))) == 1
        ):
            with open(f"{path}{r_cfg[0]}") as f:
                router.cfg = f.read()
        else:
            raise FileNotFoundError(f"The file {path}*startup-config.cfg for {router.abbreviation} does not exist.")


def show_config(routers: Fagus, configs: dict, orig=True):
    for r_id, configs in (
        x for x in configs.items() if any(c["orig_lines"] != c.get("new_lines") for c in x[1]["configs"])
    ):
        router = routers[r_id]
        print(f"[bold]{router.name} {router.abbreviation} ({router.id}) {router.node_id}[/bold]")
        for config in Fagus.values(configs, "configs", fagus=True):
            print(f"[italic]Line {config.start} until {config.start + len(config.orig_lines) - 1}[/italic]")
            print("\n".join(config.get("orig_lines" if orig else "new_lines", ())) + "\n")


def get_configs(routers: Fagus, selected: tuple, directory: str, args: List[str]) -> dict:
    configs = Fagus()
    for r_id in selected:
        router = routers[r_id]
        if not router.cfg:
            reload_config_files(routers, directory)
        cfg_lines = router.cfg.splitlines(keepends=False)
        config = Fagus()
        if args:
            record_cfg = False
            for i, line in enumerate(cfg_lines):
                if any(line.startswith(a) for a in args):
                    record_cfg = True
                    if i > config.get("start", -1) + config.count("orig_lines") - 1:
                        config = Fagus({"start": i + 1})
                        configs.append(config(), (r_id, "configs"))
                if record_cfg:
                    config.append(line, "orig_lines")
                    if line == "!":
                        record_cfg = False
        else:
            configs.append({"start": 1, "orig_lines": cfg_lines}, r_id)
    return configs()


def select_routers(routers: Fagus, router_lookup: dict, args: List[str]):
    if args:
        i = 0
        while i < len(args):
            match = re.fullmatch("(\\d+)-(\\d+)", args[i])
            if bool(match) and int(match[2]) < len(routers):
                args[i : i + 1] = (new_indices := tuple(str(a) for a in range(int(match[1]), int(match[2]) + 1)))
                i += len(new_indices) - 1
            i += 1
        selected = tuple(router_lookup[p] for p in args if p in router_lookup)
        if selected:
            print(
                "Selected routers "
                + ", ".join(f"{routers[(r, 'abbreviation')]} ({routers[r, 'id']})" for r in selected)
            )
            return selected
    print("Selected all routers")
    return tuple(router_lookup)


def list_routers(routers: Fagus):
    table = Table(title="Available routers")
    table.add_column("Id")
    table.add_column("Name")
    table.add_column("Abbreviation")
    table.add_column("Hash")
    for router in routers.values():
        table.add_row(str(router.id), router.name, router.abbreviation, router.node_id)
    print(table)
    print("You can use the id, the name, the hash or the abbreviation to refer to each router in other commands.")


def router_lookup_list(routers: Fagus):
    router_ids = {router.name: router.node_id for router in sorted(routers.values(), key=lambda x: x.name)}
    router_lookup_list_ = router_ids.copy()
    unique_abbreviations = {}
    for i, (r_name, r_id) in enumerate(router_ids.items()):
        abbreviation = re.sub("[a-z]", "", r_name)
        if abbreviation in unique_abbreviations:
            unique_abbreviations[abbreviation] += 1
            abbreviation = f"{abbreviation}_{unique_abbreviations[abbreviation]}"
            router_lookup_list_ = r_id
        else:
            unique_abbreviations[abbreviation] = 1
        routers[(r_id, "abbreviation")] = abbreviation
        routers[(r_id, "id")] = i
        router_lookup_list_[routers[(r_id, "abbreviation")]] = r_id
        router_lookup_list_[str(i)] = r_id
    return router_lookup_list_


if __name__ == "__main__":
    main()
