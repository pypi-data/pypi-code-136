import itertools
from typing import List, Tuple

import rich.box
import rich.console
import rich.table
import rich.text

from clink import handlers, participants, utils


def render_table(rich_table: rich.table.Table) -> rich.text.Text:
    console = rich.console.Console()
    with console.capture() as capture:
        console.print(rich_table)
    return rich.text.Text.from_ansi(capture.get())


def consumer_listeners_table(
    consumer: "participants.Consumer",
) -> rich.text.Text:
    table = rich.table.Table(
        rich.table.Column("Name", no_wrap=True),
        rich.table.Column("Topic", no_wrap=True),
        rich.table.Column("Handler", no_wrap=True),
        box=rich.box.SIMPLE,
        title="Consuming...",
        title_justify="left",
        title_style="bold #c837ab",
        row_styles=["none", "dim"],
    )

    for key, group in itertools.groupby(
        sorted(consumer.listeners, key=lambda listener: listener.name or ""),
        key=lambda listener: listener.name,
    ):
        topic_handlers: List[Tuple[str, handlers.Handler]] = []
        for listener in group:
            for topic in sorted(listener.topics):
                for handler in sorted(listener.handlers):
                    topic_handlers += [(topic, handler)]

        for topic, handler in sorted(topic_handlers):
            full_qualname = utils.get_full_qualname(handler.__wrapped__)
            table.add_row(
                f"{key or ''}",
                f"{topic}",
                (
                    f"[link=file://{handler.__wrapped__.__code__.co_filename}]"
                    f"{full_qualname}[/link]"
                ),
            )

    return render_table(table)
