from random import random
from typing import Any, Dict, List, Optional

import torch
import torch.nn as nn


class DropLayer(nn.Module):
    """
    Drop a layer randomly for stochastic depth.
    """

    def __init__(self, module: nn.Module, p: float = 0.0) -> None:
        super(DropLayer, self).__init__()
        self.module = module
        self.p = p

    def forward(
        self, x: Any, *args: List[Any], **kwargs: Optional[Dict[str, Any]]
    ) -> Any:
        if not self.training or random() > self.p:
            x = self.module(x, *args, **kwargs)
        return x
