from __future__ import annotations

import logging
import logging.config
from collections import OrderedDict
from os import PathLike as _PathLike
from typing import Any, Callable, Dict, IO, List, Optional, Tuple, Union

import accelerate
import torch.nn as nn
import torch.optim as optim
import torch.utils.data as data

from .base_runner import BaseRunner

PathLike = Union[str, _PathLike]
File = Union[PathLike, IO]


class Runner(BaseRunner):
    """
    Set up everything for running a job
    """
