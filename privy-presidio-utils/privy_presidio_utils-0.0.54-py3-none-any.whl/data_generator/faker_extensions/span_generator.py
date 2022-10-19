import re
from typing import List, Union, Optional

from faker import Generator, Faker

from presidio_evaluator.data_generator.faker_extensions import (
    FakerSpansResult,
    FakerSpan,
)

_re_token = re.compile(r"\{\{\s*(\w+)(:\s*\w+?)?\s*\}\}")


class SpanGenerator(Faker):
    """Generator which also returns the indices of fake values.

    :example:
    >>>from faker import Faker
    >>>from presidio_evaluator.data_generator.faker_extensions import SpanGenerator

    >>>generator = SpanGenerator()
    >>>faker = Faker(generator=generator)
    >>>res = faker.parse("My child's name is {{name}}", add_spans=True)

    >>>res.spans
        [{"value": "Daniel Gallagher", "start": 19, "end": 35, "type": "name"}]
    >>>res.fake
        "My child's name is Daniel Gallagher"
    >>>str(res)
        "My child's name is Daniel Gallagher"
    """
    def __init__(self, locale="en_US", **kwargs):
        # call init of Faker, passing given locale
        super().__init__(locale=locale, **kwargs)

    def parse(self, template: str, template_id: int) -> FakerSpansResult:
        """Parse a payload template into a token-wise labeled span."""
        spans = []
        for match in self._regex.finditer(template):
            faker_attribute = match.group()[2:-2]
            spans.append(
                FakerSpan(
                    type=faker_attribute,
                    start=match.start(),
                    end=match.end(),
                    # format calls the Faker generator, producing a (non-)PII value
                    value=str(self.format(faker_attribute.strip())),
                )
            )
        spans.sort(reverse=True, key=lambda x: x.start)
        prev_end, payload_string = self.update_indices(spans, template)
        payload_string = f"{template[0:prev_end]}{payload_string}"
        return (
            FakerSpansResult(
                fake=payload_string, spans=spans, template=template, template_id=template_id
            )
        )

    def update_indices(self, spans: List[FakerSpan], template: str) -> Tuple[int, str]:
        """Update span offsets given newly generated fake (non-PII) value which was
        inserted into the template"""
        payload_string = ""
        prev_end = len(template)
        for i, span in enumerate(spans):
            faker_attribute = span.type
            prev_len = len(faker_attribute) + 4
            new_len = len(f"{span.value}")
            payload_string = f"{template[span.end: prev_end]}{payload_string}"
            payload_string = f"{span.value}{payload_string}"
            prev_end = span.start
            len_difference = new_len - prev_len
            span.end += len_difference
            for j in range(0, i):
                spans[j].start += len_difference
                spans[j].end += len_difference
            span.type = faker_attribute.strip()
        return (prev_end, payload_string)
