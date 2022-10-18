import re
from abc import ABC, abstractmethod
from typing import Callable, Optional

import numpy as np

from docdeid.annotate.annotation import Annotation, AnnotationSet
from docdeid.doc.document import DocProcessor, Document


class BaseAnnotationProcessor(DocProcessor, ABC):
    def process(self, doc: Document, **kwargs) -> None:

        if len(doc.annotations) == 0:
            return

        doc.annotations = self.process_annotations(doc.annotations, doc.text)

    @abstractmethod
    def process_annotations(self, annotations: AnnotationSet, text: str) -> AnnotationSet:
        pass


class OverlapResolver(BaseAnnotationProcessor):
    def __init__(
        self, sort_by: list[str], sort_by_callbacks: Optional[dict[str, Callable]] = None, deterministic: bool = True
    ) -> None:
        self._sort_by = sort_by
        self._sort_by_callbacks = sort_by_callbacks
        self._deterministic = deterministic

    @staticmethod
    def _zero_runs(arr: np.array) -> np.array:
        """
        Finds al zero runs in an numpy array.
        From: https://stackoverflow.com/questions/24885092/finding-the-consecutive-zeros-in-a-numpy-array
        """

        iszero = np.concatenate(([0], np.equal(arr, 0).view(np.int8), [0]))
        absdiff = np.abs(np.diff(iszero))
        return np.where(absdiff == 1)[0].reshape(-1, 2)

    def _sort_annotations(self, annotations: AnnotationSet) -> list[Annotation]:

        return annotations.sorted(
            by=self._sort_by, callbacks=self._sort_by_callbacks, deterministic=self._deterministic
        )

    def process_annotations(self, annotations: AnnotationSet, text: str) -> AnnotationSet:

        processed_annotations = []

        mask = np.zeros(max(annotation.end_char for annotation in annotations))

        for annotation in self._sort_annotations(annotations):

            mask_annotation = mask[annotation.start_char : annotation.end_char]

            if all(val == 0 for val in mask_annotation):  # no overlap
                processed_annotations.append(annotation)

            else:  # overlap

                for start_char_run, end_char_run in self._zero_runs(mask_annotation):

                    processed_annotations.append(
                        Annotation(
                            text=annotation.text[start_char_run:end_char_run],
                            start_char=annotation.start_char + start_char_run,
                            end_char=annotation.start_char + end_char_run,
                            tag=annotation.tag,
                        )
                    )

            mask[annotation.start_char : annotation.end_char] = 1

        return AnnotationSet(processed_annotations)


class MergeAdjacentAnnotations(BaseAnnotationProcessor):
    def __init__(self, slack_regexp: str = None, check_overlap: bool = True) -> None:
        self.slack_regexp = slack_regexp
        self.check_overlap = check_overlap

    def _tags_match(self, left_tag: str, right_tag: str) -> bool:

        return left_tag == right_tag

    def _tag_replacement(self, left_tag: str, right_tag: str) -> str:

        return left_tag

    def _are_adjacent_annotations(self, left_annotation: Annotation, right_annotation: Annotation, text: str) -> bool:

        if not self._tags_match(left_annotation.tag, right_annotation.tag):
            return False

        between_text = text[left_annotation.end_char : right_annotation.start_char]

        if self.slack_regexp is None:
            return between_text == ""

        return re.fullmatch(self.slack_regexp, between_text) is not None

    def _adjacent_annotations_replacement(
        self, left_annotation: Annotation, right_annotation: Annotation, text: str
    ) -> Annotation:

        return Annotation(
            text=text[left_annotation.start_char : right_annotation.end_char],
            start_char=left_annotation.start_char,
            end_char=right_annotation.end_char,
            tag=self._tag_replacement(left_annotation.tag, right_annotation.tag),
        )

    def process_annotations(self, annotations: AnnotationSet, text: str) -> AnnotationSet:

        if self.check_overlap and annotations.has_overlap():
            raise ValueError(f"{self.__class__} received input with overlapping annotations.")

        processed_annotations = []

        annotations = annotations.sorted(by=["start_char"])

        for index in range(len(annotations) - 1):

            annotation, next_annotation = annotations[index], annotations[index + 1]

            if self._are_adjacent_annotations(annotation, next_annotation, text):
                annotations[index + 1] = self._adjacent_annotations_replacement(annotation, next_annotation, text)
            else:
                processed_annotations.append(annotation)

        processed_annotations.append(annotations[-1])  # add last one

        return AnnotationSet(processed_annotations)
