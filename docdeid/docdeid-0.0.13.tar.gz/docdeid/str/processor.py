import re
import unicodedata
from abc import ABC, abstractmethod
from typing import Optional


class BaseStringProcessor(ABC):
    @abstractmethod
    def process_items(self, items: list[str]) -> list[str]:
        pass


class BaseStringModifier(BaseStringProcessor, ABC):
    @abstractmethod
    def process(self, item: str) -> str:
        pass

    def process_items(self, items: list[str]) -> list[str]:
        return [self.process(item) for item in items]


class BaseStringFilter(BaseStringProcessor, ABC):
    @abstractmethod
    def filter(self, item: str) -> bool:
        """Return True to keep item, False to remove it (same as filter builtin)."""
        pass

    def process_items(self, items: list[str]) -> list[str]:
        return [item for item in items if self.filter(item)]


class LowercaseString(BaseStringModifier):
    def process(self, item: str) -> str:
        return item.lower()


class StripString(BaseStringModifier):
    def process(self, item: str) -> str:
        return item.strip()


class RemoveNonAsciiCharacters(BaseStringModifier):
    @staticmethod
    def _normalize_value(text: str) -> str:
        """Removes all non-ascii characters from a string"""
        text = str(bytes(text, encoding="ascii", errors="ignore"), encoding="ascii")
        return unicodedata.normalize("NFKD", text)

    def process(self, item: str) -> str:
        return self._normalize_value(item)


class ReplaceNonAsciiCharacters(BaseStringModifier):
    @staticmethod
    def _normalize_value(text: str) -> str:

        text = unicodedata.normalize("NFD", text)
        text = text.encode("ascii", "ignore")
        text = text.decode("utf-8")
        return str(text)

    def process(self, item: str) -> str:
        return self._normalize_value(item)


class ReplaceValue(BaseStringModifier):
    def __init__(self, find_value: str, replace_value: str) -> None:
        self.find_value = find_value
        self.replace_value = replace_value

    def process(self, item: str) -> Optional[str]:
        return item.replace(self.find_value, self.replace_value)


class ReplaceValueRegexp(BaseStringModifier):
    def __init__(self, find_value: str, replace_value: str) -> None:
        self.find_value = find_value
        self.replace_value = replace_value

    def process(self, item: str) -> Optional[str]:
        return re.sub(self.find_value, self.replace_value, item)


class FilterByLength(BaseStringFilter):
    def __init__(self, min_len: int) -> None:
        self.min_len = min_len

    def filter(self, item: str) -> bool:

        return len(item) >= self.min_len
