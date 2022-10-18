from os.path import commonpath
from pathlib import Path
from shutil import rmtree

import rich


def clean_docs(target: Path) -> bool:
    target = target.resolve()
    targets = list(target.glob("*"))

    if len(targets) == 0:
        return False

    for item in targets:
        if item.is_dir():
            rmtree(item)
        else:
            item.unlink()

    return True


def clean_doctrees(doctrees: Path) -> bool:
    if not doctrees.exists():
        return False
    else:
        rmtree(doctrees)
        return True


def clean_all(target: Path, doctrees: Path):
    rich.print("[green]Cleaning all generated files[/]")

    if clean_docs(target):
        rich.print(f"  [green]Removed documents in {target}...[/]")

    if commonpath([doctrees, target]) != target:
        if clean_doctrees(doctrees):
            rich.print(f"  [green]Removed doctrees in {doctrees}...[/]")
