from typing import Any, Callable, Dict, Optional, Set, Union

from wai.common.adams.imaging.locateobjects import LocatedObjects
from wai.common.cli.options import TypedOption

from ....core.component import ProcessorComponent
from ....core.domain import Instance
from ....core.stream import OutputElementType, ThenFunction, DoneFunction
from ....core.stream.util import ProcessState
from ....domain.classification import Classification
from ....domain.image.object_detection.util import get_object_label
from ....domain.image.segmentation import ImageSegmentationAnnotation

AnnotationType = Union[Classification, LocatedObjects, ImageSegmentationAnnotation]
InstanceType = Instance[Any, AnnotationType]


def format_csv(labels: Set[str]) -> str:
    headers = ','.join(f"label_{n + 1}" for n in range(0, len(labels)))
    return f"{headers}\n{format_csv_headless(labels)}"


def format_csv_headless(labels: Set[str]) -> str:
    return ','.join(labels)


def format_list(labels: Set[str]) -> str:
    return '\n'.join(labels)


def format_json(labels: Set[str], pretty: bool) -> str:
    from json import dumps
    return dumps(
        {"labels": list(labels)},
        indent=2 if pretty else None
    )


FORMATTERS: Dict[str, Callable[[Set[str]], str]] = {
    "csv": format_csv,
    "csv-headless": format_csv_headless,
    "list": format_list,
    "json": lambda labels: format_json(labels, False),
    "json-pretty": lambda labels: format_json(labels, True)
}

FORMATTER_CHOICES = tuple(FORMATTERS.keys())


class WriteLabels(
    ProcessorComponent[InstanceType, InstanceType]
):
    """
    Inline stream-processor which writes labels from the stream to disk.
    """

    output: str = TypedOption(
        "-o", "--output",
        type=str,
        required=True,
        help="the file into which to write the labels",
        metavar="FILENAME"
    )

    format: str = TypedOption(
        "-f", "--format",
        type=str,
        default=FORMATTER_CHOICES[0],
        choices=FORMATTER_CHOICES
    )

    # The set of labels seen during processing
    labels: Set[str] = ProcessState(lambda self: set())

    def process_element(
            self,
            element: InstanceType,
            then: ThenFunction[InstanceType],
            done: DoneFunction
    ):
        # Get the annotation from the element
        annotation: Optional[AnnotationType] = element.annotations

        # Extract the label from the annotation
        if annotation is None:
            pass  # Skip negative as they have no labels to extract
        elif isinstance(annotation, Classification):
            self.labels.add(annotation.label)
        elif isinstance(annotation, LocatedObjects):
            self.labels.update(
                label
                for label in (
                    get_object_label(located_object, None)
                    for located_object in annotation
                )
                if label is not None
            )
        elif isinstance(annotation, ImageSegmentationAnnotation):
            self.labels.update(annotation.labels)
        else:
            raise Exception(f"Unexpected annotation type '{annotation.__class__.__name__}': {annotation}")

        # Forward the element
        then(element)

    def finish(self, then: ThenFunction[OutputElementType], done: DoneFunction):
        # Format the discovered labels
        formatter = FORMATTERS[self.format]
        formatted = formatter(self.labels)

        with open(self.output, "w") as file:
            file.write(formatted)

        done()
