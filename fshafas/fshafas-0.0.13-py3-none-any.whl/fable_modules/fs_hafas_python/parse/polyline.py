from __future__ import annotations
from array import array as array_3
from math import (sin, cos, atan2)
import polyline
from typing import (Optional, Any, Tuple, Literal, Callable)
from ...fable_library.array import (try_find, map, sum, map_indexed as map_indexed_1)
from ...fable_library.double import (divide, sqrt)
from ...fable_library.seq import (to_array, map_indexed)
from ...fable_library.types import (Array, Float64Array)
from ...fable_library.util import round as round_1
from ..context import Context
from ..types_hafas_client import (FeatureCollection, Geometry, Feature)
from ..types_raw_hafas_client import (RawPoly, PpLocRef)
from .common import get_element_at

def decode(s: str) -> Array[Array[float]]:
    return []


def round(f: float) -> float:
    return round_1(f, 5)


default_feature_collection: FeatureCollection = FeatureCollection("featureCollection", [0] * 0)

def get_stop(ctx: Context, p: RawPoly, i: int) -> Optional[Any]:
    match_value: Optional[Array[PpLocRef]] = p.pp_loc_ref_l
    if match_value is None:
        return None

    else: 
        def predicate(p_loc_ref_l: PpLocRef, ctx: Context=ctx, p: RawPoly=p, i: int=i) -> bool:
            return p_loc_ref_l.pp_idx == i

        match_value_1: Optional[PpLocRef] = try_find(predicate, match_value)
        if match_value_1 is None:
            return None

        else: 
            return get_element_at(match_value_1.loc_x, ctx.common.locations)




def parse_polyline(ctx: Context, poly: RawPoly) -> FeatureCollection:
    def mapping(i: int, p: Array[float], ctx: Context=ctx, poly: RawPoly=poly) -> Feature:
        return Feature("Feature", get_stop(ctx, poly, i), Geometry("Point", array_3("d", [round(p[1]), round(p[0])])))

    return FeatureCollection(default_feature_collection.type, to_array(map_indexed(mapping, polyline.decode(poly.crd_enc_yx))))


def calculate_distance(p1latitude: float, p1longitude: float, p2latitude: float, p2longitude: float) -> float:
    d_lat: float = divide((p2latitude - p1latitude) * 3.141592653589793, 180.0)
    d_lon: float = divide((p2longitude - p1longitude) * 3.141592653589793, 180.0)
    lat1: float = divide(p1latitude * 3.141592653589793, 180.0)
    lat2: float = divide(p2latitude * 3.141592653589793, 180.0)
    a: float = (sin(divide(d_lat, 2.0)) * sin(divide(d_lat, 2.0))) + (((sin(divide(d_lon, 2.0)) * sin(divide(d_lon, 2.0))) * cos(lat1)) * cos(lat2))
    return 6371.0 * (2.0 * atan2(sqrt(a), sqrt(1.0 - a)))


def distance_of_feature_collection(fc: FeatureCollection) -> float:
    def mapping(f: Feature, fc: FeatureCollection=fc) -> Tuple[float, float]:
        return (f.geometry.coordinates[1], f.geometry.coordinates[0])

    lat_lon_points: Array[Tuple[float, float]] = map(mapping, fc.features, None)
    def mapping_1(i: int, _arg: Tuple[float, float], fc: FeatureCollection=fc) -> float:
        if i > 0:
            prev: Tuple[float, float] = lat_lon_points[i - 1]
            curr: Tuple[float, float] = lat_lon_points[i]
            return calculate_distance(prev[0], prev[1], curr[0], curr[1])

        else: 
            return 0.0


    class ObjectExpr443:
        @property
        def GetZero(self) -> Callable[[], float]:
            def _arrow441(__unit: Literal[None]=None) -> float:
                return 0.0

            return _arrow441

        @property
        def Add(self) -> Callable[[float, float], float]:
            def _arrow442(x: float, y: float) -> float:
                return x + y

            return _arrow442

    return sum(map_indexed_1(mapping_1, lat_lon_points, Float64Array), ObjectExpr443())


__all__ = ["decode", "round", "default_feature_collection", "get_stop", "parse_polyline", "calculate_distance", "distance_of_feature_collection"]

