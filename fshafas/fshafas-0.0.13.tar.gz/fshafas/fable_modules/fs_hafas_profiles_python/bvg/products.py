from __future__ import annotations
from array import array
from ...fable_library.types import Array
from ...fs_hafas_python.types_hafas_client import ProductType

products: Array[ProductType] = [ProductType("suburban", "train", "S-Bahn", "S", array("l", [1]), True), ProductType("subway", "train", "U-Bahn", "U", array("l", [2]), True), ProductType("tram", "train", "Tram", "T", array("l", [4]), True), ProductType("bus", "bus", "Bus", "B", array("l", [8]), True), ProductType("ferry", "watercraft", "Fähre", "F", array("l", [16]), True), ProductType("express", "train", "IC/ICE", "E", array("l", [32]), True), ProductType("regional", "train", "RB/RE", "R", array("l", [64]), True)]

__all__ = ["products"]

