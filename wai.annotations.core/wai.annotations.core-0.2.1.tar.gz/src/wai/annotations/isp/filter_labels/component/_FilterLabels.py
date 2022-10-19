from re import compile
from typing import Pattern, Optional, List

from shapely.geometry import Polygon
from wai.common.adams.imaging.locateobjects import LocatedObjects, LocatedObject
from wai.common.cli.options import TypedOption

from ....core.component import ProcessorComponent
from ....core.stream import ThenFunction, DoneFunction
from ....core.stream.util import RequiresNoFinalisation
from ....core.util import InstanceState
from ....domain.image import ImageInstance
from ....domain.image.object_detection import ImageObjectDetectionInstance
from ....domain.image.classification import ImageClassificationInstance
from ....domain.image.object_detection.util import get_object_label
from wai.annotations.core.util import to_polygon, intersect_over_union


class FilterLabels(
    RequiresNoFinalisation,
    ProcessorComponent[ImageInstance, ImageInstance]
):
    """
    Processes a stream of image object-detection instances,
    filtering out labels.
    """
    # The labels that should be included in the output format.
    # If None, use regex matching (see below)
    labels = TypedOption("-l", "--labels",
                         type=str,
                         nargs="+",
                         help="labels to use")

    # The regex to use to select labels to include when an
    # explicit list of labels is not given
    regex = TypedOption("-r", "--regexp",
                        type=str,
                        metavar="regexp",
                        help="regular expression for using only a subset of labels")

    region = TypedOption("--region",
                         type=str,
                         default=None,
                         metavar="x,y,w,h",
                         help="region that the object must overlap with in order to be included (object detection only). Between 0-1 the values are considered normalized, otherwise absolute pixels.")

    min_iou = TypedOption("--min-iou",
                          type=float,
                          metavar="FLOAT",
                          default=0.01,
                          help="the minimum IoU (intersect over union) that the object must have with the region in order to be considered an overlap (object detection only)")

    # The compiled regex
    _pattern: Optional[Pattern] = InstanceState(lambda self: compile(self.regex) if self.regex is not None else None)

    def process_element(
            self,
            element: ImageInstance,
            then: ThenFunction[ImageInstance],
            done: DoneFunction
    ):
        if isinstance(element, ImageObjectDetectionInstance):
            # Use the options to filter the located objects by label
            self.remove_invalid_objects(element.annotations, element.data.width, element.data.height)
            # no annotations left? mark as negative
            if len(element.annotations) == 0:
                new_element = type(element)(element.data, None)
                then(new_element)
                return
        elif isinstance(element, ImageClassificationInstance):
            # mark as negative if label doesn't match
            if not self.filter_label(element.annotations.label):
                new_element = type(element)(element.data, None)
                then(new_element)
                return

        then(element)

    def remove_invalid_objects(self, located_objects: LocatedObjects, width: int, height: int):
        """
        Removes objects with labels that are not valid under the given options.

        :param located_objects: The located objects to process.
        :param width: the width of the image
        :param height: the height of the image
        """
        # Create a list of objects to remove
        invalid_objects: List[int] = []

        # parse region, if necessary
        if not hasattr(self, "_region"):
            if self.region is None:
                self._region = None
                self._normalized = False
            else:
                parts = self.region.split(",")
                if len(parts) != 4:
                    raise Exception("Region must have format 'x,y,w,h', but found: %s" % self.region)
                self._region = [float(x) for x in parts]
                self._normalized = sum([(0 if (x < 1) else 1) for x in self._region]) < 4

        # Search the located objects
        for index, located_object in enumerate(located_objects):
            if not self.filter_object(located_object):
                invalid_objects.append(index)
            elif not self.filter_region(located_object, width, height):
                invalid_objects.append(index)

        # Remove the invalid objects
        for index in reversed(invalid_objects):
            located_objects.pop(index)

    def filter_label(self, label: str) -> bool:
        """
        Filter function which selects labels that match the given options.

        :param label:   The label to test.
        :return:        True if the label matches, false if not.
        """
        if len(self.labels) == 0 and self._pattern is None:
            return True
        elif len(self.labels) == 0:
            return bool(self._pattern.match(label))
        elif self._pattern is None:
            return label in self.labels
        else:
            return bool(self._pattern.match(label)) or label in self.labels

    def filter_object(self, located_object: LocatedObject) -> bool:
        """
        Filter function which selects objects whose labels match the given options.

        :param located_object:  The located object to test.
        :return:                True if the object matches, false if not.
        """
        # Filter the label
        return self.filter_label(get_object_label(located_object))

    def filter_region(self, located_object: LocatedObject, width: int, height: int) -> bool:
        """
        Ensures that the object fits into the defined region.

        :param located_object: the object to check
        :param width: the width of the image
        :type width: the height of the image
        :return: True if the objects overlaps the region or no region defined at all
        """
        if self._region is None:
            return True

        if self._normalized:
            x = int(self._region[0] * width)
            y = int(self._region[1] * height)
            w = int(self._region[2] * width)
            h = int(self._region[3] * height)
        else:
            x = self._region[0]
            y = self._region[1]
            w = self._region[2]
            h = self._region[3]

        object_poly = to_polygon(located_object)
        region_poly = Polygon([(x, y), (x+w-1, y), (x+w-1, y+h-1), (x, y+h-1)])
        iou = intersect_over_union(object_poly, region_poly)

        return iou > self.min_iou
