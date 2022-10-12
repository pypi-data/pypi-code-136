#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- mode: python -*-
from setuptools import setup, Extension
import numpy

setup(
    ext_modules=[
        Extension(
            "quicksong.features", sources=["quicksong/features.pyx"], language="c++"
        )
    ],
    include_dirs=[numpy.get_include()],
)
