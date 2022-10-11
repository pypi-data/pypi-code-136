from dataclasses import dataclass

from magnumapi.geometry.definitions.RectangularBlockDefinition import RectangularBlockDefinition


@dataclass
class HomogenizedRectangularBlockDefinition(RectangularBlockDefinition):
    """Class for a homogenized rectangular block definition.

    Attributes:
       x_0 (float):
       y_0 (float):
       x_1 (float):
       y_1 (float):
       x_2 (float):
       y_2 (float):
       x_3 (float):
       y_3 (float):
    """
    x_0: float
    y_0: float
    x_1: float
    y_1: float
    x_2: float
    y_2: float
    x_3: float
    y_3: float
