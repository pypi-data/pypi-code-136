from __future__ import annotations
from abc import abstractmethod
from dataclasses import dataclass
from typing import (Optional, Protocol, Any)
from ..fable_library.reflection import (TypeInfo, string_type, int32_type, array_type, bool_type, record_type, option_type, float64_type, obj_type, class_type)
from ..fable_library.types import (Record, Array)
from .extra_types import (IndexMap_2, IndexMap_2_reflection, Icon, Icon_reflection)

def _expr245() -> TypeInfo:
    return record_type("FsHafas.Client.ProductType", [], ProductType, lambda: [("id", string_type), ("mode", string_type), ("name", string_type), ("short", string_type), ("bitmasks", array_type(int32_type)), ("default", bool_type)])


@dataclass(eq = False, repr = False)
class ProductType(Record):
    id: str
    mode: str
    name: str
    short: str
    bitmasks: Array[int]
    default: bool

ProductType_reflection = _expr245

class Profile(Protocol):
    @property
    @abstractmethod
    def endpoint(self) -> str:
        ...

    @property
    @abstractmethod
    def journeys_from_trip(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def journeys_walking_speed(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def lines(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def locale(self) -> str:
        ...

    @property
    @abstractmethod
    def products(self) -> Array[ProductType]:
        ...

    @property
    @abstractmethod
    def radar(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def reachable_from(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def refresh_journey(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def remarks(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def remarks_get_polyline(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def timezone(self) -> str:
        ...

    @property
    @abstractmethod
    def trip(self) -> Optional[bool]:
        ...

    @property
    @abstractmethod
    def trips_by_name(self) -> Optional[bool]:
        ...


def _expr246() -> TypeInfo:
    return record_type("FsHafas.Client.Location", [], Location, lambda: [("type", string_type), ("id", option_type(string_type)), ("name", option_type(string_type)), ("poi", option_type(bool_type)), ("address", option_type(string_type)), ("longitude", option_type(float64_type)), ("latitude", option_type(float64_type)), ("altitude", option_type(float64_type)), ("distance", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Location(Record):
    type: str
    id: Optional[str]
    name: Optional[str]
    poi: Optional[bool]
    address: Optional[str]
    longitude: Optional[float]
    latitude: Optional[float]
    altitude: Optional[float]
    distance: Optional[int]

Location_reflection = _expr246

def _expr247() -> TypeInfo:
    return record_type("FsHafas.Client.ReisezentrumOpeningHours", [], ReisezentrumOpeningHours, lambda: [("Mo", option_type(string_type)), ("Di", option_type(string_type)), ("Mi", option_type(string_type)), ("Do", option_type(string_type)), ("Fr", option_type(string_type)), ("Sa", option_type(string_type)), ("So", option_type(string_type))])


@dataclass(eq = False, repr = False)
class ReisezentrumOpeningHours(Record):
    Mo: Optional[str]
    Di: Optional[str]
    Mi: Optional[str]
    Do: Optional[str]
    Fr: Optional[str]
    Sa: Optional[str]
    So: Optional[str]

ReisezentrumOpeningHours_reflection = _expr247

def _expr248() -> TypeInfo:
    return record_type("FsHafas.Client.Station", [], Station, lambda: [("type", string_type), ("id", option_type(string_type)), ("name", option_type(string_type)), ("station", option_type(Station_reflection())), ("location", option_type(Location_reflection())), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("lines", option_type(array_type(Line_reflection()))), ("is_meta", option_type(bool_type)), ("regions", option_type(array_type(string_type))), ("facilities", option_type(IndexMap_2_reflection(string_type, string_type))), ("reisezentrum_opening_hours", option_type(ReisezentrumOpeningHours_reflection())), ("stops", option_type(array_type(obj_type))), ("entrances", option_type(array_type(Location_reflection()))), ("transit_authority", option_type(string_type)), ("distance", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Station(Record):
    type: str
    id: Optional[str]
    name: Optional[str]
    station: Optional[Station]
    location: Optional[Location]
    products: Optional[IndexMap_2[str, bool]]
    lines: Optional[Array[Line]]
    is_meta: Optional[bool]
    regions: Optional[Array[str]]
    facilities: Optional[IndexMap_2[str, str]]
    reisezentrum_opening_hours: Optional[ReisezentrumOpeningHours]
    stops: Optional[Array[Any]]
    entrances: Optional[Array[Location]]
    transit_authority: Optional[str]
    distance: Optional[int]

Station_reflection = _expr248

def _expr249() -> TypeInfo:
    return record_type("FsHafas.Client.Stop", [], Stop, lambda: [("type", string_type), ("id", option_type(string_type)), ("name", option_type(string_type)), ("location", option_type(Location_reflection())), ("station", option_type(Station_reflection())), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("lines", option_type(array_type(Line_reflection()))), ("is_meta", option_type(bool_type)), ("reisezentrum_opening_hours", option_type(ReisezentrumOpeningHours_reflection())), ("ids", option_type(IndexMap_2_reflection(string_type, string_type))), ("load_factor", option_type(string_type)), ("entrances", option_type(array_type(Location_reflection()))), ("transit_authority", option_type(string_type)), ("distance", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Stop(Record):
    type: str
    id: Optional[str]
    name: Optional[str]
    location: Optional[Location]
    station: Optional[Station]
    products: Optional[IndexMap_2[str, bool]]
    lines: Optional[Array[Line]]
    is_meta: Optional[bool]
    reisezentrum_opening_hours: Optional[ReisezentrumOpeningHours]
    ids: Optional[IndexMap_2[str, str]]
    load_factor: Optional[str]
    entrances: Optional[Array[Location]]
    transit_authority: Optional[str]
    distance: Optional[int]

Stop_reflection = _expr249

def _expr250() -> TypeInfo:
    return record_type("FsHafas.Client.Region", [], Region, lambda: [("type", string_type), ("id", string_type), ("name", string_type), ("stations", array_type(string_type))])


@dataclass(eq = False, repr = False)
class Region(Record):
    type: str
    id: str
    name: str
    stations: Array[str]

Region_reflection = _expr250

def _expr251() -> TypeInfo:
    return record_type("FsHafas.Client.Line", [], Line, lambda: [("type", string_type), ("id", option_type(string_type)), ("name", option_type(string_type)), ("admin_code", option_type(string_type)), ("fahrt_nr", option_type(string_type)), ("additional_name", option_type(string_type)), ("product", option_type(string_type)), ("public", option_type(bool_type)), ("mode", option_type(string_type)), ("routes", option_type(array_type(string_type))), ("operator", option_type(Operator_reflection())), ("express", option_type(bool_type)), ("metro", option_type(bool_type)), ("night", option_type(bool_type)), ("nr", option_type(int32_type)), ("symbol", option_type(string_type)), ("directions", option_type(array_type(string_type))), ("product_name", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Line(Record):
    type: str
    id: Optional[str]
    name: Optional[str]
    admin_code: Optional[str]
    fahrt_nr: Optional[str]
    additional_name: Optional[str]
    product: Optional[str]
    public: Optional[bool]
    mode: Optional[str]
    routes: Optional[Array[str]]
    operator: Optional[Operator]
    express: Optional[bool]
    metro: Optional[bool]
    night: Optional[bool]
    nr: Optional[int]
    symbol: Optional[str]
    directions: Optional[Array[str]]
    product_name: Optional[str]

Line_reflection = _expr251

def _expr252() -> TypeInfo:
    return record_type("FsHafas.Client.Route", [], Route, lambda: [("type", string_type), ("id", string_type), ("line", string_type), ("mode", string_type), ("stops", array_type(string_type))])


@dataclass(eq = False, repr = False)
class Route(Record):
    type: str
    id: str
    line: str
    mode: str
    stops: Array[str]

Route_reflection = _expr252

def _expr253() -> TypeInfo:
    return record_type("FsHafas.Client.Cycle", [], Cycle, lambda: [("min", option_type(int32_type)), ("max", option_type(int32_type)), ("nr", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Cycle(Record):
    min: Optional[int]
    max: Optional[int]
    nr: Optional[int]

Cycle_reflection = _expr253

def _expr254() -> TypeInfo:
    return record_type("FsHafas.Client.ArrivalDeparture", [], ArrivalDeparture, lambda: [("arrival", option_type(float64_type)), ("departure", option_type(float64_type))])


@dataclass(eq = False, repr = False)
class ArrivalDeparture(Record):
    arrival: Optional[float]
    departure: Optional[float]

ArrivalDeparture_reflection = _expr254

def _expr255() -> TypeInfo:
    return record_type("FsHafas.Client.Schedule", [], Schedule, lambda: [("type", string_type), ("id", string_type), ("route", string_type), ("mode", string_type), ("sequence", array_type(ArrivalDeparture_reflection())), ("starts", array_type(string_type))])


@dataclass(eq = False, repr = False)
class Schedule(Record):
    type: str
    id: str
    route: str
    mode: str
    sequence: Array[ArrivalDeparture]
    starts: Array[str]

Schedule_reflection = _expr255

def _expr256() -> TypeInfo:
    return record_type("FsHafas.Client.Operator", [], Operator, lambda: [("type", string_type), ("id", string_type), ("name", string_type)])


@dataclass(eq = False, repr = False)
class Operator(Record):
    type: str
    id: str
    name: str

Operator_reflection = _expr256

def _expr257() -> TypeInfo:
    return record_type("FsHafas.Client.Hint", [], Hint, lambda: [("type", string_type), ("code", option_type(string_type)), ("summary", option_type(string_type)), ("text", string_type), ("trip_id", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Hint(Record):
    type: str
    code: Optional[str]
    summary: Optional[str]
    text: str
    trip_id: Optional[str]

Hint_reflection = _expr257

def _expr258() -> TypeInfo:
    return record_type("FsHafas.Client.Status", [], Status, lambda: [("type", string_type), ("code", option_type(string_type)), ("summary", option_type(string_type)), ("text", string_type), ("trip_id", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Status(Record):
    type: str
    code: Optional[str]
    summary: Optional[str]
    text: str
    trip_id: Optional[str]

Status_reflection = _expr258

def _expr259() -> TypeInfo:
    return record_type("FsHafas.Client.IcoCrd", [], IcoCrd, lambda: [("x", int32_type), ("y", int32_type), ("type", option_type(string_type))])


@dataclass(eq = False, repr = False)
class IcoCrd(Record):
    x: int
    y: int
    type: Optional[str]

IcoCrd_reflection = _expr259

def _expr260() -> TypeInfo:
    return record_type("FsHafas.Client.Edge", [], Edge, lambda: [("from_loc", option_type(obj_type)), ("to_loc", option_type(obj_type)), ("icon", option_type(Icon_reflection())), ("dir", option_type(int32_type)), ("ico_crd", option_type(IcoCrd_reflection()))])


@dataclass(eq = False, repr = False)
class Edge(Record):
    from_loc: Optional[Any]
    to_loc: Optional[Any]
    icon: Optional[Icon]
    dir: Optional[int]
    ico_crd: Optional[IcoCrd]

Edge_reflection = _expr260

def _expr261() -> TypeInfo:
    return record_type("FsHafas.Client.Event", [], Event, lambda: [("from_loc", option_type(obj_type)), ("to_loc", option_type(obj_type)), ("start", option_type(string_type)), ("end", option_type(string_type)), ("sections", option_type(array_type(string_type)))])


@dataclass(eq = False, repr = False)
class Event(Record):
    from_loc: Optional[Any]
    to_loc: Optional[Any]
    start: Optional[str]
    end: Optional[str]
    sections: Optional[Array[str]]

Event_reflection = _expr261

def _expr262() -> TypeInfo:
    return record_type("FsHafas.Client.Warning", [], Warning, lambda: [("type", string_type), ("id", option_type(string_type)), ("icon", option_type(Icon_reflection())), ("summary", option_type(string_type)), ("text", option_type(string_type)), ("category", option_type(string_type)), ("priority", option_type(int32_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("edges", option_type(array_type(Edge_reflection()))), ("events", option_type(array_type(Event_reflection()))), ("valid_from", option_type(string_type)), ("valid_until", option_type(string_type)), ("modified", option_type(string_type)), ("company", option_type(string_type)), ("categories", option_type(array_type(int32_type))), ("affected_lines", option_type(array_type(Line_reflection()))), ("from_stops", option_type(array_type(obj_type))), ("to_stops", option_type(array_type(obj_type)))])


@dataclass(eq = False, repr = False)
class Warning(Record):
    type: str
    id: Optional[str]
    icon: Optional[Icon]
    summary: Optional[str]
    text: Optional[str]
    category: Optional[str]
    priority: Optional[int]
    products: Optional[IndexMap_2[str, bool]]
    edges: Optional[Array[Edge]]
    events: Optional[Array[Event]]
    valid_from: Optional[str]
    valid_until: Optional[str]
    modified: Optional[str]
    company: Optional[str]
    categories: Optional[Array[int]]
    affected_lines: Optional[Array[Line]]
    from_stops: Optional[Array[Any]]
    to_stops: Optional[Array[Any]]

Warning_reflection = _expr262

def _expr263() -> TypeInfo:
    return record_type("FsHafas.Client.Geometry", [], Geometry, lambda: [("type", string_type), ("coordinates", array_type(float64_type))])


@dataclass(eq = False, repr = False)
class Geometry(Record):
    type: str
    coordinates: Array[float]

Geometry_reflection = _expr263

def _expr264() -> TypeInfo:
    return record_type("FsHafas.Client.Feature", [], Feature, lambda: [("type", string_type), ("properties", option_type(obj_type)), ("geometry", Geometry_reflection())])


@dataclass(eq = False, repr = False)
class Feature(Record):
    type: str
    properties: Optional[Any]
    geometry: Geometry

Feature_reflection = _expr264

def _expr265() -> TypeInfo:
    return record_type("FsHafas.Client.FeatureCollection", [], FeatureCollection, lambda: [("type", string_type), ("features", array_type(Feature_reflection()))])


@dataclass(eq = False, repr = False)
class FeatureCollection(Record):
    type: str
    features: Array[Feature]

FeatureCollection_reflection = _expr265

def _expr266() -> TypeInfo:
    return record_type("FsHafas.Client.StopOver", [], StopOver, lambda: [("stop", option_type(obj_type)), ("departure", option_type(string_type)), ("departure_delay", option_type(int32_type)), ("prognosed_departure", option_type(string_type)), ("planned_departure", option_type(string_type)), ("departure_platform", option_type(string_type)), ("prognosed_departure_platform", option_type(string_type)), ("planned_departure_platform", option_type(string_type)), ("arrival", option_type(string_type)), ("arrival_delay", option_type(int32_type)), ("prognosed_arrival", option_type(string_type)), ("planned_arrival", option_type(string_type)), ("arrival_platform", option_type(string_type)), ("prognosed_arrival_platform", option_type(string_type)), ("planned_arrival_platform", option_type(string_type)), ("remarks", option_type(array_type(obj_type))), ("pass_by", option_type(bool_type)), ("cancelled", option_type(bool_type)), ("departure_prognosis_type", option_type(string_type)), ("arrival_prognosis_type", option_type(string_type))])


@dataclass(eq = False, repr = False)
class StopOver(Record):
    stop: Optional[Any]
    departure: Optional[str]
    departure_delay: Optional[int]
    prognosed_departure: Optional[str]
    planned_departure: Optional[str]
    departure_platform: Optional[str]
    prognosed_departure_platform: Optional[str]
    planned_departure_platform: Optional[str]
    arrival: Optional[str]
    arrival_delay: Optional[int]
    prognosed_arrival: Optional[str]
    planned_arrival: Optional[str]
    arrival_platform: Optional[str]
    prognosed_arrival_platform: Optional[str]
    planned_arrival_platform: Optional[str]
    remarks: Optional[Array[Any]]
    pass_by: Optional[bool]
    cancelled: Optional[bool]
    departure_prognosis_type: Optional[str]
    arrival_prognosis_type: Optional[str]

StopOver_reflection = _expr266

def _expr267() -> TypeInfo:
    return record_type("FsHafas.Client.Trip", [], Trip, lambda: [("id", string_type), ("origin", option_type(obj_type)), ("destination", option_type(obj_type)), ("departure", option_type(string_type)), ("planned_departure", option_type(string_type)), ("prognosed_arrival", option_type(string_type)), ("departure_delay", option_type(int32_type)), ("departure_platform", option_type(string_type)), ("prognosed_departure_platform", option_type(string_type)), ("planned_departure_platform", option_type(string_type)), ("arrival", option_type(string_type)), ("planned_arrival", option_type(string_type)), ("prognosed_departure", option_type(string_type)), ("arrival_delay", option_type(int32_type)), ("arrival_platform", option_type(string_type)), ("prognosed_arrival_platform", option_type(string_type)), ("planned_arrival_platform", option_type(string_type)), ("stopovers", option_type(array_type(StopOver_reflection()))), ("schedule", option_type(float64_type)), ("price", option_type(Price_reflection())), ("operator", option_type(float64_type)), ("direction", option_type(string_type)), ("line", option_type(Line_reflection())), ("reachable", option_type(bool_type)), ("cancelled", option_type(bool_type)), ("walking", option_type(bool_type)), ("load_factor", option_type(string_type)), ("distance", option_type(int32_type)), ("public", option_type(bool_type)), ("transfer", option_type(bool_type)), ("cycle", option_type(Cycle_reflection())), ("alternatives", option_type(array_type(Alternative_reflection()))), ("polyline", option_type(FeatureCollection_reflection())), ("remarks", option_type(array_type(obj_type)))])


@dataclass(eq = False, repr = False)
class Trip(Record):
    id: str
    origin: Optional[Any]
    destination: Optional[Any]
    departure: Optional[str]
    planned_departure: Optional[str]
    prognosed_arrival: Optional[str]
    departure_delay: Optional[int]
    departure_platform: Optional[str]
    prognosed_departure_platform: Optional[str]
    planned_departure_platform: Optional[str]
    arrival: Optional[str]
    planned_arrival: Optional[str]
    prognosed_departure: Optional[str]
    arrival_delay: Optional[int]
    arrival_platform: Optional[str]
    prognosed_arrival_platform: Optional[str]
    planned_arrival_platform: Optional[str]
    stopovers: Optional[Array[StopOver]]
    schedule: Optional[float]
    price: Optional[Price]
    operator: Optional[float]
    direction: Optional[str]
    line: Optional[Line]
    reachable: Optional[bool]
    cancelled: Optional[bool]
    walking: Optional[bool]
    load_factor: Optional[str]
    distance: Optional[int]
    public: Optional[bool]
    transfer: Optional[bool]
    cycle: Optional[Cycle]
    alternatives: Optional[Array[Alternative]]
    polyline: Optional[FeatureCollection]
    remarks: Optional[Array[Any]]

Trip_reflection = _expr267

def _expr268() -> TypeInfo:
    return record_type("FsHafas.Client.Price", [], Price, lambda: [("amount", float64_type), ("currency", string_type), ("hint", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Price(Record):
    amount: float
    currency: str
    hint: Optional[str]

Price_reflection = _expr268

def _expr269() -> TypeInfo:
    return record_type("FsHafas.Client.Alternative", [], Alternative, lambda: [("trip_id", string_type), ("direction", option_type(string_type)), ("location", option_type(Location_reflection())), ("line", option_type(Line_reflection())), ("stop", option_type(obj_type)), ("when", option_type(string_type)), ("planned_when", option_type(string_type)), ("prognosed_when", option_type(string_type)), ("delay", option_type(int32_type)), ("platform", option_type(string_type)), ("planned_platform", option_type(string_type)), ("prognosed_platform", option_type(string_type)), ("remarks", option_type(array_type(obj_type))), ("cancelled", option_type(bool_type)), ("load_factor", option_type(string_type)), ("provenance", option_type(string_type)), ("previous_stopovers", option_type(array_type(StopOver_reflection()))), ("next_stopovers", option_type(array_type(StopOver_reflection()))), ("frames", option_type(array_type(Frame_reflection()))), ("polyline", option_type(FeatureCollection_reflection())), ("current_trip_position", option_type(Location_reflection())), ("origin", option_type(obj_type)), ("destination", option_type(obj_type)), ("prognosis_type", option_type(string_type))])


@dataclass(eq = False, repr = False)
class Alternative(Record):
    trip_id: str
    direction: Optional[str]
    location: Optional[Location]
    line: Optional[Line]
    stop: Optional[Any]
    when: Optional[str]
    planned_when: Optional[str]
    prognosed_when: Optional[str]
    delay: Optional[int]
    platform: Optional[str]
    planned_platform: Optional[str]
    prognosed_platform: Optional[str]
    remarks: Optional[Array[Any]]
    cancelled: Optional[bool]
    load_factor: Optional[str]
    provenance: Optional[str]
    previous_stopovers: Optional[Array[StopOver]]
    next_stopovers: Optional[Array[StopOver]]
    frames: Optional[Array[Frame]]
    polyline: Optional[FeatureCollection]
    current_trip_position: Optional[Location]
    origin: Optional[Any]
    destination: Optional[Any]
    prognosis_type: Optional[str]

Alternative_reflection = _expr269

def _expr270() -> TypeInfo:
    return record_type("FsHafas.Client.Leg", [], Leg, lambda: [("trip_id", option_type(string_type)), ("origin", option_type(obj_type)), ("destination", option_type(obj_type)), ("departure", option_type(string_type)), ("planned_departure", option_type(string_type)), ("prognosed_arrival", option_type(string_type)), ("departure_delay", option_type(int32_type)), ("departure_platform", option_type(string_type)), ("prognosed_departure_platform", option_type(string_type)), ("planned_departure_platform", option_type(string_type)), ("arrival", option_type(string_type)), ("planned_arrival", option_type(string_type)), ("prognosed_departure", option_type(string_type)), ("arrival_delay", option_type(int32_type)), ("arrival_platform", option_type(string_type)), ("prognosed_arrival_platform", option_type(string_type)), ("planned_arrival_platform", option_type(string_type)), ("stopovers", option_type(array_type(StopOver_reflection()))), ("schedule", option_type(float64_type)), ("price", option_type(Price_reflection())), ("operator", option_type(float64_type)), ("direction", option_type(string_type)), ("line", option_type(Line_reflection())), ("reachable", option_type(bool_type)), ("cancelled", option_type(bool_type)), ("walking", option_type(bool_type)), ("load_factor", option_type(string_type)), ("distance", option_type(int32_type)), ("public", option_type(bool_type)), ("transfer", option_type(bool_type)), ("cycle", option_type(Cycle_reflection())), ("alternatives", option_type(array_type(Alternative_reflection()))), ("polyline", option_type(FeatureCollection_reflection())), ("remarks", option_type(array_type(obj_type))), ("current_location", option_type(Location_reflection())), ("departure_prognosis_type", option_type(string_type)), ("arrival_prognosis_type", option_type(string_type)), ("checkin", option_type(bool_type))])


@dataclass(eq = False, repr = False)
class Leg(Record):
    trip_id: Optional[str]
    origin: Optional[Any]
    destination: Optional[Any]
    departure: Optional[str]
    planned_departure: Optional[str]
    prognosed_arrival: Optional[str]
    departure_delay: Optional[int]
    departure_platform: Optional[str]
    prognosed_departure_platform: Optional[str]
    planned_departure_platform: Optional[str]
    arrival: Optional[str]
    planned_arrival: Optional[str]
    prognosed_departure: Optional[str]
    arrival_delay: Optional[int]
    arrival_platform: Optional[str]
    prognosed_arrival_platform: Optional[str]
    planned_arrival_platform: Optional[str]
    stopovers: Optional[Array[StopOver]]
    schedule: Optional[float]
    price: Optional[Price]
    operator: Optional[float]
    direction: Optional[str]
    line: Optional[Line]
    reachable: Optional[bool]
    cancelled: Optional[bool]
    walking: Optional[bool]
    load_factor: Optional[str]
    distance: Optional[int]
    public: Optional[bool]
    transfer: Optional[bool]
    cycle: Optional[Cycle]
    alternatives: Optional[Array[Alternative]]
    polyline: Optional[FeatureCollection]
    remarks: Optional[Array[Any]]
    current_location: Optional[Location]
    departure_prognosis_type: Optional[str]
    arrival_prognosis_type: Optional[str]
    checkin: Optional[bool]

Leg_reflection = _expr270

def _expr271() -> TypeInfo:
    return record_type("FsHafas.Client.Journey", [], Journey, lambda: [("type", string_type), ("legs", array_type(Leg_reflection())), ("refresh_token", option_type(string_type)), ("remarks", option_type(array_type(obj_type))), ("price", option_type(Price_reflection())), ("cycle", option_type(Cycle_reflection())), ("scheduled_days", option_type(IndexMap_2_reflection(string_type, bool_type)))])


@dataclass(eq = False, repr = False)
class Journey(Record):
    type: str
    legs: Array[Leg]
    refresh_token: Optional[str]
    remarks: Optional[Array[Any]]
    price: Optional[Price]
    cycle: Optional[Cycle]
    scheduled_days: Optional[IndexMap_2[str, bool]]

Journey_reflection = _expr271

def _expr272() -> TypeInfo:
    return record_type("FsHafas.Client.Journeys", [], Journeys, lambda: [("earlier_ref", option_type(string_type)), ("later_ref", option_type(string_type)), ("journeys", option_type(array_type(Journey_reflection()))), ("realtime_data_from", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Journeys(Record):
    earlier_ref: Optional[str]
    later_ref: Optional[str]
    journeys: Optional[Array[Journey]]
    realtime_data_from: Optional[int]

Journeys_reflection = _expr272

def _expr273() -> TypeInfo:
    return record_type("FsHafas.Client.Duration", [], Duration, lambda: [("duration", int32_type), ("stations", array_type(obj_type))])


@dataclass(eq = False, repr = False)
class Duration(Record):
    duration: int
    stations: Array[Any]

Duration_reflection = _expr273

def _expr274() -> TypeInfo:
    return record_type("FsHafas.Client.Frame", [], Frame, lambda: [("origin", obj_type), ("destination", obj_type), ("t", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class Frame(Record):
    origin: Any
    destination: Any
    t: Optional[int]

Frame_reflection = _expr274

def _expr275() -> TypeInfo:
    return record_type("FsHafas.Client.Movement", [], Movement, lambda: [("direction", option_type(string_type)), ("trip_id", option_type(string_type)), ("line", option_type(Line_reflection())), ("location", option_type(Location_reflection())), ("next_stopovers", option_type(array_type(StopOver_reflection()))), ("frames", option_type(array_type(Frame_reflection()))), ("polyline", option_type(FeatureCollection_reflection()))])


@dataclass(eq = False, repr = False)
class Movement(Record):
    direction: Optional[str]
    trip_id: Optional[str]
    line: Optional[Line]
    location: Optional[Location]
    next_stopovers: Optional[Array[StopOver]]
    frames: Optional[Array[Frame]]
    polyline: Optional[FeatureCollection]

Movement_reflection = _expr275

def _expr276() -> TypeInfo:
    return record_type("FsHafas.Client.ServerInfo", [], ServerInfo, lambda: [("hci_version", option_type(string_type)), ("timetable_start", option_type(string_type)), ("timetable_end", option_type(string_type)), ("server_time", option_type(string_type)), ("realtime_data_updated_at", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class ServerInfo(Record):
    hci_version: Optional[str]
    timetable_start: Optional[str]
    timetable_end: Optional[str]
    server_time: Optional[str]
    realtime_data_updated_at: Optional[int]

ServerInfo_reflection = _expr276

def _expr277() -> TypeInfo:
    return record_type("FsHafas.Client.LoyaltyCard", [], LoyaltyCard, lambda: [("type", string_type), ("discount", option_type(int32_type)), ("class_", option_type(int32_type))])


@dataclass(eq = False, repr = False)
class LoyaltyCard(Record):
    type: str
    discount: Optional[int]
    class_: Optional[int]

LoyaltyCard_reflection = _expr277

def _expr278() -> TypeInfo:
    return record_type("FsHafas.Client.JourneysOptions", [], JourneysOptions, lambda: [("departure", option_type(class_type("System.DateTime"))), ("arrival", option_type(class_type("System.DateTime"))), ("earlier_than", option_type(string_type)), ("later_than", option_type(string_type)), ("results", option_type(int32_type)), ("via", option_type(string_type)), ("stopovers", option_type(bool_type)), ("transfers", option_type(int32_type)), ("transfer_time", option_type(int32_type)), ("accessibility", option_type(string_type)), ("bike", option_type(bool_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("tickets", option_type(bool_type)), ("polylines", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("remarks", option_type(bool_type)), ("walking_speed", option_type(string_type)), ("start_with_walking", option_type(bool_type)), ("language", option_type(string_type)), ("scheduled_days", option_type(bool_type)), ("first_class", option_type(bool_type)), ("age", option_type(int32_type)), ("loyalty_card", option_type(LoyaltyCard_reflection())), ("when", option_type(class_type("System.DateTime")))])


@dataclass(eq = False, repr = False)
class JourneysOptions(Record):
    departure: Optional[Any]
    arrival: Optional[Any]
    earlier_than: Optional[str]
    later_than: Optional[str]
    results: Optional[int]
    via: Optional[str]
    stopovers: Optional[bool]
    transfers: Optional[int]
    transfer_time: Optional[int]
    accessibility: Optional[str]
    bike: Optional[bool]
    products: Optional[IndexMap_2[str, bool]]
    tickets: Optional[bool]
    polylines: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    remarks: Optional[bool]
    walking_speed: Optional[str]
    start_with_walking: Optional[bool]
    language: Optional[str]
    scheduled_days: Optional[bool]
    first_class: Optional[bool]
    age: Optional[int]
    loyalty_card: Optional[LoyaltyCard]
    when: Optional[Any]

JourneysOptions_reflection = _expr278

def _expr279() -> TypeInfo:
    return record_type("FsHafas.Client.JourneysFromTripOptions", [], JourneysFromTripOptions, lambda: [("stopovers", option_type(bool_type)), ("transfer_time", option_type(int32_type)), ("accessibility", option_type(string_type)), ("tickets", option_type(bool_type)), ("polylines", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("remarks", option_type(bool_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type)))])


@dataclass(eq = False, repr = False)
class JourneysFromTripOptions(Record):
    stopovers: Optional[bool]
    transfer_time: Optional[int]
    accessibility: Optional[str]
    tickets: Optional[bool]
    polylines: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    remarks: Optional[bool]
    products: Optional[IndexMap_2[str, bool]]

JourneysFromTripOptions_reflection = _expr279

def _expr280() -> TypeInfo:
    return record_type("FsHafas.Client.LocationsOptions", [], LocationsOptions, lambda: [("fuzzy", option_type(bool_type)), ("results", option_type(int32_type)), ("stops", option_type(bool_type)), ("addresses", option_type(bool_type)), ("poi", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("lines_of_stops", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class LocationsOptions(Record):
    fuzzy: Optional[bool]
    results: Optional[int]
    stops: Optional[bool]
    addresses: Optional[bool]
    poi: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    lines_of_stops: Optional[bool]
    language: Optional[str]

LocationsOptions_reflection = _expr280

def _expr281() -> TypeInfo:
    return record_type("FsHafas.Client.TripOptions", [], TripOptions, lambda: [("stopovers", option_type(bool_type)), ("polyline", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("remarks", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class TripOptions(Record):
    stopovers: Optional[bool]
    polyline: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    remarks: Optional[bool]
    language: Optional[str]

TripOptions_reflection = _expr281

def _expr282() -> TypeInfo:
    return record_type("FsHafas.Client.StopOptions", [], StopOptions, lambda: [("lines_of_stops", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("remarks", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class StopOptions(Record):
    lines_of_stops: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    remarks: Optional[bool]
    language: Optional[str]

StopOptions_reflection = _expr282

def _expr283() -> TypeInfo:
    return record_type("FsHafas.Client.DeparturesArrivalsOptions", [], DeparturesArrivalsOptions, lambda: [("when", option_type(class_type("System.DateTime"))), ("direction", option_type(string_type)), ("line", option_type(string_type)), ("duration", option_type(int32_type)), ("results", option_type(int32_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("lines_of_stops", option_type(bool_type)), ("remarks", option_type(bool_type)), ("stopovers", option_type(bool_type)), ("include_related_stations", option_type(bool_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class DeparturesArrivalsOptions(Record):
    when: Optional[Any]
    direction: Optional[str]
    line: Optional[str]
    duration: Optional[int]
    results: Optional[int]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    lines_of_stops: Optional[bool]
    remarks: Optional[bool]
    stopovers: Optional[bool]
    include_related_stations: Optional[bool]
    products: Optional[IndexMap_2[str, bool]]
    language: Optional[str]

DeparturesArrivalsOptions_reflection = _expr283

def _expr284() -> TypeInfo:
    return record_type("FsHafas.Client.RefreshJourneyOptions", [], RefreshJourneyOptions, lambda: [("stopovers", option_type(bool_type)), ("polylines", option_type(bool_type)), ("tickets", option_type(bool_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("remarks", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RefreshJourneyOptions(Record):
    stopovers: Optional[bool]
    polylines: Optional[bool]
    tickets: Optional[bool]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    remarks: Optional[bool]
    language: Optional[str]

RefreshJourneyOptions_reflection = _expr284

def _expr285() -> TypeInfo:
    return record_type("FsHafas.Client.NearByOptions", [], NearByOptions, lambda: [("results", option_type(int32_type)), ("distance", option_type(int32_type)), ("poi", option_type(bool_type)), ("stops", option_type(bool_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("lines_of_stops", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class NearByOptions(Record):
    results: Optional[int]
    distance: Optional[int]
    poi: Optional[bool]
    stops: Optional[bool]
    products: Optional[IndexMap_2[str, bool]]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    lines_of_stops: Optional[bool]
    language: Optional[str]

NearByOptions_reflection = _expr285

def _expr286() -> TypeInfo:
    return record_type("FsHafas.Client.ReachableFromOptions", [], ReachableFromOptions, lambda: [("when", option_type(class_type("System.DateTime"))), ("max_transfers", option_type(int32_type)), ("max_duration", option_type(int32_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("polylines", option_type(bool_type))])


@dataclass(eq = False, repr = False)
class ReachableFromOptions(Record):
    when: Optional[Any]
    max_transfers: Optional[int]
    max_duration: Optional[int]
    products: Optional[IndexMap_2[str, bool]]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    polylines: Optional[bool]

ReachableFromOptions_reflection = _expr286

def _expr287() -> TypeInfo:
    return record_type("FsHafas.Client.BoundingBox", [], BoundingBox, lambda: [("north", float64_type), ("west", float64_type), ("south", float64_type), ("east", float64_type)])


@dataclass(eq = False, repr = False)
class BoundingBox(Record):
    north: float
    west: float
    south: float
    east: float

BoundingBox_reflection = _expr287

def _expr288() -> TypeInfo:
    return record_type("FsHafas.Client.RadarOptions", [], RadarOptions, lambda: [("results", option_type(int32_type)), ("frames", option_type(int32_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("duration", option_type(int32_type)), ("sub_stops", option_type(bool_type)), ("entrances", option_type(bool_type)), ("polylines", option_type(bool_type)), ("when", option_type(class_type("System.DateTime")))])


@dataclass(eq = False, repr = False)
class RadarOptions(Record):
    results: Optional[int]
    frames: Optional[int]
    products: Optional[IndexMap_2[str, bool]]
    duration: Optional[int]
    sub_stops: Optional[bool]
    entrances: Optional[bool]
    polylines: Optional[bool]
    when: Optional[Any]

RadarOptions_reflection = _expr288

def _expr289() -> TypeInfo:
    return record_type("FsHafas.Client.Filter", [], Filter, lambda: [("type", string_type), ("mode", string_type), ("value", string_type)])


@dataclass(eq = False, repr = False)
class Filter(Record):
    type: str
    mode: str
    value: str

Filter_reflection = _expr289

def _expr290() -> TypeInfo:
    return record_type("FsHafas.Client.TripsByNameOptions", [], TripsByNameOptions, lambda: [("when", option_type(class_type("System.DateTime"))), ("from_when", option_type(class_type("System.DateTime"))), ("until_when", option_type(class_type("System.DateTime"))), ("only_currently_running", option_type(bool_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("currently_stopping_at", option_type(obj_type)), ("line_name", option_type(string_type)), ("operator_names", option_type(array_type(string_type))), ("additional_filters", option_type(array_type(Filter_reflection())))])


@dataclass(eq = False, repr = False)
class TripsByNameOptions(Record):
    when: Optional[Any]
    from_when: Optional[Any]
    until_when: Optional[Any]
    only_currently_running: Optional[bool]
    products: Optional[IndexMap_2[str, bool]]
    currently_stopping_at: Optional[Any]
    line_name: Optional[str]
    operator_names: Optional[Array[str]]
    additional_filters: Optional[Array[Filter]]

TripsByNameOptions_reflection = _expr290

def _expr291() -> TypeInfo:
    return record_type("FsHafas.Client.RemarksOptions", [], RemarksOptions, lambda: [("from_", option_type(class_type("System.DateTime"))), ("to", option_type(class_type("System.DateTime"))), ("results", option_type(int32_type)), ("products", option_type(IndexMap_2_reflection(string_type, bool_type))), ("polylines", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class RemarksOptions(Record):
    from_: Optional[Any]
    to: Optional[Any]
    results: Optional[int]
    products: Optional[IndexMap_2[str, bool]]
    polylines: Optional[bool]
    language: Optional[str]

RemarksOptions_reflection = _expr291

def _expr292() -> TypeInfo:
    return record_type("FsHafas.Client.LinesOptions", [], LinesOptions, lambda: [("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class LinesOptions(Record):
    language: Optional[str]

LinesOptions_reflection = _expr292

def _expr293() -> TypeInfo:
    return record_type("FsHafas.Client.ServerOptions", [], ServerOptions, lambda: [("version_info", option_type(bool_type)), ("language", option_type(string_type))])


@dataclass(eq = False, repr = False)
class ServerOptions(Record):
    version_info: Optional[bool]
    language: Optional[str]

ServerOptions_reflection = _expr293

class HafasClient(Protocol):
    @abstractmethod
    def arrivals(self, __arg0: Any, __arg1: Optional[DeparturesArrivalsOptions]) -> Promise_1[Array[Alternative]]:
        ...

    @abstractmethod
    def departures(self, __arg0: Any, __arg1: Optional[DeparturesArrivalsOptions]) -> Promise_1[Array[Alternative]]:
        ...

    @abstractmethod
    def journeys(self, __arg0: Any, __arg1: Any, __arg2: Optional[JourneysOptions]) -> Promise_1[Journeys]:
        ...

    @abstractmethod
    def journeys_from_trip(self, __arg0: str, __arg1: StopOver, __arg2: Any, __arg3: Optional[JourneysFromTripOptions]) -> Promise_1[Array[Journey]]:
        ...

    @abstractmethod
    def lines(self, __arg0: str, __arg1: Optional[LinesOptions]) -> Promise_1[Array[Line]]:
        ...

    @abstractmethod
    def locations(self, __arg0: str, __arg1: Optional[LocationsOptions]) -> Promise_1[Array[Any]]:
        ...

    @abstractmethod
    def nearby(self, __arg0: Location, __arg1: Optional[NearByOptions]) -> Promise_1[Array[Any]]:
        ...

    @abstractmethod
    def radar(self, __arg0: BoundingBox, __arg1: Optional[RadarOptions]) -> Promise_1[Array[Movement]]:
        ...

    @abstractmethod
    def reachable_from(self, __arg0: Location, __arg1: Optional[ReachableFromOptions]) -> Promise_1[Array[Duration]]:
        ...

    @abstractmethod
    def refresh_journey(self, __arg0: str, __arg1: Optional[RefreshJourneyOptions]) -> Promise_1[Journey]:
        ...

    @abstractmethod
    def remarks(self, __arg0: Optional[RemarksOptions]) -> Promise_1[Array[Warning]]:
        ...

    @abstractmethod
    def server_info(self, __arg0: Optional[ServerOptions]) -> Promise_1[ServerInfo]:
        ...

    @abstractmethod
    def stop(self, __arg0: Any, __arg1: Optional[StopOptions]) -> Promise_1[Any]:
        ...

    @abstractmethod
    def trip(self, __arg0: str, __arg1: str, __arg2: Optional[TripOptions]) -> Promise_1[Trip]:
        ...

    @abstractmethod
    def trips_by_name(self, __arg0: str, __arg1: Optional[TripsByNameOptions]) -> Promise_1[Array[Trip]]:
        ...


__all__ = ["ProductType_reflection", "Location_reflection", "ReisezentrumOpeningHours_reflection", "Station_reflection", "Stop_reflection", "Region_reflection", "Line_reflection", "Route_reflection", "Cycle_reflection", "ArrivalDeparture_reflection", "Schedule_reflection", "Operator_reflection", "Hint_reflection", "Status_reflection", "IcoCrd_reflection", "Edge_reflection", "Event_reflection", "Warning_reflection", "Geometry_reflection", "Feature_reflection", "FeatureCollection_reflection", "StopOver_reflection", "Trip_reflection", "Price_reflection", "Alternative_reflection", "Leg_reflection", "Journey_reflection", "Journeys_reflection", "Duration_reflection", "Frame_reflection", "Movement_reflection", "ServerInfo_reflection", "LoyaltyCard_reflection", "JourneysOptions_reflection", "JourneysFromTripOptions_reflection", "LocationsOptions_reflection", "TripOptions_reflection", "StopOptions_reflection", "DeparturesArrivalsOptions_reflection", "RefreshJourneyOptions_reflection", "NearByOptions_reflection", "ReachableFromOptions_reflection", "BoundingBox_reflection", "RadarOptions_reflection", "Filter_reflection", "TripsByNameOptions_reflection", "RemarksOptions_reflection", "LinesOptions_reflection", "ServerOptions_reflection"]

