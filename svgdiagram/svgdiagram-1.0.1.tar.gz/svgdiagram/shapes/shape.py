import math
from .utils import bounds_to_center_and_size


INF_CON = float('inf')


class Shape:
    def __init__(self, svg_element):
        self.svg_element = svg_element

    def get_center_and_size(self):
        return bounds_to_center_and_size(self.svg_element.bounds)

    def get_all_discrete_anchors(self):
        raise NotImplementedError

    def get_closest_discrete_anchor(self, x, y):
        anchors = self.get_all_discrete_anchors()

        closest_dist = INF_CON
        closest_anchor = None

        for anchor in anchors:
            dist = math.sqrt((anchor.x - x)**2 + (anchor.y - y)**2)
            if dist < closest_dist:
                closest_dist = dist
                closest_anchor = anchor

        return closest_anchor

    def get_closest_floating_anchor(self, x, y):
        raise NotImplementedError
