import re
from pathlib import Path
from typing import NamedTuple, Pattern, Union

import yaml

separator_pattern: Pattern = re.compile("|".join([r",", r"\s+", r"(\sand\s)"]))


def split_separator(text: str):
    for a in separator_pattern.split(text):
        if a and a != "and":  # removes None, ''
            yield a


class StatuteLabel(NamedTuple):
    """A typical serialized statute."""

    category: str
    identifier: str

    def get_obj(self, statute_path: Path, yf: str) -> dict | None:
        """Supply a base statute path, e.g. corpus/statutes/<category>/<identifier>/target file name `yf` and extract the yaml file object."""
        # must be a single identifier to extract path
        if not self.is_single:
            return None

        custom_file = "".join([self.category.lower(), self.identifier.lower()])
        permitted = ["details", "data", "units", custom_file]
        if yf not in permitted:
            return None
        parts = [self.category.lower(), self.identifier.lower(), f"{yf}.yaml"]
        target = statute_path.joinpath("/".join(parts))
        if target.exists():
            text = target.read_text()
            obj = yaml.safe_load(text)
            return obj
        return None

    @property
    def deconstructed_identifiers(self) -> list[str]:
        """Extracts compound identifiers, e.g. "EO 1, 2, 14 and 14-A."""
        return list(split_separator(self.identifier))

    @property
    def is_single(self) -> bool:
        """Determine if only a single identifier contained in the field."""
        return len(self.deconstructed_identifiers) == 1

    @property
    def separate_identifiers(self) -> list["StatuteLabel"] | None:
        """If there multiple identifiers, produce multiple instances."""

        if self.is_single:
            return None

        labels = []
        min_length = 1  # see doubtful labels
        for i in self.deconstructed_identifiers:
            item_length = len(i)
            if item_length >= min_length:
                min_length = item_length
                labels.append(StatuteLabel(self.category, i))
            else:
                # Deals with cases where the second part is doubtful labels are doubtful e.g.:
                # RA 8493, 12 (12 is doubtful)
                # RA 8042,35 (35 is doubtful)
                # RULE_BM 793, 30
                # RA 9136, 08
                # RA 7695, and 64
                continue

        return labels


class IndeterminateStatute(NamedTuple):
    """When unable to determine the serialized state of the statute, e.g. Constitution could mean 1987 Constitution, 1973 Constitution, etc."""

    text: str
