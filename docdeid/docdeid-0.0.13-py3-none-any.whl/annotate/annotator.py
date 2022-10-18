import re
from abc import ABC, abstractmethod
from typing import Iterable, Optional, Union

from docdeid.annotate.annotation import Annotation
from docdeid.doc.document import DocProcessor, Document
from docdeid.ds import LookupSet, LookupTrie
from docdeid.pattern.pattern import TokenPattern
from docdeid.str.processor import BaseStringModifier
from docdeid.tokenize.token import Token
from docdeid.tokenize.tokenizer import BaseTokenizer


class BaseAnnotator(DocProcessor, ABC):
    def __init__(self, tag: Optional[str]) -> None:
        self.tag = tag

    def process(self, doc: Document, **kwargs) -> None:
        doc.annotations.update(self.annotate(doc))

    @abstractmethod
    def annotate(self, doc: Document) -> list[Annotation]:
        pass


class SingleTokenLookupAnnotator(BaseAnnotator):
    def __init__(
        self,
        *args,
        lookup_values: Optional[Iterable] = None,
        matching_pipeline: Optional[list[BaseStringModifier]] = None,
        tokenizer_name: Optional[str] = "default",
        **kwargs
    ) -> None:

        if lookup_values is not None:
            self.lookup_list = LookupSet(matching_pipeline=matching_pipeline)
            self.lookup_list.add_items_from_iterable(items=lookup_values)

        self._tokenizer_name = tokenizer_name
        super().__init__(*args, **kwargs)

    def _tokens_to_annotations(self, tokens: list[Token]) -> list[Annotation]:

        return [
            Annotation(
                text=token.text,
                start_char=token.start_char,
                end_char=token.end_char,
                tag=self.tag,
                start_token=token,
                end_token=token,
            )
            for token in tokens
        ]

    def annotate_lookup_values(self, doc: Document, lookup_values: Union[LookupSet, set]) -> list[Annotation]:

        annotate_tokens = []
        tokens = doc.get_tokens(tokenizer_name=self._tokenizer_name)

        if isinstance(lookup_values, LookupSet):

            if lookup_values.has_matching_pipeline():

                return self._tokens_to_annotations([token for token in tokens if token.text in lookup_values])

            lookup_values = lookup_values.items()

        annotate_tokens += tokens.token_lookup(lookup_values)

        return self._tokens_to_annotations(annotate_tokens)

    def annotate(self, doc: Document) -> list[Annotation]:

        return self.annotate_lookup_values(doc, self.lookup_list)


class MultiTokenLookupAnnotator(BaseAnnotator):
    def __init__(
        self,
        lookup_values: Iterable,
        tokenizer: BaseTokenizer,
        tag: str,
        matching_pipeline: Optional[list[BaseStringModifier]] = None,
        overlapping: bool = False,
    ) -> None:

        super().__init__(tag=tag)

        self.overlapping = overlapping
        self.trie = LookupTrie(matching_pipeline=matching_pipeline)

        for val in lookup_values:
            self.trie.add([token.text for token in tokenizer.tokenize(val)])

    def annotate(self, doc: Document) -> list[Annotation]:

        tokens = doc.get_tokens()
        tokens_text = [token.text for token in tokens]
        annotations = []

        for i in range(len(tokens_text)):

            longest_matching_prefix = self.trie.longest_matching_prefix(tokens_text[i:])

            if longest_matching_prefix is None:
                continue

            start_char = tokens[i].start_char
            end_char = tokens[i + len(longest_matching_prefix) - 1].end_char

            annotations.append(
                Annotation(
                    text=doc.text[start_char:end_char],
                    start_char=start_char,
                    end_char=end_char,
                    tag=self.tag,
                )
            )

            if not self.overlapping:
                i += len(longest_matching_prefix)  # skip ahead

        return annotations


class RegexpAnnotator(BaseAnnotator):
    def __init__(self, regexp_pattern: re.Pattern, *args, capturing_group: int = 0, **kwargs) -> None:

        self.regexp_pattern = regexp_pattern
        self.capturing_group = capturing_group
        super().__init__(*args, **kwargs)

    def annotate(self, doc: Document) -> list[Annotation]:

        annotations = []

        for match in self.regexp_pattern.finditer(doc.text):

            text = match.group(self.capturing_group)
            start, end = match.span(self.capturing_group)

            annotations.append(Annotation(text, start, end, self.tag))

        return annotations


class TokenPatternAnnotator(BaseAnnotator):
    def __init__(self, pattern: TokenPattern) -> None:
        self.pattern = pattern
        super().__init__(pattern.tag)

    def annotate(self, doc: Document) -> list[Annotation]:

        annotations = []

        if not self.pattern.doc_precondition(doc):
            return annotations

        for token in doc.get_tokens():

            if not self.pattern.token_precondition(token):
                continue

            match = self.pattern.match(token, doc.metadata)

            if match is None:
                continue

            start_token, end_token = match

            annotations.append(
                Annotation(
                    text=doc.text[start_token.start_char : end_token.end_char],
                    start_char=start_token.start_char,
                    end_char=end_token.end_char,
                    tag=self.pattern.tag,
                    start_token=start_token,
                    end_token=end_token,
                )
            )

        return annotations
