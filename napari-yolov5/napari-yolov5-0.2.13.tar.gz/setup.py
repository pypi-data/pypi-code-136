#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(package_data={'napari_yolov5': ['./*','data/*','data/*/*','resources/*','resources/Readme/*','models/*','models/hub/*','runs/*/*/*/*','utils/*/*','utils/*/*/*' ]})
#setup(package_data={'napari_yolov5': ['*/*/*/*/*']})

