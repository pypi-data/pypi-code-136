"""Feature Pyramid Network."""
from collections import OrderedDict

import torch
from torchvision.ops import FeaturePyramidNetwork as _FPN


class FeaturePyramidNetwork(_FPN):
    def forward(self, feature_list: list[torch.Tensor]) -> list[torch.Tensor]:
        """Apply feature pyramid network to feature list."""
        keys = map(str, range(len(feature_list)))
        result: OrderedDict[str, torch.Tensor] = super().forward(
            OrderedDict(zip(keys, feature_list))
        )
        return list(result.values())
