"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-3-3
- Purpose: Core types and tools for dealing with them.

This file defines the main types used for processing and storing
exploration graphs. Key types are:

- `DecisionGraph`: Represents a graph of decisions, including observed
    connections to unknown destinations.
- `Exploration`: A list of `DecisionGraph`s with position and transition
    information representing exploration over time.
"""

from typing import (
    Any, Optional, List, Set, Union, Iterable, cast, Tuple, Dict,
    TypedDict, Sequence, Collection, Literal, get_args, Callable, TextIO,
    TypeAlias
)

import re
import copy
import ast
import sys
import json
import warnings
import random
import itertools
import collections
import math
import inspect
import logging

import networkx as nx  # type: ignore

from . import graphs


#------------#
# Core types #
#------------#

Decision: 'TypeAlias' = str
"""
A type alias: decision points are defined by their names.

A decision represents a location within a decision graph where a decision
can be made about where to go, or a dead-end reached by a previous
decision. Typically, one room can have multiple decision points in it,
even though many rooms have only one. Concepts like 'room' and 'area'
that group multiple decisions together (at various scales) are handled
by the idea of a `Zone`.
"""

Transition: 'TypeAlias' = str
"""
A type alias: transitions are defined by their names.

A transition represents a means of travel from one decision to another.
Outgoing transition names have to be unique at each decision, but not
globally.
"""


State: 'TypeAlias' = dict
"""
A type alias: states are just dictionaries.

They can contain whatever key/value pairs are necessary to represent
exploration-relevant game state. Typical entries might include:

- `'powers'`: A set of `Power`s the player has acquired.
- `'tokens'`: A dictionary mapping `Token`s to integers representing how
    many of that token type have been acquired.
"""


Power: 'TypeAlias' = str
"""
A type alias: powers are defined by their names.

A power represents a capability that can be used to traverse certain
transitions. These transitions should have a `Requirement` specified to
indicate which power(s) and/or token(s) can be used to traverse it.
Powers are usually permanent, but may in some cases be temporary or be
temporarily disabled. Powers might also combine (e.g., speed booster
can't be used underwater until gravity suit is acquired).
"""

Token: 'TypeAlias' = str
"""
A type alias: tokens are defined by their type names.

A token represents an expendable item that can be used to traverse certain
transitions a limited number of times (normally once after which the
token is used up), or to permanently open certain transitions.

When a key permanently opens only one specific door, or is re-usable to
open many doors, that should be represented as a Power, not a token. Only
when there is a choice of which door to unlock (and the key is then used
up) should keys be represented as tokens.
"""

Tag: 'TypeAlias' = str
"""
A type alias: tags are strings.

A tag is an arbitrary string attached to a decision or transition.
Meanings are left up to the map-maker, but some conventions include:

- `'random'` indicates that an edge (usually an action, i.e., a
    self-edge) is not always available, but instead has some random
    element to it (for example, a random item drop from an enemy).
    Normally, the specifics of the random mechanism are not represented
    in detail.
- `'hard'` indicates that an edge is non-trivial to navigate. An
    annotation starting with `'fail:'` can be used to name another edge
    which would be traversed instead if the player fails to navigate the
    edge (e.g., a difficult series of platforms with a pit below that
    takes you to another decision). This is of course entirely
    subjective.
- `'false'` indicates that an edge doesn't actually exist, although it
    appears to. This tag is added in the same exploration step that
    requirements are updated (normally to `ReqImpossible`) to indicate
    that although the edge appeared to be traversable, it wasn't. This
    distinguishes that case from a case where edge requirements actually
    change.
- `'error'` indicates that an edge does not actually exist, and it's
    different than `'false'` because it indicates an error on the
    player's part rather than intentional deception by the game (another
    subjective distinction). It can also be used with a colon and another
    tag to indicate that that tag was applied in error (e.g., a ledge
    thought to be too high was not actually too high). This should be
    used sparingly, because in most cases capturing the player's
    perception of the world is what's desired. This is normally applied
    in the step before an edge is removed from the graph.
- `'hidden'` indicates that an edge is non-trivial to perceive. Again
    this is subjective. `'hinted'` can be used as well to indicate that
    despite being obfuscated, there are hints that suggest the edge's
    existence.
- `'internal'` indicates that this transition joins two different parts
    of the same room, which are represented as separate decisions.
- `'created'` indicates that this transition is newly created and
    represents a change to the decision layout. Normally, when entering
    a decision point, all visible options will be listed. When
    revisiting a decision, several things can happen:
        1. You could notice a transition you hadn't noticed before.
        2. You could traverse part of the room that you couldn't before,
           observing new transitions that have always been there (this
           would be represented as an internal edge to another decision
           node).
        3. You could observe that the decision had changed due to some
           action or event, and discover a new transition that didn't
           exist previously.
    This tag distinguishes case 3 from case 1. The presence or absence
    of a `'hidden'` tag in case 1 represents whether the newly-observed
    (but not new) transition was overlooked because it was hidden or was
    just overlooked accidentally.
"""

Annotation: 'TypeAlias' = str
"A type alias: annotations are strings."

Zone: 'TypeAlias' = str
"""
A type alias: A zone as part of a DecisionGraph is identified using its
name.
"""

ZoneInfo: Tuple[int, Set[Zone], Set[Union[Decision, Zone]]] = \
    collections.namedtuple('ZoneInfo', ['level', 'parents', 'contents'])
"""
Zone info holds a level integer (starting from 0 as the level directly
above decisions), a set of parent zones, and a set of child decisions
and/or zones. Zones at a particular level may only contain zones in lower
levels, although zones at any level may also contain decisions directly.
The norm is for zones at level 0 to contain decisions, while zones at
higher levels contain zones from the level directly below them.

Note that zones may have multiple parents, because one sub-zone may be
contained within multiple super-zones.
"""

if sys.version_info < (3, 8):
    AstStrNode = ast.Str
else:
    AstStrNode = ast.Constant
"An AST node representing a string constant (changed in version 3.8)."


class DefaultZone:
    """
    Default argument for a `Zone` when `None` is used to mean "Do not add
    to the zone you normally would."
    """
    pass


#-------------------#
# Utility functions #
#-------------------#

RANDOM_NAME_SUFFIXES = False
"""
Causes `uniqueName` to use random suffixes instead of sequential ones,
which is more efficient when many name collisions are expected but which
makes things harder to test and debug. False by default.
"""


def uniqueName(base: str, existing: Collection) -> str:
    """
    Finds a unique name relative to a collection of existing names,
    using the given base name, plus a unique suffix if that base name is
    among the existing names. If the base name isn't among the existing
    names, just returns the base name. The suffix consists of a period
    followed by a number, and the lowest unused number is used every
    time. This does lead to poor performance in cases where many
    collisions are expected; you can set `RANDOM_NAME_SUFFIXES` to True
    to use a random suffix instead.

    Note that if the base name already has a numerical suffix, that
    suffix will be changed instead of adding another one.
    """
    # Short-circuit if we're already unique
    if base not in existing:
        return base

    # Ensure a digit suffix
    if (
        '.' not in base
     or not base.split('.')[-1].isdigit()
    ):
        base += '.1'

    # Find the split point for the suffix
    # This will be the index after the '.'
    splitPoint = len(base) - list(reversed(base)).index('.')
    if not RANDOM_NAME_SUFFIXES:
        suffix = int(base[splitPoint:])

    while base in existing:
        if RANDOM_NAME_SUFFIXES:
            base = base[:splitPoint] + str(random.randint(0, 1000000))
        else:
            suffix += 1
            base = base[:splitPoint] + str(suffix)

    return base


#----------#
# Commands #
#----------#

# Commands represent a simplified mini-programming-language for editing a
# graph and/or exploration. The language stores a single 'current value'
# which many effects set or operate on (and which can be referred to as
# '$_' where variable names are used) The previous 'current value' is
# also stored in '$__' for convenience. It also allows the definition of
# arbitrary variables, and calling graph/exploration methods works
# mainly via keyword arguments pulled automatically from the set of
# defined variables. This allows each command to have a fixed number of
# arguments. The following definitions specify the different types of
# command, each as a named tuple with a 'command' slot in the first
# position that names the command.

LiteralValue: Tuple[Literal['val'], str] = collections.namedtuple(
    'LiteralValue',
    ['command', 'value']
)
"""
A command that replaces the current value with a specific literal value.
The values allowed are `None`, `True`, `False`, integers, floating-point
numbers, and quoted strings (single or double quotes only). Note that
lists, tuples, dictionaries, sets, and other complex data structures
cannot be created this way.
"""

EstablishCollection: Tuple[
    Literal['empty'],
    Literal['list', 'tuple', 'set', 'dict']
] = collections.namedtuple(
    'EstablishCollection',
    ['command', 'collection']
)
"""
A command which replaces the current value with an empty collection. The
collection type must be one of 'list', 'tuple', 'set', or 'dict'.
"""

AppendValue: Tuple[Literal['append'], str] = collections.namedtuple(
    'AppendValue',
    ['command', 'value']
)
"""
A command which appends/adds a specific value (either a literal value
that could be used with `LiteralValue` or a variable reference starting
with '$') to the current value, which must be a list, tuple, or set.
"""

SetValue: Tuple[Literal['set'], str, str] = collections.namedtuple(
    'SetValue',
    ['command', 'location', 'value']
)
"""
A command which sets the value for a specific key in a dictionary stored
as the current value, or for at a specific index in a tuple or list.
Both the key and the value may be either a literal that could be used
with `LiteralValue` or a variable reference starting with '$'.

When used with a set, if the value is truthy the location is added to
the set, and otherwise the location is removed from the set.
"""

PopValue: Tuple[Literal['pop']] = collections.namedtuple(
    'PopValue',
    ['command']
)
"""
A command which pops the last value in the tuple or list which is stored
as the current value, setting the value it pops as the new current value.

Does not work with sets or dictionaries.
"""

GetValue: Tuple[Literal['get'], str] = collections.namedtuple(
    'GetValue',
    ['command', 'location']
)
"""
A command which reads a value at a particular index within the current
value and sets that as the new current value. For lists or tuples, the
index must be convertible to an integer (but can also be a variable
reference storing such a value). For sets, if the listed value is in the
set the result will be `True` and otherwise it will be `False`. For
dictionaries, it looks up a value under that key.

For all other kinds of values, it looks for an attribute with the same
name as the string specified and returns the value of that attribute
(it's an error to specify a non-string value in this case).
"""

RemoveValue: Tuple[Literal['remove'], str] = collections.namedtuple(
    'RemoveValue',
    ['command', 'location']
)
"""
A command which removes an item from a tuple, list, set, or dictionary
which is stored as the current value. The value should be an integer (or
a variable holding one) if the current value is a tuple or list. Unlike
python's `.remove` method, this removes a single item at a particular
index/under a particular key, not all copies of a particular value.
"""

BinaryOperator: 'TypeAlias' = Literal[
    '+', '-', '*', '/', '//', '**', '%', '^', '|', '&', 'and', 'or',
    '<', '>', '<=', '>=', '==', 'is'
]
"""
The supported binary operators for commands.
"""

UnaryOperator: 'TypeAlias' = Literal['-', '~', 'not']
"""
The supported binary operators for commands.
"""

ApplyOperator: Tuple[
    Literal['op'],
    BinaryOperator,
    str,
    str
] = collections.namedtuple(
    'ApplyOperator',
    ['command', 'op', 'left', 'right']
)
"""
A command which establishes a new current value based on the result of an
operator. See `BinaryOperator` for the list of supported operators. The
two operand may be literals as accepted by `LiteralValue` or variable
references starting with '$'.
"""

ApplyUnary: Tuple[
    Literal['unary'],
    UnaryOperator,
    str
] = collections.namedtuple(
    'ApplyUnary',
    ['command', 'op', 'value']
)
"""
The unary version of `ApplyOperator`. See `UnaryOperator` for the list
of supported operators.
"""

VariableAssignment: Tuple[
    Literal['assign'],
    str,
    str
] = collections.namedtuple(
    'VariableAssignment',
    ['command', 'varname', 'value']
)
"""
Assigns the specified value (may be a variable reference) into a named
variable. The variable name should not start with '$', which is used when
referencing variables. If it does, variable substitution will be
performed to compute the name of the variable being created.
"""

VariableDeletion: Tuple[Literal['delete'], str] = collections.namedtuple(
    'VariableDeletion',
    ['command', 'varname']
)
"""
Deletes the variable with the given name. Doesn't actually delete the
stored object if it's reference elsewhere. Useful for unspecifying
arguments for a 'call' command.
"""

LoadVariable: Tuple[Literal['load'], str] = collections.namedtuple(
    'LoadVariable',
    ['command', 'varname']
)
"""
Loads the named variable as the current value, replacing the old current
value. The variable name should normally be specified without the '$',
with '$' variable substitution will take place and the resulting string
will be used as the name of the variable to load.
"""

CallType: 'TypeAlias' = Literal[
    'builtin',
    'stored',
    'graph',
    'exploration'
]
"""
Types of function calls available via the 'call' command.
"""

FunctionCall: Tuple[
    Literal['call'],
    CallType,
    str
] = collections.namedtuple(
    'FunctionCall',
    ['command', 'target', 'function']
)
"""
A command which calls a function or method. IF the target is 'builtin',
one of the `COMMAND_BUILTINS` will be called. If the target is 'graph' or
'exploration' then a method of the current graph or exploration will be
called. If the target is 'stored', then the function part will be
treated as a variable reference and the function stored in that variable
will be called.

For builtins, the current value will be used as the only argument. There
are two special cases: for `round`, if an 'ndigits' variable is defined
its value will be used for the optional second argument, and for `range`,
if the current value is `None`, then the values of the 'start', 'stop',
and/or 'step' variables are used for its arguments, with a default start
of 0 and a default step of 1 (there is no default stop; it's an error if
you don't supply one). If the current value is not `None`, `range` just
gets called with the current value as its only argument.

For graph/exploration methods, the current value is ignored and each
listed parameter is sourced from a defined variable of that name, with
parameters for which there is no defined variable going unsupplied
(which might be okay if they're optional). For varargs parameters, the
value of the associated variable will be converted to a tuple and that
will be supplied as if using '*'; for kwargs parameters the value of the
associated variable must be a dictionary, and it will be applied as if
using '**' (except that duplicate arguments will not cause an error;
instead those coming fro the dictionary value will override any already
supplied).
"""

COMMAND_BUILTINS: Dict[str, Callable] = {
    'len': len,
    'min': min,
    'max': max,
    'round': round,  # 'ndigits' may be specified via the environment
    'ceil': math.ceil,
    'floor': math.floor,
    'int': int,
    'float': float,
    'str': str,
    'list': list,
    'tuple': tuple,
    'dict': dict,
    'set': set,
    'copy': copy.copy,
    'deepcopy': copy.deepcopy,
    'range': range,  # parameter names are 'start', 'stop', and 'step'
    'reversed': reversed,
    'sorted': sorted,  # cannot use key= or reverse=
    'print': print,  # prints just one value, ignores sep= and end=
    'warning': logging.warning,  # just one argument
}
"""
The mapping from names to built-in functions usable in commands. Each is
available for use with the 'call' command when 'builtin' is used as the
target. See `FunctionCall` for more details.
"""

SkipCommands: Tuple[
    Literal['skip'],
    str,
    str
] = collections.namedtuple(
    'SkipCommands',
    ['command', 'condition', 'amount']
)
"""
A command which skips forward or backward within the command list it's
included in, but only if a condition value is True. A skip amount of 0
just continues execution as normal. Negative amounts jump to previous
commands (so e.g., -2 will re-execute the two commands above the skip
command), while positive amounts skip over subsequent commands (so e.g.,
1 will skip over one command after this one, resuming execution with the
second command after the skip).

If the condition is False, execution continues with the subsequent
command as normal.

If the distance value is a string instead of an integer, the skip will
redirect execution to the label that uses that name. Note that the
distance value may be a variable reference, in which case the integer or
string inside the reference will determine where to skip to.
"""

Label: Tuple[Literal['label'], str] = collections.namedtuple(
    'Label',
    ['command', 'name']
)
"""
Has no effect, but establishes a label that can be skipped to using the
'skip' command. Note that instead of just a fixed label, a variable name
can be used and variable substitution will determine the label name in
that case, BUT there are two restrictions: the value must be a string,
and you cannot execute a forward-skip to a label which has not already
been evaluated, since the value isn't known when the skip occurs. If you
use a literal label name instead of a variable, you will be able to skip
down to that label from above.

When multiple labels with the same name occur, a skip command will go to
the last label with that name before the skip, only considering labels
after the skip if there are no labels with that name beforehand (and
skipping to the first available label in that case).
"""

Command: 'TypeAlias' = Union[
    LiteralValue,
    EstablishCollection,
    AppendValue,
    SetValue,
    PopValue,
    GetValue,
    RemoveValue,
    ApplyOperator,
    ApplyUnary,
    VariableAssignment,
    VariableDeletion,
    LoadVariable,
    FunctionCall,
    SkipCommands,
    Label
]
"""
The union type for any kind of command. Note that these are all tuples,
all of their members are strings in all cases, and their first member
(named 'command') is always a string that uniquely identifies the type of
the command. Use the `command` function to get some type-checking while
constructing them.
"""

Scope: 'TypeAlias' = Dict[str, Any]
"""
A scope holds variables defined during the execution of a sequence of
commands. Variable names (sans the '$' sign) are mapped to arbitrary
Python values.
"""

CommandResult: 'TypeAlias' = Tuple[
    Scope,
    Union[int, str, None],
    Optional[str]
]
"""
The main result of a command is an updated scope (usually but not
necessarily the same scope object that was used to execute the command).
Additionally, there may be a skip integer that indicates how many
commands should be skipped (if positive) or repeated (if negative) as a
result of the command just executed. This value may also be a string to
skip to a label. There may also be a label value which indicates that
the command that was executed defines that label.
"""


def isSimpleValue(valStr: str) -> bool:
    """
    Returns `True` if the given string is a valid simple value for use
    with a command. Simple values are `None`, `True`, `False`, integers,
    floating-point numbers, and quoted strings (single or double quotes
    only).

    Examples:

    >>> isSimpleValue('None')
    True
    >>> isSimpleValue('True')
    True
    >>> isSimpleValue('False')
    True
    >>> isSimpleValue('none')
    False
    >>> isSimpleValue('12')
    True
    >>> isSimpleValue('5.6')
    True
    >>> isSimpleValue('3.2e-10')
    True
    >>> isSimpleValue('2 + 3j')  # ba-dump tsss
    False
    >>> isSimpleValue('hello')
    False
    >>> isSimpleValue('"hello"')
    True
    >>> isSimpleValue('"hel"lo"')
    False
    >>> isSimpleValue('"hel\\\\"lo"')  # note we're in a docstring here
    True
    >>> isSimpleValue("'hi'")
    True
    >>> isSimpleValue("'don\\\\'t'")
    True
    >>> isSimpleValue("")
    False
    """
    if valStr in ('None', 'True', 'False'):
        return True
    else:
        try:
            _ = int(valStr)
            return True
        except ValueError:
            pass

        try:
            _ = float(valStr)
            return True
        except ValueError:
            pass

        if (
            len(valStr) >= 2
        and valStr.startswith("'") or valStr.startswith('"')
        ):
            quote = valStr[0]
            ends = valStr.endswith(quote)
            mismatched = re.search(r'[^\\]' + quote, valStr[1:-1])
            return ends and mismatched is None
        else:
            return False


def resolveValue(valStr: str, context: Scope) -> Any:
    """
    Given a value string which could be a literal value or a variable
    reference, returns the value of that expression. Note that operators
    are not handled: only variable substitution is done.
    """
    if isVariableReference(valStr):
        varName = valStr[1:]
        if varName not in context:
            raise NameError(f"Variable '{varName}' is not defined.")
        return context[varName]
    elif not isSimpleValue(valStr):
        raise ValueError(
            f"{valStr!r} is not a valid value (perhaps you need to add"
            f" quotes to get a string, or '$' to reference a variable?)"
        )
    else:
        if valStr == "True":
            return True
        elif valStr == "False":
            return False
        elif valStr == "None":
            return None
        elif valStr.startswith('"') or valStr.startswith("'"):
            return valStr[1:-1]
        else:
            try:
                return int(valStr)
            except ValueError:
                pass

            try:
                return float(valStr)
            except ValueError:
                pass

            raise RuntimeError(
                f"Validated value {valStr!r} is not a string, a number,"
                f" or a recognized keyword type."
            )


def isVariableReference(value: str) -> bool:
    """
    Returns `True` if the given value is a variable reference. Variable
    references start with '$' and the rest of the reference must be a
    valid python identifier (i.e., a sequence of alphabetic characters,
    digits, and/or underscores which does not start with a digit).

    There is one other possibility: references that start with '$@'
    possibly followed by an identifier.

    Examples:

    >>> isVariableReference('$hi')
    True
    >>> isVariableReference('$good bye')
    False
    >>> isVariableReference('$_')
    True
    >>> isVariableReference('$123')
    False
    >>> isVariableReference('$1ab')
    False
    >>> isVariableReference('$ab1')
    True
    >>> isVariableReference('hi')
    False
    >>> isVariableReference('')
    False
    >>> isVariableReference('$@')
    True
    >>> isVariableReference('$@a')
    True
    >>> isVariableReference('$@1')
    False
    """
    if len(value) < 2:
        return False
    elif value[0] != '$':
        return False
    elif len(value) == 2:
        return value[1] == '@' or value[1].isidentifier()
    else:
        return (
            value[1:].isidentifier()
        ) or (
            value[1] == '@'
        and value[2:].isidentifier()
        )


def resolveVarName(name: str, scope: Scope) -> str:
    """
    Resolves a variable name as either a literal name, or if the name
    starts with '$', via a variable reference in the given scope whose
    value must be a string.
    """
    if name.startswith('$'):
        result = scope[name[1:]]
        if not isinstance(result, str):
            raise TypeError(
                f"Variable '{name[1:]}' cannot be referenced as a"
                f" variable name because it does not hold a string (its"
                f" value is: {result!r}"
            )
        return result
    else:
        return name


def fixArgs(command: str, requires: int, args: List[str]) -> List[str]:
    """
    Checks that the proper number of arguments has been supplied, using
    the command name as part of the message for a `ValueError` if not.
    This will fill in '$_' and '$__' for the first two missing arguments
    instead of generating an error, and returns the possibly modified
    argument list.
    """
    if not (requires - 2 <= len(args) <= requires):
        raise ValueError(
            f"Command '{command}' requires {requires} argument(s) but"
            f" you provided {len(args)}."
        )
    return (args + ['$_', '$__'])[:requires]


def requiresValue(command: str, argDesc: str, arg: str) -> str:
    """
    Checks that the given argument is a simple value, and raises a
    `ValueError` if it's not. Otherwise just returns. The given command
    name and argument description are used in the error message. The
    `argDesc` should be an adjectival phrase, like 'first'.

    Returns the argument given to it.
    """
    if not isSimpleValue(arg):
        raise ValueError(
            f"The {argDesc} argument to '{command}' must be a simple"
            f" value (got {arg!r})."
        )
    return arg


def requiresLiteralOrVariable(
    command: str,
    argDesc: str,
    options: Collection[str],
    arg: str
) -> str:
    """
    Like `requiresValue` but only allows variable references or one of a
    collection of specific strings as the argument.
    """
    if not isVariableReference(arg) and arg not in options:
        raise ValueError(
            (
                f"The {argDesc} argument to '{command}' must be either"
                f" a variable reference or one of the following strings"
                f" (got {arg!r}):\n  "
            ) + '\n  '.join(options)
        )
    return arg


def requiresValueOrVariable(command: str, argDesc: str, arg: str) -> str:
    """
    Like `requiresValue` but allows variable references as well as
    simple values.
    """
    if not (isSimpleValue(arg) or isVariableReference(arg)):
        raise ValueError(
            f"The {argDesc} argument to '{command}' must be a simple"
            f" value or a variable reference (got {arg!r})."
        )
    return arg


def requiresVariableName(command: str, argDesc: str, arg: str) -> str:
    """
    Like `requiresValue` but allows only variable names, with or without
    the leading '$'.
    """
    if not (isVariableReference(arg) or isVariableReference('$' + arg)):
        raise ValueError(
            f"The {argDesc} argument to '{command}' must be a variable"
            f" name without the '$' or a variable reference (got"
            f" {arg!r})."
        )
    return arg


COMMAND_SETUP: Dict[
    str,
    Tuple[
        type[Command],
        int,
        List[
            Union[
                Literal[
                    "requiresValue",
                    "requiresVariableName",
                    "requiresValueOrVariable"
                ],
                Tuple[
                    Literal["requiresLiteralOrVariable"],
                    Collection[str]
                ]
            ]
        ]
    ]
] = {
    'val': (LiteralValue, 1, ["requiresValue"]),
    'empty': (
        EstablishCollection,
        1,
        [("requiresLiteralOrVariable", {'list', 'tuple', 'set', 'dict'})]
    ),
    'append': (AppendValue, 1, ["requiresValueOrVariable"]),
    'set': (
        SetValue,
        2,
        ["requiresValueOrVariable", "requiresValueOrVariable"]
    ),
    'pop': (PopValue, 0, []),
    'get': (GetValue, 1, ["requiresValueOrVariable"]),
    'remove': (RemoveValue, 1, ["requiresValueOrVariable"]),
    'op': (
        ApplyOperator,
        3,
        [
            ("requiresLiteralOrVariable", get_args(BinaryOperator)),
            "requiresValueOrVariable",
            "requiresValueOrVariable"
        ]
    ),
    'unary': (
        ApplyUnary,
        2,
        [
            ("requiresLiteralOrVariable", get_args(UnaryOperator)),
            "requiresValueOrVariable"
        ]
    ),
    'assign': (
        VariableAssignment,
        2,
        ["requiresVariableName", "requiresValueOrVariable"]
    ),
    'delete': (VariableDeletion, 1, ["requiresVariableName"]),
    'load': (LoadVariable, 1, ["requiresVariableName"]),
    'call': (
        FunctionCall,
        2,
        [
            ("requiresLiteralOrVariable", get_args(CallType)),
            "requiresVariableName"
        ]
    ),
    'skip': (
        SkipCommands,
        2,
        [
            "requiresValueOrVariable",
            "requiresValueOrVariable"
        ]
    ),
    'label': (Label, 1, ["requiresVariableName"]),
}


def command(commandType: str, *_args: str) -> Command:
    """
    A convenience function for constructing a command tuple which
    type-checks the arguments a bit. Raises a `ValueError` if invalid
    information is supplied; otherwise it returns a `Command` tuple.

    Up to two missing arguments will be replaced automatically with '$_'
    and '$__' respectively in most cases.

    Examples:

    >>> command('val', '5')
    LiteralValue(command='val', value='5')
    >>> command('val')
    Traceback (most recent call last):
    ...
    ValueError...
    >>> command('empty')
    EstablishCollection(command='empty', collection='$_')
    >>> command('empty', 'list')
    EstablishCollection(command='empty', collection='list')
    >>> command('empty', '$ref')
    EstablishCollection(command='empty', collection='$ref')
    >>> command('empty', 'invalid')  # invalid argument
    Traceback (most recent call last):
    ...
    ValueError...
    >>> command('empty', 'list', 'dict')  # too many arguments
    Traceback (most recent call last):
    ...
    ValueError...
    >>> command('append', '5')
    AppendValue(command='append', value='5')
    """
    args = list(_args)

    spec = COMMAND_SETUP.get(commandType)
    if spec is None:
        raise ValueError(
            f"Command type '{commandType}' cannot be constructed by"
            f" assembleSimpleCommand (try the command function"
            f" instead)."
        )

    commandVariant, nArgs, checkers = spec

    args = fixArgs(commandType, nArgs, args)

    checkedArgs = []
    for i, (checker, arg) in enumerate(zip(checkers, args)):
        argDesc = str(i + 1)
        if argDesc.endswith('1') and nArgs != 11:
            argDesc += 'st'
        elif argDesc.endswith('2') and nArgs != 12:
            argDesc += 'nd'
        elif argDesc.endswith('3') and nArgs != 13:
            argDesc += 'rd'
        else:
            argDesc += 'th'

        if isinstance(checker, tuple):
            checkName, allowed = checker
            checkFn = globals()[checkName]
            checkedArgs.append(
                checkFn(commandType, argDesc, allowed, arg)
            )
        else:
            checkFn = globals()[checker]
            checkedArgs.append(checkFn(commandType, argDesc, arg))

    return commandVariant(
        commandType,
        *checkedArgs
    )


def parseCommandList(text: str) -> List[Command]:
    """
    Parses a string into a command list. Each line of the string encodes
    one command. It will be split on spaces (except that quoted text
    will be preserved) and turned into a command via the `command`
    function. Blank lines and any text after an unquoted '#' is ignored.

    Raises a `ValueError` if there's an issue with parsing.

    For example:

    >>> commands = parseCommandList('''\\
    ... val 5
    ... empty list
    ... # comment
    ...   append  # indentation is ignored
    ... ''')
    >>> len(commands)
    3
    >>> commands[0]
    LiteralValue(command='val', value='5')
    >>> commands[1]
    EstablishCollection(command='empty', collection='list')
    >>> commands[2]
    AppendValue(command='append', value='$_')
    """
    line = 1
    posOnLine = 0
    index = 0
    quotePos = None
    inQuote = None
    inComment = False
    escaped = False
    lines: List[List[str]] = []
    linePieces: List[str] = []
    currentPiece: Optional[str] = None
    while index < len(text):
        char = text[index]
        index += 1
        # Track lines and position on the line:
        if char == '\n':
            line += 1
            posOnLine = 0
        else:
            posOnLine += 1

        # Group characters into pieces, respecting quoted fragments
        if inQuote is not None:  # implies currentPiece is not None
            assert currentPiece is not None
            if escaped:
                currentPiece += char
            elif char == inQuote:
                currentPiece += char
                inQuote = None
            elif char == '\\':
                escaped = True
                # And don't append it to the string
            else:
                currentPiece += char
        elif inComment:
            if char == '\n':
                inComment = False
        elif char == '\n':
            if currentPiece is not None:
                linePieces.append(currentPiece)
                currentPiece = None
            lines.append(linePieces)
            linePieces = []
        elif char.isspace():
            if currentPiece is not None:
                linePieces.append(currentPiece)
                currentPiece = None
        elif char in '"\'':
            inQuote = char
            quotePos = (line, posOnLine)
            if currentPiece is None:
                currentPiece = char
            else:
                currentPiece += char
        elif char == '#':
            inComment = True
        else:
            if currentPiece is None:
                currentPiece = char
            else:
                currentPiece += char

    if inQuote is not None:
        quotePos = cast(Tuple[int, int], quotePos)
        raise ValueError(
            f"Quoted text started with a {inQuote} on line"
            f" {quotePos[0]} at position {quotePos[1]}, but was"
            f" never ended."
        )

    if currentPiece is not None:
        linePieces.append(currentPiece)

    if len(linePieces) > 0:
        lines.append(linePieces)

    result: List[Command] = []
    for thisLine in lines:
        if len(thisLine) > 0:
            result.append(command(*thisLine))

    return result


def pushCurrentValue(scope: Scope, value: Any) -> None:
    """
    Pushes the given value as the 'current value' for the given scope,
    storing it in the '_' variable. Stores the old '_' value into '__'
    if there was one.
    """
    if '_' in scope:
        scope['__'] = scope['_']
    scope['_'] = value


#---------#
# Effects #
#---------#

class TransitionEffect(TypedDict):
    """
    Represents one effect of a transition on the decision graph and/or
    game state. The `type` slot indicates what type of effect it is, and
    determines what the `value` slot will hold. The `charges` slot is
    normally `None`, but when set to an integer, the effect will only
    trigger that many times, subtracting one charge each time until it
    reaches 0, after which the effect will remain but be ignored. The
    `delay` slot is also normally `None`, but when set to an integer,
    the effect won't trigger but will instead subtract one from the
    delay until it reaches zero, at which point it will start to trigger
    (and use up charges if there are any). The `value` values for each
    `type` are:

    - `'gain'`: A `Power`s or (`Token`, amount) pair indicating a power
        gained or some tokens acquired.
    - `'lose'`: A `Power`s or (`Token`, amount) pair indicating a power
        lost or some tokens spent.
    - `'toggle'`: A list of `Power`s which will be toggled on one after
        the other, toggling the rest off. If the list only has one item,
        it will be toggled on or off depending on whether the player
        currently has that power or not, rather than based on the state
        of the toggle effect. Note that to track the toggle state, the
        order of elements in the list will be edited each time the
        effect triggers.
    - `'deactivate'`: `None`. When the effect is activated, the requirement
        for this transition will be set to `ReqImpossible`.
    - `'edit'`: A list of lists of `Command`s, with each list to be
        applied in succession on every subsequent activation of the
        transition (like toggle). These can use extra variables '$@' to
        refer to the source decision of the transition the edit effect is
        attached to, '$@d' to refer to the destination decision, '$@t' to
        refer to the transition, and '$@r' to refer to its reciprocal.
    """
    type: Literal['gain', 'lose', 'toggle', 'deactivate', 'edit']
    value: Union[
        Power,
        Tuple[Token, int],
        List[Power],
        None,
        List[List[Command]]
    ]
    charges: Optional[int]
    delay: Optional[int]


def mergeEffects(
    a: Sequence[TransitionEffect],
    b: Sequence[TransitionEffect]
) -> List[TransitionEffect]:
    """
    Merges two transition effects lists according to the
    following rules:
    1. Any `gain` or `lose` effects are included, but may be removed due
        to redundancy (they do not cancel each other; `lose` effects
        happen after `gain` effects so a transition with any active
        `lose` effect for a particular power will not result in gaining
        that power, no matter how many active `gain` effects it might
        have. Multiple token gain effects are merged into a combined
        gain with a higher value, only when they each have charges and
        delay set to None.
    2. All other effect types are included as-is. Note that interactions
        between `gain`/`lose` and `toggle` effects for the same powers
        are weird (`toggle` triggers after `gain` and `lose`).
    """
    result: List[TransitionEffect] = []

    powerGains = set()
    powerLosses = set()
    tokenGains: Dict[Token, int] = {}
    tokenLosses: Dict[Token, int] = {}
    for effect in itertools.chain(a, b):
        type = effect['type']
        value = effect['value']
        charges = effect['charges']
        delay = effect['delay']
        if charges is None and delay is None:
            if type == 'gain':
                if isinstance(value, Power):
                    powerGains.add(value)
                else: # it's a token, amount, pair
                    token, amount = cast(Tuple[Token, int], value)
                    tokenGains[token] = tokenGains.get(token, 0) + amount
            elif type == 'lose':
                if isinstance(value, Power):
                    powerLosses.add(value)
                else: # it's a token, amount, pair
                    token, amount = cast(Tuple[Token, int], value)
                    tokenLosses[token] = tokenLosses.get(token, 0) + amount
            else:
                # All other effect types get accumulated
                result.append(effect)
        else:
            # All complex effects get accumulated
            result.append(effect)

    # Cancel out power gains/losses
    for power in powerGains:
        result.append({
            'type': 'gain',
            'value': power,
            'charges': None,
            'delay': None,
        })

    for power in powerLosses:
        result.append({
            'type': 'lose',
            'value': power,
            'charges': None,
            'delay': None,
        })

    for token in tokenGains:
        n = tokenGains[token]
        result.append({
            'type': 'gain',
            'value': (token, n),
            'charges': None,
            'delay': None
        })

    for token in tokenLosses:
        n = tokenGains[token]
        result.append({
            'type': 'lose',
            'value': (token, n),
            'charges': None,
            'delay': None
        })

    return result


def effect(
    *,
    gain: Optional[Union[Power, Tuple[Token, int]]] = None,
    lose: Optional[Union[Power, Tuple[Token, int]]] = None,
    toggle: Optional[
        List[Power]
    ] = None,
    deactivate: Optional[bool] = None,
    edit: Optional[str] = None,
    delay: Optional[int] = None,
    charges: Optional[int] = None,
) -> TransitionEffect:
    """
    Factory for a transition effect which includes default values so you
    can just specify effect types that are relevant to a particular
    situation. You may not supply values for more than one of
    gain/lose/toggle/deactivate/edit, since which one you use determines
    the effect type.
    """
    tCount = len([
        x
        for x in (gain, lose, toggle, deactivate, edit)
        if x is not None
    ])
    if tCount == 0:
        raise ValueError(
            "You must specify one of gain, lose, toggle, deactivate, or"
            " edit."
        )
    elif tCount > 1:
        raise ValueError(
            f"You may only specify one of gain, lose, toggle,"
            f" deactivate, or edit (you provided values for {tCount} of"
            f" those)."
        )

    result: TransitionEffect = {
        'type': 'edit',
        'value': '',
        'delay': delay,
        'charges': charges
    }

    if gain is not None:
        result['type'] = 'gain'
        result['value'] = gain
    elif lose is not None:
        result['type'] = 'lose'
        result['value'] = lose
    elif toggle is not None:
        result['type'] = 'toggle'
        result['value'] = toggle
    elif deactivate is not None:
        result['type'] = 'deactivate'
        result['value'] = None
    elif edit is not None:
        result['type'] = 'edit'
        result['value'] = edit

    return result


#--------------#
# Requirements #
#--------------#

class Requirement:
    """
    Represents a precondition for traversing an edge or taking an action.
    This can be any boolean expression over powers and/or tokens the
    player needs to posses, with numerical values for the number of
    tokens required. For example, if the player needs either the
    wall-break power or the wall-jump power plus a balloon token, you
    could represent that using:

        ReqAny(
            ReqPower('wall-break'),
            ReqAll(
                ReqPower('wall-jump'),
                ReqTokens('balloon', 1)
            )
        )

    The subclasses define concrete requirements.
    """
    def satisfied(self, state: State) -> bool:
        """
        This will return True if the requirement is satisfied in the
        given game state, and False otherwise.
        """
        raise NotImplementedError(
            "Requirement is an abstract class and cannot be"
            " used directly."
        )

    def __eq__(self, other: Any) -> bool:
        raise NotImplementedError(
            "Requirement is an abstract class and cannot be compared."
        )

    def asGainList(self) -> List[TransitionEffect]:
        """
        Transforms this `Requirement` into a list of `TransitionEffect`
        objects that gain the `Power`s and/or `Token`s that would be
        required by this requirement.
        The requirement must be either a `ReqTokens`, a `ReqPower`, or a
        `ReqAny`/`ReqAll` which includes nothing besides those four types
        as sub-requirements. The token and power requirements at the
        leaves of the tree will be collected into a list for the result
        (note that whether `ReqAny` or `ReqAll` is used is ignored, all
        of the tokens/powers mentioned are listed). Raises a `TypeError`
        if this requirement is not suitable for transformation into a
        gains list.
        """
        raise NotImplementedError("Requirement is an abstract class.")

    @staticmethod
    def parse(req: str) -> 'Requirement':
        """
        This static method takes a string and returns a `Requirement`
        object using a mini-language for specifying requirements. The
        language uses '|' for 'or', '&' for 'and', '*' to indicate a
        token requirement (with an integer afterwards specifying the
        number of tokens) and either a valid Python identifier or a
        quoted string to name a power or token type required. You can
        also use 'X' (without quotes) for a never-satisfied requirement,
        and 'O' (without quotes) for an always-satisfied requirement. In
        particular, 'X' can be used for transitions which are only going
        to become accessible when some event takes place, like when a
        switch is flipped. Finally, you can use '-' for negation of a
        requirement; when applied to a token this flips the sense of the
        integer from 'must have at least this many' to 'must have
        strictly less than this many'.

        Examples:

        >>> Requirement.parse('power')
        ReqPower('power')
        >>> Requirement.parse('token*3')
        ReqTokens('token', 3)
        >>> Requirement.parse('power|token*3')
        ReqAny([ReqPower('power'), ReqTokens('token', 3)])
        >>> Requirement.parse('one&two|three')
        ReqAny([ReqAll([ReqPower('one'), ReqPower('two')]), ReqPower('three')])
        """
        # Parse as Python
        try:
            root = ast.parse(req.strip(), '<requirement string>', 'eval')
        except (SyntaxError, IndentationError):
            raise ValueError(f"Could not parse requirement '{req}'.")

        if not isinstance(root, ast.Expression):
            raise ValueError(
                f"Could not parse requirement '{req}'"
                f" (result must be an expression)."
            )

        top = root.body

        if not isinstance(
            top,
            (ast.BinOp, ast.UnaryOp, ast.Name, AstStrNode)
        ):
            raise ValueError(
                f"Could not parse requirement '{req}'"
                f" (result must use only '|', '&', '-', '*', quotes,"
                f" and parentheses)."
            )

        return Requirement.convertAST(top)

    @staticmethod
    def convertAST(node: ast.expr) -> 'Requirement':
        if isinstance(node, ast.UnaryOp):
            if not isinstance(node.op, ast.USub):
                raise ValueError(
                    f"Invalid unary operator:\n{ast.dump(node)}"
                )
            negated = Requirement.convertAST(node.operand)
            return ReqNot(negated)

        if isinstance(node, ast.BinOp):
            # Three valid ops: '|' for or, '&' for and, and '*' for
            # tokens.
            if isinstance(node.op, ast.BitOr):
                # An either-or requirement
                lhs = Requirement.convertAST(node.left)
                rhs = Requirement.convertAST(node.right)
                # We flatten or-or-or chains
                if isinstance(lhs, ReqAny):
                    lhs.subs.append(rhs)
                    return lhs
                elif isinstance(rhs, ReqAny):
                    rhs.subs.append(lhs)
                    return rhs
                else:
                    return ReqAny([lhs, rhs])

            elif isinstance(node.op, ast.BitAnd):
                # An all-of requirement
                lhs = Requirement.convertAST(node.left)
                rhs = Requirement.convertAST(node.right)
                # We flatten and-and-and chains
                if isinstance(lhs, ReqAll):
                    lhs.subs.append(rhs)
                    return lhs
                elif isinstance(rhs, ReqAll):
                    rhs.subs.append(lhs)
                    return rhs
                else:
                    return ReqAll([lhs, rhs])

            elif isinstance(node.op, ast.Mult):
                # Merge power into token name w/ count
                lhs = Requirement.convertAST(node.left)
                if isinstance(lhs, ReqPower):
                    name = lhs.power
                    negate = False
                elif (
                    isinstance(lhs, ReqNot)
                and isinstance(lhs.sub, ReqPower)
                ):
                    name = lhs.sub.power
                    negate = True
                else:
                    raise ValueError(
                        f"Invalid token name:\n{ast.dump(node.left)}"
                    )

                if sys.version_info < (3, 8):
                    if (
                        not isinstance(node.right, ast.Num)
                     or not isinstance(node.right.n, int)
                    ):
                        raise ValueError(
                            f"Invalid token count:\n{ast.dump(node.right)}"
                        )

                    n = node.right.n
                else:
                    if (
                        not isinstance(node.right, ast.Constant)
                     or not isinstance(node.right.value, int)
                    ):
                        raise ValueError(
                            f"Invalid token count:\n{ast.dump(node.right)}"
                        )

                    n = node.right.value

                if negate:
                    return ReqNot(ReqTokens(name, n))
                else:
                    return ReqTokens(name, n)

            else:
                raise ValueError(
                    f"Invalid operator type for requirement:"
                    f" {type(node.op)}"
                )

        elif isinstance(node, ast.Name):
            # variable names are interpreted as power names (with '*'
            # the bin-op level will convert to a token name).
            if node.id == 'X':
                return ReqImpossible()
            elif node.id == 'O':
                return ReqNothing()
            else:
                return ReqPower(node.id)

        elif isinstance(node, AstStrNode):
            # Quoted strings can be used to name powers that aren't
            # valid Python identifiers
            if sys.version_info < (3, 8):
                name = node.s
            else:
                name = node.value

            if not isinstance(name, str):
                raise ValueError(
                    f"Invalid value for requirement: '{name}'."
                )

            return ReqPower(name)

        else:
            raise ValueError(
                f"Invalid AST node for requirement:\n{ast.dump(node)}"
            )

    def unparse(self) -> str:
        """
        Returns a string which would convert back into this
        `Requirement` object if you fed it to `Requirement.parse`.

        Examples:

        >>> r = ReqAny([ReqPower('power'), ReqTokens('token', 3)])
        >>> r.unparse()
        '(power|token*3)'
        >>> back = Requirement.parse(r.unparse())
        >>> back
        ReqAny([ReqPower('power'), ReqTokens('token', 3)])
        >>> back == r
        True
        """
        raise NotImplementedError("Requirement is an abstract class.")


class ReqAny(Requirement):
    """
    A disjunction requirement satisfied when any one of its
    sub-requirements is satisfied.
    """
    def __init__(self, subs: Iterable[Requirement]) -> None:
        self.subs = list(subs)

    def __hash__(self) -> int:
        result = 179843
        for sub in self.subs:
            result = 31 * (result + hash(sub))
        return result

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqAny) and other.subs == self.subs

    def __repr__(self):
        return "ReqAny(" + repr(self.subs) + ")"

    def satisfied(self, state: State) -> bool:
        """
        True as long as any one of the sub-requirements is satisfied.
        """
        return any(sub.satisfied(state) for sub in self.subs)

    def asGainList(self) -> List[TransitionEffect]:
        """
        Returns a gain list composed by adding together the gain lists
        for each sub-requirement. This is more than would be strictly
        necessary to pass this requirement, and is the same behavior as
        `ReqAll`. Note that some types of requirement will raise a
        `TypeError` during this process if they appear as a
        sub-requirement.
        """
        result = []
        for sub in self.subs:
            result += sub.asGainList()

        return result

    def unparse(self) -> str:
        return '(' + '|'.join(sub.unparse() for sub in self.subs) + ')'


class ReqAll(Requirement):
    """
    A conjunction requirement satisfied when all of its sub-requirements
    are satisfied.
    """
    def __init__(self, subs: Iterable[Requirement]) -> None:
        self.subs = list(subs)

    def __hash__(self) -> int:
        result = 182971
        for sub in self.subs:
            result = 17 * (result + hash(sub))
        return result

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqAll) and other.subs == self.subs

    def __repr__(self):
        return "ReqAll(" + repr(self.subs) + ")"

    def satisfied(self, state: State) -> bool:
        """
        True as long as all of the sub-requirements are satisfied.
        """
        return all(sub.satisfied(state) for sub in self.subs)

    def asGainList(self) -> List[TransitionEffect]:
        """
        Returns a gain list composed by adding together the gain lists
        for each sub-requirement. Note that some types of requirement
        will raise a `TypeError` during this process if they appear as a
        sub-requirement.
        """
        result = []
        for sub in self.subs:
            result += sub.asGainList()

        return result

    def unparse(self) -> str:
        return '(' + '&'.join(sub.unparse() for sub in self.subs) + ')'


class ReqNot(Requirement):
    """
    A negation requirement satisfied when its sub-requirement is NOT
    satisfied.
    """
    def __init__(self, sub: Requirement) -> None:
        self.sub = sub

    def __hash__(self) -> int:
        return 17293 + hash(self.sub)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqNot) and other.sub == self.sub

    def __repr__(self):
        return "ReqNot(" + repr(self.sub) + ")"

    def satisfied(self, state: State) -> bool:
        """
        True as long as the sub-requirement is not satisfied.
        """
        return not self.sub.satisfied(state)

    def asGainList(self) -> List[TransitionEffect]:
        """
        Raises a `TypeError` since understanding a `ReqNot` in terms of
        powers/tokens to be gained is not straightforward, and would need
        to be done relative to a game state in any case.
        """
        raise TypeError(
            "Cannot convert ReqNot into a gain effect list:"
            " powers or tokens would have to be lost, not gained to"
            " satisfy this requirement."
        )

    def unparse(self) -> str:
        return '-(' + self.sub.unparse() + ')'


class ReqPower(Requirement):
    """
    A power requirement satisfied if the specified power is possessed by
    the player according to the given state.
    """
    def __init__(self, power: Power) -> None:
        self.power = power

    def __hash__(self) -> int:
        return 47923 + hash(self.power)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqPower) and other.power == self.power

    def __repr__(self):
        return "ReqPower(" + repr(self.power) + ")"

    def satisfied(self, state: State) -> bool:
        return self.power in state.get("powers", set())

    def asGainList(self) -> List[TransitionEffect]:
        """
        Returns a list containing a single 'gain' effect which grants
        the required power.
        """
        return [effect(gain=self.power)]

    def unparse(self) -> str:
        return self.power


class ReqTokens(Requirement):
    """
    A token requirement satisfied if the player possesses at least a
    certain number of a given type of token.

    Note that checking the satisfaction of individual doors in a specific
    state is not enough to guarantee they're jointly traversable, since
    if a series of doors requires the same kind of token, further logic
    is needed to understand that as the tokens get used up, their
    requirements may no longer be satisfied.

    Also note that a requirement for tokens does NOT mean that tokens
    will be subtracted when traversing the door (you can have re-usable
    tokens after all). To implement a token cost, use both a requirement
    and a 'lose' effect.
    """
    def __init__(self, tokenType: Token, cost: int) -> None:
        self.tokenType = tokenType
        self.cost = cost

    def __hash__(self) -> int:
        return (17 * hash(self.tokenType)) + (11 * self.cost)

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, ReqTokens)
        and other.tokenType == self.tokenType
        and other.cost == self.cost
        )

    def __repr__(self):
        return f"ReqTokens({repr(self.tokenType)}, {repr(self.cost)})"

    def satisfied(self, state: State) -> bool:
        return (
            state.setdefault('tokens', {}).get(self.tokenType, 0)
         >= self.cost
        )

    def asGainList(self) -> List[TransitionEffect]:
        """
        Returns a list containing a single 'gain' effect which grants
        the required tokens.
        """
        return [effect(gain=(self.tokenType, self.cost))]

    def unparse(self) -> str:
        return f'{self.tokenType}*{self.cost}'


class ReqNothing(Requirement):
    """
    A requirement representing that something doesn't actually have a
    requirement. This requirement is always satisfied.
    """
    def __hash__(self) -> int:
        return 127942

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqNothing)

    def __repr__(self):
        return "ReqNothing()"

    def satisfied(self, state: State) -> bool:
        return True

    def asGainList(self) -> List[TransitionEffect]:
        """
        Returns an empty list, since nothing is required.
        """
        return []

    def unparse(self) -> str:
        return 'O'


class ReqImpossible(Requirement):
    """
    A requirement representing that something is impossible. This
    requirement is never satisfied.
    """
    def __hash__(self) -> int:
        return 478743

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, ReqImpossible)

    def __repr__(self):
        return "ReqImpossible()"

    def satisfied(self, state: State) -> bool:
        return False

    def asGainList(self) -> List[TransitionEffect]:
        """
        Raises a `TypeError` since a `ReqImpossible` cannot be converted
        into an effect which would allow the transition to be taken.
        """
        raise TypeError(
            "Cannot convert ReqImpossible into a gain effect list:"
            " there are no powers or tokens which could be gained to"
            " satisfy this requirement."
        )

    def unparse(self) -> str:
        return 'X'


#-----------------------#
# Transition properties #
#-----------------------#

class TransitionProperties(TypedDict):
    """
    Represents bundled properties of a transition, including a
    requirement, effects, tags, and/or annotations. Does not include the
    reciprocal. Has the following slots:

    - `'requirement'`: The requirement for the transition. This is
        always a `Requirement`, although it might be `ReqNothing` if
        nothing special is required.
    - `'effects'`: The effects of the transition. This is a list of
        `TransitionEffect` objects.
    - `'tags'`: Any tags applied to the transition.
    - `'annotations'`: A list of annotations applied to the transition.
    """
    requirement: Requirement
    effects: List[TransitionEffect]
    tags: Set[Tag]
    annotations: List[Annotation]


def mergeProperties(
    a: Optional[TransitionProperties],
    b: Optional[TransitionProperties]
) -> TransitionProperties:
    """
    Merges two sets of transition properties, following these rules:

    1. Tags and annotations are combined. Annotations from the
        second property set are ordered after those from the first.
    2. If one of the transitions has a `ReqNothing` instance as its
        requirement, we use the other requirement. If both have
        complex requirements, we create a new `ReqAll` which
        combines them as the requirement.
    3. The effects are merged using `mergeEffects`. Note that this can
        seriously change how effects operate (TODO: Fix that)

    If either transition is `None`, then a deep copy of the other is
    returned. If both are `None`, then an empty transition properties
    dictionary is returned, with `ReqNothing` as the requirement, no
    effects, no tags, and no annotations.
    """
    if a is None:
        if b is None:
            return {
                "requirement": ReqNothing(),
                "effects": [],
                "tags": set(),
                "annotations": []
            }
        else:
            return copy.deepcopy(b)
    elif b is None:
        return copy.deepcopy(a)
    # implicitly neither a or b is None below

    result: TransitionProperties = {
        "requirement": ReqNothing(),
        "effects": mergeEffects(a["effects"], b["effects"]),
        "tags": a["tags"] | b["tags"],
        "annotations": a["annotations"] + b["annotations"],
    }

    if a["requirement"] == ReqNothing():
        result["requirement"] = b["requirement"]
    elif b["requirement"] == ReqNothing():
        result["requirement"] = a["requirement"]
    else:
        result["requirement"] = ReqAll(
            [a["requirement"], b["requirement"]]
        )

    return result


#---------------------#
# Errors and warnings #
#---------------------#

class TransitionBlockedWarning(Warning):
    """
    An warning type for indicating that a transition which has been
    requested does not have its requirements satisfied by the current
    game state.
    """
    pass


class BadStart(ValueError):
    """
    An error raised when the start method is used improperly.
    """
    pass


class MissingDecisionError(KeyError):
    """
    An error raised when attempting to use a decision that does not
    exist.
    """
    pass


class MissingTransitionError(KeyError):
    """
    An error raised when attempting to use a transition that does not
    exist.
    """
    pass


class MissingZoneError(KeyError):
    """
    An error raised when attempting to use a zone that does not exist.
    """
    pass


class InvalidLevelError(ValueError):
    """
    An error raised when an operation fails because of an invalid zone
    level.
    """
    pass


class InvalidDestinationError(ValueError):
    """
    An error raised when attempting to perform an operation with a
    transition but that transition does not lead to a destination that's
    compatible with the operation.
    """
    pass


class UnknownDestinationError(ValueError):
    """
    An error raised when attempting to perform an operation that
    requires a known destination with a node that represents an unknown
    decision, or vice versa.
    """
    pass


class DecisionCollisionError(ValueError):
    """
    An error raised when attempting to create a new decision using the
    name of a decision that already exists.
    """
    pass


class TransitionCollisionError(ValueError):
    """
    An error raised when attempting to re-use a transition name for a
    new transition, or otherwise when a transition name conflicts with
    an already-established transition.
    """
    pass


class ZoneCollisionError(ValueError):
    """
    An error raised when attempting to re-use a zone name for a new zone,
    or otherwise when a zone name conflicts with an already-established
    zone.
    """
    pass


class CommandError(Exception):
    """
    An error raised during command execution will be converted to one of
    the subtypes of this class. Stores the underlying error as `cause`,
    and also stores the `command` and `line` where the error occurred.
    """
    def __init__(
        self,
        command: Command,
        line: int,
        cause: Exception
    ) -> None:
        self.command = command
        self.line = line
        self.cause = cause

    def __str__(self):
        return (
            f"\n  Command block, line {self.line}, running command:"
            f"\n    {self.command!r}"
            f"\n{type(self.cause).__name__}: {self.cause}"
        )


class CommandValueError(CommandError, ValueError):
    "A `ValueError` encountered during command execution."
    pass


class CommandTypeError(CommandError, TypeError):
    "A `TypeError` encountered during command execution."
    pass


class CommandIndexError(CommandError, IndexError):
    "A `IndexError` encountered during command execution."
    pass


class CommandKeyError(CommandError, KeyError):
    "A `KeyError` encountered during command execution."
    pass


class CommandOtherError(CommandError):
    """
    Any error other than a `ValueError`, `TypeError`, `IndexError`, or
    `KeyError` that's encountered during command execution. You can use
    the `.cause` field to figure out what the type of the underlying
    error was.
    """
    pass


#---------------------#
# DecisionGraph class #
#---------------------#

class DecisionGraph(graphs.UniqueExitsGraph[Decision, Transition]):
    """
    Represents a view of the world as a topological graph at a moment in
    time. It derives from `networkx.MultiDiGraph`.

    Each node (a `Decision`) represents a place in the world where there
    are multiple opportunities for travel/action, or a dead end where
    you must turn around and go back; typically this is a single room in
    a game, but sometimes one room has multiple decision points. Edges
    (`Transition`s) represent choices that can be made to travel to
    other decision points (e.g., taking the left door), or when they are
    self-edges, they represent actions that can be taken within a
    location that affect the world or the game state.

    Each `Transition` includes a `TransitionEffects` dictionary
    indicating the effects that it has. Other effects of the transition
    that are not simple enough to be included in this format may be
    represented in an `Exploration` by changing the graph in the next step
    to reflect further effects of a transition.

    In addition to normal transitions between decisions, a
    `DecisionGraph` can represent potential transitions which lead to
    unknown destinations. These are represented by adding decisions with
    the `'unknown'` tag (whose names where not specified begin with
    `'_u.'`) with a separate unknown decision for each transition
    (although where it's known that two transitions lead to the same
    unknown region, this can be represented as well).

    Both nodes and edges can have `Annotation`s associated with them that
    include extra details about the explorer's perception of the
    situation. They can also have `Tag`s, which represent specific
    categories a transition or decision falls into.

    Nodes can also be part of one or more `Zones`, and zones can also be
    part of other zones, allowing for a hierarchical description of the
    underlying space.
    """
    def __init__(self) -> None:
        super().__init__()

        # Mapping from zone names to zone info
        self.zones: Dict[Zone, ZoneInfo] = {}

        # Mapping from decisions to zones they're (directly) within
        self.zoneMap: Dict[Decision, Set[Zone]] = {}

        # Number of unknown decisions that have been created (not number
        # of current unknown decisions, which is likely lower)
        self.unknownCount = 0

    # Note: not hashable

    def __eq__(self, other):
        """
        Equality checker. `DecisionGraph`s can only be equal to other
        `DecisionGraph`s, not to other kinds of things.
        """
        if not isinstance(other, DecisionGraph):
            return False
        else:
            # Checks nodes, edges, and all attached data
            if not super().__eq__(other):
                return False

            # Check unknown count
            if self.unknownCount != other.unknownCount:
                return False

            # Check zones
            if self.zones != other.zones:
                return False

            if self.zoneMap != other.zoneMap:
                return False

            return True

    def destination(
        self,
        decision: Decision,
        transition: Transition
    ) -> Decision:
        """
        Overrides base `UniqueExitsGraph.decision` to raise
        `MissingDecisionError` or `MissingTransitionError` as
        appropriate.
        """
        if decision not in self:
            raise MissingDecisionError(
                f"Decision '{decision}' does not exist."
            )
        try:
            return super().destination(decision, transition)
        except KeyError:
            raise MissingTransitionError(
                f"Transition '{transition}' does not exist at decision"
                f" '{decision}'."
            )

    def destinationsFrom(
        self,
        decision: Decision
    ) -> Dict[Transition, Decision]:
        """
        Override that just changes the type of the exception from a
        `KeyError` to a `MissingDecisionError` when the source does not
        exist.
        """
        if decision not in self:
            raise MissingDecisionError(
                f"Source decision '{decision}' does not exist."
            )
        return super().destinationsFrom(decision)

    def decisionActions(self, decision: Decision) -> Set[Transition]:
        """
        Retrieves the set of self-edges at a decision. Editing the set
        will not affect the graph.
        """
        return set(self.edges[decision, decision])

    def getTransitionProperties(
        self,
        decision: Decision,
        transition: Transition
    ) -> TransitionProperties:
        """
        Returns a dictionary containing transition properties for the
        specified transition from the specified decision. The properties
        included are:

        - 'requirement': The requirement for the transition.
        - 'effects': Any effects of the transition.
        - 'tags': Any tags applied to the transition.
        - 'annotations': Any annotations on the transition.

        The reciprocal of the transition is not included.
        """
        return {
            'requirement':
                self.getTransitionRequirement(decision, transition),
            'effects': self.getTransitionEffects(decision, transition),
            'tags': self.transitionTags(decision, transition),
            'annotations': self.transitionAnnotations(decision, transition)
        }

    def setTransitionProperties(
        self,
        decision: Decision,
        transition: Transition,
        requirement: Optional[Requirement] = None,
        effects: Optional[List[TransitionEffect]] = None,
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None
    ) -> None:
        """
        Sets one or more transition properties all at once. Can be used
        to set the requirement, effects, tags, and/or annotations. Old
        values are overwritten, although if `None`s are provided (or
        arguments are omitted), corresponding properties are not updated.

        To add tags or annotations to existing tags/annotations instead
        of replacing them, use `tagTransition` or `annotateTransition`
        instead.
        """
        if requirement is not None:
            self.setTransitionRequirement(decision, transition, requirement)
        if effects is not None:
            self.setTransitionEffects(decision, transition, effects)
        if tags is not None:
            dest = self.destination(decision, transition)
            self.edges[decision, dest, transition]['tags'] = tags
        if annotations is not None:
            dest = self.destination(decision, transition)
            self.edges[decision, dest, transition]['ann'] = annotations

    def getTransitionRequirement(
        self,
        decision: Decision,
        transition: Transition
    ) -> Requirement:
        """
        Returns the `Requirement` for accessing a specific transition at
        a specific decision. For transitions which don't have
        requirements, returns a `ReqNothing` instance.
        """
        dest = self.destination(decision, transition)

        info = self.edges[decision, dest, transition]

        return info.get('requires', ReqNothing())

    def setTransitionRequirement(
        self,
        decision: Decision,
        transition: Transition,
        requirement: Union[Requirement, str, None]
    ) -> None:
        """
        Sets the `Requirement` for accessing a specific transition at
        a specific decision. Raises a `KeyError` if the decision or
        transition does not exist.

        Deletes the requirement if `None` is given as the requirement;
        if a string is provided, converts it into a `Requirement` using
        `Requirement.parse`. Does not raise an error if deletion is
        requested for a non-existent requirement, and silently
        overwrites any previous requirement.
        """
        dest = self.destination(decision, transition)

        info = self.edges[decision, dest, transition]

        if isinstance(requirement, str):
            requirement = Requirement.parse(requirement)

        if requirement is None:
            try:
                del info['requires']
            except KeyError:
                pass
        else:
            if not isinstance(requirement, Requirement):
                raise TypeError(
                    f"Invalid requirement type: {type(requirement)}"
                )

            info['requires'] = requirement

    def getTransitionEffects(
        self,
        decision: Decision,
        transition: Transition
    ) -> List[TransitionEffect]:
        """
        Retrieves the effects of a transition.

        A `KeyError` is raised if the specified decision/transition
        combination doesn't exist.
        """
        dest = self.destination(decision, transition)

        info = self.edges[decision, dest, transition]

        return info.get('effects', [])

    def addTransitionEffect(
        self,
        decision: Decision,
        transition: Transition,
        effect: TransitionEffect
    ) -> None:
        """
        Adds the given `TransitionEffect` to the effects list for the
        specified transition.

        A `MissingDecisionError` or a `MissingTransitionError` is raised
        if the specified decision/transition combination doesn't exist.

        TODO: TEST ME
        """
        dest = self.destination(decision, transition)

        info = self.edges[decision, dest, transition]

        info.setdefault('effects', []).append(effect)

    def setTransitionEffects(
        self,
        decision: Decision,
        transition: Transition,
        effects: List[TransitionEffect]
    ) -> None:
        """
        Replaces the transition effects for the given transition at the
        given decision. Any previous effects are discarded. See
        `TransitionEffect` for the structure of these.

        A `MissingDecisionError` or a `MissingTransitionError` is raised
        if the specified decision/transition combination doesn't exist.
        """
        dest = self.destination(decision, transition)

        info = self.edges[decision, dest, transition]

        info['effects'] = effects

    def addAction(
        self,
        decision: Decision,
        action: Transition,
        requires: Union[Requirement, str, None] = None,
        effects: Optional[List[TransitionEffect]] = None
    ) -> None:
        """
        Adds the given action as a possibility at the given decision. An
        action is just a self-edge, which can have requirements like any
        edge, and which can have effects like any edge.
        The optional arguments are given to `setTransitionRequirement`
        and `setTransitionEffects`; see those functions for descriptions
        of what they mean.

        Raises a `KeyError` if a transition with the given name already
        exists at the given decision.
        """
        self.add_edge(decision, decision, action)
        self.setTransitionRequirement(decision, action, requires)
        if effects is not None:
            self.setTransitionEffects(decision, action, effects)

    def tagDecision(
        self,
        decision: Decision,
        tagOrTags: Union[Tag, Set[Tag]]
    ) -> None:
        """
        Adds a tag (or many tags from a set of tags) to a decision.
        """
        if isinstance(tagOrTags, Tag):
            tagOrTags = {tagOrTags}

        tagsAlready = self.nodes[decision].setdefault('tags', set())
        for tag in tagOrTags:
            tagsAlready.add(tag)

    def untagDecision(self, decision: Decision, tag: Tag) -> bool:
        """
        Removes a tag from a decision. Returns `True` if the tag was
        present and got removed, or `False` if the tag wasn't present.
        """
        target = self.nodes[decision]['tags']
        try:
            target.remove(tag)
            return True
        except KeyError:
            return False

    def decisionTags(self, decision: Decision) -> Set[Tag]:
        """
        Returns the set of tags for a decision. Edits will be applied to
        the graph.
        """
        return self.nodes[decision]['tags']

    def annotateDecision(
        self,
        decision: Decision,
        annotationOrAnnotations: Union[Annotation, Sequence[Annotation]]
    ) -> None:
        """
        Adds an annotation to a decision's annotations list.
        """
        if isinstance(annotationOrAnnotations, Annotation):
            annotationOrAnnotations = [annotationOrAnnotations]
        self.nodes[decision]['ann'].extend(annotationOrAnnotations)

    def decisionAnnotations(self, decision: Decision) -> List[Annotation]:
        """
        Returns the list of annotations for the specified decision.
        Modifying the list affects the graph.
        """
        return self.nodes[decision]['ann']

    def tagTransition(
        self,
        decision: Decision,
        transition: Transition,
        tagOrTags: Union[Tag, Set[Tag]]
    ) -> None:
        """
        Adds a tag (or each tag from a set) to a transition coming out of
        a specific decision.
        """
        dest = self.destination(decision, transition)
        if isinstance(tagOrTags, Tag):
            tagOrTags = {tagOrTags}

        tagsAlready = self.edges[decision, dest, transition].setdefault(
            'tags',
            set()
        )
        for tag in tagOrTags:
            tagsAlready.add(tag)

    def untagTransition(
        self,
        decision: Decision,
        transition: Transition,
        tagOrTags: Union[Tag, Set[Tag]]
    ) -> None:
        """
        Removes a tag (or each tag in a set) from a transition coming out
        of a specific decision. Raises a `KeyError` if (one of) the
        specified tag(s) is not currently applied to the specified
        transition.
        """
        dest = self.destination(decision, transition)
        if isinstance(tagOrTags, Tag):
            tagOrTags = {tagOrTags}

        tagsAlready = self.edges[decision, dest, transition].setdefault(
            'tags',
            set()
        )
        for tag in tagOrTags:
            tagsAlready.remove(tag)

    def transitionTags(
        self,
        decision: Decision,
        transition: Transition
    ) -> Set[Tag]:
        """
        Returns the set of tags for a transition. Edits will be applied
        to the graph.
        """
        dest = self.destination(decision, transition)
        return self.edges[decision, dest, transition]['tags']

    def annotateTransition(
        self,
        decision: Decision,
        transition: Transition,
        annotations: Union[Annotation, Sequence[Annotation]]
    ) -> None:
        """
        Adds an annotation (or a sequence of annotations) to a
        transition's annotations list.
        """
        dest = self.destination(decision, transition)
        if isinstance(annotations, Annotation):
            annotations = [annotations]
        self.edges[decision, dest, transition]['ann'].extend(annotations)

    def transitionAnnotations(
        self,
        decision: Decision,
        transition: Transition
    ) -> List[Annotation]:
        """
        Returns the annotation list for a specific transition at a
        specific decision. Editing the list affects the graph.
        """
        dest = self.destination(decision, transition)
        return self.edges[decision, dest, transition]['ann']

    def createZone(self, zone: Zone, level: int) -> ZoneInfo:
        """
        Creates an empty zone with the given name at the given level.
        Raises a `ZoneCollisionError` if that zone name is already in
        use (at any level), including if it's in use by a decision.

        Raises an `InvalidLevelError` if the level value is less than 0.

        Returns the `ZoneInfo` for the new blank zone.

        TODO: TESTS
        """
        if level < 0:
            raise InvalidLevelError(
                "Cannot create a zone with a negative level."
            )
        if zone in self.zones:
            raise ZoneCollisionError(f"Zone '{zone}' already exists.")
        if zone in self:
            raise ZoneCollisionError(
                f"A decision named '{zone}' already exists, so a zone"
                f" with that name cannot be created."
            )
        info: ZoneInfo = ZoneInfo(level, set(), set())
        self.zones[zone] = info
        return info

    def getZoneInfo(self, zone: Zone) -> Optional[ZoneInfo]:
        """
        Returns the `ZoneInfo` (level, parents, and contents) for the
        specified zone, or `None` if that zone does not exist.

        TODO: TESTS
        """
        return self.zones.get(zone)

    def deleteZone(self, zone: Zone) -> ZoneInfo:
        """
        Deletes the specified zone, returning a `ZoneInfo` tuple with
        the information on the level, parents, and contents of that
        zone.

        Raises a `MissingZoneError` if the zone in question does not
        exist.

        TODO: TESTS
        """
        info = self.getZoneInfo(zone)
        if info is None:
            raise MissingZoneError(
                f"Cannot delete zone '{zone}': it does not exist."
            )
        for sub in info.contents:
            if sub in self.zoneMap:
                self.zoneMap[sub].remove(zone)
        del self.zones[zone]
        return info

    def addDecisionToZone(
        self,
        decision: Decision,
        zone: Zone
    ) -> None:
        """
        Adds a decision directly to a zone. Should normally only be used
        with level-0 zones. Raises a `MissingZoneError` if the specified
        zone did not already exist.
        """
        if zone not in self.zones:
            raise MissingZoneError(f"Zone '{zone}' does not exist.")

        self.zones[zone].contents.add(decision)
        self.zoneMap.setdefault(decision, set()).add(zone)

    def removeDecisionFromZone(
        self,
        decision: Decision,
        zone: Zone
    ) -> bool:
        """
        Removes a decision from a zone if it had been in it, returning
        True if that decision had been in that zone, and False if it was
        not in that zone, including if that zone didn't exist.

        Note that this only removes a decision from direct zone
        membership. If the decision is a member of one or more zones
        which are (directly or indirectly) sub-zones of the target zone,
        the decision will remain in those zones, and will still be
        indirectly part of the target zone afterwards.

        TODO: TESTS
        """
        if zone not in self.zones:
            return False

        info = self.zones[zone]
        if decision not in info.contents:
            return False
        else:
            info.contents.remove(decision)
            self.zoneMap[decision].remove(zone)
            return True

    def addZoneToZone(
        self,
        addIt: Zone,
        addTo: Zone
    ) -> None:
        """
        Adds a zone to another zone. The `addIt` one must be at a
        strictly lower level than the `addTo` zone.

        If the zone to be added didn't already exist, it is created at
        one level below the target zone. Similarly, if the zone being
        added to didn't already exist, it is created at one level above
        the target zone. If neither existed, a `MissingZoneError` will
        be raised.

        TODO: TESTS
        """
        # Create one or the other (but not both) if they're missing
        addInfo = self.getZoneInfo(addIt)
        toInfo = self.getZoneInfo(addTo)
        if addInfo is None and toInfo is None:
            raise MissingZoneError(
                f"Cannot add zone '{addIt}' to zone '{addTo}': neither"
                f" exists already."
            )

        # Create missing addIt
        elif addInfo is None:
            toInfo = cast(ZoneInfo, toInfo)
            newLevel = toInfo.level - 1
            if newLevel < 0:
                raise InvalidLevelError(
                    f"Zone '{addTo}' is at level {toInfo.level} and so"
                    f" a new zone cannot be added underneath it."
                )
            addInfo = self.createZone(addIt, newLevel)

        # Create missing addTo
        elif toInfo is None:
            addInfo = cast(ZoneInfo, addInfo)
            newLevel = addInfo.level + 1
            if newLevel < 0:
                raise InvalidLevelError(
                    f"Zone '{addIt}' is at level {addInfo.level} (!!!)"
                    f" and so a new zone cannot be added above it."
                )
            toInfo = self.createZone(addTo, newLevel)

        # Now both addInfo and toInfo are defined
        if addInfo.level >= toInfo.level:
            raise InvalidLevelError(
                f"Cannot add zone '{addIt}' at level {addInfo.level}"
                f" to zone '{addTo}' at level {toInfo.level}: zones can"
                f" only contain zones of lower levels."
            )

        # Now both addInfo and toInfo are defined
        toInfo.contents.add(addIt)
        addInfo.parents.add(addTo)

    def removeZoneFromZone(
        self,
        removeIt: Zone,
        removeFrom: Zone
    ) -> bool:
        """
        Removes a zone from a zone if it had been in it, returning True
        if that zone had been in that zone, and False if it was not in
        that zone, including if either zone did not exist.

        TODO: TESTS
        """
        remInfo = self.getZoneInfo(removeIt)
        fromInfo = self.getZoneInfo(removeFrom)

        if remInfo is None or fromInfo is None:
            return False

        if removeIt not in fromInfo.contents:
            return False

        remInfo.parents.remove(removeFrom)
        fromInfo.contents.remove(removeIt)
        return True

    def decisionsInZone(self, zone: Zone) -> Set[Decision]:
        """
        Returns a set of all decisions included directly in the given
        zone, not counting decisions included via intermediate
        sub-zones (see `allDecisionsInZone` to include those).

        Raises a `MissingZoneError` if the specified zone does not
        exist.

        The returned set is a copy, not a live editable set.
        """
        info = self.getZoneInfo(zone)
        if info is None:
            raise MissingZoneError(f"Zone '{zone}' does not exist.")

        # Everything that's note a zone must be a decision
        return {
            item
            for item in info.contents
            if item not in self.zones
        }

    def subZones(self, zone: Zone) -> Set[Zone]:
        """
        Returns the set of all immediate sub-zones of the given zone.
        Will be an empty set if there are no sub-zones; raises a
        `MissingZoneError` if the specified zone does not exit.

        The returned set is a copy, not a live editable set.
        """
        info = self.getZoneInfo(zone)
        if info is None:
            raise MissingZoneError(f"Zone '{zone}' does not exist.")

        # Sub-zones will appear in self.zones
        return {
            item
            for item in info.contents
            if item in self.zones
        }

    def allDecisionsInZone(self, zone: Zone) -> Optional[Set[Decision]]:
        """
        Returns a set containing all decisions in the given zone,
        including those included via sub-zones.

        Raises a `MissingZoneError` if the specified zone does not
        exist.`

        TODO: TESTS
        """
        result: Set[Decision] = set()
        info = self.getZoneInfo(zone)
        if info is None:
            return None

        for item in info.contents:
            if item in self.zones:
                # This can't be none because of the condition above
                result |= cast(
                    Set[Decision],
                    self.allDecisionsInZone(item)
                )
            else:  # it's a decision
                result.add(item)

        return result

    def zoneHierarchyLevel(self, zone: Zone) -> int:
        """
        Returns the hierarchy level of the given zone, as stored in its
        zone info.

        Raises a `MissingZoneError` if the specified zone does not
        exist.
        """
        info = self.getZoneInfo(zone)
        if info is None:
            raise MissingZoneError(f"Zone '{zone}' dose not exist.")

        return info.level

#    def zoneLineage(self, zone: Zone) -> List[Set[Zone]]:
#        """
#        Returns a list containing sets of zones at each level which
#        contain (directly or indirectly) the target zone. The first
#        entry in the list will be all direct parents of the target zone,
#        the second entry will be their parents, and so on. Even if a
#        zone is the parent of other zones in the lineage at multiple
#        levels, it will not be present more than once in the lineage:
#        each zone appears at the lowest applicable level.
#
#        Raises a `MissingZoneError` if the target zone does not exist.
#        """
#        info = self.getZoneInfo(zone)
#        if info is None:
#            raise MissingZoneError(f"Zone '{zone}' does not exist.")
#
#        layer = copy.copy(info.parents)
#        result = [layer]
#        seen = copy.copy(layer)
#
#        # Keep going until we run out of added things
#        while len(layer) > 0:
#            # Create a new layer
#            newLayer = set()
#            # Collect all parents of zones in the previous layer
#            for ancestor in layer:
#                info = self.getZoneInfo(ancestor)
#                if info is None:
#                    raise RuntimeError(
#                        f"Listed ancestor '{ancestor}' does not exist!"
#                    )
#                newLayer |= info.parents
#            # remove already-seen zones
#            newLayer -= seen
#            # Add remaining zones to seen set
#            seen |= newLayer
#            # Add layer to result if it's not empty
#            if len(newLayer) > 0:
#                result.append(newLayer)
#            # Swap new layer into layer
#            layer = newLayer
#
#        return result

    def zoneParents(
        self,
        zoneOrDecision: Union[Zone, Decision]
    ) -> Set[Zone]:
        """
        Returns the set of all zones which directly contain the target
        zone or decision.

        Raises a `MissingDecisionError` if the target is neither a valid
        zone nor a valid decision.

        Returns a copy, not a live editable set.
        """
        if zoneOrDecision in self.zones:
            zoneOrDecision = cast(Zone, zoneOrDecision)
            info = cast(ZoneInfo, self.getZoneInfo(zoneOrDecision))
            return copy.copy(info.parents)
        elif zoneOrDecision in self:
            return copy.copy(self.zoneMap.get(zoneOrDecision, set()))
        else:
            raise MissingDecisionError(
                f"Name '{zoneOrDecision}' is neither a valid zone nor a"
                f" valid decision."
            )

    def zoneAncestors(
        self,
        zoneOrDecision: Union[Zone, Decision],
        exclude: Set[Zone] = set()
    ) -> Set[Zone]:
        """
        Returns the set of zones which contain the target zone or
        decision, either directly or indirectly. The target is not
        included in the set.

        Any ones listed in the `exclude` set are also excluded, as are
        any of their ancestors which are not also ancestors of the
        target zone via another path of inclusion.

        Raises a `MissingDecisionError` if the target is nether a valid
        zone nor a valid decision.
        """
        result = self.zoneParents(zoneOrDecision)
        result -= exclude
        for parent in copy.copy(result):
            # Recursively dig up ancestors, but exclude
            # results-so-far to avoid re-enumerating when there are
            # multiple braided inclusion paths.
            result |= self.zoneAncestors(parent, result | exclude)

        return result

    def zoneEdges(self, zone: Zone) -> Optional[
        Tuple[
            Set[Tuple[Decision, Transition]],
            Set[Tuple[Decision, Transition]]
        ]
    ]:
        """
        Given a zone to look at, finds all of the transitions which go
        out of and into that zone, ignoring internal transitions between
        decisions in the zone. This includes all decisions in sub-zones.
        The return value is a pair of sets for outgoing and then
        incoming transitions, where each transition is specified as a
        (sourceName, transitionName) pair.

        Returns `None` if the target zone isn't yet fully defined.

        Note that this takes time proportional to *all* edges plus *all*
        nodes in the graph no matter how large or small the zone in
        question is.

        TODO: TESTS
        """
        # Find the interior nodes
        interior = self.allDecisionsInZone(zone)
        if interior is None:
            return None

        # Set up our result
        results: Tuple[
            Set[Tuple[Decision, Transition]],
            Set[Tuple[Decision, Transition]]
        ] = (set(), set())

        # Because finding incoming edges requires searching the entire
        # graph anyways, it's more efficient to just consider each edge
        # once.
        for fromDecision in self:
            fromThere = self[fromDecision]
            for toDecision in fromThere:
                for transition in fromThere[toDecision]:
                    sourceIn = fromDecision in interior
                    destIn = toDecision in interior
                    if sourceIn and not destIn:
                        results[0].add((fromDecision, transition))
                    elif destIn and not sourceIn:
                        results[1].add((fromDecision, transition))

        return results

    def replaceZonesInHierarchy(
        self,
        target: Decision,
        zone: Zone,
        level: int
    ) -> None:
        """
        This method replaces one or more zones which contain the
        specified `target` decision with a specific zone, at a specific
        level in the zone hierarchy (see `zoneHierarchyLevel`). If the
        named zone doesn't yet exist, it will be created.

        To do this, it looks at all zones which contain the target
        decision directly or indirectly (see `zoneAncestors`) and which
        are at the specified level.

        - Any direct children of those zones which are ancestors of the
            target decision are removed from those zones and placed into
            the new zone instead, regardless of their levels. Indirect
            children are not affected (except perhaps indirectly via
            their parents' ancestors changing).
        - The new zone is placed into every direct parent of those
            zones, regardless of their levels (those parents are by
            definition all ancestors of the target decision).
        - If there were no zones at the target level, every zone at the
            next level down which is an ancestor of the target decision
            (or just that decision if the level is 0) is placed into the
            new zone as a direct child (and is removed from any previous
            parents it had). In this case, the new zone will also be
            added as a sub-zone to every ancestor of the target decision
            at the level above the specified level, if there are any.
            * In this case, if there are no zones at the level below the
                specified level, the highest level of zones smaller than
                that is treated as the level below, down to targeting
                the decision itself.
            * Similarly, if there are no zones at the level above the
                specified level but there are zones at a higher level,
                the new zone will be added to each of the zones in the
                lowest level above the target level that has zones in it.

        A `MissingDecisionError` will be raised if the specified
        decision is not valid, or if the decision is left as default but
        there is no current decision in the exploration.

        An `InvalidLevelError` will be raised if the level is less than
        zero.

        Example:
        >>> g = DecisionGraph()
        >>> g.addDecision('decision')
        >>> g.addDecision('alternate')
        >>> g.createZone('zone0', 0)
        ZoneInfo(level=0, parents=set(), contents=set())
        >>> g.createZone('zone1', 1)
        ZoneInfo(level=1, parents=set(), contents=set())
        >>> g.createZone('zone2.1', 2)
        ZoneInfo(level=2, parents=set(), contents=set())
        >>> g.createZone('zone2.2', 2)
        ZoneInfo(level=2, parents=set(), contents=set())
        >>> g.createZone('zone3', 3)
        ZoneInfo(level=3, parents=set(), contents=set())
        >>> g.addDecisionToZone('decision', 'zone0')
        >>> g.addDecisionToZone('alternate', 'zone0')
        >>> g.addZoneToZone('zone0', 'zone1')
        >>> g.addZoneToZone('zone1', 'zone2.1')
        >>> g.addZoneToZone('zone1', 'zone2.2')
        >>> g.addZoneToZone('zone2.1', 'zone3')
        >>> g.addZoneToZone('zone2.2', 'zone3')
        >>> g.zoneHierarchyLevel('zone0')
        0
        >>> g.zoneHierarchyLevel('zone1')
        1
        >>> g.zoneHierarchyLevel('zone2.1')
        2
        >>> g.zoneHierarchyLevel('zone2.2')
        2
        >>> g.zoneHierarchyLevel('zone3')
        3
        >>> sorted(g.decisionsInZone('zone0'))
        ['alternate', 'decision']
        >>> sorted(g.zoneAncestors('zone0'))
        ['zone1', 'zone2.1', 'zone2.2', 'zone3']
        >>> g.subZones('zone1')
        {'zone0'}
        >>> g.zoneParents('zone0')
        {'zone1'}
        >>> g.replaceZonesInHierarchy('decision', 'new0', 0)
        >>> g.zoneParents('zone0')
        {'zone1'}
        >>> g.zoneParents('new0')
        {'zone1'}
        >>> sorted(g.zoneAncestors('zone0'))
        ['zone1', 'zone2.1', 'zone2.2', 'zone3']
        >>> sorted(g.zoneAncestors('new0'))
        ['zone1', 'zone2.1', 'zone2.2', 'zone3']
        >>> g.decisionsInZone('zone0')
        {'alternate'}
        >>> g.decisionsInZone('new0')
        {'decision'}
        >>> sorted(g.subZones('zone1'))
        ['new0', 'zone0']
        >>> g.zoneParents('new0')
        {'zone1'}
        >>> g.replaceZonesInHierarchy('decision', 'new1', 1)
        >>> sorted(g.zoneAncestors('decision'))
        ['new0', 'new1', 'zone2.1', 'zone2.2', 'zone3']
        >>> g.subZones('zone1')
        {'zone0'}
        >>> g.subZones('new1')
        {'new0'}
        >>> g.zoneParents('new0')
        {'new1'}
        >>> sorted(g.zoneParents('zone1'))
        ['zone2.1', 'zone2.2']
        >>> sorted(g.zoneParents('new1'))
        ['zone2.1', 'zone2.2']
        >>> g.zoneParents('zone2.1')
        {'zone3'}
        >>> g.zoneParents('zone2.2')
        {'zone3'}
        >>> sorted(g.subZones('zone2.1'))
        ['new1', 'zone1']
        >>> sorted(g.subZones('zone2.2'))
        ['new1', 'zone1']
        >>> sorted(g.allDecisionsInZone('zone2.1'))
        ['alternate', 'decision']
        >>> sorted(g.allDecisionsInZone('zone2.2'))
        ['alternate', 'decision']
        >>> g.replaceZonesInHierarchy('decision', 'new2', 2)
        >>> g.zoneParents('zone2.1')
        {'zone3'}
        >>> g.zoneParents('zone2.2')
        {'zone3'}
        >>> g.subZones('zone2.1')
        {'zone1'}
        >>> g.subZones('zone2.2')
        {'zone1'}
        >>> g.subZones('new2')
        {'new1'}
        >>> g.zoneParents('new2')
        {'zone3'}
        >>> g.allDecisionsInZone('zone2.1')
        {'alternate'}
        >>> g.allDecisionsInZone('zone2.2')
        {'alternate'}
        >>> g.allDecisionsInZone('new2')
        {'decision'}
        >>> sorted(g.subZones('zone3'))
        ['new2', 'zone2.1', 'zone2.2']
        >>> g.zoneParents('zone3')
        set()
        >>> sorted(g.allDecisionsInZone('zone3'))
        ['alternate', 'decision']
        >>> g.replaceZonesInHierarchy('decision', 'new3', 3)
        >>> sorted(g.subZones('zone3'))
        ['zone2.1', 'zone2.2']
        >>> g.subZones('new3')
        {'new2'}
        >>> g.zoneParents('zone3')
        set()
        >>> g.zoneParents('new3')
        set()
        >>> g.allDecisionsInZone('zone3')
        {'alternate'}
        >>> g.allDecisionsInZone('new3')
        {'decision'}
        >>> g.replaceZonesInHierarchy('decision', 'new4', 5)
        >>> g.subZones('new4')
        {'new3'}
        >>> g.zoneHierarchyLevel('new4')
        5

        Another example of level collapse when trying to replace a zone
        at a level above :

        >>> g = DecisionGraph()
        >>> g.addDecision('A')
        >>> g.addDecision('B')
        >>> g.createZone('level0', 0)
        ZoneInfo(level=0, parents=set(), contents=set())
        >>> g.createZone('level1', 1)
        ZoneInfo(level=1, parents=set(), contents=set())
        >>> g.createZone('level2', 2)
        ZoneInfo(level=2, parents=set(), contents=set())
        >>> g.createZone('level3', 3)
        ZoneInfo(level=3, parents=set(), contents=set())
        >>> g.addDecisionToZone('B', 'level0')
        >>> g.addZoneToZone('level0', 'level1')
        >>> g.addZoneToZone('level1', 'level2')
        >>> g.addZoneToZone('level2', 'level3')
        >>> g.addDecisionToZone('A', 'level3') # missing some zone levels
        >>> g.zoneHierarchyLevel('level3')
        3
        >>> g.replaceZonesInHierarchy('A', 'newFirst', 1)
        >>> g.zoneHierarchyLevel('newFirst')
        1
        >>> g.decisionsInZone('newFirst')
        {'A'}
        >>> g.decisionsInZone('level3')
        set()
        >>> sorted(g.allDecisionsInZone('level3'))
        ['A', 'B']
        >>> g.subZones('newFirst')
        set()
        >>> sorted(g.subZones('level3'))
        ['level2', 'newFirst']
        >>> g.zoneParents('newFirst')
        {'level3'}
        >>> g.replaceZonesInHierarchy('A', 'newSecond', 2)
        >>> g.zoneHierarchyLevel('newSecond')
        2
        >>> g.decisionsInZone('newSecond')
        set()
        >>> g.allDecisionsInZone('newSecond')
        {'A'}
        >>> g.subZones('newSecond')
        {'newFirst'}
        >>> g.zoneParents('newSecond')
        {'level3'}
        >>> g.zoneParents('newFirst')
        {'newSecond'}
        >>> sorted(g.subZones('level3'))
        ['level2', 'newSecond']
        """
        if target not in self:
            raise MissingDecisionError(
                f"Decision '{target}' does not exist."
            )

        if level < 0:
            raise InvalidLevelError(
                f"Target level must be positive (got {level})."
            )

        info = self.getZoneInfo(zone)
        if info is None:
            info = self.createZone(zone, level)
        elif level != info.level:
            raise InvalidLevelError(
                f"Target level ({level}) does not match the level of"
                f" the target zone ('{zone}' at level {info.level})."
            )

        # Collect both parents & ancestors
        parents = self.zoneParents(target)
        ancestors = self.zoneAncestors(target)

        # Map from levels to sets of zones from the ancestors pool
        levelMap: Dict[int, Set[Zone]] = {}
        highest = -1
        for ancestor in ancestors:
            ancestorLevel = self.zoneHierarchyLevel(ancestor)
            levelMap.setdefault(ancestorLevel, set()).add(ancestor)
            if ancestorLevel > highest:
                highest = ancestorLevel

        # Figure out if we have target zones to replace or not
        reparentDecision = False
        if level in levelMap:
            # If there are zones at the target level,
            targetZones = levelMap[level]

            above = set()
            below = set()

            for replaced in targetZones:
                above |= self.zoneParents(replaced)
                below |= self.subZones(replaced)
                if replaced in parents:
                    reparentDecision = True

            # Only ancestors should be reparented
            below &= ancestors

        else:
            # Find levels w/ zones in them above + below
            levelBelow = level - 1
            levelAbove = level + 1
            below = levelMap.get(levelBelow, set())
            above = levelMap.get(levelAbove, set())

            while len(below) == 0 and levelBelow > 0:
                levelBelow -= 1
                below = levelMap.get(levelBelow, set())

            if len(below) == 0:
                reparentDecision = True

            while len(above) == 0 and levelAbove < highest:
                levelAbove += 1
                above = levelMap.get(levelAbove, set())

        # Handle re-parenting zones below
        for under in below:
            for parent in self.zoneParents(under):
                if parent in ancestors:
                    self.removeZoneFromZone(under, parent)
            self.addZoneToZone(under, zone)

        # Add this zone to each parent
        for parent in above:
            self.addZoneToZone(zone, parent)

        # Re-parent the decision itself if necessary
        if reparentDecision:
            for parent in parents:
                self.removeDecisionFromZone(target, parent)
            self.addDecisionToZone(target, zone)

    def getReciprocal(
        self,
        decision: Decision,
        transition: Transition
    ) -> Optional[Transition]:
        """
        Returns the reciprocal edge for the specified transition from the
        specified decision (see `setReciprocal`). Returns
        `None` if no reciprocal has been established for that
        transition, or if that decision or transition does not exist.
        """
        dest = self.getDestination(decision, transition)
        if dest is not None:
            return self.edges[decision, dest, transition].get("reciprocal")
        else:
            return None

    def setReciprocal(
        self,
        decision: Decision,
        transition: Transition,
        reciprocal: Optional[Transition],
        setBoth: bool = True,
        cleanup: bool = True
    ) -> None:
        """
        Sets the 'reciprocal' transition for a particular transition from
        a particular decision, and removes the reciprocal property from
        any old reciprocal transition.

        Raises a `MissingDecisionError` or a `MissingTransitionError` if
        the specified decision or transition does not exist.

        Raises an `InvalidDestinationError` if the reciprocal transition
        does not exist, or if it does exist but does not lead back to
        the decision the transition came from.

        If `setBoth` is True (the default) then the transition which is
        being identified as a reciprocal will also have its reciprocal
        property set, pointing back to the primary transition being
        modified, and any old reciprocal of that transition will have its
        reciprocal set to None. If you want to create a situation with
        non-exclusive reciprocals, use `setBoth=False`.

        If `cleanup` is True (the default) then abandoned reciprocal
        transitions (for both edges if `setBoth` was true) have their
        reciprocal properties removed. Set `cleanup` to false if you want
        to retain them, although this will result in non-exclusive
        reciprocal relationships.

        If the `reciprocal` value is None, this deletes the reciprocal
        value entirely, and if `setBoth` is true, it does this for the
        previous reciprocal edge as well. No error is raised in this case
        when there was not already a reciprocal to delete.

        Note that one should remove a reciprocal relationship before
        redirecting either edge of the pair in a way that gives it a new
        reciprocal, since otherwise, a later attempt to remove the
        reciprocal with `setBoth` set to True (the default) will end up
        deleting the reciprocal information from the other edge that was
        already modified. There is no way to reliably detect and avoid
        this, because two different decisions could (and often do in
        practice) have transitions with identical names, meaning that the
        reciprocal value will still be the same, but it will indicate a
        different edge in virtue of the destination of the edge changing.

        ## Example

        >>> g = DecisionGraph()
        >>> g.addDecision('G')
        >>> g.addDecision('H')
        >>> g.addDecision('I')
        >>> g.addTransition('G', 'up', 'H', 'down')
        >>> g.addTransition('G', 'next', 'H', 'prev')
        >>> g.addTransition('H', 'next', 'I', 'prev')
        >>> g.addTransition('H', 'return', 'G')
        >>> g.setReciprocal('G', 'up', 'next') # Error w/ destinations
        Traceback (most recent call last):
        ...
        exploration.core.InvalidDestinationError...
        >>> g.setReciprocal('G', 'up', 'none') # Doesn't exist
        Traceback (most recent call last):
        ...
        exploration.core.MissingTransitionError...
        >>> g.getReciprocal('G', 'up')
        'down'
        >>> g.getReciprocal('H', 'down')
        'up'
        >>> g.getReciprocal('H', 'return') is None
        True
        >>> g.setReciprocal('G', 'up', 'return')
        >>> g.getReciprocal('G', 'up')
        'return'
        >>> g.getReciprocal('H', 'down') is None
        True
        >>> g.getReciprocal('H', 'return')
        'up'
        >>> g.setReciprocal('H', 'return', None) # remove the reciprocal
        >>> g.getReciprocal('G', 'up') is None
        True
        >>> g.getReciprocal('H', 'down') is None
        True
        >>> g.getReciprocal('H', 'return') is None
        True
        >>> g.setReciprocal('G', 'up', 'down', setBoth=False) # one-way
        >>> g.getReciprocal('G', 'up')
        'down'
        >>> g.getReciprocal('H', 'down') is None
        True
        >>> g.getReciprocal('H', 'return') is None
        True
        >>> g.setReciprocal('H', 'return', 'up', setBoth=False) # non-symmetric
        >>> g.getReciprocal('G', 'up')
        'down'
        >>> g.getReciprocal('H', 'down') is None
        True
        >>> g.getReciprocal('H', 'return')
        'up'
        >>> g.setReciprocal('H', 'down', 'up') # setBoth not needed
        >>> g.getReciprocal('G', 'up')
        'down'
        >>> g.getReciprocal('H', 'down')
        'up'
        >>> g.getReciprocal('H', 'return') # unchanged
        'up'
        >>> g.setReciprocal('G', 'up', 'return', cleanup=False) # no cleanup
        >>> g.getReciprocal('G', 'up')
        'return'
        >>> g.getReciprocal('H', 'down')
        'up'
        >>> g.getReciprocal('H', 'return') # unchanged
        'up'
        >>> # Cleanup only applies to reciprocal if setBoth is true
        >>> g.setReciprocal('H', 'down', 'up', setBoth=False)
        >>> g.getReciprocal('G', 'up')
        'return'
        >>> g.getReciprocal('H', 'down')
        'up'
        >>> g.getReciprocal('H', 'return') # not cleaned up w/out setBoth
        'up'
        >>> g.setReciprocal('H', 'down', 'up') # with cleanup and setBoth
        >>> g.getReciprocal('G', 'up')
        'down'
        >>> g.getReciprocal('H', 'down')
        'up'
        >>> g.getReciprocal('H', 'return') is None # cleaned up
        True
        """
        dest = self.destination(decision, transition) # possible KeyError
        if reciprocal is None:
            rDest = None
        else:
            rDest = self.getDestination(dest, reciprocal)

        # Set or delete reciprocal property
        if reciprocal is None:
            # Delete the property
            old = self.edges[decision, dest, transition].pop('reciprocal')
            if setBoth and self.getDestination(dest, old) is not None:
                # Note this happens even if rDest is != destination!
                del self.edges[dest, decision, old]['reciprocal']
        else:
            # Set the property, checking for errors first
            if rDest is None:
                raise MissingTransitionError(
                    f"Reciprocal transition '{reciprocal}' for"
                    f" transition '{transition}' from decision"
                    f" '{decision}' does not exist in decision"
                    f" '{dest}'."
                )

            if rDest != decision:
                raise InvalidDestinationError(
                    f"Reciprocal transition '{reciprocal}' from"
                    f" decision '{dest}' does not lead back to decision"
                    f" '{decision}'."
                )

            eProps = self.edges[decision, dest, transition]
            abandoned = eProps.get('reciprocal')
            eProps['reciprocal'] = reciprocal
            if cleanup and abandoned not in (None, reciprocal):
                del self.edges[dest, decision, abandoned]['reciprocal']

            if setBoth:
                rProps = self.edges[dest, decision, reciprocal]
                revAbandoned = rProps.get('reciprocal')
                rProps['reciprocal'] = transition
                # Sever old reciprocal relationship
                if cleanup and revAbandoned not in (None, transition):
                    raProps = self.edges[decision, dest, revAbandoned]
                    del raProps['reciprocal']

    def getReciprocalPair(
        self,
        decision: Decision,
        transition: Transition
    ) -> Optional[Tuple[Decision, Transition]]:
        """
        Returns a tuple containing both the destination decision and the
        transition at that decision which is the reciprocal of the
        specified destination & transition. Returns `None` if no
        reciprocal has been established for that transition, or if that
        decision or transition does not exist.

        TODO: TEST ME
        """
        reciprocal = self.getReciprocal(decision, transition)
        if reciprocal is None:
            return None
        else:
            destination = self.getDestination(decision, transition)
            if destination is None:
                return None
            else:
                return (destination, reciprocal)

    def isUnknown(self, decision: Decision) -> bool:
        """
        Returns True if the specified decision is an 'unknown' decision
        (i.e., if has the 'unknown' tag) and False otherwise. These
        decisions represent unknown territory rather than a real visited
        part of the graph, although their names may be known already and
        some of their properties may be known.
        """
        return 'unknown' in self.decisionTags(decision)

    def setUnknown(self, decision: Decision, setUnknown: bool = True):
        """
        Sets the unknown status of a decision according to the given
        boolean (default True). Does nothing if the unknown status
        already matched the desired status.
        """
        if setUnknown:
            self.tagDecision(decision, 'unknown')
        else:
            self.untagDecision(decision, 'unknown')

    def addDecision(
        self,
        name: Decision,
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None
    ) -> None:
        """
        Adds a decision to the graph, without any transitions yet. Each
        decision needs a unique name. A set of tags and/or a list of
        annotations (strings in both cases) may be provided.

        Raises a `DecisionCollisionError` if a decision with the provided
        name already exists (decision names must be unique).
        """
        # Defaults
        if tags is None:
            tags = set()
        if annotations is None:
            annotations = []

        # Error checking
        if name in self:
            raise DecisionCollisionError(
                f"Cannot add decision '{name}': That decision already"
                f" exists."
            )

        # Add the decision
        self.add_node(name, tags=tags, ann=annotations)

    def addTransition(
        self,
        fromDecision: Decision,
        name: Transition,
        toDecision: Decision,
        revName: Optional[Transition] = None,
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None,
        revTags: Optional[Set[Tag]] = None,
        revAnnotations: Optional[List[Annotation]] = None,
        requires: Union[Requirement, str, None] = None,
        effects: Optional[List[TransitionEffect]] = None,
        revRequires: Union[Requirement, str, None] = None,
        revEffects: Optional[List[TransitionEffect]] = None
    ) -> None:
        """
        Adds a transition connecting two decisions. The name of each
        decision is required, as is a name for the transition. If a
        `revName` is provided, a reciprocal edge will be added in the
        opposite direction using that name; by default only the specified
        edge is added. A `TransitionCollisionError` will be raised if the
        `revName` matches the name of an existing edge at the destination
        decision.

        Both decisions must already exist, or a `MissingDecisionError`
        will be raised.

        A set of tags and/or a list of annotations (strings in both
        cases) may be provided. Tags and/or annotations for the reverse
        edge may also be specified if one is being added.

        The `requires`, `effects`, `revRequires`, and `revEffects`
        arguments specify requirements and/or effects of the new outgoing
        and reciprocal edges.
        """
        # Defaults
        if tags is None:
            tags = set()
        if annotations is None:
            annotations = []
        if revTags is None:
            revTags = set()
        if revAnnotations is None:
            revAnnotations = []

        # Error checking
        if fromDecision not in self:
            raise MissingDecisionError(
                f"Cannot add a transition from '{fromDecision}' to"
                f" '{toDecision}': '{fromDecision}' does not exist."
            )

        if toDecision not in self:
            raise MissingDecisionError(
                f"Cannot add a transition from '{fromDecision}' to"
                f" '{toDecision}': '{toDecision}' does not exist."
            )

        # Note: have to check this first so we don't add the forward edge
        # and then error out after a side effect!
        if (
            revName is not None
        and self.getDestination(toDecision, revName) is not None
        ):
            raise TransitionCollisionError(
                f"Cannot add a transition from '{fromDecision}' to"
                f" '{toDecision}' with reciprocal edge '{revName}':"
                f" '{revName}' is already used as an edge name at"
                f" '{toDecision}'."
            )

        # Add the edge
        self.add_edge(
            fromDecision,
            toDecision,
            key=name,
            tags=tags,
            ann=annotations
        )
        self.setTransitionRequirement(fromDecision, name, requires)
        if effects is not None:
            self.setTransitionEffects(fromDecision, name, effects)
        if revName is not None:
            # Add the reciprocal edge
            self.add_edge(
                toDecision,
                fromDecision,
                key=revName,
                tags=revTags,
                ann=revAnnotations
            )
            self.setReciprocal(fromDecision, name, revName)
            self.setTransitionRequirement(toDecision, revName, revRequires)
            if revEffects is not None:
                self.setTransitionEffects(toDecision, revName, revEffects)

    def removeTransition(
        self,
        fromDecision: Decision,
        transition: Transition,
        removeReciprocal=False
    ) -> Union[
        TransitionProperties,
        Tuple[TransitionProperties, TransitionProperties]
    ]:
        """
        Removes a transition. If `removeReciprocal` is true (False is the
        default) any reciprocal transition will also be removed (but no
        error will occur if there wasn't a reciprocal).

        For each removed transition, *every* transition that targeted
        that transition as its reciprocal will have its reciprocal set to
        `None`, to avoid leaving any invalid reciprocal values.

        Raises a `KeyError` if either the target decision or the target
        transition does not exist.

        Returns a transition properties dictionary with the properties
        of the removed transition, or if `removeReciprocal` is true,
        returns a pair of such dictionaries for the target transition
        and its reciprocal.

        ## Example

        >>> g = DecisionGraph()
        >>> g.addDecision('A')
        >>> g.addDecision('B')
        >>> g.addTransition('A', 'up', 'B', 'down', tags={'wide'})
        >>> g.addTransition('A', 'in', 'B', 'out') # we won't touch this
        >>> g.addTransition('A', 'next', 'B')
        >>> g.setReciprocal('A', 'next', 'down', setBoth=False)
        >>> p = g.removeTransition('A', 'up')
        >>> p['tags']
        {'wide'}
        >>> g.destinationsFrom('A')
        {'in': 'B', 'next': 'B'}
        >>> g.destinationsFrom('B')
        {'down': 'A', 'out': 'A'}
        >>> g.getReciprocal('B', 'down') is None
        True
        >>> g.getReciprocal('A', 'next') # Asymmetrical left over
        'down'
        >>> g.getReciprocal('A', 'in') # not affected
        'out'
        >>> g.getReciprocal('B', 'out') # not affected
        'in'
        >>> # Now with removeReciprocal set to True
        >>> g.addTransition('A', 'up', 'B') # add this back in
        >>> g.setReciprocal('A', 'up', 'down') # sets both
        >>> p = g.removeTransition('A', 'up', removeReciprocal=True)
        >>> g.destinationsFrom('A')
        {'in': 'B', 'next': 'B'}
        >>> g.destinationsFrom('B')
        {'out': 'A'}
        >>> g.getReciprocal('A', 'next') is None
        True
        >>> g.getReciprocal('A', 'in') # not affected
        'out'
        >>> g.getReciprocal('B', 'out') # not affected
        'in'
        >>> g.removeTransition('A', 'none')
        Traceback (most recent call last):
        ...
        exploration.core.MissingTransitionError...
        >>> g.removeTransition('Z', 'nope')
        Traceback (most recent call last):
        ...
        exploration.core.MissingDecisionError...
        """
        # raises if either is missing:
        destination = self.destination(fromDecision, transition)
        reciprocal = self.getReciprocal(fromDecision, transition)

        # Get dictionaries of parallel & antiparallel edges to be
        # checked for invalid reciprocals after removing edges
        # Note: these will update live as we remove edges
        allAntiparallel = self[destination][fromDecision]
        allParallel = self[fromDecision][destination]

        # Remove the target edge
        fProps = self.getTransitionProperties(fromDecision, transition)
        self.remove_edge(fromDecision, destination, transition)

        # Clean up any dangling reciprocal values
        for tProps in allAntiparallel.values():
            if tProps.get('reciprocal') == transition:
                del tProps['reciprocal']

        # Remove the reciprocal if requested
        if removeReciprocal and reciprocal is not None:
            rProps = self.getTransitionProperties(destination, reciprocal)
            self.remove_edge(destination, fromDecision, reciprocal)

            # Clean up any dangling reciprocal values
            for tProps in allParallel.values():
                if tProps.get('reciprocal') == reciprocal:
                    del tProps['reciprocal']

            return (fProps, rProps)
        else:
            return fProps

    def addUnexploredEdge(
        self,
        fromDecision: Decision,
        name: Transition,
        destinationName: Optional[Decision] = None,
        reciprocal: Optional[Transition] = 'return',
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None,
        revTags: Optional[Set[Tag]] = None,
        revAnnotations: Optional[List[Annotation]] = None,
        requires: Union[Requirement, str, None] = None,
        effects: Optional[List[TransitionEffect]] = None,
        revRequires: Union[Requirement, str, None] = None,
        revEffects: Optional[List[TransitionEffect]] = None
    ) -> Decision:
        """
        Adds a transition connecting to a new decision named `'_u.-n-'`
        where '-n-' is the number of unknown decisions (named or not)
        that have ever been created in this graph (or using the
        specified destination name if one is provided). This represents
        a transition to an unknown destination. Also adds a reciprocal
        transition in the reverse direction, unless `reciprocal` is set
        to `None`. The reciprocal will use provided name (default is
        'return').

        The name of the decision that was created is returned.

        A `MissingDecisionError` will be raised if the starting decision
        does not exist, a `TransitionCollisionError` will be raised if
        it exists but already has a transition with the given name, and a
        `DecisionCollisionError` will be raised if a decision with the
        specified destination name already exists (won't happen when
        using an automatic name).

        Lists of tags and/or annotations (strings in both cases) may be
        provided. These may also be provided for the reciprocal edge.
        The created node will always be tagged with `'unknown'`.

        Similarly, requirements and/or effects for either edge may be
        provided.

        ## Example

        >>> g = DecisionGraph()
        >>> g.addDecision('A')
        >>> g.addUnexploredEdge('A', 'up')
        '_u.0'
        >>> g.addUnexploredEdge('A', 'right', 'B')
        'B'
        >>> g.addUnexploredEdge('A', 'down', None, 'up')
        '_u.2'
        >>> g.addUnexploredEdge(
        ...    '_u.0',
        ...    'beyond',
        ...    tags={'fast'},
        ...    revTags={'slow'},
        ...    annotations=['comment'],
        ...    revAnnotations=['one', 'two'],
        ...    requires=ReqPower('dash'),
        ...    revRequires=ReqPower('super dash'),
        ...    effects=[effect(gain='super dash')],
        ...    revEffects=[effect(lose='super dash')]
        ... )
        '_u.3'
        >>> g.transitionTags('_u.0', 'beyond')
        {'fast'}
        >>> g.transitionAnnotations('_u.0', 'beyond')
        ['comment']
        >>> g.getTransitionRequirement('_u.0', 'beyond')
        ReqPower('dash')
        >>> e = g.getTransitionEffects('_u.0', 'beyond')
        >>> e == [effect(gain='super dash')]
        True
        >>> g.transitionTags('_u.3', 'return')
        {'slow'}
        >>> g.transitionAnnotations('_u.3', 'return')
        ['one', 'two']
        >>> g.getTransitionRequirement('_u.3', 'return')
        ReqPower('super dash')
        >>> e = g.getTransitionEffects('_u.3', 'return')
        >>> e == [effect(lose='super dash')]
        True
        """
        # Defaults
        if tags is None:
            tags = set()
        if annotations is None:
            annotations = []
        if revTags is None:
            revTags = set()
        if revAnnotations is None:
            revAnnotations = []

        # Error checking
        if fromDecision not in self:
            raise MissingDecisionError(
                f"Cannot add a new unexplored edge '{name}' to"
                f" '{fromDecision}': That decision does not exist."
            )

        if name in self.destinationsFrom(fromDecision):
            raise TransitionCollisionError(
                f"Cannot add a new edge '{name}': '{fromDecision}'"
                f" already has an outgoing edge with that name."
            )

        if destinationName in self:
            raise DecisionCollisionError(
                f"Cannot add a new unexplored node '{destinationName}':"
                f" A decision with that name already exists.\n(Leave"
                f" destinationName as None to use an automatic name.)"
            )

        # Create the new unexplored decision and add the edge
        if destinationName is None:
            toName = '_u.' + str(self.unknownCount)
        else:
            toName = destinationName
        self.unknownCount += 1
        self.addDecision(toName, tags={'unknown'}, annotations=[])
        self.addTransition(
            fromDecision,
            name,
            toName,
            tags=tags,
            annotations=annotations
        )
        self.setTransitionRequirement(fromDecision, name, requires)
        if effects is not None:
            self.setTransitionEffects(fromDecision, name, effects)

        # Create the reciprocal edge
        if reciprocal is not None:
            self.addTransition(
                toName,
                reciprocal,
                fromDecision,
                tags=revTags,
                annotations=revAnnotations
            )
            self.setTransitionRequirement(toName, reciprocal, revRequires)
            if revEffects is not None:
                self.setTransitionEffects(toName, reciprocal, revEffects)
            # Set as a reciprocal
            self.setReciprocal(fromDecision, name, reciprocal)

        # Return name of destination
        return toName

    def retargetTransition(
        self,
        fromDecision: Decision,
        transition: Transition,
        newDestination: Decision,
        swapReciprocal=True,
        errorOnNameColision=True
    ) -> Optional[Transition]:
        """
        Given a particular decision and a transition at that decision,
        changes that transition so that it goes to the specified new
        destination instead of wherever it was connected to before. If
        the new destination is the same as the old one, no changes are
        made.

        If `swapReciprocal` is set to True (the default) then any
        reciprocal edge at the old destination will be deleted, and a
        new reciprocal edge from the new destination with equivalent
        properties to the original reciprocal will be created, pointing
        to the origin of the specified transition. If `swapReciprocal`
        is set to False, then the reciprocal relationship with any old
        reciprocal edge will be removed, but the old reciprocal edge
        will not be changed.

        Note that if `errorOnNameColision` is True (the default), then
        if the reciprocal transition has the same name as a transition
        which already exists at the new destination node, a
        `TransitionCollisionError` will be thrown. However, if it is set
        to False, the reciprocal transition will be renamed with a suffix
        to avoid any possible name collisions. Either way, the name of
        the reciprocal transition (possibly just changed) will be
        returned, or None if there was no reciprocal transition.

        ## Example

        >>> g = DecisionGraph()
        >>> for fr, to, nm in [
        ...     ('A', 'B', 'up'),
        ...     ('A', 'B', 'up2'),
        ...     ('B', 'A', 'down'),
        ...     ('B', 'B', 'self'),
        ...     ('B', 'C', 'next'),
        ...     ('C', 'B', 'prev')
        ... ]:
        ...     if fr not in g:
        ...        g.addDecision(fr)
        ...     if to not in g:
        ...         g.addDecision(to)
        ...     g.addTransition(fr, nm, to)
        >>> g.setReciprocal('A', 'up', 'down')
        >>> g.setReciprocal('B', 'next', 'prev')
        >>> g.destination('A', 'up')
        'B'
        >>> g.destination('B', 'down')
        'A'
        >>> g.retargetTransition('A', 'up', 'C')
        'down'
        >>> g.destination('A', 'up')
        'C'
        >>> g.getDestination('B', 'down') is None
        True
        >>> g.destination('C', 'down')
        'A'
        >>> g.addTransition('A', 'next', 'B')
        >>> g.addTransition('B', 'prev', 'A')
        >>> g.setReciprocal('A', 'next', 'prev')
        >>> # Can't swap a reciprocal in a way that would collide names
        >>> g.getReciprocal('C', 'prev')
        'next'
        >>> g.retargetTransition('C', 'prev', 'A')
        Traceback (most recent call last):
        ...
        exploration.core.TransitionCollisionError...
        >>> g.retargetTransition('C', 'prev', 'A', swapReciprocal=False)
        'next'
        >>> g.destination('C', 'prev')
        'A'
        >>> g.destination('A', 'next') # not changed
        'B'
        >>> # Reciprocal relationship is severed:
        >>> g.getReciprocal('C', 'prev') is None
        True
        >>> g.getReciprocal('B', 'next') is None
        True
        >>> # Swap back so we can do another demo
        >>> g.retargetTransition('C', 'prev', 'B', swapReciprocal=False)
        >>> # Note return value was None here because there was no reciprocal
        >>> g.setReciprocal('C', 'prev', 'next')
        >>> # Swap reciprocal by renaming it
        >>> g.retargetTransition('C', 'prev', 'A', errorOnNameColision=False)
        'next.1'
        >>> g.getReciprocal('C', 'prev')
        'next.1'
        >>> g.destination('C', 'prev')
        'A'
        >>> g.destination('A', 'next.1')
        'C'
        >>> g.destination('A', 'next')
        'B'
        >>> # Note names are the same but these are from different nodes
        >>> g.getReciprocal('A', 'next')
        'prev'
        >>> g.getReciprocal('A', 'next.1')
        'prev'
        """
        # Figure out the old destination of the transition we're swapping
        oldDestination = self.destination(fromDecision, transition)
        reciprocal = self.getReciprocal(fromDecision, transition)

        # If thew new destination is the same, we don't do anything!
        if oldDestination == newDestination:
            return reciprocal

        # First figure out reciprocal business so we can error out
        # without making changes if we need to
        if swapReciprocal and reciprocal is not None:
            reciprocal = self.rebaseTransition(
                oldDestination,
                reciprocal,
                newDestination,
                swapReciprocal=False,
                errorOnNameColision=errorOnNameColision
            )

        # Handle the forward transition...
        # Find the transition properties
        tProps = self.getTransitionProperties(fromDecision, transition)

        # Delete the edge
        self.removeEdgeByKey(fromDecision, transition)

        # Add the new edge
        self.addTransition(fromDecision, transition, newDestination)

        # Reapply the transition properties
        self.setTransitionProperties(fromDecision, transition, **tProps)

        # Handle the reciprocal transition if there is one...
        if reciprocal is not None:
            if not swapReciprocal:
                # Then sever the relationship, but only if that edge
                # still exists (we might be in the middle of a rebase)
                check = self.getDestination(oldDestination, reciprocal)
                if check is not None:
                    self.setReciprocal(
                        oldDestination,
                        reciprocal,
                        None,
                        setBoth=False # Other transition was deleted already
                    )
            else:
                # Establish new reciprocal relationship
                self.setReciprocal(
                    fromDecision,
                    transition,
                    reciprocal
                )

        return reciprocal

    def rebaseTransition(
        self,
        fromDecision: Decision,
        transition: Transition,
        newBase: Decision,
        swapReciprocal=True,
        errorOnNameColision=True
    ) -> Transition:
        """
        Given a particular destination and a transition at that
        destination, changes that transition's origin to a new base
        decision. If the new source is the same as the old one, no
        changes are made.

        If `swapReciprocal` is set to True (the default) then any
        reciprocal edge at the destination will be retargeted to point
        to the new source so that it can remain a reciprocal. If
        `swapReciprocal` is set to False, then the reciprocal
        relationship with any old reciprocal edge will be removed, but
        the old reciprocal edge will not be otherwise changed.

        Note that if `errorOnNameColision` is True (the default), then
        if the transition has the same name as a transition which
        already exists at the new source node, a
        `TransitionCollisionError` will be raised. However, if it is set
        to False, the transition will be renamed with a suffix to avoid
        any possible name collisions. Either way, the (possibly new) name
        of the transition that was rebased will be returned.

        ## Example

        >>> g = DecisionGraph()
        >>> for fr, to, nm in [
        ...     ('A', 'B', 'up'),
        ...     ('A', 'B', 'up2'),
        ...     ('B', 'A', 'down'),
        ...     ('B', 'B', 'self'),
        ...     ('B', 'C', 'next'),
        ...     ('C', 'B', 'prev')
        ... ]:
        ...     if fr not in g:
        ...        g.addDecision(fr)
        ...     if to not in g:
        ...         g.addDecision(to)
        ...     g.addTransition(fr, nm, to)
        >>> g.setReciprocal('A', 'up', 'down')
        >>> g.setReciprocal('B', 'next', 'prev')
        >>> g.destination('A', 'up')
        'B'
        >>> g.destination('B', 'down')
        'A'
        >>> g.rebaseTransition('B', 'down', 'C')
        'down'
        >>> g.destination('A', 'up')
        'C'
        >>> g.getDestination('B', 'down') is None
        True
        >>> g.destination('C', 'down')
        'A'
        >>> g.addTransition('A', 'next', 'B')
        >>> g.addTransition('B', 'prev', 'A')
        >>> g.setReciprocal('A', 'next', 'prev')
        >>> # Can't rebase in a way that would collide names
        >>> g.rebaseTransition('B', 'next', 'A')
        Traceback (most recent call last):
        ...
        exploration.core.TransitionCollisionError...
        >>> g.rebaseTransition('B', 'next', 'A', errorOnNameColision=False)
        'next.1'
        >>> g.destination('C', 'prev')
        'A'
        >>> g.destination('A', 'next') # not changed
        'B'
        >>> # Collision is avoided by renaming
        >>> g.destination('A', 'next.1')
        'C'
        >>> # Swap without reciprocal
        >>> g.getReciprocal('A', 'next.1')
        'prev'
        >>> g.getReciprocal('C', 'prev')
        'next.1'
        >>> g.rebaseTransition('A', 'next.1', 'B', swapReciprocal=False)
        'next.1'
        >>> g.getReciprocal('C', 'prev') is None
        True
        >>> g.destination('C', 'prev')
        'A'
        >>> g.getDestination('A', 'next.1') is None
        True
        >>> g.destination('A', 'next')
        'B'
        >>> g.destination('B', 'next.1')
        'C'
        >>> g.getReciprocal('B', 'next.1') is None
        True
        >>> # Rebase in a way that creates a self-edge
        >>> g.rebaseTransition('A', 'next', 'B')
        'next'
        >>> g.getDestination('A', 'next') is None
        True
        >>> g.destination('B', 'next')
        'B'
        >>> g.destination('B', 'prev') # swapped as a reciprocal
        'B'
        >>> g.getReciprocal('B', 'next') # still reciprocals
        'prev'
        >>> g.getReciprocal('B', 'prev')
        'next'
        >>> # And rebasing of a self-edge also works
        >>> g.rebaseTransition('B', 'prev', 'A')
        'prev'
        >>> g.destination('A', 'prev')
        'B'
        >>> g.destination('B', 'next')
        'A'
        >>> g.getReciprocal('B', 'next') # still reciprocals
        'prev'
        >>> g.getReciprocal('A', 'prev')
        'next'
        >>> # We've effectively reversed this edge/reciprocal pair
        >>> # by rebasing twice
        """
        # If thew new base is the same, we don't do anything!
        if newBase == fromDecision:
            return transition

        # First figure out reciprocal business so we can swap it later
        # without making changes if we need to
        destination = self.destination(fromDecision, transition)
        reciprocal = self.getReciprocal(fromDecision, transition)
        # Check for an already-deleted reciprocal
        if (
            reciprocal is not None
        and self.getDestination(destination, reciprocal) is None
        ):
            reciprocal = None

        # Handle the base swap...
        # Find the transition properties
        tProps = self.getTransitionProperties(fromDecision, transition)

        # Check for a collision
        targetDestinations = self.destinationsFrom(newBase)
        collision = transition in targetDestinations
        if collision:
            if errorOnNameColision:
                raise TransitionCollisionError(
                    f"Cannot rebase transition '{transition}' from"
                    f" '{fromDecision}': it would be a duplicate"
                    f" transition name at the new base decision"
                    f" '{newBase}'."
                )
            else:
                # Figure out a good fresh name
                newName = uniqueName(
                    transition,
                    targetDestinations
                )
        else:
            newName = transition

        # Delete the edge
        self.removeEdgeByKey(fromDecision, transition)

        # Add the new edge
        self.addTransition(newBase, newName, destination)

        # Reapply the transition properties
        self.setTransitionProperties(newBase, newName, **tProps)

        # Handle the reciprocal transition if there is one...
        if reciprocal is not None:
            if not swapReciprocal:
                # Then sever the relationship
                self.setReciprocal(
                    destination,
                    reciprocal,
                    None,
                    setBoth=False # Other transition was deleted already
                )
            else:
                # Otherwise swap the reciprocal edge
                self.retargetTransition(
                    destination,
                    reciprocal,
                    newBase,
                    swapReciprocal=False
                )

                # And establish a new reciprocal relationship
                self.setReciprocal(
                    newBase,
                    newName,
                    reciprocal
                )

        # Return the new name in case it was changed
        return newName

    # TODO: zone merging!

    # TODO: Double-check that explroation vars get updated when this is
    # called!
    def mergeDecisions(
        self,
        merge: Decision,
        mergeInto: Decision,
        errorOnNameColision=True
    ) -> Dict[Transition, Transition]:
        """
        Merges two decisions, deleting the first after transferring all
        of its incoming and outgoing edges to target the second one,
        whose name is retained. The second decision will be added to any
        zones that the first decision was a member of. If either decision
        does not exist, a `MissingDecisionError` will be raised. If
        `merge` and `mergeInto` are the same, then nothing will be
        changed.

        Unless `errorOnNameColision` is set to False, a
        `TransitionCollisionError` will be raised if the two decisions
        have outgoing transitions with the same name. If
        `errorOnNameColision` is set to False, then such edges will be
        renamed using a suffix to avoid name collisions, with edges
        connected to the second decision retaining their original names
        and edges that were connected to the first decision getting
        renamed.

        The tags and annotations of the merged decision are added to the
        tags and annotations of the merge target. If this is undesired
        behavior, clear the tags/annotations of the merged decision
        before the merge.

        Returns a dictionary mapping each original transition name to
        its new name in cases where transitions get renamed; this will
        be empty when no re-naming occurs, including when
        `errorOnNameColision` is True. If there were any transitions
        connecting the nodes that were merged, these become self-edges
        of the merged node (and may be renamed if necessary).
        Note that all renamed transitions were originally based on the
        first (merged) node, since transitions of the second (merge
        target) node are not renamed.

        ## Example

        >>> g = DecisionGraph()
        >>> for fr, to, nm in [
        ...     ('A', 'B', 'up'),
        ...     ('A', 'B', 'up2'),
        ...     ('B', 'A', 'down'),
        ...     ('B', 'B', 'self'),
        ...     ('B', 'C', 'next'),
        ...     ('C', 'B', 'prev'),
        ...     ('A', 'C', 'right')
        ... ]:
        ...     if fr not in g:
        ...        g.addDecision(fr)
        ...     if to not in g:
        ...         g.addDecision(to)
        ...     g.addTransition(fr, nm, to)
        >>> sorted(g)
        ['A', 'B', 'C']
        >>> g.setReciprocal('A', 'up', 'down')
        >>> g.setReciprocal('B', 'next', 'prev')
        >>> g.mergeDecisions('C', 'B')
        {}
        >>> g.destinationsFrom('A')
        {'up': 'B', 'up2': 'B', 'right': 'B'}
        >>> g.destinationsFrom('B')
        {'down': 'A', 'self': 'B', 'prev': 'B', 'next': 'B'}
        >>> 'C' in g
        False
        >>> g.mergeDecisions('A', 'A') # does nothing
        {}
        >>> # Can't merge non-existent decision
        >>> g.mergeDecisions('A', 'Z')
        Traceback (most recent call last):
        ...
        exploration.core.MissingDecisionError...
        >>> g.mergeDecisions('Z', 'A')
        Traceback (most recent call last):
        ...
        exploration.core.MissingDecisionError...
        >>> # Can't merge decisions w/ shared edge names
        >>> g.addDecision('D')
        >>> g.addTransition('D', 'next', 'A')
        >>> g.addTransition('A', 'prev', 'D')
        >>> g.setReciprocal('D', 'next', 'prev')
        >>> g.mergeDecisions('D', 'B') # both have a 'next' transition
        Traceback (most recent call last):
        ...
        exploration.core.TransitionCollisionError...
        >>> # Auto-rename colliding edges
        >>> g.mergeDecisions('D', 'B', errorOnNameColision=False)
        {'next': 'next.1'}
        >>> g.destination('B', 'next') # merge target unchanged
        'B'
        >>> g.destination('B', 'next.1') # merged decision name changed
        'A'
        >>> g.destination('B', 'prev') # name unchanged (no collision)
        'B'
        >>> g.getReciprocal('B', 'next') # unchanged (from B)
        'prev'
        >>> g.getReciprocal('B', 'next.1') # from A
        'prev'
        >>> g.getReciprocal('A', 'prev') # from B
        'next.1'

        ## Folding four nodes into a 2-node loop

        >>> g = DecisionGraph()
        >>> g.addDecision('X')
        >>> g.addDecision('Y')
        >>> g.addTransition('X', 'next', 'Y', 'prev')
        >>> g.addDecision('preX')
        >>> g.addDecision('postY')
        >>> g.addTransition('preX', 'next', 'X', 'prev')
        >>> g.addTransition('Y', 'next', 'postY', 'prev')
        >>> g.mergeDecisions('preX', 'Y', errorOnNameColision=False)
        {'next': 'next.1'}
        >>> g.destinationsFrom('X')
        {'next': 'Y', 'prev': 'Y'}
        >>> g.destinationsFrom('Y')
        {'prev': 'X', 'next': 'postY', 'next.1': 'X'}
        >>> 'preX' in g
        False
        >>> g.destinationsFrom('postY')
        {'prev': 'Y'}
        >>> g.mergeDecisions('postY', 'X', errorOnNameColision=False)
        {'prev': 'prev.1'}
        >>> g.destinationsFrom('X')
        {'next': 'Y', 'prev': 'Y', 'prev.1': 'Y'}
        >>> g.destinationsFrom('Y') # order 'cause of 'next' re-target
        {'prev': 'X', 'next.1': 'X', 'next': 'X'}
        >>> 'preX' in g
        False
        >>> 'postY' in g
        False
        >>> # Reciprocals are tangled...
        >>> g.getReciprocal('X', 'prev')
        'next.1'
        >>> g.getReciprocal('X', 'prev.1')
        'next'
        >>> g.getReciprocal('Y', 'next')
        'prev.1'
        >>> g.getReciprocal('Y', 'next.1')
        'prev'
        >>> # Note: one merge cannot handle both extra transitions
        >>> # because their reciprocals are crossed (e.g., prev.1 <-> next)
        >>> # (It would merge both edges but the result would retain
        >>> # 'next.1' instead of retaining 'next'.)
        >>> g.mergeTransitions('X', 'prev.1', 'prev', mergeReciprocal=False)
        >>> g.mergeTransitions('Y', 'next.1', 'next', mergeReciprocal=True)
        >>> g.destinationsFrom('X')
        {'next': 'Y', 'prev': 'Y'}
        >>> g.destinationsFrom('Y')
        {'prev': 'X', 'next': 'X'}
        >>> # Reciprocals were salvaged in second merger
        >>> g.getReciprocal('X', 'prev')
        'next'
        >>> g.getReciprocal('Y', 'next')
        'prev'
        """
        # Create our result as an empty dictionary
        result: Dict[Transition, Transition] = {}

        # Short-circuit if the two decisions are the same
        if merge == mergeInto:
            return result

        # MissingDecisionErrors from here if either doesn't exist
        allNewOutgoing = set(self.destinationsFrom(merge))
        allOldOutgoing = set(self.destinationsFrom(mergeInto))
        # Find colliding transition names
        collisions = allNewOutgoing & allOldOutgoing
        if len(collisions) > 0 and errorOnNameColision:
            raise TransitionCollisionError(
                f"Cannot merge decision '{merge}' into decision"
                f" '{mergeInto}': the decisions share {len(collisions)}"
                f" transition names: {collisions}\n(Note that"
                f" errorOnNameColision was set to True, set it to False"
                f" to allow the operation by renaming half of those"
                f" transitions.)"
            )

        # Record zones that will have to change after the merge
        zoneParents = self.zoneParents(merge)

        # First, swap all incoming edges, along with their reciprocals
        # This will include self-edges, which will be retargeted and
        # whose reciprocals will be rebased in the process, leading to
        # the possibility of a missing edge during the loop
        for source, incoming in self.allEdgesTo(merge):
            # Skip this edge if it was already swapped away because it's
            # a self-loop with a reciprocal whose reciprocal was
            # processed earlier in the loop
            if incoming not in self.destinationsFrom(source):
                continue

            # Find corresponding outgoing edge
            outgoing = self.getReciprocal(source, incoming)

            # Swap both edges to new destination
            newOutgoing = self.retargetTransition(
                source,
                incoming,
                mergeInto,
                swapReciprocal=True,
                errorOnNameColision=False # collisions were detected above
            )
            # Add to our result if the name of the reciprocal was
            # changed
            if (
                outgoing is not None
            and newOutgoing is not None
            and outgoing != newOutgoing
            ):
                result[outgoing] = newOutgoing

        # Next, swap any remaining outgoing edges (which didn't have
        # reciprocals, or they'd already be swapped, unless they were
        # self-edges previously). Note that in this loop, there can't be
        # any self-edges remaining, although there might be connections
        # between the merging nodes that need to become self-edges
        # because they used to be a self-edge that was half-retargeted
        # by the previous loop.
        # Note: a copy is used here to avoid iterating over a changing
        # dictionary
        for stillOutgoing in copy.copy(self.destinationsFrom(merge)):
            newOutgoing = self.rebaseTransition(
                merge,
                stillOutgoing,
                mergeInto,
                swapReciprocal=True,
                errorOnNameColision=False # collisions were detected above
            )
            if stillOutgoing != newOutgoing:
                result[stillOutgoing] = newOutgoing

        # At this point, there shouldn't be any remaining incoming or
        # outgoing edges!
        assert self.degree(merge) == 0

        # Merge tags & annotations
        # Note that these operations affect the underlying graph
        destTags = self.decisionTags(mergeInto)
        destTags |= self.decisionTags(merge)
        self.decisionAnnotations(mergeInto).extend(
            self.decisionAnnotations(merge)
        )

        # Transfer zones
        for zone in zoneParents:
            self.addDecisionToZone(mergeInto, zone)

        # Delete the old node
        self.removeDecision(merge)

        return result

    def removeDecision(self, decision: Decision) -> None:
        """
        Deletes the specified decision from the graph, updating
        attendant structures like zones.
        """
        # Remove the target from all zones:
        for zone in self.zones:
            self.removeDecisionFromZone(decision, zone)

        self.remove_node(decision)

    def renameDecision(
        self,
        decision: Decision,
        newName: Decision
    ):
        """
        Renames a decision. Note that this actually merges the old
        decision into a newly-created decision, so it both requires a
        substantial amount of work and might invalidate some of the
        active data structures like tag or annotation views.

        Raises a `DecisionCollisionError` if a decision using the new
        name already exists.

        Example:

        >>> g = DecisionGraph()
        >>> g.addDecision('one')
        >>> g.addDecision('three')
        >>> g.addTransition('one', '>', 'three')
        >>> g.addTransition('three', '<', 'one')
        >>> g.tagDecision('three', 'hi')
        >>> g.annotateDecision('three', 'note')
        >>> g.destination('one', '>')
        'three'
        >>> g.destination('three', '<')
        'one'
        >>> g.renameDecision('three', 'two')
        >>> g.destination('one', '>')
        'two'
        >>> g.getDestination('three', '<') is None
        True
        >>> g.destination('two', '<')
        'one'
        >>> g.decisionTags('two')
        {'hi'}
        >>> g.decisionAnnotations('two')
        ['note']
        """
        if newName in self:
            raise DecisionCollisionError(
                f"Can't rename '{decision}' as '{newName}' because a"
                f" decision with that name already exists."
            )
        self.addDecision(newName, tags=set(), annotations=[])
        self.mergeDecisions(decision, newName)

    def mergeTransitions(
        self,
        fromDecision: Decision,
        merge: Transition,
        mergeInto: Transition,
        mergeReciprocal=True
    ) -> None:
        """
        Given a decision and two transitions that start at that decision,
        merges the first transition into the second transition, combining
        their transition properties (using `mergeProperties`) and
        deleting the first transition. By default any reciprocal of the
        first transition is also merged into the reciprocal of the
        second, although you can set `mergeReciprocal` to `False` to
        disable this in which case the old reciprocal will lose its
        reciprocal relationship, even if the transition that was merged
        into does not have a reciprocal.

        If the two names provided are the same, nothing will happen.

        If the two transitions do not share the same destination, they
        cannot be merged, and an `InvalidDestinationError` will result.
        Use `retargetTransition` beforehand to ensure that they do if you
        want to merge transitions with different destinations.

        A `MissingDecisionError` or `MissingTransitionError` will result
        if the decision or either transition does not exist.

        If merging reciprocal properties was requested and the first
        transition does not have a reciprocal, then no reciprocal
        properties change. However, if the second transition does not
        have a reciprocal and the first does, the first transition's
        reciprocal will be set to the reciprocal of the second
        transition, and that transition will not be deleted as usual.

        ## Example

        >>> g = DecisionGraph()
        >>> g.addDecision('A')
        >>> g.addDecision('B')
        >>> g.addTransition('A', 'up', 'B')
        >>> g.addTransition('B', 'down', 'A')
        >>> g.setReciprocal('A', 'up', 'down')
        >>> # Merging a transition with no reciprocal
        >>> g.addTransition('A', 'up2', 'B')
        >>> g.mergeTransitions('A', 'up2', 'up')
        >>> g.getDestination('A', 'up2') is None
        True
        >>> g.getDestination('A', 'up')
        'B'
        >>> # Merging a transition with a reciprocal & tags
        >>> g.addTransition('A', 'up2', 'B')
        >>> g.addTransition('B', 'down2', 'A')
        >>> g.setReciprocal('A', 'up2', 'down2')
        >>> g.tagTransition('A', 'up2', 'one')
        >>> g.tagTransition('B', 'down2', 'two')
        >>> g.mergeTransitions('B', 'down2', 'down')
        >>> g.getDestination('A', 'up2') is None
        True
        >>> g.getDestination('A', 'up')
        'B'
        >>> g.getDestination('B', 'down2') is None
        True
        >>> g.getDestination('B', 'down')
        'A'
        >>> # Merging requirements uses ReqAll (i.e., 'and' logic)
        >>> g.addTransition('A', 'up2', 'B')
        >>> g.setTransitionProperties('A', 'up2', requirement=ReqPower('dash'))
        >>> g.setTransitionProperties('A', 'up', requirement=ReqPower('slide'))
        >>> g.mergeTransitions('A', 'up2', 'up')
        >>> g.getDestination('A', 'up2') is None
        True
        >>> repr(g.getTransitionRequirement('A', 'up'))
        "ReqAll([ReqPower('dash'), ReqPower('slide')])"
        >>> # Errors if destinations differ, or if something is missing
        >>> g.mergeTransitions('A', 'down', 'up')
        Traceback (most recent call last):
        ...
        exploration.core.MissingTransitionError...
        >>> g.mergeTransitions('Z', 'one', 'two')
        Traceback (most recent call last):
        ...
        exploration.core.MissingDecisionError...
        >>> g.addDecision('C')
        >>> g.addTransition('A', 'down', 'C')
        >>> g.mergeTransitions('A', 'down', 'up')
        Traceback (most recent call last):
        ...
        exploration.core.InvalidDestinationError...
        >>> # Merging a reciprocal onto an edge that doesn't have one
        >>> g.addTransition('A', 'down2', 'C')
        >>> g.addTransition('C', 'up2', 'A')
        >>> g.setReciprocal('A', 'down2', 'up2')
        >>> g.tagTransition('C', 'up2', 'narrow')
        >>> g.getReciprocal('A', 'down') is None
        True
        >>> g.mergeTransitions('A', 'down2', 'down')
        >>> g.getDestination('A', 'down2') is None
        True
        >>> g.getDestination('A', 'down')
        'C'
        >>> g.getDestination('C', 'up2')
        'A'
        >>> g.getReciprocal('A', 'down')
        'up2'
        >>> g.getReciprocal('C', 'up2')
        'down'
        >>> g.transitionTags('C', 'up2')
        {'narrow'}
        >>> # Merging without a reciprocal
        >>> g.addTransition('C', 'up', 'A')
        >>> g.mergeTransitions('C', 'up2', 'up', mergeReciprocal=False)
        >>> g.getDestination('C', 'up2') is None
        True
        >>> g.getDestination('C', 'up')
        'A'
        >>> g.transitionTags('C', 'up') # tag gets merged
        {'narrow'}
        >>> g.getDestination('A', 'down')
        'C'
        >>> g.getReciprocal('A', 'down') is None
        True
        >>> g.getReciprocal('C', 'up') is None
        True
        >>> # Merging w/ normal reciprocals
        >>> g.addDecision('D')
        >>> g.addDecision('E')
        >>> g.addTransition('D', 'up', 'E', 'return')
        >>> g.addTransition('E', 'down', 'D')
        >>> g.mergeTransitions('E', 'return', 'down')
        >>> g.getDestination('D', 'up')
        'E'
        >>> g.getDestination('E', 'down')
        'D'
        >>> g.getDestination('E', 'return') is None
        True
        >>> g.getReciprocal('D', 'up')
        'down'
        >>> g.getReciprocal('E', 'down')
        'up'
        >>> # Merging w/ weird reciprocals
        >>> g.addTransition('E', 'return', 'D')
        >>> g.setReciprocal('E', 'return', 'up', setBoth=False)
        >>> g.getReciprocal('D', 'up')
        'down'
        >>> g.getReciprocal('E', 'down')
        'up'
        >>> g.getReciprocal('E', 'return') # shared
        'up'
        >>> g.mergeTransitions('E', 'return', 'down')
        >>> g.getDestination('D', 'up')
        'E'
        >>> g.getDestination('E', 'down')
        'D'
        >>> g.getDestination('E', 'return') is None
        True
        >>> g.getReciprocal('D', 'up')
        'down'
        >>> g.getReciprocal('E', 'down')
        'up'
        """
        # Short-circuit in the no-op case
        if merge == mergeInto:
            return

        # These lines will raise a KeyError if needed
        # TODO: Convert it to a MissingDecisionError? Or do that inside?
        dest1 = self.destination(fromDecision, merge)
        dest2 = self.destination(fromDecision, mergeInto)

        if dest1 != dest2:
            raise InvalidDestinationError(
                f"Cannot merge transition '{merge}' into transition"
                f" '{mergeInto}' from decision '{fromDecision}' because"
                f" their destinations are different ('{dest1}' and"
                f" '{dest2}').\nNote: you can use `retargetTransition`"
                f" to change the destination of a transition."
            )

        # Find and the transition properties
        props1 = self.getTransitionProperties(fromDecision, merge)
        props2 = self.getTransitionProperties(fromDecision, mergeInto)
        merged = mergeProperties(props1, props2)
        # Note that this doesn't change the reciprocal:
        self.setTransitionProperties(fromDecision, mergeInto, **merged)

        # Merge the reciprocal properties if requested
        # Get reciprocal to merge into
        reciprocal = self.getReciprocal(fromDecision, mergeInto)
        # Get reciprocal that needs cleaning up
        altReciprocal = self.getReciprocal(fromDecision, merge)
        # If the reciprocal to be merged actually already was the
        # reciprocal to merge into, there's nothing to do here
        if altReciprocal != reciprocal:
            if not mergeReciprocal:
                # In this case, we sever the reciprocal relationship if
                # there is a reciprocal
                if altReciprocal is not None:
                    self.setReciprocal(dest1, altReciprocal, None)
                    # By default setBoth takes care of the other half
            else:
                # In this case, we try to merge reciprocals
                # If altReciprocal is None, we don't need to do anything
                if altReciprocal is not None:
                    # Was there already a reciprocal or not?
                    if reciprocal is None:
                        # altReciprocal becomes the new reciprocal and is
                        # not deleted
                        self.setReciprocal(
                            fromDecision,
                            mergeInto,
                            altReciprocal
                        )
                    else:
                        # merge reciprocal properties
                        props1 = self.getTransitionProperties(
                            dest1,
                            altReciprocal
                        )
                        props2 = self.getTransitionProperties(
                            dest2,
                            reciprocal
                        )
                        merged = mergeProperties(props1, props2)
                        self.setTransitionProperties(
                            dest1,
                            reciprocal,
                            **merged
                        )

                        # delete the old reciprocal transition
                        self.remove_edge(dest1, fromDecision, altReciprocal)

        # Delete the old transition (reciprocal deletion/severance is
        # handled above if necessary)
        self.remove_edge(fromDecision, dest1, merge)

    def replaceUnexplored(
        self,
        fromDecision: Decision,
        transition: Transition,
        connectTo: Optional[Decision] = None,
        revName: Optional[Transition] = None,
        requirement: Optional[Requirement] = None,
        applyEffects: Optional[List[TransitionEffect]] = None,
        placeInZone: Union[type[DefaultZone], Zone, type[None]] = None,
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None,
        revRequires: Union[Requirement, str, None] = None,
        revEffects: Optional[List[TransitionEffect]] = None,
        revTags: Optional[Set[Tag]] = None,
        revAnnotations: Optional[List[Annotation]] = None,
        decisionTags: Optional[Set[Tag]] = None,
        decisionAnnotations: Optional[List[Annotation]] = None
    ) -> Tuple[
        Dict[Transition, Transition],
        Dict[Transition, Transition]
    ]:
        """
        Given a decision and an edge name in that decision, where the
        named edge leads to an unexplored decision, replaces the
        unexplored decision on the other end of that edge with either a
        new decision using the given `connectTo` name, or if a decision
        using that name already exists, with that decision. If a
        `revName` is provided, a reciprocal edge will be added using
        that name connecting the `connectTo` decision back to the
        original decision. If this transition already exists, it must
        also point to an unexplored node, which will also be merged into
        the fromDecision node.

        If `connectTo` is not given (or is set to `None` explicitly)
        then the name of the unknown decision will not be changed,
        unless that name has the form `'_u.-n-'` where `-n-` is a
        positive integer (i.e., the form given to automatically-named
        unknown nodes). In that case, the name will be changed to
        `'_x.-n-'` using the same number, or a higher number if that
        name is already taken. In any case, the `'unknown'` tag will be
        removed from the decision.

        If a `placeInZone` is specified, the destination will be placed
        directly into that zone (even if it already existed and has zone
        information), and it will be removed from any other zones it had
        been a direct member of. If `placeInZone` is set to
        `DefaultZone`, then the destination will be placed into each zone
        which is a direct parent of the origin, but only if the
        destination is not an already-explored existing zone (in that
        case no zone changes are made). This will also remove it from
        any previous zones it had been a part of. If `placeInZone` is
        left as `None` (the default) no zone changes are made.

        If `placeInZone` is specified and that zone didn't already exist,
        it will be created as a new level-0 zone and will be added as a
        sub-zone of each zone that's a direct parent of any level-0 zone
        that the origin is a member of.

        Any additional edges pointing to or from the unknown node(s)
        being replaced will also be re-targeted at the now-discovered
        known destination(s). These edges will retain their reciprocal
        names, or if this would cause a name clash, they will be renamed
        with a suffix (see `retargetTransition`).

        The return value is a pair of dictionaries mapping old names to
        new ones that just includes the names which were changed. The
        first dictionary contains renamed transitions that are outgoing
        from the new destination node (which used to be outgoing from
        the unexplored node). The second dictionary contains renamed
        transitions that are outgoing from the source node (which used
        to be outgoing from the unexplored node attached to the
        reciprocal transition; if there was no reciprocal transition
        specified then this will always be an empty dictionary).

        An `UnknownDestinationError` will be raised if the destination
        of the specified transition is not an unknown decision (see
        `isUnknown`). An `UnknownDestinationError` will also be raised if
        the `connectTo`'s `revName` transition does not lead to an
        unknown decision (it's okay if this second transition doesn't
        exist). A `TransitionCollisionError` will be raised if the
        unknown destination decision already has an outgoing transition
        with the specified `revName` which does not lead back to the
        `fromDecision`.

        The transition properties (requirement and/or effects) of the
        replaced transition will be copied over to the new transition.
        Transition properties from the reciprocal transition will also
        be copied for the newly created reciprocal edge. Properties for
        any additional edges to/from the unknown node will also be
        copied.

        Also, any transition properties on existing forward or reciprocal
        edges from the destination node with the indicated reverse name
        will be merged with those from the target transition. Note that
        this merging process may introduce corruption of complex
        transition effects. TODO: Fix that!

        Any tags and annotations are added to copied tags/annotations,
        but specified requirements, and/or effects will replace previous
        requirements/effects, rather than being added to them.

        ## Example

        >>> g = DecisionGraph()
        >>> g.addDecision('A')
        >>> g.addUnexploredEdge('A', 'up')
        '_u.0'
        >>> g.destination('A', 'up')
        '_u.0'
        >>> g.destination('_u.0', 'return')
        'A'
        >>> g.replaceUnexplored('A', 'up', 'B', 'down')
        ({}, {})
        >>> g.destination('A', 'up')
        'B'
        >>> g.destination('B', 'down')
        'A'
        >>> g.getDestination('B', 'return') is None
        True
        >>> '_u.0' in g
        False
        >>> g.getReciprocal('A', 'up')
        'down'
        >>> g.getReciprocal('B', 'down')
        'up'
        >>> # Two unexplored edges to the same node:
        >>> g.addDecision('C')
        >>> g.addTransition('B', 'next', 'C')
        >>> g.addTransition('C', 'prev', 'B')
        >>> g.setReciprocal('B', 'next', 'prev')
        >>> g.addUnexploredEdge('A', 'next', 'D', 'prev')
        'D'
        >>> g.addTransition('C', 'down', 'D')
        >>> g.addTransition('D', 'up', 'C')
        >>> g.setReciprocal('C', 'down', 'up')
        >>> g.replaceUnexplored('C', 'down')
        ({}, {})
        >>> g.destination('C', 'down')
        'D'
        >>> g.destination('A', 'next')
        'D'
        >>> g.destinationsFrom('D')
        {'prev': 'A', 'up': 'C'}
        >>> g.decisionTags('D')
        set()
        >>> # An unexplored transition which turns out to connect to a
        >>> # known decision, with name collisions
        >>> g.addUnexploredEdge('D', 'next', reciprocal='prev')
        '_u.2'
        >>> g.tagDecision('_u.2', 'wet')
        >>> g.addUnexploredEdge('B', 'next', reciprocal='prev') # edge taken
        Traceback (most recent call last):
        ...
        exploration.core.TransitionCollisionError...
        >>> g.addUnexploredEdge('A', 'prev', reciprocal='next')
        '_u.3'
        >>> g.tagDecision('_u.3', 'dry')
        >>> # Add transitions that will collide when merged
        >>> g.addUnexploredEdge('_u.2', 'up') # collides with A/up
        '_u.4'
        >>> g.addUnexploredEdge('_u.3', 'prev') # collides with D/prev
        '_u.5'
        >>> g.replaceUnexplored('A', 'prev', 'D', 'next') # two decisions gone
        ({'prev': 'prev.1'}, {'up': 'up.1'})
        >>> g.destination('A', 'prev')
        'D'
        >>> g.destination('D', 'next')
        'A'
        >>> g.getReciprocal('A', 'prev')
        'next'
        >>> g.getReciprocal('D', 'next')
        'prev'
        >>> # Note that further unexplored structures are NOT merged
        >>> # even if they match against existing structures...
        >>> g.destination('A', 'up.1')
        '_u.4'
        >>> g.destination('D', 'prev.1')
        '_u.5'
        >>> '_u.2' in g
        False
        >>> '_u.3' in g
        False
        >>> g.decisionTags('D') # tags are merged
        {'dry'}
        >>> g.decisionTags('A')
        {'wet'}
        >>> # Auto-renaming an anonymous unexplored node
        >>> g.addUnexploredEdge('B', 'out')
        '_u.6'
        >>> g.replaceUnexplored('B', 'out')
        ({}, {})
        >>> '_u.6' in g
        False
        >>> g.destination('B', 'out')
        '_x.6'
        >>> g.destination('_x.6', 'return')
        'B'
        >>> # Placing a node into a zone
        >>> g.addUnexploredEdge('B', 'through')
        '_u.7'
        >>> g.replaceUnexplored(
        ...     'B',
        ...     'through',
        ...     'E',
        ...     'back',
        ...     placeInZone='Zone'
        ... )
        ({}, {})
        >>> g.destination('B', 'through')
        'E'
        >>> g.destination('E', 'back')
        'B'
        >>> g.zoneParents('E')
        {'Zone'}
        """

        if tags is None:
            tags = set()
        if annotations is None:
            annotations = []
        if revTags is None:
            revTags = set()
        if revAnnotations is None:
            revAnnotations = []
        if decisionTags is None:
            decisionTags = set()
        if decisionAnnotations is None:
            decisionAnnotations = []

        # Figure out destination decision
        oldUnknown = self.destination(fromDecision, transition)

        # Check that it's unknown
        if not self.isUnknown(oldUnknown):
            raise UnknownDestinationError(
                f"Transition '{transition}' from '{fromDecision}' does"
                f" not lead to an unexplored decision (it leads to"
                f" '{oldUnknown}')."
            )

        # Check that the old unknown doesn't have a reciprocal edge that
        # would collide with the specified return edge
        if revName is not None:
            revFromUnknown = self.getDestination(oldUnknown, revName)
            if revFromUnknown not in (None, fromDecision):
                raise TransitionCollisionError(
                    f"Transition '{revName}' from '{oldUnknown}' exists"
                    f" and does not lead back to '{fromDecision}' (it"
                    f" leads to '{revFromUnknown}')."
                )

        # If connectTo name wasn't specified, use current name of
        # unknown node unless it's a default name
        if connectTo is None:
            if (
                oldUnknown.startswith('_u.')
            and oldUnknown[3:].isdigit()
            ):
                connectTo = uniqueName('_x.' + oldUnknown[3:], self)
            else:
                connectTo = oldUnknown

        # Apply any new tags or annotations, or create a new node
        needsZoneInfo = False
        if connectTo in self:
            # Before applying tags, check if we need to error out
            # because of a reciprocal edge that points to a known
            # destination:
            if revName is not None:
                otherOldUnknown = self.getDestination(connectTo, revName)
                if (
                    otherOldUnknown is not None
                and not self.isUnknown(otherOldUnknown)
                ):
                    raise UnknownDestinationError(
                        f"Reciprocal transition '{revName}' from"
                        f" '{connectTo}' does not lead to an unexplored"
                        f" decision (it leads to '{otherOldUnknown}')."
                    )
            self.tagDecision(connectTo, decisionTags)
            self.annotateDecision(connectTo, decisionAnnotations)
            # Still needs zone info if the place we're connecting to was
            # unknown up until now, since unknown nodes don't normally
            # get zone info when they're created.
            if self.isUnknown(connectTo):
                needsZoneInfo = True
        else:
            needsZoneInfo = True
            self.addDecision(
                connectTo,
                tags=decisionTags,
                annotations=decisionAnnotations
            )
            # In this case there can't be an other old unknown
            otherOldUnknown = None

        # Remember old reciprocal edge for future merging in case
        # it's not revName
        oldReciprocal = self.getReciprocal(fromDecision, transition)

        # First, merge the old unknown with the connectTo node...
        destRenames = self.mergeDecisions(
            oldUnknown,
            connectTo,
            errorOnNameColision=False
        )
        sourceRenames = {} # empty for now

        # Remove the 'unknown' tag transferred during the merge
        self.untagDecision(connectTo, "unknown")

        # Apply the new zone if there is one
        if placeInZone is not None:
            if placeInZone is DefaultZone:
                # When using DefaultZone, changes are only made for new
                # destinations: they get placed into each zone parent of
                # the source decision.
                if needsZoneInfo:
                    # Remove destination from all current parents
                    for parent in self.zoneParents(connectTo):
                        self.removeDecisionFromZone(connectTo, parent)
                    # Add it to parents of origin
                    for parent in self.zoneParents(fromDecision):
                        self.addDecisionToZone(connectTo, parent)
            else:
                placeInZone = cast(Zone, placeInZone)
                # Create the zone if it doesn't already exist
                if self.getZoneInfo(placeInZone) is None:
                    self.createZone(placeInZone, 0)
                    # Add it to each grandparent of the from decision
                    for parent in self.zoneParents(fromDecision):
                        for grandparent in self.zoneParents(parent):
                            self.addZoneToZone(placeInZone, grandparent)
                # Remove destination from all current parents
                for parent in self.zoneParents(connectTo):
                    self.removeDecisionFromZone(connectTo, parent)
                # Add it to the specified zone
                self.addDecisionToZone(connectTo, placeInZone)

        # Next, if there is a reciprocal name specified, we do more...
        if revName is not None:
            # Figure out what kind of merging needs to happen
            if otherOldUnknown is None and revFromUnknown is None:
                # Just create the desired reciprocal transition, which
                # we know does not already exist
                self.addTransition(connectTo, revName, fromDecision)
                otherOldReciprocal = None
            elif otherOldUnknown is not None:
                otherOldReciprocal = self.getReciprocal(connectTo, revName)
                # we need to merge otherOldUnknown into our fromDecision
                sourceRenames = self.mergeDecisions(
                    otherOldUnknown,
                    fromDecision,
                    errorOnNameColision=False
                )
                # Remove the 'unknown' tag transferred during the merge
                self.untagDecision(fromDecision, "unknown")
            else:
                otherOldReciprocal = None
                # Only other possibility is that otherOldUnknown is None
                # and revFromUnknown is not None, in which case the revName
                # transition already exists and points to fromDecision; it
                # could not have been renamed during the merge because
                # otherOldUnknown was None.

            # No matter what happened we ensure the reciprocal
            # relationship is set up:
            self.setReciprocal(fromDecision, transition, revName)

            # Now we might need to merge some transitions:
            # - Any reciprocal of the target transition should be merged
            #   with revName (if it was already revName, that's a
            #   no-op).
            # - Any reciprocal of the revName transition from the target
            #   node (leading to otherOldUnknown) should be merged with
            #   the target transition, even if it shared a name and was
            #   renamed as a result.
            # - If revName was renamed during the initial merge, those
            #   transitions should be merged.

            # Merge old reciprocal into revName
            if oldReciprocal is not None:
                oldRev = destRenames.get(oldReciprocal, oldReciprocal)
                if self.getDestination(connectTo, oldRev) is not None:
                    # Note that we don't want to auto-merge the reciprocal,
                    # which is the target transition
                    self.mergeTransitions(
                        connectTo,
                        oldRev,
                        revName,
                        mergeReciprocal=False
                    )
                    # Remove it from the renames map
                    if oldReciprocal in destRenames:
                        del destRenames[oldReciprocal]

            # Merge revName reciprocal from otherOldUnknown
            if otherOldReciprocal is not None:
                otherOldRev = sourceRenames.get(
                    otherOldReciprocal,
                    otherOldReciprocal
                )
                # Note that the reciprocal is revName, which we don't
                # need to merge
                self.mergeTransitions(
                    fromDecision,
                    otherOldRev,
                    transition,
                    mergeReciprocal=False
                )
                # Remove it from the renames map
                if otherOldReciprocal in sourceRenames:
                    del sourceRenames[otherOldReciprocal]

            # Merge any renamed revName onto revName
            if revName in destRenames:
                extraRev = destRenames[revName]
                self.mergeTransitions(
                    connectTo,
                    extraRev,
                    revName,
                    mergeReciprocal=False
                )
                # Remove it from the renames map
                del destRenames[revName]

        # Accumulate new tags & annotations for the transitions
        self.tagTransition(fromDecision, transition, tags)
        self.annotateTransition(fromDecision, transition, annotations)

        if revName is not None:
            self.tagTransition(connectTo, revName, revTags)
            self.annotateTransition(connectTo, revName, revAnnotations)

        # Override copied requirement/effects for the transitions
        if requirement is not None:
            self.setTransitionRequirement(
                fromDecision,
                transition,
                requirement
            )
        if applyEffects is not None:
            self.setTransitionEffects(
                fromDecision,
                transition,
                applyEffects
            )

        if revName is not None:
            if revRequires is not None:
                self.setTransitionRequirement(
                    connectTo,
                    revName,
                    revRequires
                )
            if revEffects is not None:
                self.setTransitionEffects(
                    connectTo,
                    revName,
                    revEffects
                )

        # Return our final rename dictionaries
        return (destRenames, sourceRenames)

    def addEnding(
        self,
        fromDecision: Decision,
        name: Decision,
        tags: Optional[Set[Tag]] = None,
        annotations: Optional[List[Annotation]] = None,
        endTags: Optional[Set[Tag]] = None,
        endAnnotations: Optional[List[Annotation]] = None,
        requires: Union[Requirement, str, None] = None,
        effects: Optional[List[TransitionEffect]] = None
    ) -> Transition:
        """
        Adds an edge labeled `'_e:-name-'` where '-name-' is the provided
        name, connecting to a new (or existing) decision named
        `'_e:-name-'` (same as the edge). This represents a transition to
        a game-end state. No reciprocal edge is added, but tags may be
        applied to the added transition and/or the ending room. The new
        transition and decision are both automatically tagged with
        'ending'. Returns the augmented transition/decision name.

        The starting decision must already exist (or a
        `MissingDecisionError` will be raised), and must not already have
        a transition with the transition name (or a
        `TransitionCollisionError` will be raised). Note that this means
        that ending names should not overlap with common transition
        names, since they may need to be used from multiple decisions in
        the graph; the '_e:' prefix should help with this.

        Requirements and/or effects if provided will be applied to the
        transition.
        """
        # Defaults
        if tags is None:
            tags = set()
        if annotations is None:
            annotations = []
        if endTags is None:
            endTags = set()
        if endAnnotations is None:
            endAnnotations = []

        tags.add("ending")
        endTags.add("ending")

        namePlus = '_e:' + name

        # Error checking
        if fromDecision not in self:
            raise MissingDecisionError(
                f"Cannot add a new ending transition '{name}' to"
                f" '{fromDecision}': That decision does not exist."
            )

        if namePlus in self.destinationsFrom(fromDecision):
            raise TransitionCollisionError(
                f"Cannot add a new ending edge '{name}':"
                f" '{fromDecision}' already has an outgoing edge named"
                f" '{namePlus}'."
            )

        # Create or new ending decision if we need to
        if namePlus not in self:
            self.addDecision(
                namePlus,
                tags=endTags,
                annotations=endAnnotations
            )
        else:
            # Or tag/annotate the existing decision
            self.tagDecision(namePlus, endTags)
            self.annotateDecision(namePlus, endAnnotations)

        # Add the edge
        self.addTransition(
            fromDecision,
            namePlus,
            namePlus,
            tags=tags,
            annotations=annotations
        )
        self.setTransitionRequirement(fromDecision, namePlus, requires)
        if effects is not None:
            self.setTransitionEffects(fromDecision, namePlus, effects)

        return namePlus


#-------------------#
# Exploration class #
#-------------------#

Situation: Tuple[
    DecisionGraph,
    Optional[Decision],
    State,
    Optional[Transition],
    List[Annotation]
] = collections.namedtuple(
    'Situation',
    ['graph', 'position', 'state', 'transition', 'annotations']
)
"""
Holds all of the pieces of an exploration's state at a single
exploration step.
"""


class Exploration:
    """
    A list of `DecisionGraph`s representing exploration over time, with
    specific positions for each step and transitions into them
    specified. Each decision graph represents a new state of the world
    (and/or new knowledge about a persisting state of the world), and the
    transition between graphs indicates which edge was followed, or what
    event happened to cause update(s). Depending on the resolution, it
    could represent a close record of every decision made or a more
    coarse set of snapshots from gameplay with more time in between.

    The steps of the exploration can also be annotated (see `annotate`).

    When a new `Exploration` is created, it starts out with an empty
    `DecisionGraph`. Use the `start` method to name the starting decision
    point and set things up for other methods.

    Tracking of player goals and destinations is also possible (see the
    `quest`, `progress`, `complete`, `destination`, and `arrive` methods).
    TODO: That
    """
    def __init__(self) -> None:
        self.graphs: List[DecisionGraph] = [DecisionGraph()]
        self.positions: List[Optional[Decision]] = [None]
        self.states: List[State] = [{}]
        self.transitions: List[Transition] = []
        # The transition at index i indicates the transition followed
        # (from the decision in the positions list at index i) or the
        # action taken that leads to the graph and position at index i + 1.
        # Normally, if there are n graphs, there will be n - 1
        # transitions listed.
        self.annotations: List[List[Annotation]] = [[]]

    # Note: not hashable

    def __eq__(self, other):
        """
        Equality checker. `Exploration`s can only be equal to other
        `Exploration`s, not to other kinds of things.
        """
        if not isinstance(other, Exploration):
            return False
        else:
            # Compare simplest first
            return (
                self.positions == other.positions
            and self.transitions == other.transitions
            and self.annotations == other.annotations
            and self.graphs == other.graphs
            and self.states == other.states
            )

    @staticmethod
    def fromGraph(
        graph: DecisionGraph,
        state: Optional[State] = None
    ) -> 'Exploration':
        """
        Creates an exploration which has just a single step whose graph
        is the entire specified graph. The graph is copied, so that
        changes to the exploration will not modify it. A starting state
        may also be specified if desired, although if not an empty state
        will be used.

        Example:

        >>> g = DecisionGraph()
        >>> g.addDecision('Room1')
        >>> g.addDecision('Room2')
        >>> g.addTransition('Room1', 'door', 'Room2', 'door')
        >>> e = Exploration.fromGraph(g)
        >>> len(e)
        1
        >>> e.currentGraph() == g
        True
        >>> e.getCurrentPosition() is None
        True
        >>> e.setCurrentPosition('Room1')
        >>> e.observe('hatch')
        >>> e.currentGraph() == g
        False
        >>> e.currentGraph().destinationsFrom('Room1')
        {'door': 'Room2', 'hatch': '_u.0'}
        >>> g.destinationsFrom('Room1')
        {'door': 'Room2'}
        """
        result = Exploration()
        result.graphs[0] = copy.deepcopy(graph)
        if state is None:
            state = {}
        else:
            state = copy.deepcopy(state)
        result.states[0] = state
        return result

    @staticmethod
    def load(stream: TextIO) -> 'Exploration':
        """
        Loads a new `Exploration` from the JSON data in the given text
        stream (e.g., a file open in read mode).
        """

    def save(self, stream: TextIO) -> None:
        """
        Saves this graph as JSON into the given text stream (e.g., a
        file open in writing mode).
        """

    def __len__(self) -> int:
        """
        The 'length' of an exploration is the number of steps.
        """
        return len(self.graphs)

    def graphAtStep(self, n: int) -> DecisionGraph:
        """
        Returns the `DecisionGraph` at the given step index. Raises an
        `IndexError` if the step index is out of bounds (see `__len__`).
        """
        return self.graphs[n]

    def getGraphAtStep(self, n: int) -> Optional[DecisionGraph]:
        """
        Like `graphAtStep` but returns None instead of raising an error
        if there is no graph at that step.
        """
        try:
            return self.graphAtStep(n)
        except IndexError:
            return None

    def positionAtStep(self, n: int) -> Decision:
        """
        Returns the position at the given step index. Raises an
        `IndexError` if the step index is out of bounds (see `__len__`).
        Raises a `MissingDecisionError` if there is no current position.
        """
        result = self.positions[n]
        if result is None:
            raise MissingDecisionError(
                f"There is no position at step {n}"
            )
        return result

    def getPositionAtStep(self, n: int) -> Optional[Decision]:
        """
        Like `positionAtStep` but returns None instead of raising
        an error if there is no position at that step.
        """
        try:
            return self.positionAtStep(n)
        except (IndexError, MissingDecisionError):
            return None

    def stateAtStep(self, n: int) -> State:
        """
        Returns the game state at the specified step. Raises an
        `IndexError` if the step value is out-of-bounds.
        """
        return self.states[n]

    def getStateAtStep(self, n: int) -> Optional[State]:
        """
        Like `stateAtStep` but returns None instead of raising
        an error if there is no transition at that step.
        """
        try:
            return self.stateAtStep(n)
        except IndexError:
            return None

    def transitionAtStep(self, n: int) -> Optional[Transition]:
        """
        Returns the transition taken from the situation at the given step
        index to the next situation (a `Transition` indicating which exit
        or action was taken). Raises an `IndexError` if the step index is
        out of bounds (see `__len__`), but returns `None` for the last
        step, which will not have a transition yet.
        """
        # Negative indices need an offset
        if n < 0:
            if n == -1 and len(self.graphs) > 0:
                transition = None
            else:
                transition = self.transitions[n + 1]
        # Positive indices just allow for None if we go one over
        else:
            if n == len(self.transitions) and len(self.graphs) > 0:
                transition = None
            else:
                # IndexError here for inappropriate indices
                transition = self.transitions[n]

        return transition

    def getTransitionAtStep(
        self,
        n: int
    ) -> Optional[Transition]:
        """
        Like `transitionAtStep` but returns None instead of raising
        an error if there is no transition at that step.
        """
        try:
            return self.transitionAtStep(n)
        except IndexError:
            return None

    def annotationsAtStep(self, n: int) -> List[Annotation]:
        """
        Fetches all annotations at the given exploration step.

        Raises an `IndexError` if an invalid step is given.

        Returns a live editable list of the annotations at that step.
        """
        return self.annotations[n]

    def getAnnotationsAtStep(self, n: int) -> List[Annotation]:
        """
        Works like `annotationsAtStep` but returns an empty list if there
        are no annotations at that step or if an invalid step is given,
        rather than raising an error.
        """
        try:
            return self.annotationsAtStep(n)
        except IndexError:
            return []

    def situationAtStep(self, n: int) -> Situation:
        """
        Returns a `Situation` named tuple detailing the state of the
        exploration at a given step. For the last step, the transition
        will be `None`.

        Raises an `IndexError` if asked for a step that's out-of-range.
        """
        return Situation(
            graph=self.graphs[n],
            position=self.positions[n],
            state=self.states[n],
            transition=self.getTransitionAtStep(n),
            annotations=self.getAnnotationsAtStep(n)
        )

    def getSituationAtStep(self, n: int) -> Optional[Situation]:
        """
        Like `situationAtStep` but returns `None` instead of raising an
        error if there is no situation at that step.
        """
        try:
            return self.situationAtStep(n)
        except IndexError:
            return None

    def currentGraph(self) -> DecisionGraph:
        """
        Returns the current graph, which will be an empty
        `DecisionGraph` when called on a fresh `Exploration` object.
        """
        return self.graphAtStep(-1)

    def currentPosition(self) -> Decision:
        """
        Returns the current position. Returns `None` if there is no
        current position (e.g., before the exploration is started).
        """
        return self.positionAtStep(-1)

    def getCurrentPosition(self) -> Optional[Decision]:
        """
        Like `currentPosition` but returns `None` instead of raising an
        error if there is no current position.
        """
        return self.getPositionAtStep(-1)

    def setCurrentPosition(
        self,
        decision: Optional[Decision]
    ) -> None:
        """
        Changes the current position without adding an exploration step.
        Normally you should use some other method to update the position,
        like `warp`. Raises a `MissingDecisionError` if a decision not
        in the current graph is listed. The decision can be set to `None`
        to erase the current position, leaving it blank.
        """
        if decision is not None and decision not in self.currentGraph():
            raise MissingDecisionError(
                f"Cannot set the current position to '{decision}': That"
                f" decision does not exist in the current graph."
            )
        self.positions[-1] = decision

    def currentState(self) -> State:
        """
        Returns the current game state. This will be an empty dictionary
        before the start of the exploration.
        """
        return self.stateAtStep(-1)

    def currentSituation(self) -> Situation:
        """
        Returns the current `Situation` named tuple. Note that the
        `transition` component will always be `None`.
        """
        return self.situationAtStep(-1)

    def annotateStep(
        self,
        annotationOrAnnotations: Union[Annotation, Sequence[Annotation]],
        n: Optional[int] = None
    ) -> None:
        """
        Adds an annotation to the current exploration step, or to a
        specific step if `n` is given as an integer rather than the
        default `None`.
        """
        if n is None:
            n = -1
        if isinstance(annotationOrAnnotations, Annotation):
            self.annotationsAtStep(n).append(annotationOrAnnotations)
        else:
            self.annotationsAtStep(n).extend(annotationOrAnnotations)

    def hasPowerNow(self, power: Power) -> bool:
        """
        Returns True if th player currently has the specified power, and
        False otherwise.
        """
        return power in self.currentState().get('powers', set())

    def gainPowerNow(self, power: Power) -> None:
        """
        Modifies the current game state to add the specified `Power` to
        the player's capabilities. No changes are made to the current
        graph.
        """
        self.currentState().setdefault('powers', set()).add(power)

    def losePowerNow(self, power: Power) -> None:
        """
        Modifies the current game state to remove the specified `Power`
        from the player's capabilities. Does nothing if the player
        doesn't already have that power.
        """
        try:
            self.currentState().setdefault('powers', set()).remove(power)
        except KeyError:
            pass

    def tokenCountNow(self, tokenType: Token) -> Optional[int]:
        """
        Returns the number of tokens the player currently has of a given
        type. Returns `None` if the player has never acquired or lost
        tokens of that type.
        """
        return self.currentState().get('tokens', {}).get(tokenType)

    def adjustTokensNow(self, tokenType: Token, amount: int) -> None:
        """
        Modifies the current game state to add the specified number of
        `Token`s of the given type to the player's tokens. No changes are
        made to the current graph. Reduce the number of tokens by
        supplying a negative amount.
        """
        state = self.currentState()
        tokens = state.setdefault('tokens', {})
        tokens[tokenType] = tokens.get(tokenType, 0) + amount

    def setTokensNow(self, tokenType: Token, amount: int) -> None:
        """
        Modifies the current game state to set number of `Token`s of the
        given type to a specific amount, regardless of the old value. No
        changes are made to the current graph.
        """
        state = self.currentState()
        tokens = state.setdefault('tokens', {})
        tokens[tokenType] = amount

    def updateRequirementNow(
        self,
        decision: Decision,
        transition: Transition,
        requirement: Union[Requirement, str, None]
    ) -> None:
        """
        Updates the requirement for a specific transition in a specific
        decision. If a `Requirement` object is given, that will be used;
        if a string is given, it will be turned into a `Requirement`
        using `Requirement.parse`. If `None` is given, the requirement
        for that edge will be removed.
        """
        if requirement is None:
            requirement = ReqNothing()
        self.currentGraph().setTransitionRequirement(
            decision,
            transition,
            requirement
        )

    def traversableAtStep(
        self,
        step: int,
        decision: Decision,
        transition: Transition
    ) -> bool:
        """
        Returns True if the specified transition from the specified
        decision had its requirement satisfied by the game state at the
        specified step. Raises an `IndexError` if the specified step
        doesn't exist, and a `KeyError` if the decision or transition
        specified does not exist in the `DecisionGraph` at that step.
        """
        graph = self.graphAtStep(step)
        req = graph.getTransitionRequirement(decision, transition)
        return req.satisfied(self.stateAtStep(step))

    def traversableNow(
        self,
        decision: Decision,
        transition: Transition
    ) -> bool:
        """
        Returns True if the specified transition from the specified
        decision has its requirement satisfied by the current game
        state. Raises an `IndexError` if there are no game states yet.
        """
        return self.traversableAtStep(-1, decision, transition)

    def applyEffectsNow(
        self,
        effects: Sequence[TransitionEffect],
        where: Tuple[Decision, Optional[Transition]]
    ) -> None:
        """
        Applies the specified effects to the current state & graph,
        without creating a new exploration step. Effects are applied in
        phases: first all gain effects, then all lose effects, then all
        toggles, then all deactivates, then all edits. Within each
        phase, effects are applied in the order they appear in the
        effects list.

        A decision/transition pair must be specified to indicate which
        transition deactivate effects apply and where to set initial
        relative targets for edit effects. `None` may be given as the
        transition of this pair when there is no relevant transition,
        but in that case, a `ValueError` will result when applying
        `deactivate` effects, and edit effects might also result in
        errors if they don't specify a transition target before
        attempting to edit the current transition.
        """
        gains = []
        losses = []
        toggles = []
        deactivates = []
        edits = []
        for effect in effects:
            if effect['type'] == 'gain':
                gains.append(effect)
            elif effect['type'] == 'lose':
                losses.append(effect)
            elif effect['type'] == 'toggle':
                toggles.append(effect)
            elif effect['type'] == 'deactivate':
                deactivates.append(effect)
            elif effect['type'] == 'edit':
                edits.append(effect)

        for phase in gains, losses, toggles, deactivates, edits:
            for effect in phase:
                self.applyEffectNow(effect, where)

    def applyEffectNow(
        self,
        effect: TransitionEffect,
        where: Optional[Tuple[Decision, Optional[Transition]]] = None
    ) -> None:
        """
        Applies a single transition effect to the state & graph. Also
        edits the effect in cases where delay, charges, or a toggle list
        are relevant. For 'deactivate' effects, a transition must be
        specified via `where`, but other effects do not need that. Note
        that `edit` effects also usually assume a decision and
        transition target will be provided.
        """
        typ = effect['type']
        value = effect['value']

        # If there's a delay, just count down and don't actually do
        # anything
        if effect['delay'] is not None and effect['delay'] > 0:
            effect['delay'] -= 1
            return

        # If there are charges, subtract one, and don't do anything if
        # there are 0 charges left
        if effect['charges'] is not None:
            if effect['charges'] == 0:
                return
            else:
                effect['charges'] -= 1

        if typ == "gain":
            if isinstance(value, Power):
                self.gainPowerNow(value)
            else: # must be a token, amount pair
                token, amount = cast(Tuple[Token, int], value)
                self.adjustTokensNow(token, amount)

        elif typ == "lose":
            if isinstance(value, Power):
                self.losePowerNow(value)
            else: # must be a token, amount pair
                token, amount = cast(Tuple[Token, int], value)
                self.adjustTokensNow(token, -amount)

        elif typ == "toggle":
            # Length-1 list just toggles a power on/off based on current
            # state:
            value = cast(List[Power], value)
            if len(value) == 0:
                raise ValueError("Toggle effect has empty powers list.")
            if len(value) == 1:
                power = value[0]
                if self.hasPowerNow(power):
                    self.losePowerNow(power)
                else:
                    self.gainPowerNow(power)
            else:
                # Otherwise toggle all powers off, then first one on,
                # and then rotate the list
                for power in value:
                    self.losePowerNow(power)
                self.gainPowerNow(value[0])
                value.append(value.pop(0))

        elif typ == "deactivate":
            if where is None or where[1] is None:
                raise ValueError(
                    "Can't apply a deactivate effect without specifying"
                    " which transition it applies to."
                )

            decision, transition = cast(Tuple[Decision, Transition],
                                        where)
            self.currentGraph().setTransitionRequirement(
                decision,
                transition,
                ReqImpossible()
            )

        elif typ == "edit":
            value = cast(List[List[Command]], value)
            # If there are no blocks, do nothing
            if len(value) > 0:
                # Apply the first block of commands and then rotate the list
                scope: Scope = {}
                if where is not None:
                    here: str = where[0]
                    outwards: Optional[str] = where[1]
                    scope['@'] = here
                    scope['@t'] = outwards
                    if outwards is not None:
                        now = self.currentGraph()
                        reciprocal = now.getReciprocal(here, outwards)
                        destination = now.getDestination(here, outwards)
                    else:
                        reciprocal = None
                        destination = None
                    scope['@r'] = reciprocal
                    scope['@d'] = destination
                self.runCommandBlock(value[0], scope)
                value.append(value.pop(0))

        else:
            raise ValueError(f"Invalid effect type '{typ}'.")

    def applyTransitionEffectsNow(
        self,
        decision: Decision,
        transition: Transition,
        step: int = -1
    ) -> None:
        """
        Applies the effects of the specified transition from the
        specified decision to the current graph and state. By default,
        these effects are read from the transition information in the
        current graph, but specifying a non-default `step` value will
        cause the effects to be read from the graph at a different step.
        The effects will be edited (e.g., delay reduced or charges
        deducted) from the step being read from, so usually setting a
        non-default step will cause problems!

        Raises an `IndexError` if the specified step doesn't exist, or a
        `MissingDecisionError` or `MissingTransitionError` if the
        decision or transition specified doesn't exist in the graph at
        the specified step.

        This function does not check whether any requirements for the
        specified transition are satisfied.
        """
        then = self.graphAtStep(step)
        effects = then.getTransitionEffects(decision, transition)
        self.applyEffectsNow(effects, (decision, transition))

    def start(
        self,
        decision: Decision,
        connections: Optional[
            Iterable[
                Union[
                    Transition,
                    Tuple[Transition, Decision],
                    Tuple[Transition, Decision, Transition]
                ]
            ]
        ] = None,
        startState: Dict[str, Any] = None,
        zone: Optional[Zone] = None
    ) -> None:
        """
        Places an initial decision in the empty starting graph with the
        given name. The given connections are added using `observe`.

        Raises a `BadStart` error if the current graph isn't empty.

        - The given `startState` replaces any existing state, although
            you can leave it as the default `None` to avoid that and
            retain any state that's been set up already.
        - The decision will be added to the given `zone`, creating it at
            level 0 if necessary, although if that is left as the default
            (`None`) no zone information will be changed.

        A special transition name "_START_" is used for the 'transition'
        from the empty graph.
        """
        if connections is None:
            connections = []

        now = copy.deepcopy(self.currentGraph())
        if len(now) > 0:
            raise BadStart(
                "Cannot start an exploration which already has decisions"
                " in it (use 'start' only once)."
            )

        if startState is None:
            startState = copy.deepcopy(self.currentState())

        now.addDecision(decision)

        if zone is not None:
            if now.getZoneInfo(zone) is None:
                now.createZone(zone, 0)
            now.addDecisionToZone(decision, zone)

        # Add the graph to our graphs list and set our starting position
        self.graphs.append(now)
        self.positions.append(decision)
        self.states.append(startState)
        self.transitions.append("_START_")

        # Observe connections (happens after transition effects)
        self.observe(*connections)

    def explore(
        self,
        transition: Transition,
        destination: Decision,
        connections: Optional[
            Iterable[
                Union[
                    Transition,
                    Tuple[Transition, Decision],
                    Tuple[Transition, Decision, Transition]
                ]
            ]
        ] = None,
        reciprocal: Optional[Transition] = None,
        zone: Union[Zone, type[DefaultZone], type[None]] = DefaultZone
    ) -> None:
        """
        Adds a new graph to the exploration graph representing the
        traversal of the specified transition from the current position,
        and updates the current position to be the new decision added.
        The transition must have been pointing to an unexplored region,
        which will be replaced by a new decision with the given name.

        - That decision will have each of the given `connections` added
            to it via `observe`.
        - If a `reciprocal` name is specified, the reciprocal transition
            will be renamed using that name, or created with that name if
            it didn't already exist. If reciprocal is left as `None` (the
            default) then no change will be made to the reciprocal
            transition, and it will not be created if it doesn't exist.
        - If a `zone` is specified, the newly-explored decision will be
            added to that zone (and that zone will be created at level 0
            if it didn't already exist). If `zone` is set to `None` then
            it will not be added to any new zones. If `zone` is left as
            the default (the `DefaultZone` class) then the explored
            decision will be added to each zone that the decision it was
            explored from is a part of. If a zone needs to be created,
            that zone will be added as a sub-zone of each zone which is a
            parent of a zone that directly contains the origin decision.
        - A `MissingDecisionError will be raised if there is no current
            position (e.g., before `start` has been called), and a
            `MissingTransitionError` will be raised if the listed
            transition does not exist at the current position.
        - An `UnknownDestinationError` will be raised if the specified
            transition does not lead to an unknown region, or if a
            another decision with the destination name name already
            exists
        - A `TransitionBlockedWarning` will be issued if the specified
            transition is not traversable given the current game state
            (but in that last case the step will still be taken).
        - The reciprocal may not be one of the listed new connections to
            create (because they will all be created pointing to unknown
            regions).
        """
        if connections is None:
            connections = []

        here = self.currentPosition()

        if not self.traversableNow(here, transition):
            warnings.warn(
                (
                    f"The requirements for transition '{transition}'"
                    f" from decision '{here}' are not met at step"
                    f" {len(self)}."
                ),
                TransitionBlockedWarning
            )

        now = copy.deepcopy(self.currentGraph())
        current = copy.deepcopy(self.currentState())

        currentDestinationName = now.getDestination(here, transition)

        if destination in now and destination != currentDestinationName:
            raise UnknownDestinationError(
                f"Cannot explore to decision '{destination}' because it"
                f" already exists (use `returnTo` when revisiting a"
                f" previous decision)."
            )

        now.replaceUnexplored(
            here,
            transition,
            destination,
            reciprocal,
            placeInZone=zone
        )

        # Grow our state-list variables
        self.graphs.append(now)
        self.transitions.append(transition)
        self.positions.append(destination)
        self.states.append(current)

        # Pick up state effects of the transition
        self.applyTransitionEffectsNow(here, transition)
        # Note: we apply the transition effects from the copied + updated
        # graph, not from the previous-step graph. This shouldn't make
        # any difference, since we just copied the graph.

        # Observe connections (happens after transition effects)
        self.observe(*connections)

    def returnTo(
        self,
        transition: Transition,
        destination: Decision,
        reciprocal: Optional[Transition] = None
    ) -> None:
        """
        Adds a new graph to the exploration that replaces the given
        transition at the current position (which must lead to an unknown
        node, or a `MissingDecisionError` will result). The new
        transition will connect back to the specified destination, which
        must already exist (or a different `ValueError` will be raised).

        If a `reciprocal` transition is specified, that transition must
        either not already exist in the destination decision or lead to
        an unknown region; it will be replaced (or added) as an edge
        leading back to the current position.

        A `TransitionBlockedWarning` will be issued if the requirements
        for the transition are not met, but the step will still be taken.
        Raises a `MissingDecisionError` if there is no current
        transition.
        """
        # Get current position and graph
        now = copy.deepcopy(self.currentGraph())
        here = self.currentPosition()
        state = copy.deepcopy(self.currentState())

        if not self.traversableNow(here, transition):
            warnings.warn(
                (
                    f"The requirements for transition '{transition}'"
                    f" from decision '{here}' are not met at step"
                    f" {len(self)}."
                ),
                TransitionBlockedWarning
            )

        if destination not in now:
            raise MissingDecisionError(
                f"Cannot return to decision '{destination}' because it"
                f" does not yet exist (use `explore` when visiting a new"
                f" decision)."
            )

        # Replace with connection to existing destination
        now.replaceUnexplored(
            here,
            transition,
            destination,
            reciprocal
        )

        # Grow our state-list variables
        self.graphs.append(now)
        self.transitions.append(transition)
        self.positions.append(destination)
        self.states.append(state)

        # Apply transition effects
        self.applyTransitionEffectsNow(here, transition)

    def takeAction(
        self,
        action: Transition,
        requires: Union[Requirement, str, None] = None,
        effects: Optional[List[TransitionEffect]] = None
    ) -> None:
        """
        Adds a new graph to the exploration based on taking the given
        action, which must be a self-transition in the graph. If the
        action does not already exist in the graph, it will be created;
        either way the requirements and effects of the action will be
        updated to match any specified here, and those are the
        requirements/effects that will count. The optional arguments
        specify a requirement and/or effect for the action.

        Issues a `TransitionBlockedWarning` if the current game state
        doesn't satisfy the requirements for the action.

        Raises a `MissingDecisionError` if there is no current decision.
        """
        here = self.currentPosition()
        now = copy.deepcopy(self.currentGraph())
        state = copy.deepcopy(self.currentState())

        # If the action doesn't already exist, we create it in the new
        # graph (e.g, if there's a hidden cutscene trigger).
        if now.getDestination(here, action) is None:
            now.addAction(here, action, requires, effects)
        else:
            # Otherwise, just update the transition effects (before the
            # action is taken)
            now.setTransitionRequirement(here, action, requires)
            if effects is not None:
                now.setTransitionEffects(here, action, effects)

        # Note: can't use traversableNow here, because if we just added
        # the action, it won't appear in the current graph yet
        # (self.graph.append happens below, and must happen after this).
        req = now.getTransitionRequirement(here, action)
        if not req.satisfied(self.currentState()):
            warnings.warn(
                (
                    f"The requirements for action '{action}' in"
                    f" decision '{here}' are not met in the game state"
                    f" at step {len(self)}."
                ),
                TransitionBlockedWarning
            )

        self.graphs.append(now)
        self.transitions.append(action)
        self.positions.append(self.currentPosition())
        self.states.append(state)

        self.applyTransitionEffectsNow(here, action)

    def retrace(
        self,
        transition: Transition,
    ) -> None:
        """
        Adds a new graph to the exploration based on taking the given
        transition, which must already exist and which must not lead to
        an unknown region.

        Issues a `TransitionBlockedWarning` if the current game state
        doesn't satisfy the requirements for the transition.

        A `MissingTransitionError` is raised if the specified transition
        does not yet exist or leads to an unknown area.
        """
        here = self.currentPosition()
        now = copy.deepcopy(self.currentGraph())
        state = copy.deepcopy(self.currentState())

        # Check for a valid destination
        dest = now.getDestination(here, transition)
        if dest is None:
            raise MissingTransitionError(
                f"Cannot retrace transition '{transition}' from"
                f" decision '{here}' because it does not yet exist."
            )

        if now.isUnknown(dest):
            raise UnknownDestinationError(
                f"Cannot retrace transition '{transition}' from"
                f" decision '{here}' because it leads to an unknown"
                f" decision.\nUse `Exploration.explore` and provide"
                f" destination decision details instead."
            )

        if not self.traversableNow(here, transition):
            warnings.warn(
                (
                    f"The requirements for transition '{transition}' in"
                    f" decision '{here}' are not met in the game state"
                    f" at step {len(self)}."
                ),
                TransitionBlockedWarning
            )

        self.graphs.append(now)
        self.transitions.append(transition)
        self.positions.append(dest)
        self.states.append(state)

        self.applyTransitionEffectsNow(here, transition)

    def warp(
        self,
        destination: Decision,
        message: str = "",
        effects: Optional[List[TransitionEffect]] = None,
        zone: Union[Zone, type[DefaultZone], type[None]] = DefaultZone
    ) -> None:
        """
        Adds a new graph to the exploration that's a copy of the current
        graph, with the position updated to be at the destination without
        actually creating a transition from the old position to the new
        one.

        - If the destination did not already exist, it will be created.
            Initially, it will be disconnected from all other decisions.
        - The transition is listed in the log as '~~:' plus the specified
            `message` (or just '~~' if the message is an empty string).
            That transition string must NOT be a valid transition in the
            current room.
        - If the destination is the same as the current position, the
            transition prefix (or content) will be '..' instead of '~~'.
        - The position is set to the specified destination, and if
            `effects` are specified they are applied. Note that
            'deactivate' effects are NOT allowed, and 'edit' effects must
            establish their own transition target because there is no
            transition that the effects are being applied to. If the
            destination had been unknown, it will lose that status.
        - If a `zone` is specified, the destination will be added to that
            zone (even if the destination already existed) and that zone
            will be created (as a level-0 zone) if need be. If `zone` is
            set to `None`, then no zone will be applied. If `zone` is
            left as the default (`DefaultZone`) then the destination will
            be added to all zones that the origin was a part of if the
            destination is newly created, but otherwise the destination
            will not be added to any zones. If the specified zone has to
            be created, it will be added as a sub-zone to all parents of
            zones directly containing the origin.
        - A `TransitionCollisionError` is raised if the specified
            transition name already exists.
        """
        here = self.currentPosition()
        now = copy.deepcopy(self.currentGraph())
        state = copy.deepcopy(self.currentState())

        # Create the decision if it didn't exist
        new = False
        if destination not in now:
            new = True
            now.addDecision(destination)

        # Figure out the destination
        prefix = '~~'
        if here == destination:
            prefix = '..'

        if message == '':
            tName = prefix
        else:
            tName = prefix + ':' + message

        # If the transition already exists, it's not a valid warp
        # message.
        dest = now.getDestination(here, tName)
        if dest is not None:
            raise TransitionCollisionError(
                f"Cannot use '{message}' as a warp message because"
                f" transition '{tName}' exists at decision '{here}'."
            )

        # Remove unknown status from destination if it had it
        now.setUnknown(destination, False)

        # Handle zones
        if zone is DefaultZone:
            if new:
                for prevZone in now.zoneParents(here):
                    now.addDecisionToZone(destination, prevZone)
            # Otherwise don't update zones
        elif zone is not None:
            # Newness is ignored when a zone is specified
            zone = cast(Zone, zone)
            # Create the zone at level 0 if it didn't already exist
            if now.getZoneInfo(zone) is None:
                now.createZone(zone, 0)
                # Add the newly created zone to each 2nd-level parent of
                # the previous decision
                for prevZone in now.zoneParents(here):
                    for prevUpper in now.zoneParents(prevZone):
                        now.addZoneToZone(zone, prevUpper)
            # Finally add the destination to the (maybe new) zone
            now.addDecisionToZone(destination, zone)
        # else don't touch zones

        # Modify state variables
        self.graphs.append(now)
        self.transitions.append(tName)
        self.positions.append(destination)
        self.states.append(state)

        if effects is not None:
            self.applyEffectsNow(effects, (here, None))

    def wait(
        self,
        message: str = "",
        effects: Optional[List[TransitionEffect]] = None
    ) -> None:
        """
        Adds a warp which leaves the player in the same position. If
        effects are specified, they are applied.

        A `ValueError` is raised if the message implies a transition name
        which already exists (this is unlikely).
        """
        here = self.currentPosition()
        self.warp(here, message, effects)

    def observe(
        self,
        *transitions: Union[
            Transition,
            Tuple[Transition, Decision],
            Tuple[Transition, Decision, Transition]
        ],
        where: Optional[Decision] = None
    ):
        """
        Observes one or more new transitions, applying changes to the
        current graph. The transitions can be specified in one of three
        ways:

        1. A transition name. The transition will be created and will
            point to a new unexplored node.
        2. A pair containing a transition name and a destination name. If
            the destination does not exist it will be created as an
            unexplored node.
        3. A triple containing a transition name, a destination name,
            and a reciprocal name. Works the same as the pair case but
            also specifies the name for the reciprocal transition.

        The new transitions are outgoing from the current position, and
        are added only to the most recent step graph. Optionally, the
        `where` keyword argument may be specified to change the base node
        that the transitions are placed on. A `MissingDecisionError` is
        raised if this base node doesn't exist.
        """
        now = self.currentGraph()
        if where is None:
            where = self.currentPosition()
        elif where not in now:
            raise MissingDecisionError(
                f"Decision '{where}' cannot be the basis for newly"
                f" observed transition(s) because it does not exist"
                f" yet."
            )

        for entry in transitions:
            if isinstance(entry, Transition):
                now.addUnexploredEdge(where, entry)
            elif len(entry) == 2:
                entry = cast(Tuple[Transition, Decision], entry)
                transition, destination = entry
                if destination in now:
                    now.addTransition(where, transition, destination)
                else:
                    now.addUnexploredEdge(where, transition, destination)
            elif len(entry) == 3:
                entry = cast(Tuple[Transition, Decision, Transition], entry)
                transition, destination, reciprocal = entry
                if destination in now:
                    now.addTransition(
                        where,
                        transition,
                        destination,
                        reciprocal
                    )
                else:
                    now.addUnexploredEdge(
                        where,
                        transition,
                        destination
                    )
            else:
                raise ValueError(
                    f"Each transition observed must be either a"
                    f" transition name, a transition, destination"
                    f" pair, or a transition, destination,"
                    f" reciprocal triple, but you provided:"
                    f" {entry!r}"
                )

    def reZone(
        self,
        zone: Zone,
        replace: Union[Zone, int] = 0,
        where: Optional[Decision] = None
    ) -> None:
        """
        Alters the current graph without adding a new exploration step.

        Calls `DecisionGraph.replaceZonesInHierarchy` targeting the
        current position (or the specified decision if `where` is set).
        Note that per the logic of that method, ALL zones at the
        specified hierarchy level are replaced, even if a specific zone
        to replace is specified here.

        TODO: not that?

        The level value is either specified via `replace` (default 0) or
        deduced from the zone provided as the `replace` value using
        `DecisionGraph.zoneHierarchyLevel`.
        """
        if where is None:
            where = self.currentPosition()

        now = self.currentGraph()

        if isinstance(replace, int):
            level = replace
        else:
            level = now.zoneHierarchyLevel(replace)

        now.replaceZonesInHierarchy(where, zone, level)

    def runCommand(
        self,
        command: Command,
        scope: Optional[Scope] = None,
        line: int = -1
    ) -> CommandResult:
        """
        Runs a single `Command` applying effects to the exploration, its
        current graph, and the provided execution context, and returning
        a command result, which contains the modified scope plus
        optional skip and label values (see `CommandResult`). This
        function also directly modifies the scope you give it. Variable
        references in the command are resolved via entries in the
        provided scope. If no scope is given, an empty one is created.

        A line number may be supplied for use in error messages; if left
        out line -1 will be used.

        Raises an error if the command is invalid.

        For commands that establish a value as the 'current value', that
        value will be stored in the '_' variable. When this happens, the
        old contents of '_' are stored in '__' first, and the old
        contents of '__' are discarded. Note that non-automatic
        assignment to '_' does not move the old value to '__'.
        """
        try:
            if scope is None:
                scope = {}

            skip: Union[int, str, None] = None
            label: Optional[str] = None

            if command.command == 'val':
                command = cast(LiteralValue, command)
                result = resolveValue(command.value, scope)
                pushCurrentValue(scope, result)

            elif command.command == 'empty':
                command = cast(EstablishCollection, command)
                collection = resolveVarName(command.collection, scope)
                pushCurrentValue(
                    scope,
                    {
                        'list': [],
                        'tuple': (),
                        'set': set(),
                        'dict': {},
                    }[collection]
                )

            elif command.command == 'append':
                command = cast(AppendValue, command)
                target = scope['_']
                addIt = resolveValue(command.value, scope)
                if isinstance(target, list):
                    target.append(addIt)
                elif isinstance(target, tuple):
                    scope['_'] = target + (addIt,)
                elif isinstance(target, set):
                    target.add(addIt)
                elif isinstance(target, dict):
                    raise TypeError(
                        "'append' command cannot be used with a"
                        " dictionary. Use 'set' instead."
                    )
                else:
                    raise TypeError(
                        f"Invalid current value for 'append' command."
                        f" The current value must be a list, tuple, or"
                        f" set, but it was a '{type(target).__name__}'."
                    )

            elif command.command == 'set':
                command = cast(SetValue, command)
                target = scope['_']
                where = resolveValue(command.location, scope)
                what = resolveValue(command.value, scope)
                if isinstance(target, list):
                    if not isinstance(where, int):
                        raise TypeError(
                            f"Cannot set item in list: index {where!r}"
                            f" is not an integer."
                        )
                    target[where] = what
                elif isinstance(target, tuple):
                    if not isinstance(where, int):
                        raise TypeError(
                            f"Cannot set item in tuple: index {where!r}"
                            f" is not an integer."
                        )
                    if not (
                        0 <= where < len(target)
                    or -1 >= where >= -len(target)
                    ):
                        raise IndexError(
                            f"Cannot set item in tuple at index"
                            f" {where}: Tuple has length {len(target)}."
                        )
                    scope['_'] = target[:where] + (what,) + target[where + 1:]
                elif isinstance(target, set):
                    if what:
                        target.add(where)
                    else:
                        try:
                            target.remove(where)
                        except KeyError:
                            pass
                elif isinstance(target, dict):
                    target[where] = what

            elif command.command == 'pop':
                command = cast(PopValue, command)
                target = scope['_']
                if isinstance(target, list):
                    result = target.pop()
                    pushCurrentValue(scope, result)
                elif isinstance(target, tuple):
                    result = target[-1]
                    updated = target[:-1]
                    scope['__'] = updated
                    scope['_'] = result
                else:
                    raise TypeError(
                        f"Cannot 'pop' from a {type(target).__name__}"
                        f" (current value must be a list or tuple)."
                    )

            elif command.command == 'get':
                command = cast(GetValue, command)
                target = scope['_']
                where = resolveValue(command.location, scope)
                if isinstance(target, list):
                    if not isinstance(where, int):
                        raise TypeError(
                            f"Cannot get item from list: index"
                            f" {where!r} is not an integer."
                        )
                elif isinstance(target, tuple):
                    if not isinstance(where, int):
                        raise TypeError(
                            f"Cannot get item from tuple: index"
                            f" {where!r} is not an integer."
                        )
                elif isinstance(target, set):
                    result = where in target
                    pushCurrentValue(scope, result)
                elif isinstance(target, dict):
                    result = target[where]
                    pushCurrentValue(scope, result)
                else:
                    result = getattr(target, where)
                    pushCurrentValue(scope, result)

            elif command.command == 'remove':
                command = cast(RemoveValue, command)
                target = scope['_']
                where = resolveValue(command.location, scope)
                if isinstance(target, (list, tuple)):
                    # this cast is not correct but suppresses warnings
                    # given insufficient narrowing by MyPy
                    target = cast(Tuple[Any, ...], target)
                    if not isinstance(where, int):
                        raise TypeError(
                            f"Cannot remove item from list or tuple:"
                            f" index {where!r} is not an integer."
                        )
                    scope['_'] = target[:where] + target[where + 1:]
                elif isinstance(target, set):
                    target.remove(where)
                elif isinstance(target, dict):
                    del target[where]
                else:
                    raise TypeError(
                        f"Cannot use 'remove' on a/an"
                        f" {type(target).__name__}."
                    )

            elif command.command == 'op':
                command = cast(ApplyOperator, command)
                left = resolveValue(command.left, scope)
                right = resolveValue(command.right, scope)
                op = command.op
                if op == '+':
                    result = left + right
                elif op == '-':
                    result = left - right
                elif op == '*':
                    result = left * right
                elif op == '/':
                    result = left / right
                elif op == '//':
                    result = left // right
                elif op == '**':
                    result = left ** right
                elif op == '%':
                    result = left % right
                elif op == '^':
                    result = left ^ right
                elif op == '|':
                    result = left | right
                elif op == '&':
                    result = left & right
                elif op == 'and':
                    result = left and right
                elif op == 'or':
                    result = left or right
                elif op == '<':
                    result = left < right
                elif op == '>':
                    result = left > right
                elif op == '<=':
                    result = left <= right
                elif op == '>=':
                    result = left >= right
                elif op == '==':
                    result = left == right
                elif op == 'is':
                    result = left is right
                else:
                    raise RuntimeError("Invalid operator '{op}'.")

                pushCurrentValue(scope, result)

            elif command.command == 'unary':
                command = cast(ApplyUnary, command)
                value = resolveValue(command.value, scope)
                op = command.op
                if op == '-':
                    result = -value
                elif op == '~':
                    result = ~value
                elif op == 'not':
                    result = not value

                pushCurrentValue(scope, result)

            elif command.command == 'assign':
                command = cast(VariableAssignment, command)
                varname = resolveVarName(command.varname, scope)
                value = resolveValue(command.value, scope)
                scope[varname] = value

            elif command.command == 'delete':
                command = cast(VariableDeletion, command)
                varname = resolveVarName(command.varname, scope)
                del scope[varname]

            elif command.command == 'load':
                command = cast(LoadVariable, command)
                varname = resolveVarName(command.varname, scope)
                pushCurrentValue(scope, result)

            elif command.command == 'call':
                command = cast(FunctionCall, command)
                function = command.function
                if function.startswith('$'):
                    function = resolveValue(function, scope)

                toCall: Callable
                args: Tuple[str, ...]
                kwargs: Dict[str, Any]

                if command.target == 'builtin':
                    toCall = COMMAND_BUILTINS[function]
                    args = (scope['_'],)
                    kwargs = {}
                    if toCall == round:
                        if 'ndigits' in scope:
                            kwargs['ndigits'] = scope['ndigits']
                    elif toCall == range and args[0] is None:
                        start = scope.get('start', 0)
                        stop = scope['stop']
                        step = scope.get('step', 1)
                        args = (start, stop, step)

                else:
                    if command.target == 'stored':
                        toCall = function
                    elif command.target == 'graph':
                        toCall = getattr(self.currentGraph(), function)
                    elif command.target == 'exploration':
                        toCall = getattr(self, function)
                    else:
                        raise TypeError(
                            f"Invalid call target '{command.target}'"
                            f" (must be one of 'builtin', 'stored',"
                            f" 'graph', or 'exploration'."
                        )

                    # Fill in arguments via kwargs defined in scope
                    args = ()
                    kwargs = {}
                    signature = inspect.signature(toCall)
                    # TODO: Maybe try some type-checking here?
                    for argName, param in signature.parameters.items():
                        if param.kind == inspect.Parameter.VAR_POSITIONAL:
                            if argName in scope:
                                args = args + tuple(scope[argName])
                            # Else leave args as-is
                        elif param.kind == inspect.Parameter.KEYWORD_ONLY:
                            # These must have a default
                            if argName in scope:
                                kwargs[argName] = scope[argName]
                        elif param.kind == inspect.Parameter.VAR_KEYWORD:
                            # treat as a dictionary
                            if argName in scope:
                                argsToUse = scope[argName]
                                if not isinstance(argsToUse, dict):
                                    raise TypeError(
                                        f"Variable '{argName}' must"
                                        f" hold a dictionary when"
                                        f" calling function"
                                        f" '{toCall.__name__} which"
                                        f" uses that argument as a"
                                        f" keyword catchall."
                                    )
                                kwargs.update(scope[argName])
                        else:  # a normal parameter
                            if argName in scope:
                                args = args + (scope[argName],)
                            elif param.default == inspect.Parameter.empty:
                                raise TypeError(
                                    f"No variable named '{argName}' has"
                                    f" been defined to supply the"
                                    f" required parameter with that"
                                    f" name for function"
                                    f" '{toCall.__name__}'."
                                )

                result = toCall(*args, **kwargs)
                pushCurrentValue(scope, result)

            elif command.command == 'skip':
                command = cast(SkipCommands, command)
                doIt = resolveValue(command.condition, scope)
                if doIt:
                    skip = resolveValue(command.amount, scope)
                    if not isinstance(skip, (int, str)):
                        raise TypeError(
                            f"Skip amount must be an integer or a label"
                            f" name (got {skip!r})."
                        )

            elif command.command == 'label':
                command = cast(Label, command)
                label = resolveValue(command.name, scope)
                if not isinstance(label, str):
                    raise TypeError(
                        f"Label name must be a string (got {label!r})."
                    )

            else:
                raise ValueError(
                    f"Invalid command type: {command.command!r}"
                )
        except ValueError as e:
            raise CommandValueError(command, line, e)
        except TypeError as e:
            raise CommandTypeError(command, line, e)
        except IndexError as e:
            raise CommandIndexError(command, line, e)
        except KeyError as e:
            raise CommandKeyError(command, line, e)
        except Exception as e:
            raise CommandOtherError(command, line, e)

        return (scope, skip, label)

    def runCommandBlock(
        self,
        commands: List[Command],
        scope: Optional[Scope] = None
    ) -> Scope:
        """
        Runs a list of commands, using the given scope (or creating a new
        empty scope if none was provided). Returns the scope after
        running all of the commands, which may also edit the exploration
        and/or the current graph of course.

        Note that if a skip command would skip past the end of the
        block, execution will end. If a skip command would skip before
        the beginning of the block, execution will start from the first
        command.

        Example:

        >>> e = Exploration()
        >>> scope = e.runCommandBlock([
        ...    command('assign', 'decision', "'START'"),
        ...    command('call', 'exploration', 'start'),
        ...    command('empty', 'tuple'),
        ...    command('append', "'left'"),
        ...    command('append', "'right'"),
        ...    command('assign', 'transitions'),
        ...    command('call', 'exploration', 'observe'),
        ...    command('call', 'graph', 'destinationsFrom'),
        ...    command('call', 'builtin', 'print'),
        ...    command('assign', 'transition', "'right'"),
        ...    command('assign', 'destination', "'EastRoom'"),
        ...    command('call', 'exploration', 'explore'),
        ... ])
        {'left': '_u.0', 'right': '_u.1'}
        >>> scope['decision']
        'START'
        >>> scope['_'] is None
        True
        >>> scope['transitions']
        ('left', 'right')
        >>> scope['transition']
        'right'
        >>> scope['destination']
        'EastRoom'
        >>> g = e.currentGraph()
        >>> len(e)
        3
        >>> len(g)
        3
        >>> sorted(g)
        ['EastRoom', 'START', '_u.0']
        """
        if scope is None:
            scope = {}

        labelPositions: Dict[str, List[int]] = {}

        # Keep going until we've exhausted the commands list
        index = 0
        while index < len(commands):

            # Execute the next command
            scope, skip, label = self.runCommand(
                commands[index],
                scope,
                index + 1
            )

            # Increment our index, or apply a skip
            if skip is None:
                index = index + 1

            elif isinstance(skip, int):  # Integer skip value
                if skip < 0:
                    index += skip
                    if index < 0:  # can't skip before the start
                        index = 0
                else:
                    index += skip + 1  # may end loop if we skip too far

            else:  # must be a label name
                if skip in labelPositions:  # an established label
                    # We jump to the last previous index, or if there
                    # are none, to the first future index.
                    prevIndices = [
                        x
                        for x in labelPositions[skip]
                        if x < index
                    ]
                    futureIndices = [
                        x
                        for x in labelPositions[skip]
                        if x >= index
                    ]
                    if len(prevIndices) > 0:
                        index = max(prevIndices)
                    else:
                        index = min(futureIndices)
                else:  # must be a forward-reference
                    for future in range(index + 1, len(commands)):
                        inspect = commands[future]
                        if inspect.command == 'label':
                            inspect = cast(Label, inspect)
                            if inspect.name == skip:
                                index = future
                                break
                    else:
                        raise KeyError(
                            f"Skip command indicated a jump to label"
                            f" {skip!r} but that label had not already"
                            f" been defined and there is no future"
                            f" label with that name either (future"
                            f" labels based on variables cannot be"
                            f" skipped to from above as their names"
                            f" are not known yet)."
                        )

            # If there's a label, record it
            if label is not None:
                labelPositions.setdefault(label, []).append(index)

            # And now the while loop continues, or ends if we're at the
            # end of the commands list.

        # Return the scope object.
        return scope


#--------------------#
# JSON Serialization #
#--------------------#

class CustomJSONEncoder(json.JSONEncoder):
    """
    A custom JSON encoder that has special protocols for handling
    `Requirement`, `DecisionGraph`, and `Exploration` objects. It also
    handles `set`, `tuple`, and `namedtuple` objects specially so that
    those types can be decoded back to their original form.
    """
    def default(self, o: Any) -> Any:
        """
        Re-writes objects for encoding. We re-write `Requirement`,
        `DecisionGraph`, and `Exploration` objects.
        """
        if isinstance(o, tuple):
            if hasattr(o, '_fields') and hasattr(o, '__name__'):
                # Named tuples
                return {
                    '__decode_as__': 'namedtuple',
                    'name': o.__name__,  # type: ignore
                    'values': o._asdict()  # type: ignore
                    # TODO: Better way to type-check these?
                }
            else:  # Normal tuples
                return {
                    '__decode_as__': 'tuple',
                    'values': list(o)
                }

        elif isinstance(o, set):
            return {
                '__decode_as__': 'set',
                'values': list(o)
            }

        elif isinstance(o, Requirement):
            return {
                '__decode_as__': 'Requirement',
                'value': o.unparse()
            }

        elif isinstance(o, DecisionGraph):
            return {
                '__decode_as__': 'DecisionGraph',
                'node_links': nx.node_link_data(o),
                '_byEdge': o._byEdge,
                'zones': o.zones,
                'zoneMap': o.zoneMap,
                'unknownCount': o.unknownCount
            }

        elif isinstance(o, Exploration):
            return {
                '__decode_as__': 'Exploration',
                'graphs': o.graphs,
                'positions': o.positions,
                'states': o.states,
                'transitions': o.transitions,
                'annotations': o.annotations
            }


class CustomJSONDecoder(json.JSONDecoder):
    """
    A custom JSON decoder that has special protocols for handling
    `set`, `tuple`, `namedtuple`, `Requirement`, `DecisionGraph`, and
    `Exploration` objects.

    Examples:

    >>> r = ReqAny([ReqPower('power'), ReqTokens('money', 5)])
    >>> s = json.dumps(r, cls=CustomJSONEncoder)
    >>> s
    '{"__decode_as__": "Requirement", "value": "(power|money*5)"}'
    >>> l = json.loads(s, cls=CustomJSONDecoder)
    >>> r == l
    True
    """
    def __init__(self, *args, **kwargs):
        if 'object_hook' in kwargs:
            outerHook = kwargs['object_hook']
            kwargs['object_hook'] = (
                lambda o: outerHook(CustomJSONDecoder.unpack(o))
            )
            # TODO: What if it's a positional argument? :(
        else:
            kwargs['object_hook'] = CustomJSONDecoder.unpack
        super().__init__(*args, **kwargs)

    @staticmethod
    def unpack(obj: Any) -> Any:
        """
        Unpacks an object; used as the `object_hook` for decoding.
        """
        if '__decode_as__' in obj:
            asType = obj['__decode_as__']
            if asType == 'tuple':
                return tuple(obj['values'])

            elif asType == 'set':
                return set(obj['values'])

            elif asType == 'namedtuple':
                g = globals()
                name = obj['name']
                values = obj['values']
                # Use an existing global namedtuple class if there is
                # one that goes by the specified name, so that we don't
                # create too many spurious equivalent namedtuple
                # classes. But fall back on creating a new namedtuple
                # class if we need to:
                ntClass = g.get(name)
                if (
                    ntClass is None
                 or not issubclass(ntClass, tuple)
                 or not hasattr(ntClass, '_asdict')
                ):
                    ntClass = collections.namedtuple(  # type: ignore
                        name,
                        values.keys()
                    )
                ntClass = cast(Callable, ntClass)
                return ntClass(**values)

            elif asType == 'Requirement':
                return Requirement.parse(obj['value'])

            elif asType == 'DecisionGraph':
                baseGraph: nx.MultiDiGraph = nx.node_link_graph(
                    obj['node_links']
                )
                graphResult = DecisionGraph()
                # Copy over each attribute
                for attr in dir(baseGraph):
                    setattr(
                        graphResult,
                        attr,
                        copy.deepcopy(getattr(baseGraph, attr))
                    )
                graphResult._byEdge = obj['_byEdge']
                graphResult.zones = obj['zones']
                graphResult.zoneMap = obj['zoneMap']
                graphResult.unknownCount = obj['unknownCount']
                return graphResult

            elif asType == 'Exploration':
                exResult = Exploration()
                exResult.graphs = obj['graphs']
                exResult.positions = obj['positions']
                exResult.states = obj['states']
                exResult.transitions = obj['transitions']
                exResult.annotations = obj['annotations']
                return exResult

            else:
                raise NotImplementedError(
                    f"No special handling has been defined for"
                    f" '__decode_as__' value '{asType}'."
                )

        else:
            return obj
