from abc import ABC, abstractmethod
from collections import defaultdict

from docdeid.annotate.annotation import Annotation, AnnotationSet
from docdeid.doc.document import DocProcessor, Document


class BaseRedactor(DocProcessor, ABC):
    def process(self, doc: Document, **kwargs) -> None:
        redacted_text = self.redact(doc.text, doc.annotations)
        doc.set_deidentified_text(redacted_text)

    @abstractmethod
    def redact(self, text: str, annotations: AnnotationSet) -> str:
        """Redact the text."""


class RedactAllText(BaseRedactor):
    def __init__(self, open_char: str = "[", close_char: str = "]") -> None:
        self.open_char = open_char
        self.close_char = close_char

    def redact(self, text: str, annotations: AnnotationSet) -> str:

        return f"{self.open_char}REDACTED{self.close_char}"


class SimpleRedactor(BaseRedactor):
    def __init__(self, open_char: str = "[", close_char: str = "]") -> None:
        self.open_char = open_char
        self.close_char = close_char

    @staticmethod
    def _group_annotations_by_tag(annotations: AnnotationSet) -> dict[str, list[Annotation]]:

        groups = defaultdict(list)

        for annotation in annotations:
            groups[annotation.tag].append(annotation)

        return groups

    @staticmethod
    def _replace_annotations_in_text(text: str, annotations: AnnotationSet, replacement: dict[Annotation, str]) -> str:

        sorted_annotations = annotations.sorted(by=["end_char"], callbacks={"end_char": lambda x: -x})

        for annotation in sorted_annotations:

            text = text[: annotation.start_char] + replacement[annotation] + text[annotation.end_char :]

        return text

    def redact(self, text: str, annotations: AnnotationSet) -> str:

        annotation_text_to_counter = {}

        for tag, annotation_group in self._group_annotations_by_tag(annotations).items():

            annotation_text_to_counter_group = {}

            annotation_group = sorted(annotation_group, key=lambda a: a.get_sort_key(by=["end_char"]))

            for annotation in annotation_group:

                if annotation.text not in annotation_text_to_counter_group:
                    annotation_text_to_counter_group[annotation.text] = len(annotation_text_to_counter_group) + 1

            annotation_text_to_counter |= annotation_text_to_counter_group

        annotation_replacement = {}

        for annotation in annotations:

            annotation_replacement[annotation] = (
                f"{self.open_char}"
                f"{annotation.tag.upper()}"
                f"-"
                f"{annotation_text_to_counter[annotation.text]}"
                f"{self.close_char}"
            )

        return self._replace_annotations_in_text(text, annotations, annotation_replacement)
