from typing import Dict, Set, Union, List
from numparser.fsm.engine import FSM, FSMResultParser
from numparser.fsm.patterns import predefined_patterns
from numparser.fsm.tokenizer import Tokenizer

from numparser.output import ParsedNumber


# fmt: off
DEFAULT_NOT_UNITS = {
    "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
    "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
    "january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december",
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December",
    "mon", "tue", "wed", "thu", "fri", "sat", "sun",
    "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun",
    "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",
}
# fmt: on


class FSMParser:
    """A parser implemented using FSM/FSA. To deal with units and non-units, the parser relies on
    a tokenizer & classifier that groups the text together and classify whether it's a unit, not a unit, or unknown
    """

    def __init__(
        self,
        patterns: Union[List[str], Dict[str, FSM]] = None,
        pattern_parsers: Dict[str, FSMResultParser] = None,
        units: Set[str] = None,
        not_units: Set[str] = None,
    ):
        if patterns is not None and isinstance(patterns, dict):
            assert pattern_parsers is not None
            self.patterns = patterns
            self.pattern_parsers = pattern_parsers
        else:
            self.patterns = {}
            self.pattern_parsers = {}
            for name, (pattern, parser) in predefined_patterns("us").items():
                self.patterns[name] = pattern
                self.pattern_parsers[name] = parser

            if patterns is not None:
                self.patterns = {name: self.patterns[name] for name in patterns}
                self.pattern_parsers = {
                    name: self.pattern_parsers[name] for name in patterns
                }

        self.tokenizer = Tokenizer(units, not_units)

    @staticmethod
    def default():
        return FSMParser(not_units=DEFAULT_NOT_UNITS)

    def parse_value(self, value: str, lowercase: bool = True) -> List[ParsedNumber]:
        """Parse a single number from text."""
        value = value.strip()
        seq = self.tokenizer.tokenize(value.lower() if lowercase else value)
        for name, pattern in self.patterns.items():
            match = pattern.execute(seq)
            if match is not None:
                return self.pattern_parsers[name](match, value)
        return []
