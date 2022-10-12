from datetime import datetime

import typer
from prettytable import MARKDOWN, PrettyTable


class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def print_bold(text):
    typer.echo(color.BOLD + text + color.END, err=True)


def print_bullet(text, replace=False, additional_space=""):
    end = "\n"
    if replace:
        end = "\r"
    typer.echo(additional_space + f"\N{bullet} {text}{end}", nl=False, err=True)


def print_ok(text, additional_space=""):
    typer.echo(color.GREEN + color.BOLD + additional_space + "\N{check mark} " + color.END + text, err=True)


def print_failed(text, additional_space=""):
    typer.echo(color.RED + color.BOLD + additional_space + "\N{ballot X} " + color.END + text, err=True)


def print_failed_with_catch(text, additional_space=""):
    typer.echo(color.YELLOW + color.BOLD + additional_space + "\N{ballot X} " + color.END + text, err=True)


class PrintStep:
    def __init__(self, text, additional_space=None, catch_exc=False, quiet=False):
        self.text = text
        self.additional_space = additional_space if additional_space is not None else "  "
        self.catch_exc = catch_exc
        self.quiet = quiet
        if not quiet:
            print_bullet(self.text, replace=True, additional_space=self.additional_space)

    def __enter__(self):
        return self

    def __exit__(self, exc, value, traceback):
        if exc and not self.quiet:
            if self.catch_exc:
                print_failed_with_catch(self.text, self.additional_space)
            else:
                print_failed(self.text, self.additional_space)

            return self.catch_exc

        if not self.quiet:
            print_ok(self.text, self.additional_space)


def print_table(table: PrettyTable, table_format=None, border=False):
    if table_format:
        table_format = table_format.lower()
    if table_format == "json":
        print(table.get_json_string())
    elif table_format == "markdown":
        table.set_style(MARKDOWN)
        print(table.get_string())
    elif table_format == "html":
        print(table.get_html_string())
    else:
        if border is None:
            border = False
        table.border = border
        table.align = "l"
        print(table.get_string())


def print_table_column(table: PrettyTable, column_name: str, header=False):
    table.header = header
    table.border = False
    table.align = "l"
    print(table.get_string(fields=[column_name]))


def convert_mps_apps_list_to_pretty_table(apps):
    table = PrettyTable()
    table.field_names = ["APP ID", "EAD SHORT NAME", "EAD NAMESPACE", "DOCKER IMAGE", "CREATED"]
    for app in apps["items"]:
        table.add_row(
            [
                app["active_preview"]["app"]["id"],
                app["active_preview"]["app"]["ead"]["name_short"],
                app["active_preview"]["app"]["ead"]["namespace"],
                app["active_preview"]["app"]["registry_image_url"],
                datetime.strptime(app["active_preview"]["app"]["updated_at"], "%Y-%m-%dT%H:%M:%S.%f").strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),
            ]
        )
    return table


def convert_slides_list_to_pretty_table(slides):
    table = PrettyTable()
    table.field_names = ["SLIDE ID", "PATH", "TISSUE", "STAIN", "BLOCK", "CASE ID", "CREATED", "UPDATED"]
    for slide in slides["items"]:
        table.add_row(
            [
                slide["id"],
                slide["path"],
                slide["tissue"],
                slide["stain"],
                slide["block"],
                slide["case_id"],
                datetime.fromtimestamp(slide["created_at"]).strftime("%Y-%m-%d %H:%M:%S"),
                datetime.fromtimestamp(slide["updated_at"]).strftime("%Y-%m-%d %H:%M:%S"),
            ]
        )
    return table


def convert_jobs_list_to_pretty_table(jobs):
    def _get_timestamp(timestamp):
        if timestamp:
            timestamp = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
        else:
            timestamp = "-"
        return timestamp

    table = PrettyTable()
    table.field_names = ["JOB ID", "STATUS", "APP ID", "CREATED", "STARTED", "ENDED"]
    for job in jobs["items"]:
        table.add_row(
            [
                job["id"],
                job["status"],
                job["app_id"],
                _get_timestamp(job["created_at"]),
                _get_timestamp(job["started_at"]),
                _get_timestamp(job["ended_at"]),
            ]
        )
    return table
