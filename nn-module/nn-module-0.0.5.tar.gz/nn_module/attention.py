import math
import random

import torch
from torch_scatter import scatter_sum

from nn_module import Module


def sparse_multihead_softmax(values: torch.Tensor, index: torch.Tensor, eps: float = 1e-16) -> torch.Tensor:
    """
    :param values: (b, m, h)
    :param index: (m,)
    :param eps:
    :return: (b, m, h)
    """
    assert len(values.shape) == 3
    assert len(index.shape) == 1
    assert index.dtype == torch.int64
    assert values.shape[1] == index.shape[0]

    values = values - values.max()  # shift does not change softmax, use this to avoid overflow and reduce numerical err
    exp_logits = torch.exp(values)
    exp_logits_sum = scatter_sum(src=exp_logits, index=index, dim=1)[:, index, :]
    return exp_logits / (exp_logits_sum + eps)


def sparse_multihead_attention(
        q: torch.Tensor, k: torch.Tensor, edge_index: torch.Tensor, head_index: torch.Tensor,
):
    """
    :param q: (b, n, d) - (batch, node, dim)
    :param k: (b, n, d) - (batch, node, dim)
    :param edge_index: (2, m) - (2, edge)
    :param head_index: (d,) - (dim,)
    :return: (b, m, h) - (batch, edge, head)
    """
    assert len(q.shape) == 3
    assert len(k.shape) == 3
    assert q.shape == k.shape

    assert len(edge_index.shape) == 2
    assert edge_index.shape[0] == 2
    assert edge_index.dtype == torch.int64

    assert len(head_index.shape) == 1
    assert head_index.shape[0] == q.shape[2]

    src_q = q[:, edge_index[0, :], :]  # (b, m, d)
    dst_k = k[:, edge_index[1, :], :]  # (b, m, d)
    a_e = src_q * dst_k  # (b, m, d)
    a_e_sum = scatter_sum(src=a_e, index=head_index, dim=2)  # (b, m, h)
    return a_e_sum


class SparseMultiheadAttention(Module):
    def __init__(self,
                 key_dim: int,
                 hidden_dim: int,
                 edge_index: torch.Tensor,
                 num_heads: int = 1,
                 ):
        """
        :param edge_index: (2, m)
        """
        assert hidden_dim % num_heads == 0
        assert len(edge_index.shape) == 2
        assert edge_index.shape[0] == 2
        assert edge_index.dtype == torch.int64

        super().__init__()

        self.num_heads = num_heads
        self.key_dim = key_dim
        self.hidden_dim = hidden_dim

        self.register_buffer("edge_index", edge_index)
        self.register_buffer("head_index", torch.tensor(
            [i // (hidden_dim // num_heads) for i in range(hidden_dim)]
            , dtype=torch.int64,
        ))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(key_dim={self.key_dim}, hidden_dim={self.hidden_dim}, num_heads={self.num_heads})"

    def forward(self, q: torch.Tensor, k: torch.Tensor, reduce_dim: int = 1) -> torch.Tensor:
        """
        :param q: (b, n, d)
        :param k: (b, n, d)
        :param reduce_dim: reduce_dim=1, sum of each row is 1
        :return: (b, m, h)
        """
        assert len(q.shape) == 3
        assert len(k.shape) == 3
        assert q.shape == k.shape
        a_values = sparse_multihead_attention(
            q=q,
            k=k,
            edge_index=self.edge_index,
            head_index=self.head_index,
        ) / math.sqrt(self.key_dim)  # (b, m, h)
        a_values = sparse_multihead_softmax(values=a_values, index=self.edge_index[1 - reduce_dim, :])
        return a_values


if __name__ == "__main__":
    def _attention(q: torch.Tensor, k: torch.Tensor):
        """
        :param q: (b, n, d)
        :param k: (b, n, d)
        :return: (b, n, n)
        """
        assert len(q.shape) == 3
        assert len(k.shape) == 3
        assert q.shape == k.shape
        a_sum = torch.bmm(q, k.transpose(1, 2))
        return a_sum


    def _sparse_multihead_attention_elementwise(
            q: torch.Tensor, k: torch.Tensor, edge_index: torch.Tensor, head_index: torch.Tensor,
    ):
        """
        :param q: (b, n, d) - (batch, node, dim)
        :param k: (b, n, d) - (batch, node, dim)
        :param edge_index: (2, m) - (2, edge)
        :param head_index: (d,) - (dim,)
        :return: (b, m, h) - (batch, edge, head)
        """
        a_sum_list = []
        for i in head_index.unique():
            q_i = q[:, :, head_index == i]
            k_i = k[:, :, head_index == i]
            a_sum_i = _attention(q_i, k_i)
            a_sum_list.append(a_sum_i)
        a_sum = torch.stack(a_sum_list, dim=3)  # (b, n, n, h)
        a_e_sum_list = []
        for e in range(edge_index.shape[1]):
            i, j = edge_index[:, e]
            a_e_sum_list.append(a_sum[:, i, j, :])
        a_e_sum = torch.stack(a_e_sum_list, dim=1)  # (b, m, h)
        return a_e_sum


    # test sparse_multi_headed_attention
    b, n, d = 3, 5, 4
    q = torch.rand(b, n, d)
    k = torch.rand(b, n, d)
    edge_index = []
    for i in range(n):
        for j in range(n):
            if random.random() < 0.5:
                edge_index.append((i, j))
    edge_index = torch.tensor(edge_index).T
    head_index = torch.tensor([0, 0, 1, 1])
    expected = _sparse_multihead_attention_elementwise(q, k, edge_index, head_index)
    actual = sparse_multihead_attention(q, k, edge_index, head_index)
    assert torch.isclose(expected, actual).all()
