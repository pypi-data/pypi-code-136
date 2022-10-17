from __future__ import annotations
from array import array
from ...fable_library.types import Array
from ...fs_hafas_python.types_hafas_client import ProductType

products: Array[ProductType] = [ProductType("national-train", "train", "InterCity", "IC", array("l", [1]), True), ProductType("national-train-2", "train", "ICL", "ICL", array("l", [2]), True), ProductType("local-train", "train", "Regional", "RE", array("l", [4]), True), ProductType("o", "train", "Ø", "Ø", array("l", [8]), True), ProductType("s-tog", "train", "S-Tog A/B/Bx/C/E/F/H", "S", array("l", [16]), True)]

__all__ = ["products"]

