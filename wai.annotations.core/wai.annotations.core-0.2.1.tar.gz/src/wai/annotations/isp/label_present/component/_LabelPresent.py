from re import compile
from typing import Pattern, Optional, List

from shapely.geometry import Polygon
from wai.common.adams.imaging.locateobjects import LocatedObjects, LocatedObject
from wai.common.cli.options import TypedOption, FlagOption

from ....core.component import ProcessorComponent
from ....core.stream import ThenFunction, DoneFunction
from ....core.stream.util import RequiresNoFinalisation
from ....core.util import InstanceState
from ....domain.image import ImageInstance
from ....domain.image.object_detection import ImageObjectDetectionInstance
from ....domain.image.object_detection.util import get_object_label
from wai.annotations.core.util import to_polygon, intersect_over_union


class LabelPresent(
    RequiresNoFinalisation,
    ProcessorComponent[ImageInstance, ImageInstance]
):
    """
    Processes a stream of object-detection instances,
    marking images as negative if annotations don't match the criteria.
    """

    labels = TypedOption(
        "-l", "--labels",
        type=str,
        nargs="+",
        help="explicit list of labels to check")

    regex = TypedOption(
        "-r", "--regexp",
        type=str,
        metavar="regexp",
        help="regular expression for using only a subset of labels")

    region = TypedOption(
        "--region",
        type=str,
        default=None,
        metavar="x,y[;x,y[;...]]",
        nargs="*",
        help="semicolon-separated list of comma-separated x/y pairs defining the region that the object must overlap with in order to be included. Values between 0-1 are considered normalized, otherwise absolute pixels.")

    coordinate_separator = TypedOption(
        "--coordinate-separator",
        type=str,
        default=";",
        metavar="CHAR",
        help="the separator between coordinates")

    pair_separator = TypedOption(
        "--pair-separator",
        type=str,
        default=",",
        metavar="CHAR",
        help="the separator between the x and y of a pair")

    min_iou = TypedOption(
        "--min-iou",
        type=float,
        metavar="FLOAT",
        default=0.01,
        help="the minimum IoU (intersect over union) that the object must have with the region(s) in order to be considered an overlap (object detection only)")

    invert_regions = FlagOption(
        "--invert-regions",
        help="Inverts the matching sense from 'labels have to overlap at least one of the region(s)' to 'labels cannot overlap any region'")

    verbose = FlagOption(
        "--verbose",
        help="Outputs some debugging information")

    # The compiled regex
    _pattern: Optional[Pattern] = InstanceState(lambda self: compile(self.regex) if self.regex is not None else None)

    def process_element(
            self,
            element: ImageObjectDetectionInstance,
            then: ThenFunction[ImageObjectDetectionInstance],
            done: DoneFunction
    ):
        # determines annotations that match criteria
        indices = self.find_valid_objects(element.annotations, element.data.width, element.data.height)
        if self.verbose:
            self.logger.info("indices: %s" % str(indices))
        if len(indices) > 0:
            then(element)

    def find_valid_objects(self, located_objects: LocatedObjects, width: int, height: int) -> List[int]:
        """
        Returns indices of objects that match the search criteria.

        :param located_objects: The located objects to process.
        :param width: the width of the image
        :param height: the height of the image
        :return: the list of indices of objects matching the criteria
        """
        result: List[int] = []

        self._init_regions()

        # Search the located objects
        for index, located_object in enumerate(located_objects):
            label = get_object_label(located_object)
            label_ok = self.check_label(label)
            if self.verbose:
                self.logger.info("check_label: %s = %s" % (label, str(label_ok)))
            if label_ok:
                if self.check_regions(located_object, width, height):
                    result.append(index)

        return result

    def _init_regions(self):
        """
        Parses the regions, if necessary.
        """
        if hasattr(self, "_regions"):
            return

        if len(self.coordinate_separator) != 1:
            raise Exception("Coordinate separator must be a single character, but found: %s" % self.coordinate_separator)
        if len(self.pair_separator) != 1:
            raise Exception("Pair separator must be a single character, but found: %s" % self.pair_separator)

        self._regions = []
        self._normalized = True
        self._polygons = {}
        if self.region is not None:
            for r in self.region:
                region = []
                coords = r.split(self.coordinate_separator)
                if len(coords) < 3:
                    raise Exception("Region must have at least three coordinates of format 'x,y' separated by '%s', but found: %s" % (self.coordinate_separator, r))
                for coord in coords:
                    pair = coord.split(self.pair_separator)
                    if len(pair) != 2:
                        raise Exception("Coordinates must have format 'x%sy', but found '%s' in region '%s'!" % (self.pair_separator, coord, r))
                    region.append([float(x) for x in pair])
                self._regions.append(region)
                # not normalized?
                if sum([(0 if (sum(x) < 2) else 1) for x in region]) > 0:
                    self._normalized = False

    def check_label(self, label: str) -> bool:
        """
        Checks whether the label fits the criteria.

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

    def check_regions(self, located_object: LocatedObject, width: int, height: int) -> bool:
        """
        Checks whether the object falls within at least one of the regions or, when inverting,
        whether it does not fall within any.

        :param located_object: the object to check
        :param width: the width of the image
        :param height: the height of the image
        :return: True if no regions defined or if object matches at least one region (invert_regions=False) or none at all (invert_regions=True)
        """
        if len(self._regions) == 0:
            return True

        key = "%d-%d" % (width, height)

        # already created polygons for image dimensions?
        if key not in self._polygons:
            region_polys = []
            self._polygons[key] = region_polys
            for region in self._regions:
                if self._normalized:
                    points = []
                    for x, y in region:
                        points.append([int(x * width), int(y * height)])
                else:
                    points = region
                region_polys.append(Polygon(points))
        else:
            region_polys = self._polygons[key]

        # overlap with any region?
        object_poly = to_polygon(located_object)
        match = False
        for region_poly in region_polys:
            iou = intersect_over_union(object_poly, region_poly)
            if self.verbose:
                self.logger.info("object_poly: %s" % str(object_poly))
                self.logger.info("region_poly: %s" % str(region_poly))
                self.logger.info("iou: %f > %f = %s" % (iou, self.min_iou, str(iou > self.min_iou)))
            if iou > self.min_iou:
                match = True
                break

        result = (not self.invert_regions and match) or (self.invert_regions and not match)
        if self.verbose:
            self.logger.info("check_regions = %s" % str(result))
        return result
