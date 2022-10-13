"""
Tools for handling Deep Learning data management and pipelines
"""
import warnings
from .data_generator import DataGenerator, DataGeneratorMap, FileLoader
from .sample_integrity import load_sample_identification, save_sample_identification

try:
    from .tf_types import BBOX, TfRange
except ImportError:
    warnings.warn("Tensorflow not installed; tf types are not available", ImportWarning)
