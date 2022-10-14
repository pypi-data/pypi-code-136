from typing import List, Callable

import torch
from torch import nn

from nn_module import Module


class FeedForward(Module):
    def __init__(
            self,
            dim_list: List[int],
            activation: Callable[[], nn.Module] = nn.ReLU,
    ):
        super().__init__()
        assert len(dim_list) >= 2
        sequence: List[nn.Module] = []
        for i in range(len(dim_list) - 1):
            in_dim = dim_list[i]
            out_dim = dim_list[i + 1]
            sequence.append(nn.Linear(in_features=in_dim, out_features=out_dim))
            if i < len(dim_list) - 2:  # not last layer
                sequence.append(activation())
        self.register_module("sequence", nn.Sequential(*sequence))

    def forward(self, x: torch.Tensor):
        return self.sequence.forward(x)


if __name__ == "__main__":
    m = FeedForward([3, 5, 6, 3])
    print(list(m.parameters()))
