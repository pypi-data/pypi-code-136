"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-10-15
- Purpose: Main API entry points to support the `__main__.py` script.
"""

from __future__ import annotations

import argparse
import pathlib
import textwrap
import networkx as nx  # type: ignore

from typing import (
    Literal, Optional, Union, get_args, TypeAlias
)

from . import journal
from . import core


#------------#
# File input #
#------------#

SourceType: TypeAlias = Literal[
    "graph",
    "dot",
    "exploration",
    "journal",
]
"""
The file types we recognize.
"""


def determineFileType(filename: str) -> SourceType:
    if filename.endswith('.dcg'):
        return 'graph'
    elif filename.endswith('.dot'):
        return 'dot'
    elif filename.endswith('.exg'):
        return 'exploration'
    elif filename.endswith('.exj'):
        return 'journal'
    else:
        raise ValueError(
            f"Could not determine the file type of file '{filename}':"
            f" it does not end with '.dcg', '.dot', '.exg', or '.exj'."
        )


def loadDecisionGraph(path: pathlib.Path) -> core.DecisionGraph:
    """
    Loads a JSON-encoded decision graph from a file. The extension
    should normally be '.dcg'.
    """
    with path.open('r', encoding='utf-8') as fInput:
        return core.DecisionGraph.load(fInput)


def saveDecisionGraph(
    path: pathlib.Path,
    graph: core.DecisionGraph
) -> None:
    """
    Saves a decision graph encoded as JSON in the specified file. The
    file should normally have a '.dcg' extension.
    """
    with path.open('w', encoding='utf-8') as fOutput:
        graph.save(fOutput)


def loadDotFile(path: pathlib.Path) -> core.DecisionGraph:
    """
    Loads a `core.DecisionGraph` form the file at the specified path
    (whose extension should normally be '.dot'). The file format is the
    GraphViz "dot" format.
    """
    raise NotImplementedError(":(")


def saveDotFile(path: pathlib.Path, graph: core.DecisionGraph) -> None:
    """
    Saves a `core.DecisionGraph` as a GraphViz "dot" file. The file
    extension should normally be ".dot".
    """
    # TODO: Custom method for this to capture more stuff?
    nx.nx_pydot.write_dot(graph, str(path))


def loadExploration(path: pathlib.Path) -> core.Exploration:
    """
    Loads a JSON-encoded `core.Exploration` object from the file at the
    specified path. The extension should normally be '.exg'.
    """
    with path.open('r', encoding='utf-8') as fInput:
        return core.Exploration.load(fInput)


def saveExploration(
    path: pathlib.Path,
    exploration: core.Exploration
) -> None:
    """
    Saves a `core.Exploration` object as JSON in the specified file. The
    file extension should normally be '.exg'.
    """
    with path.open('w', encoding='utf-8') as fOutput:
        exploration.save(fOutput)


def loadJournal(path: pathlib.Path) -> core.Exploration:
    """
    Loads a `core.Exploration` object from a journal file (extension
    should normally be '.exj'). Uses the `journal.convertJournal`
    function.
    """
    with path.open('r', encoding='utf-8') as fInput:
        return journal.convertJournal(fInput.read())


def saveAsJournal(
    path: pathlib.Path,
    exploration: core.Exploration
) -> None:
    """
    Saves a `core.Exploration` object as a text journal in the specified
    file. The file extension should normally be '.exj'.

    TODO: This?!
    """
    raise NotImplementedError(
        "Exploration-to-journal conversion is not implemented yet."
    )


def loadSource(
    path: pathlib.Path,
    formatOverride: Optional[SourceType] = None
) -> Union[core.DecisionGraph, core.Exploration]:
    """
    Loads either a `core.DecisionGraph` or a `core.Exploration` from the
    specified file, depending on its file extension (or the specified
    format given as `formatOverride` if there is one).
    """
    if formatOverride is not None:
        format = formatOverride
    else:
        format = determineFileType(str(path))

    if format == "graph":
        return loadDecisionGraph(path)
    if format == "dot":
        return loadDotFile(path)
    elif format == "exploration":
        return loadExploration(path)
    elif format == "journal":
        return loadJournal(path)
    else:
        raise ValueError(
            f"Unrecognized file format '{format}' (recognized formats"
            f" are 'graph', 'exploration', and 'journal')."
        )


#---------------#
# API Functions #
#---------------#

def show(
    source: pathlib.Path,
    formatOverride: Optional[SourceType] = None,
    step: int = -1
) -> None:
    """
    Shows the graph or exploration stored in the `source` file. The file
    extension is used to determine how to load the data, although the
    `--format` option may override this. '.dcg' files are assumed to be
    decision graphs in JSON format, '.exg' files are assumed to be
    exploration objects in JSON format, and '.exj' files are assumed to
    be exploration journals in the default journal format. If the object
    that gets loaded is an exploration, the final graph for that
    exploration will be displayed, or a specific graph may be selected
    using `--step`.
    """
    obj = loadSource(source, formatOverride)
    if isinstance(obj, core.Exploration):
        obj = obj.graphAtStep(step)

    import matplotlib.pyplot # type: ignore

    # This draws the graph in a new window that pops up. You have to close
    # the window to end the program.
    nx.draw(obj)
    matplotlib.pyplot.show()


def analyze(
    source: pathlib.Path,
    formatOverride: Optional[SourceType] = None
) -> None:
    """
    Analyzes the exploration stored in the `source` file. The file
    extension is used to determine how to load the data, although this
    may be overridden by the `--format` option. Normally, '.exg' files
    are treated as JSON-encoded exploration objects, while '.exj' files
    are treated as journals using the default journal format.

    TODO: What does this actually do?
    """
    obj = loadSource(source, formatOverride)
    if isinstance(obj, core.DecisionGraph):
        obj = core.Exploration.fromGraph(obj)

    # TODO


def convert(
    source: pathlib.Path,
    destination: pathlib.Path,
    inputFormatOverride: Optional[SourceType] = None,
    outputFormatOverride: Optional[SourceType] = None,
    step: int = -1
) -> None:
    """
    Converts between exploration and graph formats. By default, formats
    are determined by file extensions, but using the `--format` and
    `--output-format` options can override this. The available formats
    are:

    - '.dcg' A `core.DecisionGraph` stored in JSON format.
    - '.dot' A `core.DecisionGraph` stored as a GraphViz DOT file (TODO:
        reading this format).
    - '.exg' A `core.Exploration` stored in JSON format.
    - '.exj' A `core.Exploration` stored as a journal (see
        `journal.JournalObserver`; TODO: writing this format).

    When converting a decision graph into an exploration format, the
    resulting exploration will have a single starting step containing
    the entire specified graph. When converting an exploration into a
    decision graph format, only the current graph will be saved, unless
    `--step` is used to specify a different step index to save.
    """
    # TODO dot reading, journal writing, and JSON reading/writing for
    # all objects...
    obj = loadSource(source, inputFormatOverride)

    if outputFormatOverride is None:
        outputFormat = determineFileType(str(destination))
    else:
        outputFormat = outputFormatOverride

    if outputFormat in ("graph", "dot"):
        if isinstance(obj, core.Exploration):
            obj = obj.graphAtStep(step)
        if outputFormat == "graph":
            saveDecisionGraph(destination, obj)
        else:
            saveDotFile(destination, obj)
    else:
        if isinstance(obj, core.DecisionGraph):
            obj = core.Exploration.fromGraph(obj)
        if outputFormat == "exploration":
            saveExploration(destination, obj)
        else:
            saveAsJournal(destination, obj)


#--------------#
# Parser setup #
#--------------#

parser = argparse.ArgumentParser(
    prog="python -m exploration",
    description="""\
Runs various commands for processing exploration graphs and journals,
and for converting between them or displaying them in various formats.
"""
)
subparsers = parser.add_subparsers(
    title="commands",
    description="The available commands are:",
    help="use these with -h/--help for more details"
)

showParser = subparsers.add_parser(
    'show',
    help="show an exploration",
    description=textwrap.dedent(str(show.__doc__)).strip()
)
showParser.set_defaults(run="show")
showParser.add_argument(
    "source",
    type=pathlib.Path,
    help="The file to load"
)
showParser.add_argument(
    '-f',
    "--format",
    choices=get_args(SourceType),
    help=(
        "Which format the source file is in (normally that can be"
        " determined from the file extension)."
    )
)
showParser.add_argument(
    '-s',
    "--step",
    type=int,
    default=-1,
    help="Which graph step to show (when loading an exploration)."
)

analyzeParser = subparsers.add_parser(
    'analyze',
    help="analyze an exploration",
    description=textwrap.dedent(str(analyze.__doc__)).strip()
)
analyzeParser.set_defaults(run="analyze")
analyzeParser.add_argument(
    "source",
    type=pathlib.Path,
    help="The file holding the exploration to analyze"
)
analyzeParser.add_argument(
    '-f',
    "--format",
    choices=get_args(SourceType),
    help=(
        "Which format the source file is in (normally that can be"
        " determined from the file extension)."
    )
)

convertParser = subparsers.add_parser(
    'convert',
    help="convert an exploration",
    description=textwrap.dedent(str(convert.__doc__)).strip()
)
convertParser.set_defaults(run="convert")
convertParser.add_argument(
    "source",
    type=pathlib.Path,
    help="The file holding the graph or exploration to convert."
)
convertParser.add_argument(
    "destination",
    type=pathlib.Path,
    help=(
        "The file name where the output should be written (this file"
        " will be overwritten without warning)."
    )
)
convertParser.add_argument(
    '-f',
    "--format",
    choices=get_args(SourceType),
    help=(
        "Which format the source file is in (normally that can be"
        " determined from the file extension)."
    )
)
convertParser.add_argument(
    '-o',
    "--output-format",
    choices=get_args(SourceType),
    help=(
        "Which format the converted file should be saved as (normally"
        " that is determined from the file extension)."
    )
)
convertParser.add_argument(
    '-s',
    "--step",
    type=int,
    default=-1,
    help=(
        "Which graph step to save (when converting from an exploration"
        " format to a graph format)."
    )
)

if __name__ == "__main__":
    options = parser.parse_args()
    if options.run == "show":
        show(
            options.source,
            formatOverride=options.format,
            step=options.step
        )
    elif options.run == "analyze":
        analyze(
            options.source,
            formatOverride=options.format
        )
    elif options.run == "convert":
        convert(
            options.source,
            options.destination,
            inputFormatOverride=options.format,
            outputFormatOverride=options.output_format,
            step=options.step
        )
    else:
        raise RuntimeError(
            f"Invalid 'run' default value: '{options.run}'."
        )
