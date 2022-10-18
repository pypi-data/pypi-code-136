from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Any, Optional

from docdeid.annotate.annotation import AnnotationSet
from docdeid.tokenize.token import TokenList
from docdeid.tokenize.tokenizer import BaseTokenizer


class MetaData:
    def __init__(self, items: dict) -> None:
        self._items = items

    def __getitem__(self, item: str) -> Optional[Any]:
        return self._items.get(item, None)

    def __setitem__(self, key: str, value: Any) -> None:

        if key in self._items:
            raise RuntimeError(f"Key {key} already present in Metadata, cannot overwrite (read only)")

        self._items[key] = value


class Document:
    def __init__(
        self,
        text: str,
        tokenizers: Optional[dict[str, BaseTokenizer]] = None,
        metadata: Optional[dict] = None,
    ) -> None:

        self._text = text
        self._annotations = AnnotationSet()

        self._tokenizers = tokenizers
        self.metadata = MetaData(metadata or {})

        self._token_lists = {}
        self._deidentified_text = None

    @property
    def text(self) -> str:
        return self._text

    def get_tokens(self, tokenizer_name: str = "default") -> TokenList:

        if tokenizer_name not in self._tokenizers:
            raise ValueError(f"Cannot get tokens from unknown tokenizer {tokenizer_name}")

        if tokenizer_name not in self._token_lists or self._token_lists[tokenizer_name] is None:
            self._token_lists[tokenizer_name] = self._tokenizers[tokenizer_name].tokenize(self._text)

        return self._token_lists[tokenizer_name]

    @property
    def annotations(self) -> AnnotationSet:
        return self._annotations

    @annotations.setter
    def annotations(self, value: AnnotationSet) -> None:
        self._annotations = value

    @property
    def deidentified_text(self) -> str:

        return self._deidentified_text

    def set_deidentified_text(self, deidentified_text: str) -> None:

        self._deidentified_text = deidentified_text

    def get_metadata_item(self, key: str) -> Optional[Any]:

        return self.metadata[key]


class DocProcessor(ABC):
    @abstractmethod
    def process(self, doc: Document, **kwargs) -> None:
        pass


class DocProcessorGroup(OrderedDict):
    def process(self, doc: Document, processors_enabled: Optional[list[str]] = None) -> None:

        for name, proc in self.items():
            if (processors_enabled is None) or (name in processors_enabled):
                proc.process(doc, processors_enabled=processors_enabled)
