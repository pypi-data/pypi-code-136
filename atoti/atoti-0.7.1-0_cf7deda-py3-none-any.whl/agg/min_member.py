from __future__ import annotations

from atoti_core import doc

from .._measures.generic_measure import GenericMeasure
from ..level import Level
from ..measure_description import MeasureConvertible, MeasureDescription
from ._utils import EXTREMUM_MEMBER_DOC


@doc(
    EXTREMUM_MEMBER_DOC,
    op="min",
    example="""
        >>> m["City with minimum price"] = tt.agg.min_member(m["Price"], l["City"])

        At the given level, the measure is equal to the current member of the City level:

        >>> cube.query(m["City with minimum price"], levels=[l["City"]])
                               City with minimum price
        Continent     City
        Europe        Berlin                    Berlin
                      London                    London
                      Paris                      Paris
        North America New York                New York

        At a level above it, the measure is equal to the city of each continent with the minimum price:

        >>> cube.query(m["City with minimum price"], levels=[l["Continent"]])
                      City with minimum price
        Continent
        Europe                         Berlin
        North America                New York

        At the top level, the measure is equal to the city with the minimum price across all continents:

        >>> cube.query(m["City with minimum price"])
          City with minimum price
        0                  Berlin""".replace(
        "\n", "", 1
    ),
)
def min_member(measure: MeasureConvertible, /, level: Level) -> MeasureDescription:
    return GenericMeasure(
        "COMPARABLE_MAX",
        measure._measure_description,
        level._coordinates.java_description,
        False,
        "MEMBER",
    )
