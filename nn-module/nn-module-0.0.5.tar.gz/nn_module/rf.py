import torch

from nn_module import Module


class RandomFeature(Module):
    def __init__(self, dim: int, width: int):
        super().__init__()
        r = torch.randn(dim, width)
        r = r / torch.linalg.norm(r, dim=0)
        self.register_buffer("rotation", r)

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return input @ self.rotation
