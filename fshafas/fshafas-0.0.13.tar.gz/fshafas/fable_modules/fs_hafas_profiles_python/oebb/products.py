from __future__ import annotations
from array import array
from ...fable_library.types import Array
from ...fs_hafas_python.types_hafas_client import ProductType

products: Array[ProductType] = [ProductType("nationalExpress", "train", "InterCityExpress & RailJet", "ICE/RJ", array("l", [1]), True), ProductType("national", "train", "InterCity & EuroCity", "IC/EC", array("l", [2, 4]), True), ProductType("interregional", "train", "Durchgangszug & EuroNight", "D/EN", array("l", [8, 4096]), True), ProductType("regional", "train", "Regional & RegionalExpress", "R/REX", array("l", [16]), True), ProductType("suburban", "train", "S-Bahn", "S", array("l", [32]), True), ProductType("bus", "bus", "Bus", "B", array("l", [64]), True), ProductType("ferry", "watercraft", "Ferry", "F", array("l", [128]), True), ProductType("subway", "train", "U-Bahn", "U", array("l", [256]), True), ProductType("tram", "train", "Tram", "T", array("l", [512]), True), ProductType("onCall", "taxi", "on-call transit, lifts, etc", "on-call/lift", array("l", [2048]), True)]

__all__ = ["products"]

