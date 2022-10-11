"""Detection config."""
from dataclasses import dataclass


@dataclass
class Config:
    # Model
    backbone_name: str = "resnet18"
    fpn_out_channels: int = 256

    # Loss
    classification_weight: float = 2.0
    regression_weight: float = 2.0
    centerness_weight: float = 5.0
