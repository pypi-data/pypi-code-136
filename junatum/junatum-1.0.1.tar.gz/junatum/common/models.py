#!/usr/bin/env python3
from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return {(e.value, e.name) for e in cls}
