import torch
from torch import nn


class Module(nn.Module):
    """
    Module: nn.Module with device and dtype properties
    """

    def __init__(self):
        super(Module, self).__init__()
        self.register_buffer("dummy_buffer", torch.empty(0))

    @property
    def device(self) -> torch.device:
        return self.dummy_buffer.device

    @property
    def dtype(self) -> torch.dtype:
        return self.dummy_buffer.dtype
