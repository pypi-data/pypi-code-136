"""FCOS object detector."""
from collections import OrderedDict
from typing import Optional

import timm
import torch
from timm.models.features import FeatureListNet
from torchvision.models.detection import FCOS as _FCOS
from torchvision.models.detection.anchor_utils import AnchorGenerator
from torchvision.models.detection.image_list import ImageList

from .base import SparrowDetector
from .box_ops import decode_box_offsets
from .fpn import FeaturePyramidNetwork


class _FCOSBackbone(torch.nn.Module):
    def __init__(self, backbone: FeatureListNet, out_channels: int) -> None:
        super().__init__()
        self.backbone = backbone
        self.out_channels = out_channels
        self.fpn = FeaturePyramidNetwork(backbone.feature_info.channels(), out_channels)

    def forward(self, x: torch.Tensor) -> list[torch.Tensor]:
        features = self.backbone(x)
        return self.fpn(features)


class FCOS(SparrowDetector):
    def __init__(
        self,
        n_classes: int,
        backbone_name: str = "resnet50",
        fpn_out_channels: int = 256,
    ) -> None:
        super().__init__()
        self.n_classes = n_classes
        feature_extractor: FeatureListNet = timm.create_model(
            backbone_name, pretrained=True, features_only=True
        )
        self.backbone = _FCOSBackbone(feature_extractor, fpn_out_channels)
        anchor_generator = AnchorGenerator(
            feature_extractor.feature_info.reduction(), (1,)
        )
        self.anchors: Optional[torch.Tensor] = None
        self.n_anchors_per_level: Optional[list[int]] = None
        self._fcos = _FCOS(
            self.backbone,
            n_classes,
            anchor_generator=anchor_generator,
        )

    def forward(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        features: list[torch.Tensor] = self.backbone(x)
        logits = self._fcos.head.classification_head(features)
        box_offsets, centerness = self._fcos.head.regression_head(features)
        if self.anchors is None:
            (self.anchors,) = self._fcos.anchor_generator(
                ImageList(x, [x.shape[-2:]]), features
            )
        if self.n_anchors_per_level is None:
            self.n_anchors_per_level = [x.size(2) * x.size(3) for x in features]
        boxes = decode_box_offsets(box_offsets, self.anchors)
        scores, labels = torch.max(torch.sigmoid(logits), dim=-1)
        return OrderedDict(
            boxes=boxes,
            scores=scores,
            labels=labels,
            logits=logits,
            box_offsets=box_offsets,
            centerness=centerness,
        )

    def compute_loss(
        self, targets: list[dict[str, torch.Tensor]], outputs: dict[str, torch.Tensor]
    ) -> dict[str, torch.Tensor]:
        head_outputs = {
            "cls_logits": outputs["logits"],
            "bbox_regression": outputs["box_offsets"],
            "bbox_ctrness": outputs["centerness"],
        }
        losses = self._fcos.compute_loss(
            targets,
            head_outputs,
            [self.anchors] * len(targets),
            self.n_anchors_per_level,
        )
        return {
            "classification": losses["classification"],
            "regression": losses["bbox_regression"],
            "centerness": losses["bbox_ctrness"],
        }
