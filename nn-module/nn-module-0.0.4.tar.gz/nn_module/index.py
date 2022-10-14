import torch

from nn_module import Module


class Index(Module):
    def __init__(self, n: int, d: int):
        super().__init__()
        self.register_buffer("index", torch.randn(n, d, dtype=torch.float32))

    def __repr__(self):
        return f"{self.__class__.__name__}(n={self.index.shape[0]}, d={self.index.shape[1]})"

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        :param x: (b, n)
        :return: (b, n, d)
        """
        assert len(x.shape) == 2
        assert x.shape[1] == self.index.shape[0]
        x_ = x.unsqueeze(2).repeat(1, 1, self.index.shape[1])
        return x_ * self.index.unsqueeze(0)


if __name__ == "__main__":
    i = Index(5, 3)
    print(i.index)
    x = torch.tensor([
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
    ])
    print(i.forward(x))
