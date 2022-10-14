# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import math
import warnings

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch import Tensor
from typing import Any, Callable, Dict, List, Optional, Tuple

from .transformer import MultiheadAttention


class EnformerAttention(MultiheadAttention):
    r"""
    bin_size: Bin sized used to partition the sequence. This can be used to
    compute features on the absolute scale relative to the genome.
    feature_functions: List of different feature functions to use. Each function
    will take as argument: positions, sequence length and number of features
    to compute.
    symmetric: If True, the resulting features will be symmetric across the
    relative position of 0 (i.e. only absolute value of positions will
    matter). If false, then both the symmetric and asymmetric version
    (symmetric multiplied by sign(positions)) of the features will be used.
    """

    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        dropout: float = 0.0,
        scale_factor: float = 1.0,
        bias: bool = True,
        add_bias_kv: bool = False,
        add_zero_attn: bool = False,
        kdim: Optional[int] = None,
        vdim: Optional[int] = None,
        batch_first: Optional[bool] = False,
        pos_embed_size: Optional[int] = 1000,
        pos_embed_bin_size: Optional[int] = 10,
        pos_embed_dropout: Optional[int] = 1000,
        **kwargs: Optional[Dict[str, Any]]
    ) -> None:
        super().__init__(
            embed_dim,
            num_heads,
            dropout,
            scale_factor,
            bias,
            add_bias_kv,
            add_zero_attn,
            kdim,
            vdim,
            batch_first,
        )

        self.pos_embed_size = pos_embed_size

        self.pos_embed = nn.Linear(self.embed_dim, self.embed_dim)
        self.content_bias = nn.Parameter(
            torch.zeros([self.num_heads, 1, self.head_dim])
        )
        self.pos_embed_bias = nn.Parameter(
            torch.zeros([self.num_heads, 1, self.head_dim])
        )
        self.pos_embed_dropout = nn.Dropout(pos_embed_dropout)
        self.pos_embed_bin_size = pos_embed_bin_size
        self.pos_embed_functions = [
            "positional_features_exponential",
            "positional_features_central_mask",
            "positional_features_gamma",
            "positional_features_cosine",
            "positional_features_linear_masks",
            "positional_features_sin_cos",
        ]
        self.pos_embed_symmetric = False
        self.pos_embed_components = len(
            self.pos_embed_functions
        )  # 1 per each basis function
        if not self.pos_embed_symmetric:
            self.pos_embed_components = 2 * self.pos_embed_components
        # For now, we do not allow odd sized embeddings.
        # if self.embed_dim % num_components != 0:
        #     raise ValueError(
        #         f'embed_dim has to be divisible by {num_components}')
        self.feature_size = self.embed_dim // self.pos_embed_components

    def attention(
        self,
        q: Tensor,
        k: Tensor,
        v: Tensor,
        attn_bias: Optional[Tensor] = None,
        attn_mask: Optional[Tensor] = None,
    ) -> Tuple[Tensor, Tensor]:
        r"""
        Computes scaled dot product attention on query, key and value tensors, using
        an optional attention mask if passed, and applying dropout if a probability
        greater than 0.0 is specified.
        Returns a tensor pair containing attended values and attention weights.
        Args:
            q, k, v: query, key and value tensors. See Shape section for shape details.
            attn_mask: optional tensor containing mask values to be added to calculated
                attention. May be 2D or 3D; see Shape section for details.
            attn_bias: optional tensor containing bias values to be added to calculated
                attention. Used for relative positional embedding. May be 2D or 3D; see
                Shape section for details.
        Shape:
            - q: :math:`(B, Nt, E)` where B is batch size, Nt is the target sequence length,
                and E is embedding dimension.
            - key: :math:`(B, Ns, E)` where B is batch size, Ns is the source sequence length,
                and E is embedding dimension.
            - value: :math:`(B, Ns, E)` where B is batch size, Ns is the source sequence length,
                and E is embedding dimension.
            - attn_bias: either a 3D tensor of shape :math:`(B, Nt, Ns)` or a 2D tensor of
                shape :math:`(Nt, Ns)`.
            - attn_mask: either a 3D tensor of shape :math:`(B, Nt, Ns)` or a 2D tensor of
                shape :math:`(Nt, Ns)`.
            - Output: attention values have shape :math:`(B, Nt, E)`; attention weights
                have shape :math:`(B, Nt, Ns)`
        """
        q *= self.scaling

        bsz, seq_len, _ = q.shape
        bsz = bsz // self.num_heads
        pe_index = torch.arange(q.shape[1]).long().cuda()
        pos_embed = self.positional_features_all(positions=pe_index, seq_length=seq_len)
        pos_embed = self.pos_embed_dropout(pos_embed)
        pos_embed = (
            self.pos_embed(pos_embed)
            .expand(bsz, -1, -1)
            .reshape(bsz * self.num_heads, seq_len, self.head_dim)
        )

        # (B, Nt, E) x (B, E, Ns) -> (B, Nt, Ns)
        content_logits = (q + self.content_bias.repeat(bsz, seq_len, 1)) @ k.transpose(
            -2, -1
        )
        pos_embed_logits = (
            q + self.pos_embed_bias.repeat(bsz, seq_len, 1)
        ) @ pos_embed.transpose(-2, -1)
        attn = content_logits + pos_embed_logits

        if attn_bias is not None:
            attn += attn_bias
        if attn_mask is not None:
            attn += attn_mask
        attn = F.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        # (B, Nt, Ns) x (B, Ns, E) -> (B, Nt, E)
        output = torch.bmm(attn, v)
        return output, attn

    def positional_features_all(
        self, positions: Tensor, seq_length: Optional[int] = 500
    ):
        """Compute relative positional encodings/features.
        Each positional feature function will compute/provide the same fraction of
        features, making up the total of embed_dim.
        Args:
            positions: Tensor of relative positions of arbitrary shape.
            seq_length: Sequence length denoting the characteristic length that
            the individual positional features can use. This is required since the
            parametrization of the input features should be independent of `positions`
            while it could still require to use the total number of features.
        Returns:
            Tensor of shape: `positions.shape + (self.embed_dim,)`.
        """
        embeddings = torch.cat(
            [
                getattr(self, f)(positions.abs(), seq_length=seq_length)
                for f in self.pos_embed_functions
            ],
            axis=-1,
        )
        if not self.pos_embed_symmetric:
            embeddings = torch.cat(
                [embeddings, positions.sign()[..., None] * embeddings], axis=-1
            )

        return embeddings

    @staticmethod
    def _prepend_dims(x, num_dims):
        return x.view([1] * num_dims + list(x.shape))

    @staticmethod
    def gamma_pdf(x, concentration, rate):
        """Gamma probability distribution function: p(x|concentration, rate)."""
        log_unnormalized_prob = torch.xlogy(concentration - 1.0, x) - rate * x
        log_normalization = torch.lgamma(concentration) - concentration * torch.log(
            rate
        )
        return torch.exp(log_unnormalized_prob - log_normalization)

    def positional_features_exponential(
        self,
        positions: Tensor,
        seq_length: Optional[int] = None,
        min_half_life: Optional[float] = 3.0,
        **kwargs: Optional[Dict[str, Any]]
    ):
        """Create exponentially decaying positional weights.
        Args:
            positions: Position tensor (arbitrary shape).
            seq_length: Sequence length.
            min_half_life: Smallest exponential half life in the grid of half lives.
        Returns:
            A Tensor with shape [2 * seq_length - 1, self.feature_size].
        """
        if seq_length is None:
            seq_length = torch.max(positions.abs()) + 1
        # Grid of half lifes from [3, seq_length / 2] with self.feature_size
        # distributed on the log scale.
        max_range = math.log(seq_length) / math.log(2.0)
        # [TODO]: self.feature_size = 1 is atemp solution to match dim
        half_life = torch.pow(
            2.0, torch.linspace(min_half_life, max_range, self.feature_size + 1)
        ).cuda()
        half_life = self._prepend_dims(half_life, len(positions.shape))
        positions = positions.abs()
        outputs = torch.exp(-math.log(2.0) / half_life * positions[..., None])
        return outputs

    def positional_features_central_mask(
        self, positions: Tensor, **kwargs: Optional[Dict[str, Any]]
    ):
        """Positional features using a central mask (allow only central features)."""
        center_widths = torch.pow(
            2.0,
            torch.arange(
                self.feature_size, dtype=torch.float32, device=positions.device
            )
            + 1,
        )
        center_widths = center_widths - 1
        center_widths = self._prepend_dims(center_widths, len(positions.shape))
        outputs = (center_widths > positions.abs()[..., None]).float()
        return outputs

    def positional_features_gamma(
        self,
        positions: Tensor,
        seq_length: Optional[int] = None,
        stddev=None,
        start_mean=None,
        **kwargs: Optional[Dict[str, Any]]
    ):
        """Positional features computed using the gamma distributions."""
        if seq_length is None:
            seq_length = torch.max(positions.abs()) + 1
        if stddev is None:
            stddev = seq_length / (2 * self.feature_size)
        if start_mean is None:
            start_mean = seq_length / self.feature_size
        mean = torch.linspace(
            start_mean, seq_length, self.feature_size, device=positions.device
        )
        mean = self._prepend_dims(mean, len(positions.shape))
        concentration = (mean / stddev) ** 2
        rate = mean / stddev**2
        probabilities = self.gamma_pdf(
            positions.abs().float()[..., None], concentration, rate
        )
        probabilities += 1e-8  # To ensure numerical stability.
        outputs = probabilities / torch.max(probabilities)
        return outputs

    def positional_features_cosine(
        self, positions: Tensor, **kwargs: Optional[Dict[str, Any]]
    ):
        """Cosine positional features."""
        periodicity = 1.25 * torch.pow(
            2.0,
            torch.arange(
                self.feature_size, dtype=torch.float32, device=positions.device
            ),
        )
        periodicity = self._prepend_dims(periodicity, len(positions.shape))

        outputs = torch.cos(2 * math.pi * positions[..., None] / periodicity)
        return outputs

    def positional_features_linear_masks(
        self, positions: Tensor, **kwargs: Optional[Dict[str, Any]]
    ):
        """Exponentially increasing point focuses."""
        distances = torch.arange(
            self.feature_size, dtype=torch.float32, device=positions.device
        )
        distances = self._prepend_dims(distances, len(positions.shape))
        outputs = (distances == torch.abs(positions[..., None])).float()

        return outputs

    def positional_features_sin_cos(
        self,
        positions: Tensor,
        max_time: Optional[int] = 10000.0,
        **kwargs: Optional[Dict[str, Any]]
    ):
        """Sine/cosine positional encodings."""
        # [TODO]: self.feature_size = 1 is atemp solution to match dim
        # if self.feature_size % 2 != 0:
        #     raise ValueError('self.feature_size needs to be divisible by 2.')
        i = torch.arange(
            0, self.feature_size + 1, 2, dtype=torch.float32, device=positions.device
        )
        i = self._prepend_dims(i, len(positions.shape))

        # Concat sines and cosines and return.
        outputs = torch.cat(
            [
                torch.sin(
                    positions[..., None] / max_time ** (i / self.feature_size + 1)
                ),
                torch.cos(
                    positions[..., None] / max_time ** (i / self.feature_size + 1)
                ),
            ],
            -1,
        )

        return outputs
