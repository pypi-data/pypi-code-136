"""
- Authors: Peter Mawhorter
- Consulted:
- Date: 2022-9-4
- Purpose: Parsing for journal-format exploration records.

A journal fundamentally consists of a number of lines detailing
decisions reached, options observed, and options chosen. Other
information like enemies fought, items acquired, or general comments may
also be present.

The start of each line is a single letter that determines the entry
type, and remaining parts of that line separated by whitespace determine
the specifics of that entry. Indentation is allowed and ignored; its
suggested use is to indicate which entries apply to previous entries
(e.g., tags, annotations, effects, and requirements).

The `convertJournal` function converts a journal string into a
`core.Exploration` object, or adds to an existing exploration object if
one is specified.

To support slightly different journal formats, a `Format` dictionary is
used to define the exact notation used for various things.
"""

from __future__ import annotations

from typing import (
    Optional, List, Tuple, Dict, Union, Collection, get_args, cast,
    Sequence, Literal
)

import re
import warnings

from . import core


#----------------------#
# Parse format details #
#----------------------#

JournalEntryType = Literal[
    'zonePrefixes',
    'alias',
    'custom',

    'START',
    'explore',
    'return',
    'action',
    'retrace',
    'warp',
    'wait',
    'observe',
    'END',

    'requirement',
    'effect',
    'apply',

    'tag',
    'annotate',

    'zone',

    'unify',
    'obviate',

    'relative'
]
"""
One of the types of entries that can be present in a journal. Each
journal line is either an entry or a continuation of a previous entry.
The available types are:

- 'zonePrefixes': Appearing followed by one of the words 'on' or 'off',
    this specifies whether or not the names of level-0 zones should be
    automatically prepended to all room names specified. This applies to
    anywhere a room name is specified which does not contain a
    `zoneSeparator` already, and happens as entries are being parsed.
    The zone used is the level-0 zone of the current target decision
    (the exploration's current decision in normal mode and the target
    decision in relative mode).
- 'alias': Followed by zero or more words and then a block of commands,
    this establishes an alias that can be used as a custom command.
    Within the command block, curly braces surrounding a word will be
    replaced by the argument in the same position that that word appears
    following the alias (for example, an alias defined using:

        = redDoor name [
          o {name}
            qb red
        ]

    could be referenced using:

        > redDoor door

    and that reference would be equivalent to:

        o door
          qb red

    To help aliases be more flexible, if '_' is referenced between curly
    braces (or '_' followed by an integer), it will be substituted with
    an underscore followed by a unique number (these numbers will count
    up with each such reference used by a specific `JournalObserver`
    object). References within each alias substitution which are
    suffixed with the same digit (or which are unsuffixed) will get the
    same value. So for example, an alias:

        = savePoint [
          o {_}
          x {_} {_1} {_2}
              g savePoint
          a save
          t {_2}
        ]

    when deployed twice like this:

        > savePoint
        > savePoint

    might translate to:

        o _17
        x _17 _18 _19
            g savePoint
        a save
        t _19
        o _20
        x _20 _21 _22
            g savePoint
        a save
        t _22

- 'custom': Re-uses the code from a previously-defined alias. This command
    type is followed by an alias name and then one argument for each
    parameter of the named alias (see above for examples).

- 'START': Names the starting decision (and possibly a level-0 zone to
    place it in); must appear first except in journal fragments.
- 'explore': Names a transition taken and the decision reached as a
    result, possible with a name for the reciprocal transition which is
    created, and possibly with a zone name for the level-0 zone at the
    destination (if different from the zone of the origin). Use 'zone'
    afterwards to swap around zones above level 0.
- 'return': Names a transition taken and decision returned to,
    connecting a transition which previously connected to an unexplored
    area back to a known decision instead.
- 'action': Names an action taken at the current decision and may
    include effects and/or requirements.
- 'retrace': Names a transition taken, where the destination is already
    explored.
- 'wait': indicates a step of exploration where no transition is taken,
    optionally with effects that occur. Use 'action' instead for
    player-initiated effects.
- 'warp': Names a new decision to be at, but without adding a transition
    there from the previous decision. May also include a zone name to
    place the destination node into that level-0 zone (which will be
    created if necessary). If no zone name is provided but the
    destination is a novel decision, it will be placed into the same
    zones as the origin.
- 'observe': Names a transition observed from the current decision, or a
    transition plus destination if the destination is known, or a
    transition plus destination plus reciprocal if reciprocal
    information is also available. Observations don't create exploration
    steps.
- 'END': Names an ending which is reached from the current decision via
    a new automatically-named transition.

- 'requirement': Specifies a requirement to apply to the
    most-recently-defined transition or its reciprocal.
- 'effect': Specifies an effect to add to the most-recently-defined
    transition or its reciprocal. The remainder of the line should be
    parsable using `ParseFormat.parseEffect`.
- 'apply': Specifies an effect to be immediately applied to the current
    state, relative to the most-recently-taken or -defined transition. If
    a 'transition' target specifier is included, the effect will also be
    recorded as an effect of the most-recently-taken transition, but
    otherwise it will just be applied without being stored in the graph.
    Use this to capture surprising effects which only became apparent
    after a transition was taken, or without the transition target to
    specify changes that occurred without being associated with a
    transition (especially one-time changes).

- 'tag': Applies one or more tags to the current decision, or to either
    the most-recently-taken transition or its reciprocal if a target
    part is specified.
- 'annotate': Like 'tag' but applies an annotation.

- 'zone': Specifies a zone name and a level (via extra `zonePart`
    characters) that will replace the current zone at the given
    hierarchy level for the current decision. This is done using the
    `core.Exploration.reZone` method.

- 'unify': Specifies a decision with which the current decision will be
    unified (or two decisions that will be unified with each other),
    merging their transitions. Can instead target a transition or
    reciprocal to merge (which must be at the current decision), although
    the transition to merge with must either lead to the same destination
    or lead to an unknown destination (which will then be merged with the
    transition's destination).
- 'obviate': Specifies a transition at the current decision and a
    decision that it links to and updates that information, without
    actually crossing the transition. The reciprocal transition must also
    be specified, although one will be created if it didn't already
    exist. If the reciprocal does already exist, it must lead to an
    unknown decision.

- 'relative': Specifies a decision to be treated as the 'current
    decision' without actually setting the position there. Until used to
    reverse this effect, all position-changing entries change this
    relative position value instead of the actual position in the graph,
    and updates are applied to the current graph without creating new
    exploration steps or applying any effects. Useful for doing things
    like noting information about far-away locations disclosed in a
    cutscene. Can target a transition at the current node, in which case
    that is counted as the 'most-recent-transition' for entry purposes
    and the same relative mode is entered.
"""

JournalTargetType = Literal[
    'decisionPart',
    'transitionPart',
    'reciprocalPart',
    'bothPart',
    'zonePart',
]
"""
The different parts that an entry can target. The signifiers for these
target types will be concatenated with a journal entry signifier in some
cases. For example, by default 'g' as an entry type means 'tag', and 't'
as a target type means 'transition'. So 'gt' as an entry type means 'tag
transition' and applies the relevant tag to the most-recently-created
transition instead of the most-recently-created decision. The available
target parts are each valid only for specific entry types. The target
parts are:

- 'decisionPart' - Use to specify that the entry applies to a decision
    when it would normally apply to something else.
- 'transitionPart' - Use to specify that the entry applies to a
    transition instead of a decision.
- 'reciprocalPart' - Use to specify that the entry applies to a
    reciprocal transition instead of a decision or the normal
    transition.
- 'bothPart' - Use to specify that the entry applies to both of two
    possibilities, such as to a transition and its reciprocal.
- 'zonePart' - Use only for re-zoning to indicate the hierarchy level. May
    be repeated; each instance increases the hierarchy level by 1
    starting from 0.

The entry types where a target specifier can be applied are:

- 'requirement': By default these are applied to transitions, but the
    'reciprocalPart' target can be used to apply to a reciprocal
    instead. Use `bothPart` to apply the same requirement to both the
    transition and its reciprocal.
- 'effect': Same as 'requirement'.
- 'apply': Same as 'requirement'.
- 'tag': Applies the tag to the specified target instead of the
    most-recently-created decision, which is the default.
- 'annotation': Same as 'tag', but can also use a decision-part target
    to annotate the current decision (default is to annotate the
    exploration step).
- 'unify': By default applies to a decision, but can be applied to a
    transition or reciprocal instead.
- 'relative': Only 'transition' applies here and changes the
    most-recent-transition value when entering relative mode instead of
    just changing the current-decision value. Can be used within
    relative mode to pick out an existing transition as well.
- 'zone': This is the only place where the 'zonePart' target type
    applies, and it can actually be applied as many times as you want.
    Each application makes the zone specified apply to a higher level in
    the hierarchy of zones, so that instead of swapping the level-0 zone
    using 'z', the level-1 zone can be changed using 'zz' or the level 2
    zone using 'zzz', etc.
"""

JournalInfoType = Literal[
    'on',
    'off',
    'comment',
    'unknownItem',
    'tokenQuantity',
    'requirement',
    'reciprocalSeparator',
    'zoneSeparator',
    'transitionAtDecision',
    'blockDelimiters',
]
"""
Represents a part of the journal syntax which isn't an entry type but is
used to mark something else. For example, the character denoting an
unknown item. The available values are:

- 'on': The word or character used to indicate toggling something on.
- 'off': The word or character used to indicate toggling something off.
- 'unknownItem': Used in place of an item name to indicate that
    although an item is known to exist, it's not yet know what that item
    is. Note that when journaling, you should make up names for items
    you pick up, even if you don't know what they do yet. This notation
    should only be used for items that you haven't picked up because
    they're inaccessible, and despite being apparent, you don't know
    what they are because they come in a container (e.g., you see a
    sealed chest, but you don't know what's in it).
- 'tokenQuantity': This is used to separate a token name from a token
    quantity when defining items picked up. Note that the parsing for
    requirements is not as flexible, and always uses '*' for this, so to
    avoid confusion it's preferable to leave this at '*'.
- 'reciprocalSeparator': Used to indicate, within a requirement or a
    tag set, a separation between requirements/tags to be applied to the
    forward direction and requirements/tags to be applied to the reverse
    direction. Not always applicable (e.g., actions have no reverse
    direction).
- 'zoneSeparator': Used to separate zone part(s) from a decision name part
    from a decision name which includes zone information.
- 'transitionAtDecision' Used to separate a decision name from a
    transition name when identifying a specific transition.
- 'blockDelimiters' Two characters used to delimit the start and end of
    a block of entries. Used for things like edit effects.
"""

JournalEffectType = Literal[
    'gain',
    'lose',
    'toggle',
    'deactivate',
    'edit'
]
"""
Represents a type of effect. The available types are:

- 'gain': The player gains powers and/or tokens. Multiple powers/tokens
    can be listed in a single effect line. Use the 'tokenQuantity' glyph
    to distinguish between powers and tokens (e.g., 'key' is a power,
    but 'key*1' is a single key token, if '*' is the 'tokenQuantity'
    marker).
- 'lose': The inverse of 'gain'.
- 'toggle': Lists multiple powers that will be toggled on/off in turn on
    successive transitions. If there's just one power, it is gained and
    then lost in succession, if there are multiple, the *n*th transition
    will cause the player to gain the *n*th power, and lose all of the
    other listed powers. TODO: Toggling for game states!
- 'deactivate': Deactivates the transition it is associated with, by
    setting the requirement to `ReqImpossible`.
- 'edit': This is the most complex effect: it is followed by one or more
    multi-line blocks (using `blockDelimiters`) which represent lists of
    commands to be run on subsequent activations of the effect. With only
    a single commands block, that block runs every time the effect
    triggers. With more than one, each subsequent triggering of the
    effect triggers the next block, until it wraps around to the first
    block again when it runs out. The commands are parsed using
    `core.parseCommandList` and saved as a list of commands (one such
    list per block) which is executed using
    `core.exploration.runCommandBlock`. The '@', '@t', '@r', and '@d'
    variables will be set when executing an edit command tied to a
    transition: '@' will be the source decision, '@t' will be the
    transition, and '@r' will be the reciprocal of the transition (if
    there is one) and '@d' will be the destination decision.

    The commands are executed in relative
    mode where the target starts as the decision + transition that the
    effect is being attached to. The commands in the block cannot exit
    relative mode (such a command would be an error) and so they only edit
    the graph without adding steps.

    The command blocks are interpreted like aliases, although they cannot
    use parameter substitution except for unique names.
"""

JournalEffectModifier = Literal[
    'charges',
    'delay',
]
"""
A modifier that can apply to an effect. One of:

- 'charges': Specifies that the effect can only be applied a certain
    number of times before being used up. An effect with charges
    subtracts one charge each time it is applied. If it has zero
    or negative charges, it will be skipped, and the number of charges
    will not be decremented.
- 'delay': Specifies that an effect doesn't apply until the nth time it
    would normally apply. Whenever an effect with a delay would normally
    be applied, instead the delay value is reduced by 1. Only if the
    delay value is zero or negative does the effect actually apply (and
    in that case, the delay value is unchanged).
"""

JournalMarkerType = Union[
    JournalEntryType,
    JournalTargetType,
    JournalInfoType,
    JournalEffectType,
    JournalEffectModifier
]
"Any journal marker type."


Format = Dict[JournalMarkerType, str]
"""
A journal format is specified using a dictionary with keys that denote
journal marker types and values which are one-to-several-character
strings indicating the markup used for that entry/info type.
"""

DEFAULT_FORMAT: Format = {
    # Toggles
    'zonePrefixes': 'P',

    # Alias handling
    'alias': '=',
    'custom': '>',

    # Core methods
    'START': 'S',
    'explore': 'x',
    'return': 'r',
    'action': 'a',
    'retrace': 't',
    'wait': 'w',
    'warp': 'p',
    'observe': 'o',
    'END': 'E',

    # Transition properties
    'requirement': 'q',
    'effect': 'e',
    'apply': 'A',

    # Tags & annotations
    'tag': 'g',
    'annotate': 'n',

    # Zones
    'zone': 'z',

    # Revisions
    'unify': 'u',
    'obviate': 'v',

    # Relative mode
    'relative': '@',

    # Target specifiers
    'decisionPart': 'd',
    'transitionPart': 't',
    'reciprocalPart': 'r',
    'bothPart': 'b',
    'zonePart': 'z',

    # Info markers
    'on': 'on',
    'off': 'off',
    'comment': '#',
    'unknownItem': '?',
    'tokenQuantity': '*',
    'reciprocalSeparator': '/',
    'zoneSeparator': '::',
    'transitionAtDecision': '%',
    'blockDelimiters': '[]',

    # Effect types
    'gain': 'gain',
    'lose': 'lose',
    'toggle': 'toggle',
    'deactivate': 'deactivate',
    'edit': 'edit',

    # Effect modifiers
    'charges': '*',
    'delay': ',',
}
"""
The default `Format` dictionary.
"""


class ParseFormat:
    """
    A ParseFormat manages the mapping from markers to entry types and
    vice versa.
    """
    def __init__(self, formatDict: Format = DEFAULT_FORMAT):
        """
        Sets up the parsing format. Requires a `Format` dictionary to
        define the specifics. Raises a `ValueError` unless the keys of
        the `Format` dictionary exactly match the `JournalMarkerType`
        values.
        """
        self.formatDict = formatDict

        # Build comment regular expression
        self.commentRE = re.compile(
            formatDict.get('comment', '#') + '.*$',
            flags=re.MULTILINE
        )

        # Get block delimiters
        blockDelimiters = formatDict.get('blockDelimiters', '[]')
        if len(blockDelimiters) != 2:
            raise ValueError(
                f"Block delimiters must be a length-2 string containing"
                f" the start and end markers. Got: {blockDelimiters!r}."
            )
        blockStart = blockDelimiters[0]
        blockEnd = blockDelimiters[1]
        self.blockStart = blockStart
        self.blockEnd = blockEnd

        # Add backslash for literal if it's an RE special char
        if blockStart in '[]()*.?^$&+\\':
            blockStart = '\\' + blockStart
        if blockEnd in '[]()*.?^$&+\\':
            blockEnd = '\\' + blockEnd

        # Build block start and end regular expressions
        self.blockStartRE = re.compile(
            blockStart + r'\s*$',
            flags=re.MULTILINE
        )
        self.blockEndRE = re.compile(
            r'^\s*' + blockEnd,
            flags=re.MULTILINE
        )

        # Check that formatDict doesn't have any extra keys
        markerTypes = (
            get_args(JournalEntryType)
          + get_args(JournalTargetType)
          + get_args(JournalInfoType)
          + get_args(JournalEffectType)
          + get_args(JournalEffectModifier)
        )
        for key in formatDict:
            if key not in markerTypes:
                raise ValueError(
                    f"Format dict has key '{key}' which is not a"
                    f" recognized entry or info type."
                )

        # Check completeness of formatDict
        for mtype in markerTypes:
            if mtype not in formatDict:
                raise ValueError(
                    f"Format dict is missing an entry for marker type"
                    f" '{mtype}'."
                )

        # Build reverse dictionaries from markers to entry types and
        # from markers to target types (no reverse needed for info
        # types).
        self.entryMap: Dict[str, JournalEntryType] = {}
        self.targetMap: Dict[str, JournalTargetType] = {}
        self.effectMap: Dict[str, JournalEffectType] = {}
        self.effectModMap: Dict[str, JournalEffectModifier] = {}
        entryTypes = set(get_args(JournalEntryType))
        targetTypes = set(get_args(JournalTargetType))
        effectTypes = set(get_args(JournalEffectType))
        effectModifierTypes = set(get_args(JournalEffectModifier))

        # Check for duplicates and create reverse maps
        for name, marker in formatDict.items():
            if name in entryTypes:
                # Duplicates not allowed among entry types
                if marker in self.entryMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.entryMap[marker]}'."
                    )

                # Map markers to entry types
                self.entryMap[marker] = cast(JournalEntryType, name)
            elif name in targetTypes:
                # Duplicates not allowed among entry types
                if marker in self.targetMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.targetMap[marker]}'."
                    )

                # Map markers to entry types
                self.targetMap[marker] = cast(JournalTargetType, name)
            elif name in effectTypes:
                # Duplicates not allowed among effect types
                if marker in self.effectMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.effectMap[marker]}'."
                    )

                # Map markers to entry types
                self.effectMap[marker] = cast(JournalEffectType, name)

            elif name in effectModifierTypes:
                # Duplicates not allowed among effect types
                if marker in self.effectModMap:
                    raise ValueError(
                        f"Format dict entry for '{name}' duplicates"
                        f" previous format dict entry for"
                        f" '{self.effectModMap[marker]}'."
                    )

                # Map markers to entry types
                self.effectModMap[marker] = cast(
                    JournalEffectModifier,
                    name
                )

            # else ignore it since it's an info type

    def markers(self) -> List[str]:
        """
        Returns the list of all entry-type markers (but not other kinds
        of markers), sorted from longest to shortest to help avoid
        ambiguities when matching.
        """
        entryTypes = get_args(JournalEntryType)
        return sorted(
            (
                m
                for (et, m) in self.formatDict.items()
                if et in entryTypes
            ),
            key=lambda m: -len(m)
        )

    def markerFor(self, markerType: JournalMarkerType) -> str:
        """
        Returns the marker for the specified entry/info/effect/etc.
        type.
        """
        return self.formatDict[markerType]

    def determineEntryType(self, entryBits: List[str]) -> Tuple[
        JournalEntryType,
        Union[None, JournalTargetType, int],
        List[str]
    ]:
        """
        Given a sequence of strings that specify a command, returns a
        tuple containing the entry type, target part, and list of
        arguments for that command. If no target type was included, the
        second entry of the return value will be `None`, and in the
        special case of zones, it will be an integer indicating the
        hierarchy level according to how many times the 'zonePart'
        target specifier was present, default 0.
        """
        # Get entry specifier
        entrySpecifier = entryBits[0]
        entryArgs = entryBits[1:]

        # Figure out entry type from first character
        typeSpecifier = entrySpecifier[0]
        if typeSpecifier not in self.entryMap:
            raise JournalParseError(
                f"Entry does not begin with a recognized entry"
                f" marker:\n{entryBits}"
            )
        entryType = self.entryMap[typeSpecifier]

        # Figure out the entry target from second+ character(s)
        targetSpecifiers = entrySpecifier[1:]
        entryTarget: Union[None, JournalTargetType, int] = None
        if entryType == 'zone':
            specifiers = set(targetSpecifiers)
            if len(specifiers) > 0 and specifiers != {'z'}:
                raise JournalParseError(
                    f"Invalid target specifier for zone:\n{entryBits}"
                )
            entryTarget = len(targetSpecifiers)
        elif len(targetSpecifiers) > 0:
            if len(targetSpecifiers) > 1:
                raise JournalParseError(
                    f"Entry has too many target specifiers:\n{entryBits}"
                )
            elif targetSpecifiers not in self.targetMap:
                raise JournalParseError(
                    f"Unrecognized target specifier:\n{entryBits}"
                )
            entryTarget = self.targetMap[targetSpecifiers]
        # else entryTarget remains None

        return (entryType, entryTarget, entryArgs)

    def onOff(self, word: str) -> Optional[bool]:
        """
        Parse an on/off indicator and returns a boolean (`True` for on
        and `False` for off). Returns `None` if the word isn't either
        the 'on' or the 'off' word. Generates a `JournalParseWarning`
        (and still returns `None`) if the word is a case-swapped version
        of the 'on' or 'off' word and is not equal to either of them.
        """
        onWord = self.formatDict['on']
        offWord = self.formatDict['off']

        # Generate warning if we suspect a case error
        if (
            word.casefold() in (onWord, offWord)
        and word not in (onWord, offWord)
        ):
            warnings.warn(
                (
                    f"Word '{word}' cannot be interpreted as an on/off"
                    f" value, although it is almost one (the correct"
                    f" values are '{onWord}' and '{offWord}'."
                ),
                JournalParseWarning
            )

        # return the appropriate value
        if word == onWord:
            return True
        elif word == offWord:
            return False
        else:
            return None

    def hasZoneParts(self, name: str) -> bool:
        """
        Returns true if the specified name contains zone parts (using
        the `zoneSeparator`).
        """
        return self.formatDict["zoneSeparator"] in name

    def splitZone(
        self,
        name: str
    ) -> Tuple[List[core.Zone], core.Decision]:
        """
        Splits a decision name that includes zone information into the
        list-of-zones part and the decision part. If there is no zone
        information in the name, the list-of-zones will be an empty
        list.
        """
        sep = self.formatDict['zoneSeparator']
        parts = name.split(sep)
        return (list(parts[:-1]), parts[-1])

    def prefixWithZone(
        self,
        name: core.Decision,
        zone: core.Zone
    ) -> core.Decision:
        """
        Returns the given decision name, prefixed with the given zone
        name. Does NOT check whether the decision name already includes
        a prefix or not.
        """
        return zone + self.formatDict['zoneSeparator'] + name

    def parseSpecificTransition(
        self,
        content: str
    ) -> Tuple[core.Decision, core.Transition]:
        """
        Splits a decision:transition pair to the decision and transition
        part, using a custom separator if one is defined.
        """
        sep = self.formatDict['transitionAtDecision']
        n = content.count(sep)
        if n == 0:
            raise JournalParseError(
                f"Cannot split '{content}' into a decision name and a"
                f" transition name (no separator '{sep}' found)."
            )
        elif n > 1:
            raise JournalParseError(
                f"Cannot split '{content}' into a decision name and a"
                f" transition name (too many ({n}) '{sep}' separators"
                f" found)."
            )
        else:
            return cast(
                Tuple[core.Decision, core.Transition],
                tuple(content.split(sep))
            )

    def splitDirections(
        self,
        content: str
    ) -> Tuple[Optional[str], Optional[str]]:
        """
        Splits a piece of text using the 'reciprocalSeparator' into two
        pieces. If there is no separator, the second piece will be
        `None`; if either side of the separator is blank, that side will
        be `None`, and if there is more than one separator, a
        `JournalParseError` will be raised. Whitespace will be stripped
        from both sides of each result.

        Examples:

        >>> pf = ParseFormat()
        >>> pf.splitDirections('abc / def')
        ('abc', 'def')
        >>> pf.splitDirections('abc def ')
        ('abc def', None)
        >>> pf.splitDirections('abc def /')
        ('abc def', None)
        >>> pf.splitDirections('/abc def')
        (None, 'abc def')
        >>> pf.splitDirections('a/b/c') # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
          ...
        JournalParseError: ...
        """
        sep = self.formatDict['reciprocalSeparator']
        count = content.count(sep)
        if count > 1:
            raise JournalParseError(
                f"Too many split points ('{sep}') in content:"
                f" '{content}' (only one is allowed)."
            )

        elif count == 1:
            before, after = content.split(sep)
            before = before.strip()
            after = after.strip()
            return (before or None, after or None)

        else: # no split points
            stripped = content.strip()
            if stripped:
                return stripped, None
            else:
                return None, None

    def parseItem(
        self,
        item: str
    ) -> Union[core.Power, Tuple[core.Token, int]]:
        """
        Parses an item, which is either a power (just a string) or a
        token-type:number pair (returned as a tuple with the number
        converted to an integer). The 'tokenQuantity' format value
        determines the separator which indicates a token instead of a
        power.
        """
        sep = self.formatDict['tokenQuantity']
        if sep in item:
            # It's a token w/ an associated count
            parts = item.split(sep)
            if len(parts) != 2:
                raise JournalParseError(
                    f"Item '{item}' has a '{sep}' but doesn't separate"
                    f" into a token type and a count."
                )
            typ, count = parts
            try:
                num = int(count)
            except ValueError:
                raise JournalParseError(
                    f"Item '{item}' has invalid token count '{count}'."
                )

            return (typ, num)
        else:
            # It's just a power
            return item

    def effectType(self, effectMarker: str) -> Optional[JournalEffectType]:
        """
        Returns the `JournalEffectType` string corresponding to the
        given effect marker string. Returns `None` for an unrecognized
        marker.
        """
        return self.effectMap.get(effectMarker)

    def effectModifier(
        self,
        arg: str
    ) -> Optional[Tuple[JournalEffectModifier, int]]:
        """
        Given an effect argument, determines whether or not it's an
        effect modifier. If it is not, it returns `None`. If it is a
        modifier, it returns a tuple containing the modifier type (one
        of the `JournalEffectModifier` strings) and the modifier value
        (an integer).
        """
        # Iterate through possibilities from longest to shortest to
        # avoid a shorter key which is a prefix of a longer key from
        # stealing values:
        for key in sorted(self.effectModMap, key=lambda x: -len(x)):
            # If arg starts with a key, it's a modifier
            if arg.startswith(key):
                modType = self.effectModMap[key]
                try:
                    modValue = int(arg[len(key):])
                except ValueError:
                    raise JournalParseError(
                        f"An effect modifier must consist of a modifier"
                        f" marker plus an integer. The argument {arg}"
                        f" starts with '{key}' but the rest of it is"
                        f" not an integer."
                    )
                return modType, modValue

        return None

    def parseEffect(self, effectParts: List[str]) -> core.TransitionEffect:
        """
        Given a list of strings specifying an effect, returns the
        `TransitionEffect` object that it specifies.
        """

        # Check for empty list
        if len(effectParts) == 0:
            raise JournalParseError(
                "Effect must include at least a type."
            )

        # Get the effect type
        fType = self.effectType(effectParts[0])

        if fType is None:
            raise JournalParseError(
                f"Unrecognized effect type {effectParts[0]}. Check the"
                f" JournalEffectType entries in the format dictionary."
            )

        # Default result
        result: core.TransitionEffect = {
            'type': fType,
            'value': None,  # likely invalid for the specific type
            'delay': None,
            'charges': None
        }

        # Process delay and charge modifiers at any point among the
        # arguments.
        cleanArgs = []
        seen: Dict[JournalEffectModifier, str] = {}
        for arg in effectParts[1:]:
            mod = self.effectModifier(arg)
            if mod is not None:
                modType, value = mod
                # Warn about duplicate modifiers
                if modType in seen:
                    warnings.warn(
                        (
                            f"Got multiple values for '{modType}':"
                            f" {seen[modType]!r} and {arg!r}. Only the"
                            f" last one will apply."
                        ),
                        JournalParseWarning
                    )
                seen[modType] = arg
                result[modType] = value
            else:
                cleanArgs.append(arg)

        if fType in ("gain", "lose"):
            if len(cleanArgs) != 1:
                raise JournalParseError(
                    f"'{fType}' effect must have exactly one argument (got"
                    f" {len(cleanArgs)}."
                )
            result['value'] = self.parseItem(cleanArgs[0])

        elif fType == "toggle":
            items = [self.parseItem(arg) for arg in cleanArgs]
            if any(not isinstance(item, core.Power) for item in items):
                raise JournalParseError(
                    "Only powers may be toggled, not tokens."
                )
            result['value'] = cast(List[core.Power], items)

        elif fType == "deactivate":
            if len(cleanArgs) != 0:
                raise JournalParseError(
                    f"A 'deactivate' effect may not include any"
                    f" arguments (got {len(cleanArgs)})."
                )

        elif fType == "edit":
            if len(cleanArgs) == 0:
                raise JournalParseError(
                    "An 'edit' effect requires at least one argument."
                )
            result["value"] = cast(List[List[core.Command]], [])
            for arg in cleanArgs:
                cast(
                    List[List[core.Command]],
                    result["value"]
                ).append(core.parseCommandList(arg))

        return result

    def removeComments(self, text: str) -> str:
        """
        Given one or more lines from a journal, removes all comments from
        it/them. Any '#' and any following characters through the end of
        a line counts as a comment.

        Returns the text without comments.

        Example:

        >>> pf = ParseFormat()
        >>> pf.removeComments('abc # 123')
        'abc '
        >>> pf.removeComments('''\\
        ... line one # comment
        ... line two # comment
        ... line three
        ... line four # comment
        ... ''')
        'line one \\nline two \\nline three\\nline four \\n'
        """
        return self.commentRE.sub('', text)

    def findBlockEnd(self, string: str, startIndex: int) -> int:
        """
        Given a string and a start index where a block open delimiter
        is, returns the index within the string of the matching block
        closing delimiter.

        There are two possibilities: either both the opening and closing
        delimiter appear on the same line, or the block start appears at
        the end of a line (modulo whitespce) and the block end appears
        at the beginning of a line (modulo whitespace). Any other
        configuration is invalid and may lead to a `JournalParseError`.

        Note that blocks may be nested within each other, including
        nesting single-line blocks in a multi-line block. It's also
        possible for several single-line blocks to appear on the same
        line.

        Examples:

        >>> pf = ParseFormat()
        >>> pf.findBlockEnd('[ A ]', 0)
        4
        >>> pf.findBlockEnd('[ A ] [ B ]', 0)
        4
        >>> pf.findBlockEnd('[ A ] [ B ]', 6)
        10
        >>> pf.findBlockEnd('[ A [ B ] ]', 0)
        10
        >>> pf.findBlockEnd('[ A [ B ] ]', 4)
        8
        >>> pf.findBlockEnd('[ [ B ]', 0)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[\\nABC\\n]', 0)
        6
        >>> pf.findBlockEnd('[\\nABC]', 0)  # End marker must start line
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[\\nABC\\nDEF[\\nGHI\\n]\\n  ]', 0)
        19
        >>> pf.findBlockEnd('[\\nABC\\nDEF[\\nGHI\\n]\\n  ]', 9)
        15
        >>> pf.findBlockEnd('[\\nABC\\nDEF[ GHI ]\\n  ]', 0)
        19
        >>> pf.findBlockEnd('[\\nABC\\nDEF[ GHI ]\\n  ]', 9)
        15
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 0)
        24
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 11)
        22
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n  ]\\n]', 16)
        18
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H \\n  ]\\n]', 16)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        >>> pf.findBlockEnd('[  \\nABC\\nDEF[\\nGHI[H]\\n\\n]', 0)
        Traceback (most recent call last):
        ...
        exploration.journal.JournalParseError...
        """
        # Find end of the line that the block opens on
        try:
            endOfLine = string.index('\n', startIndex)
        except ValueError:
            endOfLine = len(string)

        # Determine if this is a single-line or multi-line block based
        # on the presence of *anything* after the opening delimiter
        restOfLine = string[startIndex + 1:endOfLine]
        if restOfLine.strip() != '':  # A single-line block
            level = 1
            for restIndex, char in enumerate(restOfLine):
                if char == self.blockEnd:
                    level -= 1
                    if level <= 0:
                        break
                elif char == self.blockStart:
                    level += 1

            if level == 0:
                return startIndex + 1 + restIndex
            else:
                raise JournalParseError(
                    f"Got to end of line in single-line block without"
                    f" finding the matching end-of-block marker."
                    f" Remainder of line is:\n  {restOfLine!r}"
                )

        else:  # It's a multi-line block
            level = 1
            index = startIndex + 1
            while level > 0 and index < len(string):
                nextStart = self.blockStartRE.search(string, index)
                nextEnd = self.blockEndRE.search(string, index)
                if nextEnd is None:
                    break  # no end in sight; level won't be 0
                elif (
                    nextStart is None
                 or nextStart.start() > nextEnd.start()
                ):
                    index = nextEnd.end()
                    level -= 1
                    if level <= 0:
                        break
                else:  # They cannot be equal
                    index = nextStart.end()
                    level += 1

            if level == 0:
                if nextEnd is None:
                    raise RuntimeError(
                        "Parsing got to level 0 with no valid end"
                        " match."
                    )
                return nextEnd.end() - 1
            else:
                raise JournalParseError(
                    f"Got to the end of the entire string and didn't"
                    f" find a matching end-of-block marker. Started at"
                    f" index {startIndex}."
                )


#-------------------#
# Errors & Warnings #
#-------------------#

class JournalParseError(ValueError):
    """
    Represents a error encountered when parsing a journal.
    """
    pass


class LocatedJournalParseError(JournalParseError):
    """
    An error during journal parsing that includes additional location
    information.
    """
    def __init__(
        self,
        src: str,
        index: int,
        cause: Exception
    ) -> None:
        """
        In addition to the underlying error, the journal source text and
        the index within that text where the error occurred are
        required.
        """
        super().__init__("localized error")
        self.src = src
        self.index = index
        self.cause = cause

    def __str__(self):
        """
        Includes information about the location of the error and the
        line it appeared on.
        """
        context, line, pos = errorContext(self.src, self.index)
        context = context.rstrip('\n')
        return (
            f"\n  In journal on line {line} near character {pos}:"
            f"\n    {context}"
            f"\n  Error is:"
            f"\n{type(self.cause).__name__}: {self.cause}"
        )


def errorContext(string: str, index: int) -> Optional[Tuple[str, int, int]]:
    """
    Returns the line of text, the line number, and the character within
    that line for the given absolute index into the given string.
    Newline characters count as the last character on their line. Lines
    and characters are numbered starting from 1.

    Returns `None` for out-of-range indices.

    Examples:

    >>> errorContext('a\\nb\\nc', 0)
    ('a\\n', 1, 1)
    >>> errorContext('a\\nb\\nc', 1)
    ('a\\n', 1, 2)
    >>> errorContext('a\\nbcd\\ne', 2)
    ('bcd\\n', 2, 1)
    >>> errorContext('a\\nbcd\\ne', 3)
    ('bcd\\n', 2, 2)
    >>> errorContext('a\\nbcd\\ne', 4)
    ('bcd\\n', 2, 3)
    >>> errorContext('a\\nbcd\\ne', 5)
    ('bcd\\n', 2, 4)
    >>> errorContext('a\\nbcd\\ne', 6)
    ('e', 3, 1)
    >>> errorContext('a\\nbcd\\ne', -1)
    ('e', 3, 1)
    >>> errorContext('a\\nbcd\\ne', -2)
    ('bcd\\n', 2, 4)
    >>> errorContext('a\\nbcd\\ne', 7) is None
    True
    >>> errorContext('a\\nbcd\\ne', 8) is None
    True
    """
    # Convert negative to positive indices
    if index < 0:
        index = len(string) + index

    # Return None for out-of-range indices
    if not 0 <= index < len(string):
        return None

    # Count lines + look for start-of-line
    line = 1
    lineStart = 0
    for where, char in enumerate(string):
        if where >= index:
            break
        if char == '\n':
            line += 1
            lineStart = where + 1

    try:
        endOfLine = string.index('\n', where)
    except ValueError:
        endOfLine = len(string)

    return (string[lineStart:endOfLine + 1], line, index - lineStart + 1)


class JournalParseWarning(Warning):
    """
    Represents a warning encountered when parsing a journal.
    """
    pass


class PathEllipsis:
    """
    Represents part of a path which has been omitted from a journal and
    which should therefore be inferred.
    """
    pass


#-----------------#
# Parsing manager #
#-----------------#


class JournalObserver:
    """
    Keeps track of extra state needed when parsing a journal in order to
    produce a `core.Exploration` object. The methods of this class act
    as an API for constructing explorations that have several special
    properties. The API is designed to allow journal entries (which
    represent specific observations/events during an exploration) to be
    directly accumulated into an exploration object, including entries
    which apply to things like the most-recent-decision or -transition.

    You can use the `convertJournal` function to handle things instead,
    since that function creates and manages a `JournalObserver` object
    for you.

    The basic usage is as follows:

    1. Create a `JournalObserver`, optionally specifying a custom
        `ParseFormat`.
    2. Repeatedly either:
        * Call `record*` API methods corresponding to specific entries
            observed or...
        * Call `JournalObserver.observe` to parse one or more
            journal blocks from a string and call the appropriate
            methods automatically.
    3. Call `JournalObserver.getExploration` to retrieve the
        `core.Exploration` object that's been created.

    You can just call `convertJournal` to do all of these things at
    once.

    Notes:

    - `JournalObserver.getExploration` may be called at any time to get
        the exploration object constructed so far, and that that object
        (unless it's `None`) will always be the same object (which gets
        modified as entries are recorded). Modifying this object
        directly is possible for making changes not available via the
        API, but must be done carefully, as there are important
        conventions around things like decision names that must be
        respected if the API functions need to keep working.
    - To get the latest graph, simply use the
        `core.Exploration.currentGraph` method of the
        `JournalObserver.getExploration` result.

    ## Examples

    >>> obs = JournalObserver()
    >>> e = obs.getExploration()
    >>> len(e) # blank starting state
    1
    >>> e.getPositionAtStep(0) # position is None before starting
    >>> # We start by using the record* methods...
    >>> obs.recordStart("Start")
    >>> obs.recordObserve("bottom")
    >>> len(e) # blank + started states
    2
    >>> e.positionAtStep(1)
    'Start'
    >>> obs.recordExplore("left", "West", "right")
    >>> len(e) # starting states + one step
    3
    >>> e.positionAtStep(1)
    'Start'
    >>> e.transitionAtStep(1)
    'left'
    >>> e.positionAtStep(2)
    'West'
    >>> obs.recordRetrace("right")
    >>> len(e) # starting states + two steps
    4
    >>> e.positionAtStep(1)
    'Start'
    >>> e.transitionAtStep(1)
    'left'
    >>> e.positionAtStep(2)
    'West'
    >>> e.transitionAtStep(2)
    'right'
    >>> e.positionAtStep(3)
    'Start'
    >>> obs.recordRetrace("bad") # transition doesn't exist
    Traceback (most recent call last):
    ...
    exploration.core.MissingTransitionError...
    >>> obs.recordObserve('right', 'East', 'left')
    >>> e.currentGraph().getTransitionRequirement('Start', 'right')
    ReqNothing()
    >>> obs.recordRequirement('crawl|small')
    >>> e.currentGraph().getTransitionRequirement('Start', 'right')
    ReqAny([ReqPower('crawl'), ReqPower('small')])
    >>> # The use of relative mode to add remote observations
    >>> obs.relative('East')
    >>> obs.recordObserve('top_vent')
    >>> obs.recordRequirement('crawl')
    >>> obs.recordReciprocalRequirement('crawl')
    >>> obs.recordExplore('right_door', 'Outside', 'left_door')
    >>> obs.recordRequirement('X')
    >>> obs.recordReciprocalRequirement('X')
    >>> obs.recordAction('lever') # no info on what it does yet...
    >>> # TODO door-toggling lever example
    >>> obs.relative() # leave relative mode
    >>> len(e) # starting states + two steps, no steps happen in relative mode
    4
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement(
    ...     g.getDestination('East', 'top_vent'),
    ...     'return'
    ... )
    ReqPower('crawl')
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqPower('crawl')
    >>> g.getTransitionRequirement('East', 'right_door')
    ReqImpossible()
    >>> g.getTransitionRequirement('Outside', 'left_door')
    ReqImpossible()
    >>> # Now we demonstrate the use of "observe"
    >>> obs.observe("o up Attic down\\nx up\\no vent\\nq crawl")
    >>> e.currentPosition()
    'Attic'
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement('Attic', 'vent')
    ReqPower('crawl')
    >>> sorted(list(g.destinationsFrom('Attic').items()))
    [('down', 'Start'), ('vent', '_u.6')]
    >>> obs.observe("a getCrawl\\nAt gain crawl\\nr vent East top_vent")
    >>> g = e.currentGraph()
    >>> g.getTransitionRequirement('East', 'top_vent')
    ReqPower('crawl')
    >>> g.getDestination('Attic', 'vent')
    'East'
    >>> g.getDestination('East', 'top_vent')
    'Attic'
    >>> len(e) # exploration, action, and return are each 1
    7
    >>> e.positionAtStep(3)
    'Start'
    >>> e.transitionAtStep(3)
    'up'
    >>> e.positionAtStep(4)
    'Attic'
    >>> e.transitionAtStep(4)
    'getCrawl'
    >>> e.positionAtStep(5)
    'Attic'
    >>> e.transitionAtStep(5)
    'vent'
    >>> e.positionAtStep(6)
    'East'

    An example of the use of `recordUnify` and `recordObviate`.

    >>> obs = JournalObserver()
    >>> obs.observe('''
    ... S start
    ... x right hall left
    ... x right room left
    ... x vent vents right_vent
    ... ''')
    >>> obs.recordObviate('middle_vent', 'hall', 'vent')
    >>> obs.recordExplore('left_vent', 'new_room', 'vent')
    >>> obs.recordUnify('start')
    >>> e = obs.getExploration()
    >>> len(e)
    6
    >>> [e.getPositionAtStep(n) for n in range(6)]
    [None, 'start', 'hall', 'room', 'vents', 'start']
    >>> g = e.currentGraph()
    >>> g.getDestination('start', 'vent')
    'vents'
    >>> g.getDestination('vents', 'left_vent')
    'start'
    >>> g.getReciprocal('start', 'vent')
    'left_vent'
    >>> g.getReciprocal('vents', 'left_vent')
    'vent'
    >>> 'new_room' in g
    False
    """

    parseFormat: ParseFormat
    """
    The parse format used to parse entries supplied as text. This also
    ends up controlling some of the decision and transition naming
    conventions that are followed, so it is not safe to change it
    mid-journal; it should be set once before observation begins, and
    may be accessed but should not be changed.
    """

    exploration: core.Exploration
    """
    This is the exploration object being built via journal observations.
    Note that the exploration object may be empty (i.e., have length 0)
    even after the first few entries have been recorded because in some
    cases entries are ambiguous and are not translated into exploration
    steps until a further entry resolves that ambiguity.
    """

    zonePrefixes: bool
    """
    Specifies whether level-0 zone names are automatically added to
    decision names to create compound decision names. Note that names
    which already contain the relevant `zoneSeparator` are not modified.
    """

    uniqueNumber: int
    """
    A unique number to be substituted (prefixed with '_') into
    underscore-substitutions within aliases. Will be incremented for each
    such substitution.
    """

    aliases: Dict[str, Tuple[List[str], str]]
    """
    The defined aliases for this observer. Each alias has a name, and
    stored under that name is a list of parameters followed by a
    commands string.
    """

    def __init__(
        self,
        parseFormat: Optional[ParseFormat] = None,
        zonePrefixes: bool = False
    ):
        """
        Sets up the observer. If a parse format is supplied, that will
        be used instead of the default parse format, which is just the
        result of creating a `ParseFormat` with default arguments.

        If `zonePrefixes` is set to `True` (the default is `False`) then
        decision names will be automatically prefixed with the current
        level-0 zone name (separated by the format's `zoneSeparator`)
        unless they always contain a `zoneSeparator`. If there is not
        current level-0 zone, '_' will be used. This applies to decision
        names specified via the `record*` methods, which thereby
        includes decision names specified in journals input using
        `observe`. Use the `zonePrefixes` entry type to toggle this
        behavior on or off.

        Note that if a level-0 zone is applied or changed after a
        decision is created, the decision will be renamed.

        So for example:

        >>> o = JournalObserver(zonePrefixes=True)
        >>> o.recordStart('hi')
        >>> e = o.getExploration()
        >>> len(e)
        2
        >>> g = e.currentGraph()
        >>> len(g)
        1
        >>> e.currentPosition()
        '_::hi'
        >>> list(g.nodes)[0]
        '_::hi'
        >>> o.recordObserve('option')
        >>> list(g.nodes)
        ['_::hi', '_u.0']
        >>> o.recordZone(0, 'Lower')
        >>> sorted(e.currentGraph().nodes)
        ['Lower::hi', '_u.0']
        >>> e.currentPosition()
        'Lower::hi'
        >>> o.recordZone(1, 'Upper')
        >>> o.recordExplore('option', 'bye', 'back')
        >>> g = e.currentGraph()
        >>> list(g.nodes)
        ['Lower::hi', 'Lower::bye']
        >>> o.recordObserve('option2')
        >>> o.recordExplore('option2', 'hi', 'back', 'Lower2')
        >>> g = e.currentGraph()
        >>> list(g.nodes)
        ['Lower::hi', 'Lower::bye', 'Lower2::hi']
        >>> # Prefix must be specified because it's in a different zone:
        >>> o.recordWarp('Lower::hi')
        >>> g = e.currentGraph()
        >>> list(g.nodes)
        ['Lower::hi', 'Lower::bye', 'Lower2::hi']
        >>> e.currentPosition()
        'Lower::hi'
        >>> # Prefix will be automatic within the same zone
        >>> o.recordWarp('bye')
        >>> g = e.currentGraph()
        >>> list(g.nodes)
        ['Lower::hi', 'Lower::bye', 'Lower2::hi']
        >>> e.currentPosition()
        'Lower::bye'
        """
        if parseFormat is None:
            self.parseFormat = ParseFormat()
        else:
            self.parseFormat = parseFormat

        self.zonePrefixes = zonePrefixes
        self.uniqueNumber = 0
        self.aliases = {}

        # Create a blank exploration
        self.exploration = core.Exploration()

        # State variables

        # Tracks the most-recent transition so that things which apply to
        # a transition can be applied. Note that the current position is
        # just tracked via the `Exploration` object. This value is either
        # None or a pair including a decision and a transition name at
        # that decision.
        self.currentTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

        # Stored decision/transition values that can be restored as the
        # current decision/transition later. This is used to support
        # relative mode.
        self.storedTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

        # Whether or not we're in relative mode.
        self.inRelativeMode = False

        # Decision/transition values that are currently being targeted
        # in relative mode.
        self.targetDecision: Optional[core.Decision] = None
        self.targetTransition: Optional[
            Tuple[core.Decision, core.Transition]
        ] = None

    def getExploration(self) -> core.Exploration:
        """
        Returns the exploration that this observer edits.
        """
        return self.exploration

    def nextUniqueName(self) -> str:
        """
        Returns the next unique name for this observer, which is just an
        underscore followed by an integer. This increments
        `uniqueNumber`.
        """
        result = '_' + str(self.uniqueNumber)
        self.uniqueNumber += 1
        return result

    def currentDecisionTarget(self) -> Optional[core.Decision]:
        """
        Returns the decision which decision-based changes should be
        applied to. Changes depending on whether relative mode is
        active. Will be `None` when there is no current position (e.g.,
        before the exploration is started).
        """
        if self.inRelativeMode:
            return self.targetDecision
        else:
            return self.exploration.getCurrentPosition()

    def definiteDecisionTarget(self) -> core.Decision:
        """
        Works like `currentDecisionTarget` but raises a
        `core.MissingDecisionError` instead of returning `None` if there
        is no current decision.
        """
        if self.inRelativeMode:
            result = self.targetDecision
        else:
            result = self.exploration.currentPosition()

        if result is None:
            raise core.MissingDecisionError(
                "There is no current decision."
            )
        else:
            return result

    def currentTransitionTarget(
        self
    ) -> Optional[Tuple[core.Decision, core.Transition]]:
        """
        Returns the decision, transition pair that identifies the current
        transition which transition-based changes should apply to. Will
        be `None` when there is no current transition (e.g., just after a
        warp).
        """
        if self.inRelativeMode:
            return self.targetTransition
        else:
            return self.currentTransition

    def currentReciprocalTarget(
        self
    ) -> Optional[Tuple[core.Decision, core.Transition]]:
        """
        Returns the decision, transition pair that identifies the
        reciprocal of the `currentTransitionTarget`. Will be `None` when
        there is no current transition, or when the current transition
        doesn't have a reciprocal (e.g., after an ending).
        """
        # relative mode is handled by `currentTransitionTarget`
        target = self.currentTransitionTarget()
        if target is None:
            return None
        now = self.exploration.currentGraph()
        return now.getReciprocalPair(*target)

    def checkFormat(
        self,
        entryType: str,
        target: Union[None, JournalTargetType, int],
        pieces: List[str],
        expectedTargets: Union[
            None,
            type[int],
            Collection[
                Union[None, JournalTargetType, int]
            ]
        ],
        expectedPieces: Union[None, int, Collection[int]]
    ) -> None:
        """
        Does format checking for a journal entry after
        `determineEntryType` is called. Checks that the target is one
        from an allowed list of targets (or is `None` if
        `expectedTargets` is set to `None`) and that the number of
        pieces of content is a specific number or within a specific
        collection of allowed numbers. If `expectedPieces` is set to
        None, there is no restriction on the number of pieces.

        Raises a `JournalParseError` if its expectations are violated.
        """
        if expectedTargets is None:
            if target is not None:
                raise JournalParseError(
                    f"{entryType} entry may not specify a target."
                )
        elif expectedTargets is int:
            if not isinstance(target, int):
                raise JournalParseError(
                    f"{entryType} entry must have an integer target."
                )
        elif target not in cast(
            Collection[
                Union[None, JournalTargetType, int]
            ],
            expectedTargets
        ):
            raise JournalParseError(
                f"{entryType} entry had invalid target '{target}'."
            )

        if expectedPieces is None:
            # No restriction
            pass
        elif isinstance(expectedPieces, int):
            if len(pieces) != expectedPieces:
                raise JournalParseError(
                    f"{entryType} entry had {len(pieces)} arguments but"
                    f" only {expectedPieces} argument(s) is/are allowed."
                )

        elif len(pieces) not in expectedPieces:
            allowed = ', '.join(str(x) for x in expectedPieces)
            raise JournalParseError(
                f"{entryType} entry had {len(pieces)} arguments but the"
                f" allowed argument counts are: {allowed}"
            )

    def parseOneCommand(
        self,
        journalText: str,
        startIndex: int
    ) -> Tuple[List[str], int]:
        """
        Parses a single command from the given journal text, starting at
        the specified start index. Each command occupies a single line,
        except when blocks are present in which case it may stretch
        across multiple lines. This function splits the command up into a
        list of strings (including multi-line strings and/or strings
        with spaces in them when blocks are used). It returns that list
        of strings, along with the index after the newline at the end of
        the command it parsed (which could be used as the start index
        for the next command). If the command has no newline after it
        (only possible when the string ends) the returned index will be
        the length of the string.

        If the line starting with the start character is empty (or just
        contains spaces), the result will be an empty list along with the
        index for the start of the next line.

        Examples:

        >>> o = JournalObserver()
        >>> commands = '''\\
        ... S start
        ... o option
        ...
        ... x option next back
        ... o lever
        ...   e edit [
        ...     o bridge
        ...       q speed
        ...   ] [
        ...     o bridge
        ...       q X
        ...   ]
        ... a lever
        ... '''
        >>> o.parseOneCommand(commands, 0)
        (['S', 'start'], 8)
        >>> o.parseOneCommand(commands, 8)
        (['o', 'option'], 17)
        >>> o.parseOneCommand(commands, 17)
        ([], 18)
        >>> o.parseOneCommand(commands, 18)
        (['x', 'option', 'next', 'back'], 37)
        >>> o.parseOneCommand(commands, 37)
        (['o', 'lever'], 45)
        >>> bits, end = o.parseOneCommand(commands, 45)
        >>> bits[:2]
        ['e', 'edit']
        >>> bits[2]
        'o bridge\\n      q speed'
        >>> bits[3]
        'o bridge\\n      q X'
        >>> len(bits)
        4
        >>> end
        116
        >>> o.parseOneCommand(commands, end)
        (['a', 'lever'], 124)

        >>> o = JournalObserver()
        >>> s = "o up Attic down\\nx up\\no vent\\nq crawl"
        >>> o.parseOneCommand(s, 0)
        (['o', 'up', 'Attic', 'down'], 16)
        >>> o.parseOneCommand(s, 16)
        (['x', 'up'], 21)
        >>> o.parseOneCommand(s, 21)
        (['o', 'vent'], 28)
        >>> o.parseOneCommand(s, 28)
        (['q', 'crawl'], 35)
        """

        index = startIndex
        unit: Optional[str] = None
        bits: List[str] = []
        pf = self.parseFormat  # shortcut variable
        while index < len(journalText):
            char = journalText[index]
            if char.isspace():
                # Space after non-spaces -> end of unit
                if unit is not None:
                    bits.append(unit)
                    unit = None
                # End of line -> end of command
                if char == '\n':
                    index += 1
                    break
            else:
                # Non-space -> check for block
                if char == pf.blockStart:
                    if unit is not None:
                        bits.append(unit)
                        unit = None
                    blockEnd = pf.findBlockEnd(journalText, index)
                    block = journalText[index + 1:blockEnd - 1].strip()
                    bits.append(block)
                    index = blockEnd  # +1 added below
                elif unit is None:  # Initial non-space -> start of unit
                    unit = char
                else:  # Continuing non-space -> accumulate
                    unit += char
            # Increment index
            index += 1

        # Grab final unit if there is one hanging
        if unit is not None:
            bits.append(unit)

        return (bits, index)

    def observe(self, journalText: str) -> None:
        """
        Ingests one or more journal blocks in text format (as a
        multi-line string) and updates the exploration being built by
        this observer, as well as updating internal state.

        This method can be called multiple times to process a longer
        journal incrementally including line-by-line.

        ## Example:

        >>> obs = JournalObserver()
        >>> obs.observe('''\\
        ... P on
        ... S start Room1
        ... zz Region
        ... o nope
        ...   q power|tokens*3
        ... o unexplored
        ... o onwards
        ... x onwards sub_room backwards
        ... t backwards
        ... o down
        ...
        ... x down middle up Room2
        ... a box
        ...   At deactivate
        ...   At gain tokens*1
        ... o left
        ... o right
        ...   gt blue
        ...
        ... x right middle left Room3
        ... o right
        ... a miniboss
        ...   At deactivate
        ...   At gain power
        ... x right - left
        ... o ledge
        ...   q tall
        ... t left
        ... t left
        ... t up
        ...
        ... x nope secret back
        ... ''')
        >>> obs.zonePrefixes
        True
        >>> e = obs.getExploration()
        >>> len(e)
        13
        >>> g = e.currentGraph()
        >>> len(g)
        9
        >>> def showDestinations(g, r):
        ...     d = g.destinationsFrom(r)
        ...     for outgoing in sorted(d):
        ...         req = g.getTransitionRequirement(r, outgoing)
        ...         if req is None or req == core.ReqNothing():
        ...             req = ''
        ...         else:
        ...             req = ' ' + repr(req)
        ...         print(outgoing, d[outgoing] + req)
        ...
        >>> "start" in g
        False
        >>> showDestinations(g, "Room1::start")
        down Room2::middle
        nope Room1::secret ReqAny([ReqPower('power'), ReqTokens('tokens', 3)])
        onwards Room1::sub_room
        unexplored _u.1
        >>> showDestinations(g, "Room1::secret")
        back Room1::start
        >>> showDestinations(g, "Room1::sub_room")
        backwards Room1::start
        >>> showDestinations(g, "Room2::middle")
        box Room2::middle ReqImpossible()
        left _u.4
        right Room3::middle
        up Room1::start
        >>> g.transitionTags("Room2::middle", "right")
        {'blue'}
        >>> showDestinations(g, "Room3::middle")
        left Room2::middle
        miniboss Room3::middle ReqImpossible()
        right Room3::-
        >>> showDestinations(g, "Room3::-")
        ledge _u.7 ReqPower('tall')
        left Room3::middle
        >>> showDestinations(g, "_u.7")
        return Room3::-
        >>> e.currentPosition()
        'Room1::secret'

        Note that there are plenty of other annotations not shown in
        this example; see `DEFAULT_FORMAT` for the default mapping from
        journal entry types to markers, and see `JournalEntryType` for
        the explanation for each entry type.

        Most entries start with a marker (which includes one character
        for the type and possibly one for the target) followed by a
        single space, and everything after that is the content of the
        entry.
        """
        # Normalize newlines
        journalText = journalText\
            .replace('\r\n', '\n')\
            .replace('\n\r', '\n')\
            .replace('\r', '\n')

        # Shortcut variable
        pf = self.parseFormat

        # Remove comments from entire text
        journalText = pf.removeComments(journalText)

        startAt = 0
        currentStartPos = 0
        try:
            while startAt < len(journalText):
                currentStartPos = startAt
                bits, startAt = self.parseOneCommand(journalText, startAt)

                if len(bits) == 0:
                    continue

                eType, eTarget, eParts = pf.determineEntryType(bits)
                if eType == 'zonePrefixes':
                    self.checkFormat(
                        'zonePrefixes',
                        eTarget,
                        eParts,
                        None,
                        {0, 1}
                    )
                    if len(eParts) == 0:
                        self.zonePrefixes = not self.zonePrefixes
                    else:
                        onOrOff = pf.onOff(eParts[0])
                        if onOrOff is None:
                            warnings.warn(
                                (
                                    f"On/off value '{eParts[0]}' is neither"
                                    f" '{pf.markerFor('on')}' nor"
                                    f" '{pf.markerFor('off')}'. Assuming"
                                    f" 'off'."
                                ),
                                JournalParseWarning
                            )
                        self.zonePrefixes = bool(onOrOff)

                elif eType == 'alias':
                    self.checkFormat(
                        "alias",
                        eTarget,
                        eParts,
                        None,
                        None
                    )

                    if len(eParts) < 2:
                        raise JournalParseError(
                            "Alias entry must include at least an alias"
                            " name and a commands list."
                        )
                    aliasName = eParts[0]
                    parameters = eParts[1:-1]
                    commands = eParts[-1]
                    self.defineAlias(aliasName, parameters, commands)

                elif eType == 'custom':
                    self.checkFormat(
                        "custom",
                        eTarget,
                        eParts,
                        None,
                        None
                    )
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "Custom entry must include at least an alias"
                            " name."
                        )
                    self.deployAlias(eParts[0], eParts[1:])

                elif eType == 'START':
                    self.checkFormat(
                        "START",
                        eTarget,
                        eParts,
                        None,
                        {1, 2}
                    )

                    self.recordStart(*eParts)

                elif eType == 'explore':
                    self.checkFormat(
                        "explore",
                        eTarget,
                        eParts,
                        None,
                        {1, 2, 3, 4}
                    )

                    self.recordExplore(*eParts)

                elif eType == 'return':
                    self.checkFormat(
                        "return",
                        eTarget,
                        eParts,
                        None,
                        {2, 3}
                    )
                    self.recordReturn(*eParts)

                elif eType == 'action':
                    self.checkFormat(
                        "action",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordAction(*eParts)

                elif eType == 'retrace':
                    self.checkFormat(
                        "retrace",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordRetrace(*eParts)

                elif eType == 'warp':
                    self.checkFormat(
                        "warp",
                        eTarget,
                        eParts,
                        None,
                        {1, 2}
                    )

                    self.recordWarp(*eParts)

                elif eType == 'wait':
                    self.checkFormat(
                        "warp",
                        eTarget,
                        eParts,
                        None,
                        0
                    )
                    self.recordWait()

                elif eType == 'observe':
                    self.checkFormat(
                        "observe",
                        eTarget,
                        eParts,
                        None,
                        (1, 2, 3)
                    )
                    self.recordObserve(*eParts)

                elif eType == 'END':
                    self.checkFormat(
                        "END",
                        eTarget,
                        eParts,
                        None,
                        1
                    )
                    self.recordEnd(*eParts)

                elif eType == 'requirement':
                    self.checkFormat(
                        "requirement",
                        eTarget,
                        eParts,
                        (None, 'reciprocalPart', 'bothPart'),
                        None
                    )
                    req = core.Requirement.parse(' '.join(eParts))
                    if eTarget in (None, 'bothPart'):
                        self.recordRequirement(req)
                    if eTarget in ('reciprocalPart', 'bothPart'):
                        self.recordReciprocalRequirement(req)

                elif eType == 'effect':
                    self.checkFormat(
                        "effect",
                        eTarget,
                        eParts,
                        None,
                        None
                    )

                    effect: core.TransitionEffect = pf.parseEffect(eParts)

                    self.recordTransitionEffect(effect)

                elif eType == 'apply':
                    self.checkFormat(
                        "apply",
                        eTarget,
                        eParts,
                        (None, 'transitionPart'),
                        None
                    )

                    toApply: core.TransitionEffect = pf.parseEffect(eParts)

                    # Apply the effect
                    self.exploration.applyEffectNow(
                        toApply,
                        self.currentTransition
                    )

                    # If we targeted a transition, that means we wanted to
                    # both apply the effect now AND set it up as an effect
                    # of the transition we just took.
                    if eTarget == 'transitionPart':
                        self.recordTransitionEffect(toApply)

                elif eType == 'tag':
                    self.checkFormat(
                        "tag",
                        eTarget,
                        eParts,
                        (
                            None,
                            'transitionPart',
                            'reciprocalPart',
                            'bothPart'
                        ),
                        None
                    )
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "tag entry must include at least one tag."
                        )
                    if eTarget is None:
                        self.recordTagDecision(*eParts)
                    elif eTarget == "transitionPart":
                        self.recordTagTranstion(*eParts)
                    elif eTarget == "reciprocalPart":
                        self.recordTagReciprocal(*eParts)
                    elif eTarget == "bothPart":
                        self.recordTagTranstion(*eParts)
                        self.recordTagReciprocal(*eParts)
                    else:
                        raise JournalParseError(
                            f"Invalid tag target type '{eTarget}'."
                        )

                elif eType == 'annotate':
                    self.checkFormat(
                        "annotate",
                        eTarget,
                        eParts,
                        (
                            None,
                            'decisionPart',
                            'transitionPart',
                            'reciprocalPart',
                            'bothPart'
                        ),
                        None
                    )
                    if len(eParts) == 0:
                        raise JournalParseError(
                            "annotation may not be empty."
                        )
                    if eTarget is None:
                        self.recordAnnotateStep(' '.join(eParts))
                    elif eTarget == "decisionPart":
                        self.recordAnnotateDecision(' '.join(eParts))
                    elif eTarget == "transitionPart":
                        self.recordAnnotateTranstion(' '.join(eParts))
                    elif eTarget == "reciprocalPart":
                        self.recordAnnotateReciprocal(' '.join(eParts))
                    elif eTarget == "bothPart":
                        self.recordAnnotateTranstion(' '.join(eParts))
                        self.recordAnnotateReciprocal(' '.join(eParts))
                    else:
                        raise JournalParseError(
                            f"Invalid annotation target type '{eTarget}'."
                        )

                elif eType == 'zone':
                    self.checkFormat(
                        "zone",
                        eTarget,
                        eParts,
                        int,
                        1
                    )
                    if eTarget is None:
                        eTarget = 0
                    self.recordZone(cast(int, eTarget), eParts[0])

                elif eType == 'unify':
                    self.checkFormat(
                        "unify",
                        eTarget,
                        eParts,
                        (None, 'transitionPart', 'reciprocalPart'),
                        (1, 2)
                    )
                    if eTarget is None:
                        self.recordUnify(*eParts)
                    elif eTarget == 'transitionPart':
                        if len(eParts) != 1:
                            raise JournalParseError(
                                "A transition unification entry may only"
                                f" have one argument, but we got"
                                f" {len(eParts)}."
                            )
                        self.recordUnifyTransition(eParts[0])
                    elif eTarget == 'reciprocalPart':
                        if len(eParts) != 1:
                            raise JournalParseError(
                                "A transition unification entry may only"
                                f" have one argument, but we got"
                                f" {len(eParts)}."
                            )
                        self.recordUnifyReciprocal(eParts[0])
                    else:
                        raise RuntimeError(
                            f"Invalid target type {eTarget} after check"
                            f" for unify entry!"
                        )

                elif eType == 'obviate':
                    self.checkFormat(
                        "obviate",
                        eTarget,
                        eParts,
                        None,
                        3
                    )
                    transition, targetDecision, targetTransition = eParts
                    self.recordObviate(
                        transition,
                        targetDecision,
                        targetTransition
                    )

                elif eType == 'relative':
                    self.checkFormat(
                        "relative",
                        eTarget,
                        eParts,
                        None,
                        (0, 1, 2)
                    )
                    try:
                        self.relative(*eParts)
                    except core.BadStart:
                        raise JournalParseError(
                            "You cannot enter relative mode before the"
                            " 'start' entry."
                        )

                else:
                    raise NotImplementedError(
                        f"Unrecognized event type '{eType}'."
                    )
        except Exception as e:
            raise LocatedJournalParseError(journalText, currentStartPos, e)

    def prefixedName(
        self,
        name: core.Decision,
        zone: Optional[core.Zone] = None
    ) -> core.Decision:
        """
        Prepends zone information to a decision to get a fully-qualified
        name based on the `zonePrefixes` setting (see `__init__`).

        If a specific zone is provided, that zone will be used as the
        prefix; otherwise the alphabetically-first level-0 zone of the
        current decision target will be used, with '_' as a default if
        there is no such zone.
        """
        if self.zonePrefixes:
            # Leave it alone if it already has zone parts, or if it
            # already exists
            if (
                self.parseFormat.hasZoneParts(name)
             or name in self.exploration.currentGraph()
            ):
                return name

            # Figure out which zone to use as the prefix
            if zone is None:
                target = self.currentDecisionTarget()
                if target is None:
                    zone = '_'
                else:
                    now = self.getExploration().currentGraph()
                    parents = now.zoneParents(target)
                    if len(parents) == 0:
                        zone = '_'
                    else:
                        zone = min(parents)

            return self.parseFormat.prefixWithZone(name, zone)

        else:  # Otherwise don't change the name
            return name

    def defineAlias(
        self,
        name: str,
        parameters: Sequence[str],
        commands: str
    ) -> None:
        """
        Defines an alias: a block of commands that can be played back
        later using the 'custom' command, with parameter substitutions.

        If an alias with the specified name already existed, it will be
        replaced.

        Each of the listed parameters must be supplied when invoking the
        alias, and where they appear within curly braces in the commands
        string, they will be substituted in. Additional names starting
        with '_' plus an optional integer will also be substituted with
        unique names (see `nextUniqueName`), with the same name being
        used for every instance that shares the same numerical suffix
        within each application of the command.

        For example:

        >>> o = JournalObserver()
        >>> o.defineAlias(
        ...     'hintRoom',
        ...     ['name'],
        ...     'o {_5}\\nx {_5} {name} {_5}\\ng hint\\nt {_5}'
        ... ) # _5 to show that the suffix doesn't matter if it's consistent
        >>> o.recordStart('start')
        >>> o.deployAlias('hintRoom', ['hint1'])
        >>> o.deployAlias('hintRoom', ['hint2'])
        >>> e = o.getExploration()
        >>> e.currentPosition()
        'start'
        >>> e.positionAtStep(2)
        'hint1'
        >>> e.positionAtStep(3)
        'start'
        >>> e.positionAtStep(4)
        'hint2'
        >>> e.positionAtStep(5)
        'start'
        >>> e.transitionAtStep(1)
        '_0'
        >>> e.transitionAtStep(2)
        '_0'
        >>> e.transitionAtStep(3)
        '_1'
        >>> e.transitionAtStep(4)
        '_1'
        >>> g = e.currentGraph()
        >>> len(g)
        3
        >>> sorted(g)
        ['hint1', 'hint2', 'start']
        >>> g.decisionTags('hint1')
        {'hint'}
        >>> g.decisionTags('hint2')
        {'hint'}
        """
        self.aliases[name] = (list(parameters), commands)

    def deployAlias(self, name: str, arguments: Sequence[str]) -> None:
        """
        Deploys an alias, taking its command string and substituting in
        the provided argument values for each of the alias' parameters,
        plus any unique names that it requests. Substitution happens
        first for named arguments and then for unique strings, so named
        arguments of the form '{_-n-}' where -n- is an integer will end
        up being substituted for unique names.

        Raises a `JournalParseError` if the specified alias does not
        exist, or if the wrong number of parameters has been supplied.

        See `defineAlias` for an example.
        """
        # Fetch the alias
        alias = self.aliases.get(name)
        if alias is None:
            raise JournalParseError(
                f"Alias '{name}' has not been defined yet."
            )
        paramNames, commands = alias

        # Check arguments
        arguments = list(arguments)
        if len(arguments) != len(paramNames):
            raise JournalParseError(
                f"Alias '{name}' requires {len(paramNames)} parameters,"
                f" but you supplied {len(arguments)}."
            )

        # Find unique names
        uniques = set([
            match.strip('{}')
            for match in re.findall('{_[0-9]*}', commands)
        ])

        # Build substitution dictionary that passes through uniques
        firstWave = {unique: '{' + unique + '}' for unique in uniques}
        firstWave.update({
            param: value
            for (param, value) in zip(paramNames, arguments)
        })

        # Substitute parameter values
        commands = commands.format(**firstWave)

        uniques = set([
            match.strip('{}')
            for match in re.findall('{_[0-9]*}', commands)
        ])

        # Substitute for remaining unique names
        uniqueValues = {
            unique: self.nextUniqueName()
            for unique in sorted(uniques)  # sort for stability
        }
        commands = commands.format(**uniqueValues)

        # Now run the commands
        self.observe(commands)

    def recordStart(
        self,
        name: core.Decision,
        zone: Optional[core.Zone] = None
    ) -> None:
        """
        Records the start of the exploration. Use only once, as the very
        first entry (possibly after some zone declarations).

        To create new decision points that are disconnected from the rest
        of the graph, use the `relative` method.
        """
        if self.inRelativeMode:
            raise ValueError(
                "Can't start the exploration in relaive mode."
            )

        name = self.prefixedName(name, zone)

        self.exploration.start(
            name,
            connections=[],
            zone=zone
        )

    def recordObserve(
        self,
        name: core.Transition,
        destination: Optional[core.Decision] = None,
        reciprocal: Optional[core.Transition] = None
    ) -> None:
        """
        Records the observation of a new option at the current decision.

        If two or three arguments are given, the destination is still
        marked as unknown, but is given a name (with two arguments)
        and the reciprocal transition is named (with three arguments).
        """
        here = self.definiteDecisionTarget()
        self.exploration.observe(name, where=here)
        if self.inRelativeMode:
            self.targetTransition = (here, name)
        else:
            self.currentTransition = (here, name)

        # Rename the destination & reciprocal if names for them were
        # specified
        now = self.exploration.currentGraph()
        newUnknown = now.destination(here, name)

        if destination is not None:
            # Get prefixed destination name
            destination = self.prefixedName(destination)
            now.renameDecision(newUnknown, destination)
        else:
            destination = newUnknown

        if reciprocal is not None:
            now.addTransition(destination, reciprocal, here)
            now.mergeTransitions(
                destination,
                cast(core.Transition, now.getReciprocal(here, name)),
                reciprocal
            )

    def recordExplore(
        self,
        transition: core.Transition,
        destination: Optional[core.Decision] = None,
        reciprocal: Optional[core.Transition] = None,
        zone: Union[
            core.Zone,
            type[core.DefaultZone],
            type[None]
        ] = core.DefaultZone
    ) -> None:
        """
        Records the exploration of a transition which leads to a
        specific destination. The name of the reciprocal transition may
        also be specified. Creates the transition if it needs to. A zone
        may be specified and will be used as the new level-0 zone for
        the destination (otherwise the destination will be in all of the
        same zones as the origin, and will take its prefix from the
        alphabetically first such zone). Setting zone to `None` will not
        put the destination into any new zones.

        If no destination name is specified, the destination node must
        already exist and the name of the destination must not begin
        with '_u.' otherwise a `JournalParseError` will be generated.

        Sets the current transition to the transition taken.

        In relative mode, this makes all the same changes to the graph,
        without adding a new exploration step or applying transition
        effects.
        """
        here = self.definiteDecisionTarget()
        # Create transition if it doesn't already exist
        now = self.exploration.currentGraph()
        leadsTo = now.getDestination(here, transition)
        if leadsTo is None:
            if destination is None:
                raise JournalParseError(
                    f"Transition '{transition}' at decision '{here}'"
                    f" does not already exist, so a destination name"
                    f" must be provided."
                )
            else:
                now.addUnexploredEdge(here, transition)
        elif destination is None:
            # TODO: Generalize this... ?
            if leadsTo.startswith('_u.'):
                raise JournalParseError(
                    f"Destination '{leadsTo}' from decision '{here}'"
                    f" via transition '{transition}' must be named when"
                    f" explored, because it does not already have a"
                    f" name."
                )
            else:
                destination = leadsTo

        # Adjust destination name
        if zone is None:
            destination = self.prefixedName(destination, '_')
        elif zone is core.DefaultZone:
            fromZones = now.zoneParents(here)
            if fromZones:
                fromZone = min(fromZones)
            else:
                fromZone = None
            destination = self.prefixedName(destination, fromZone)
        else:
            zone = cast(core.Zone, zone)
            destination = self.prefixedName(destination, zone)

        if zone is None:
            zone = core.DefaultZone
        if self.inRelativeMode:
            now.replaceUnexplored(
                here,
                transition,
                destination,
                reciprocal,
                placeInZone=zone
            )
            self.targetDecision = destination
            self.targetTransition = (here, transition)
        else:
            self.exploration.explore(
                transition,
                destination,
                [],
                reciprocal,
                zone
            )
            self.currentTransition = (here, transition)

    def recordRetrace(self, transition: core.Transition) -> None:
        """
        Records retracing a transition which leads to a known
        destination.

        Sets the current transition to the transition taken.

        In relative mode, simply sets the current transition target to
        the transition taken and sets the current decision target to its
        destination (it does not apply transition effects).
        """
        here = self.definiteDecisionTarget()
        if self.inRelativeMode:
            now = self.exploration.currentGraph()
            self.targetDecision = now.destination(here, transition)
            self.targetTransition = (here, transition)
        else:
            self.exploration.retrace(transition)
            self.currentTransition = (here, transition)

    def recordAction(self, name: core.Transition) -> None:
        """
        Records an action taken at the current decision. If a transition
        of that name already existed, it will be converted into an action
        assuming that its destination is unexplored and has no
        connections yet, and that its recirocal also has no special
        properties yet. If those assumptions do not hold, a
        `JournalParseError` will be raised under the assumption that the
        name collision was an accident, not intentional, since the
        destination and reciprocal are deleted in the process of
        converting a normal transition into an action.

        In relative mode, the action is created (or the transition is
        converted into an action) but effects are not applied.

        Example:

        >>> o = JournalObserver()
        >>> e = o.getExploration()
        >>> o.recordStart('start')
        >>> o.recordObserve('transition')
        >>> e.currentState().get('powers', set())
        set()
        >>> o.recordObserve('action') # not noted as an action yet...
        >>> # TODO: 'oa' syntax for this?
        >>> o.recordTransitionEffect(
        ...     {
        ...         'type': 'gain',
        ...         'value': 'power',
        ...         'charges': None,
        ...         'delay': None
        ...     }
        ... )
        >>> o.recordAction('action') # turns it into an action
        >>> e.currentState().get('powers', set())
        {'power'}
        >>> o.recordAction('another') # add effects after...
        >>> effect = {
        ...         'type': 'lose',
        ...         'value': 'power',
        ...         'charges': None,
        ...         'delay': None
        ... }
        >>> # These lines apply the effect and then add it to the
        >>> # transition, since we alread took the transition
        >>> e.applyEffectNow(effect, o.currentTransition)
        >>> o.recordTransitionEffect(effect)
        >>> e.currentState()['powers']
        set()
        >>> len(e)
        4
        >>> e.getPositionAtStep(0)
        >>> e.positionAtStep(1)
        'start'
        >>> e.positionAtStep(2)
        'start'
        >>> e.positionAtStep(3)
        'start'
        >>> e.transitionAtStep(0)
        '_START_'
        >>> e.transitionAtStep(1)
        'action'
        >>> e.transitionAtStep(2)
        'another'
        """
        here = self.definiteDecisionTarget()

        # Check if the transition already exists
        now = self.exploration.currentGraph()
        destinations = now.destinationsFrom(here)
        if name in destinations:
            destination = destinations[name]
            reciprocal = now.getReciprocal(here, name)
            # To replace a transition with an action, the transition may
            # only have outgoing properties. Otherwise we assume it's an
            # error to name the action after a transition which was
            # intended to be a real transition.
            if (
                not now.isUnknown(destination)
             or now.degree(destination) > 2
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination is already explored or has"
                    f" been connected to."
                )
            if (
                reciprocal is not None
            and now.getTransitionProperties(
                    destination,
                    reciprocal
                ) != {
                    'requirement': core.ReqNothing(),
                    'effects': [],
                    'tags': set(),
                    'annotations': []
                }
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its reciprocal has custom properties."
                )

            if (
                now.decisionAnnotations(destination) != []
             or now.decisionTags(destination) != {'unknown'}
            ):
                raise JournalParseError(
                    f"Action '{name}' has the same name as outgoing"
                    f" transition '{name}' at decision '{here}'. We"
                    f" cannot turn that transition into an action since"
                    f" its destination has tags and/or annotations."
                )

            # If we get here, re-target the transition, and then destroy
            # the old destination along with the old reciprocal edge.
            now.retargetTransition(
                here,
                name,
                here,
                swapReciprocal=False
            )
            now.removeDecision(destination)

        # This will either take the existing action OR create it if
        # necessary
        if self.inRelativeMode:
            if name not in destinations:
                now.addAction(here, name)
            self.targetTransition = (here, name)
        else:
            self.exploration.takeAction(name)
            self.currentTransition = (here, name)

    def recordReturn(
        self,
        transition: core.Transition,
        destination: core.Decision,
        reciprocal: Optional[core.Transition] = None
    ) -> None:
        """
        Records an exploration which leads back to a
        previously-encountered decision. If a reciprocal is specified,
        we connect to that transition as our reciprocal (it must have
        led to an unknown area or not have existed) or if not, we make a
        new connection with an automatic reciprocal name.

        Sets the current transition to the transition taken.

        In relative mode, does the same stuff but doesn't apply any
        transition effects.
        """
        here = self.definiteDecisionTarget()
        now = self.exploration.currentGraph()
        destination = self.prefixedName(destination)
        if self.inRelativeMode:
            now.replaceUnexplored(
                here,
                transition,
                destination,
                reciprocal
            )
            self.targetDecision = destination
            self.targetTransition = (here, transition)
        else:
            self.exploration.returnTo(
                transition,
                destination,
                reciprocal
            )
            self.currentTransition = (here, transition)

    def recordWarp(
        self,
        destination: core.Decision,
        zone: Union[
            core.Zone,
            type[core.DefaultZone],
            type[None]
        ] = core.DefaultZone
    ) -> None:
        """
        Records a warp to a specific destination without creating a
        transition. If the destination did not exist, it will be
        created. By default, if the destination gets created, it will be
        added to the same zones as the previous position. However, if
        the destination already exists its zones won't be changed. A
        specific zone may be supplied to add the destination to that
        zone instead (regardless of whether it is new or existing). The
        `zone` argument can also be set to `None` to avoid putting the
        destination in any zones.

        If the destination has a `zoneSeparator` in it, it will be used
        as-is, but if not, `prefixedName` will be used to get a modified
        name for the destination.

        Sets the current transition to `None`.

        In relative mode, simply updates the current target decision and
        sets the current target transition to `None`. It will still
        create the destination if necessary, and if a zone is specified
        explicitly it will put the destination in that zone, but in
        relative mode, the destination is not marked as unknown (in
        normal mode it's marked as unknown in the step before the warp
        and known afterwards).
        """
        now = self.exploration.currentGraph()

        destination = self.prefixedName(destination)

        # Create the destination if it didn't exist already
        if destination not in now:
            now.addDecision(destination)
            if not self.inRelativeMode:
                now.setUnknown(destination)
                # The warp step will mark it as known in the next
                # exploration step, but in this one it's unknown.

        if self.inRelativeMode:
            self.targetDecision = destination
            self.targetTransition = None
            if zone is not None and zone is not core.DefaultZone:
                zone = cast(core.Zone, zone)
                now.addDecisionToZone(destination, zone)
        else:
            self.exploration.warp(destination, zone=zone)
            self.currentTransition = None

        # Handle zone

    def recordWait(self) -> None:
        """
        Records a wait step. Does not modify the current transition.

        Raises a `JournalParseError` in relative mode, since it wouldn't
        have any effect.
        """
        if self.inRelativeMode:
            raise JournalParseError("Can't wait in relative mode.")
        else:
            self.exploration.wait()

    def recordEnd(self, name: core.Decision) -> None:
        """
        Records an ending. Sets the current transition to the transition
        that leads to the ending. Endings are not added to zones, and
        their names also don't get prefixed with zones.

        Does the same thing in relative mode.
        """
        graph = self.exploration.currentGraph()
        here = self.definiteDecisionTarget()
        fullName = graph.addEnding(here, name)
        if self.inRelativeMode:
            self.targetDecision = fullName
            self.targetTransition = (here, fullName)
        else:
            self.exploration.retrace(fullName)
            self.currentTransition = (here, fullName)
        # TODO: Prevent things like adding unexplored nodes to the
        # ending...

    def recordRequirement(self, req: core.Requirement) -> None:
        """
        Records a requirement observed on the most recently
        defined/taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a requirement because there is no current"
                " transition."
            )
        self.exploration.currentGraph().setTransitionRequirement(
            *target,
            req
        )

    def recordReciprocalRequirement(self, req: core.Requirement) -> None:
        """
        Records a requirement observed on the reciprocal of the most
        recently defined/taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Can't set a reciprocal requirement because there is no"
                " current transition or it doesn't have a reciprocal."
            )
        graph = self.exploration.currentGraph()
        graph.setTransitionRequirement(*target, req)

    def recordTransitionEffect(
        self,
        effect: core.TransitionEffect
    ) -> None:
        """
        Records a transition effect, which is immediately added to any
        effects of the currently-relevant transition (the most-recently
        created or taken transition). A `JournalParseError` will be
        raised if there is no current transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply an effect because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.addTransitionEffect(*target, effect)

    def recordReciprocalEffect(
        self,
        effect: core.TransitionEffect
    ) -> None:
        """
        Like `recordTransitionEffect` but applies the effect to the
        reciprocal of the current transition. Will cause a
        `JournalParseError` if the current transition has no reciprocal
        (e.g., it's an ending transition).
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot apply a reciprocal effect because there is no"
                " current transition, or it doesn't have a reciprocal."
            )

        now = self.exploration.currentGraph()
        now.addTransitionEffect(*target, effect)

    def recordTagDecision(
        self,
        *tags: core.Tag
    ) -> None:
        """
        Records tags to be applied to the current decision.
        """
        now = self.exploration.currentGraph()
        now.tagDecision(self.definiteDecisionTarget(), set(tags))

    def recordTagTranstion(
        self,
        *tags: core.Tag
    ) -> None:
        """
        Records tags to be applied to the most-recently-defined or
        -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.tagTransition(*target, set(tags))

    def recordTagReciprocal(
        self,
        *tags: core.Tag
    ) -> None:
        """
        Records tags to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot tag a transition because there is no current"
                " transition."
            )

        now = self.exploration.currentGraph()
        now.tagTransition(*target, set(tags))

    def recordAnnotateStep(
        self,
        *annotations: core.Annotation
    ) -> None:
        """
        Records annotations to be applied to the current exploration
        step.
        """
        self.exploration.annotateStep(annotations)

    def recordAnnotateDecision(
        self,
        *annotations: core.Annotation
    ) -> None:
        """
        Records annotations to be applied to the current decision.
        """
        now = self.exploration.currentGraph()
        now.annotateDecision(self.definiteDecisionTarget(), annotations)

    def recordAnnotateTranstion(
        self,
        *annotations: core.Annotation
    ) -> None:
        """
        Records annotations to be applied to the most-recently-defined
        or -taken transition.
        """
        target = self.currentTransitionTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a transition because there is no"
                " current transition."
            )

        now = self.exploration.currentGraph()
        now.annotateTransition(*target, annotations)

    def recordAnnotateReciprocal(
        self,
        *annotations: core.Annotation
    ) -> None:
        """
        Records annotations to be applied to the reciprocal of the
        most-recently-defined or -taken transition.
        """
        target = self.currentReciprocalTarget()
        if target is None:
            raise JournalParseError(
                "Cannot annotate a reciprocal because there is no"
                " current transition or because it doens't have a"
                " reciprocal."
            )

        now = self.exploration.currentGraph()
        now.annotateTransition(*target, annotations)

    def recordZone(self, level: int, zone: core.Zone) -> None:
        """
        Records a new current zone to be swapped with the zone(s) at the
        specified hierarchy level for the current decision target. See
        `core.Exploration.reZone` and
        `core.DecisionGraph.replaceZonesInHierarchy` for details on what
        exactly happens; the summary is that the zones at the specified
        hierarchy level are replaced with the provided zone (which is
        created if necessary) and their children are re-parented onto
        the provided zone, while that zone is also set as a child of
        their parents.

        If the zone is at level 0, and `zonePrefixes` is active,
        new children of the zone will be renamed to use it as their
        prefix.

        Does the same thing in relative mode as in normal mode.
        """
        # Rename any decisions in the old zone
        rename = False
        if level == 0 and self.zonePrefixes:
            rename = True

        self.exploration.reZone(
            zone,
            level,
            self.definiteDecisionTarget()
        )

        # If we're renaming decisions, do that
        if rename:
            now = self.exploration.currentGraph()
            here = self.exploration.currentPosition()
            toRename = now.decisionsInZone(zone)
            # Find all children of the zone after rezoning
            for child in toRename:
                zones, base = self.parseFormat.splitZone(child)
                if len(zones) <= 1:
                    newName = self.prefixedName(base, zone)
                now.renameDecision(child, newName)
                if here == child:
                    self.exploration.setCurrentPosition(newName)

    def recordUnify(
        self,
        merge: core.Decision,
        mergeInto: Optional[core.Decision] = None
    ) -> None:
        """
        Records a unification between two decisions. This marks an
        observation that they are actually the same decision and it
        merges them. If only one decision is given the current decision
        is merged into that one. After the merge, the first decision (or
        the current decision if only one was given) will no longer
        exist.

        If one of the merged decisions was the current position of the
        exploration, the merged decision will be the current position
        after the merge, and this happens even when in relative mode.
        In relative mode, the target decision is also updated if it
        needs to be.

        A `TransitionCollisionError` will be raised if the two decisions
        have outgoing transitions that share a name.

        Logs a `JournalParseWarning` if the two decisions were in
        different zones.
        """
        if mergeInto is None:
            mergeInto = merge
            merge = self.definiteDecisionTarget()

        # TODO: Do we need to avoid applying prefixes to unknown
        # decisions? Or maybe to *any* existing decision name?
        merge = self.prefixedName(merge)
        mergeInto = self.prefixedName(mergeInto)

        now = self.exploration.currentGraph()
        now.mergeDecisions(merge, mergeInto)

        # Update current position if it was merged
        if self.exploration.currentPosition() == merge:
            self.exploration.positions[-1] = mergeInto

        # Update targets if they were merged
        if self.inRelativeMode:
            if self.targetDecision == merge:
                self.targetDecision = mergeInto
            if (
                self.targetTransition
            and self.targetTransition[0] == merge
            ):
                self.targetTransition = (
                    mergeInto,
                    self.targetTransition[1]
                )
        else:
            # Update current transition if it was merged
            if (
                self.currentTransition
            and self.currentTransition[0] == merge
            ):
                self.currentTransition = (
                    mergeInto,
                    self.currentTransition[1]
                )

        # Update stored decision/transition
        if self.storedTransition and self.storedTransition[0] == merge:
            self.storedTransition = (
                mergeInto,
                self.storedTransition[1]
            )

    def recordUnifyTransition(self, target: core.Transition) -> None:
        """
        Records a unification between the most-recently-defined or
        -taken transition and the specified transition (which must be
        outgoing from the same decision). This marks an observation that
        two transitions are actually the same transition and it merges
        them.

        After the merge, the target transition will still exist but the
        previously most-recent transition will have been deleted.

        Their reciprocals will also be merged.

        A `JournalParseError` is raised if there is no most-recent
        transition.
        """
        now = self.exploration.currentGraph()
        affected = self.currentTransitionTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        destination = now.getDestination(decision, transition)
        if destination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{transition}' at decision '{decision}' has no"
                f" destination."
            )

        finalDestination = now.getDestination(decision, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify transitions: transition"
                f" '{target}' at decision '{decision}' has no"
                f" destination."
            )

        if destination != finalDestination:
            if not now.isUnknown(destination):
                raise JournalParseError(
                    f"Cannot unify transitions: destination"
                    f" '{destination}' of transition '{transition}' at"
                    f" decision '{decision}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            now.retargetTransition(
                decision,
                transition,
                finalDestination
            )
            now.removeDecision(destination)
            if self.targetDecision == destination:
                self.targetDecision = finalDestination
            # TODO: What if that destination was part of another target?

        # Now we can merge transitions
        now.mergeTransitions(decision, transition, target)

    def recordUnifyReciprocal(
        self,
        target: core.Transition
    ) -> None:
        """
        Records a unification between the reciprocal of the
        most-recently-defined or -taken transition and the specified
        transition, which must be outgoing from the current transition's
        destination. This marks an observation that two transitions are
        actually the same transition and it merges them, deleting the
        original reciprocal. Note that the current transition will also
        be merged with the reciprocal of the target.

        A `JournalParseError` is raised if there is no current
        transition, or if it does not have a reciprocal.
        """
        now = self.exploration.currentGraph()
        affected = self.currentReciprocalTarget()
        if affected is None or affected[1] is None:
            raise JournalParseError(
                "Cannot unify transitions: there is no current"
                " transition."
            )

        decision, transition = affected

        destination = now.destination(decision, transition)
        reciprocal = now.getReciprocal(decision, transition)
        if reciprocal is None:
            raise JournalParseError(
                "Cannot unify reciprocal: there is no reciprocal of the"
                " current transition."
            )

        # If they don't share a target, then the current transition must
        # lead to an unknown node, which we will dispose of
        finalDestination = now.getDestination(destination, target)
        if finalDestination is None:
            raise JournalParseError(
                f"Cannot unify reciprocal: transition"
                f" '{target}' at decision '{destination}' has no"
                f" destination."
            )

        if decision != finalDestination:
            if not now.isUnknown(decision):
                raise JournalParseError(
                    f"Cannot unify reciprocal: destination"
                    f" '{decision}' of transition '{reciprocal}' at"
                    f" decision '{destination}' is not an unknown"
                    f" decision."
                )
            # Retarget and delete the unknown node that we abandon
            # TODO: Merge nodes instead?
            now.retargetTransition(
                destination,
                reciprocal,
                finalDestination
            )
            now.removeDecision(decision)
            # TODO: Retargeting stuff!! HERE

        # Actually merge the transitions
        now.mergeTransitions(destination, reciprocal, target)

    def recordObviate(
        self,
        transition: core.Transition,
        otherDecision: core.Decision,
        otherTransition: core.Transition
    ) -> None:
        """
        Records the obviation of a transition at another decision. This
        is the observation that a specific transition at the current
        decision is the reciprocal of a different transition at another
        decision which previously led to an unknown area. The difference
        between this and `recordReturn` is that `recordReturn` logs
        movement across the newly-connected transition, while this
        leaves the player at their original decision (and does not even
        add a step to the current exploration).

        Both transitions will be created if they didn't already exist.

        In relative mode does the same thing but doesn't move the current
        decision across the transition updated.

        If the destination is unknown, it will remain unknown after this
        operation.
        """
        now = self.exploration.currentGraph()
        here = self.definiteDecisionTarget()
        otherDecision = self.prefixedName(otherDecision)
        otherDestination = now.getDestination(
            otherDecision,
            otherTransition
        )
        if otherDestination is not None:
            if not now.isUnknown(otherDestination):
                raise JournalParseError(
                    f"Cannot obviate transition '{otherTransition}' at"
                    f" decision '{otherDecision}': that transition leads"
                    f" to decision '{otherDestination}' which is not an"
                    f" unknown decision."
                )
        else:
            # We must create the other destination
            now.addUnexploredEdge(otherDecision, otherTransition)

        destination = now.getDestination(here, transition)
        if destination is not None:
            if not now.isUnknown(destination):
                raise JournalParseError(
                    f"Cannot obviate using transition '{transition}' at"
                    f" decision '{here}': that transition leads to"
                    f" decision '{destination}' which is not an unknown"
                    f" decision."
                )
        else:
            # we need to create it
            now.addUnexploredEdge(here, transition)

        # Track unknown status of destination (because
        # `replaceUnexplored` will overwrite it but we want to preserve
        # it in this case.
        if otherDecision is not None:
            unknown = now.isUnknown(otherDecision)

        # Now connect the transitions and clean up the unknown nodes
        now.replaceUnexplored(
            here,
            transition,
            otherDecision,
            otherTransition
        )
        # Restore unknown status if it had it
        if unknown:
            now.setUnknown(otherDecision)
        if self.inRelativeMode:
            self.targetTransition = (here, transition)
        else:
            self.currentTransition = (here, transition)

    def relative(
        self,
        where: Optional[core.Decision] = None,
        transition: Optional[core.Transition] = None,
    ) -> None:
        """
        Enters 'relative mode' where the exploration ceases to add new
        steps but edits can still be performed on the current graph. This
        also changes the current decision/transition settings so that
        edits can be applied anywhere. It can accept 0, 1, or 2
        arguments. With 0 arguments, it simply enters relative mode but
        maintains the current position as the target decision and the
        last-taken or last-created transition as the target transition
        (note that that transition usually originates at a different
        decision). With 1 argument, it sets the target decision to the
        decision named, and sets the target transition to None. With 2
        arguments, it sets the target decision to the decision named, and
        the target transition to the transition named, which must
        originate at that target decision.

        If given the name of a decision which does not yet exist, it will
        create that decision in the current graph, disconnected from the
        rest of the graph. In that case, it is an error to also supply a
        transition to target (you can use other commands once in relative
        mode to build more transitions and decisions out from the
        newly-created decision).

        When called in relative mode, it updates the current position
        and/or decision, or if called with no arguments, it exits
        relative mode. When exiting relative mode, the current decision
        is set back to the graph's current position, and the current
        transition is set to whatever it was before relative mode was
        entered.

        Raises a `TypeError` if a transition is specified without
        specifying a decision. Raises a `ValueError` if given no
        arguments and the exploration does not have a current position.
        Also raises a `ValueError` if told to target a specific
        transition which does not exist. Raises a `core.BadStart` error
        if called before the exploration is started.
        """
        if len(self.exploration.currentGraph()) == 0:
            raise core.BadStart(
                "Cannot enter relative mode before the exploration is"
                " started (call `recordStart` first)."
            )

        if where is None:
            if transition is not None:
                raise TypeError(
                    "Cannot specify a transition without also"
                    " specifying a decision."
                )
            if self.inRelativeMode:
                # If we're in relative mode, cancel it
                self.inRelativeMode = False

                # Here we restore saved sate
                self.currentTransition = self.storedTransition
                self.storedTransition = None
                self.targetTransition = None

            else:
                # Enter relative mode and set up the current
                # decision/transition as the targets

                # Store state
                self.storedTransition = self.currentTransition

                # Enter relative mode
                self.inRelativeMode = True

                # Set targets
                self.targetDecision = self.exploration.currentPosition()
                if self.targetDecision is None:
                    raise ValueError(
                        "Cannot enter relative mode at the current"
                        " position becuase there is no current"
                        " position."
                    )
                self.targetTransition = self.currentTransition

        else: # we have at least a decision to target
            where = self.prefixedName(where)
            # If we're entering relative mode instead of just changing
            # focus, we need to set up the targetTransition if no
            # transition was specified.
            if not self.inRelativeMode:
                # We'll be entering relative mode, so store state
                self.storedTransition = self.currentTransition
                if transition is None:
                    self.targetTransition = self.currentTransition

            # Enter (or stay in) relative mode
            self.inRelativeMode = True

            # Target the specified decision
            self.targetDecision = where

            # Target the specified transition
            now = self.exploration.currentGraph()
            if transition is not None:
                self.targetTransition = (where, transition)
                if now.getDestination(where, transition) is None:
                    raise ValueError(
                        f"Cannot target transition '{transition}' at"
                        f" decision '{where}': there is no such"
                        f" transition."
                    )
            # otherwise leave self.targetTransition alone

            # If we're targeting a previously non-existent decision,
            # create it.
            if self.targetDecision not in now:
                if transition is not None:
                    raise TypeError(
                        f"Cannot specify a target transition when"
                        f" entering relative mode at previously"
                        f" non-existent decision '{where}'."
                    )
                now.addDecision(self.targetDecision)


#--------------------#
# Shortcut Functions #
#--------------------#

def convertJournal(
    journal: str,
    format: Optional[ParseFormat] = None
) -> core.Exploration:
    """
    Converts a journal in text format into a `core.Exploration` object,
    using a fresh `JournalObserver`. An optional `ParseFormat` may be
    specified if the journal doesn't follow the default parse format.
    """
    obs = JournalObserver(format)
    obs.observe(journal)
    return obs.getExploration()
