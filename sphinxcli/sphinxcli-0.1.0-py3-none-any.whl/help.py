from typing import cast

import click
import rich


def help_commands(ctx: click.core.Context, show_repl_command: bool = True):
    c = ctx.parent or ctx
    group = cast(click.Group, c.command)
    command_names = {name for name in group.commands}
    if not show_repl_command:
        command_names.remove("repl")
    rich.print(f"\n[green]Available commands:[/]")
    max_len = max([len(x) for x in command_names])
    for command in sorted(command_names):
        cmd = group.commands[command]
        rich.print(f"  [blue]{command.ljust(max_len)}[/]", end="")
        if cmd.help:
            help_text = cmd.help.partition("\f")[0].strip()
            print(f" - {help_text}")
        else:
            print()
