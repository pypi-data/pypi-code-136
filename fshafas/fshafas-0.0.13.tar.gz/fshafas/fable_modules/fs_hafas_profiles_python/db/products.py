from __future__ import annotations
from array import array
from ...fable_library.types import Array
from ...fs_hafas_python.types_hafas_client import ProductType

products: Array[ProductType] = [ProductType("nationalExpress", "train", "InterCityExpress", "ICE", array("l", [1]), True), ProductType("national", "train", "InterCity & EuroCity", "IC/EC", array("l", [2]), True), ProductType("regionalExp", "train", "RegionalExpress & InterRegio", "RE/IR", array("l", [4]), True), ProductType("regional", "train", "Regio", "RB", array("l", [8]), True), ProductType("suburban", "train", "S-Bahn", "S", array("l", [16]), True), ProductType("bus", "bus", "Bus", "B", array("l", [32]), True), ProductType("ferry", "watercraft", "Ferry", "F", array("l", [64]), True), ProductType("subway", "train", "U-Bahn", "U", array("l", [128]), True), ProductType("tram", "train", "Tram", "T", array("l", [256]), True), ProductType("taxi", "taxi", "Group Taxi", "Taxi", array("l", [512]), True)]

__all__ = ["products"]

