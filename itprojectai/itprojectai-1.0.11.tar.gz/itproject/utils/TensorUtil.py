import torch


def ndarrayToTensor(X):
    """把ndarray转换成tensor"""
    return torch.from_numpy(X).to(torch.float32)
