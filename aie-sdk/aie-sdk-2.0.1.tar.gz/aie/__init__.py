#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "2.0.1"

import aie
from .aie_env import AIEEnv
from aie.map.aie_map import Map
from aie.export import Export
import types


from aie.aie_object.image import Image

from aie.aie_object.collection import Collection

from aie.aie_object.image_collection import ImageCollection

from aie.aie_object.geometry import Geometry

from aie.aie_object.feature import Feature

from aie.aie_object.feature_collection import FeatureCollection

from aie.aie_object.filter import Filter

from aie.aie_object.reducer import Reducer

from aie.aie_object.terrain import Terrain


def Authenticate(token=None):
    aie.auth.Authenticate.auth(token)


def Initialize(debug_level=aie.g_var.LogLevel.INFO_LEVEL):
    AIEEnv.init(debug_level)
