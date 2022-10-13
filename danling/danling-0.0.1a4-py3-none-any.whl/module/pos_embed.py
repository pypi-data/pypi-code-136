import math
from typing import Optional

import torch
import torch.nn as nn
from torch import Tensor


# this is from T5
def relative_position_bucket(
    seq_max_len: int,
    bidirectional: Optional[bool] = True,
    num_buckets: Optional[int] = 32,
    max_distance: Optional[int] = 128,
):
    context_position = torch.arange(seq_max_len, dtype=torch.long)[:, None]
    memory_position = torch.arange(seq_max_len, dtype=torch.long)[None, :]
    relative_position = memory_position - context_position
    ret = 0
    n = -relative_position
    if bidirectional:
        num_buckets //= 2
        ret = (n < 0).long() * num_buckets  # mtf.to_int32(mtf.less(n, 0)) * num_buckets
        n = torch.abs(n)
    else:
        n = torch.max(n, torch.zeros_like(n))
    # now n is in the range [0, inf)

    # half of the buckets are for exact increments in positions
    max_exact = num_buckets // 2
    is_small = n < max_exact

    # The other half of the buckets are for logarithmically bigger bins in positions up to max_distance
    val_if_large = (
        max_exact
        + (
            torch.log(n.float() / max_exact)
            / math.log(max_distance / max_exact)
            * (num_buckets - max_exact)
        ).long()
    )
    val_if_large = torch.min(
        val_if_large, torch.full_like(val_if_large, num_buckets - 1)
    )

    ret += torch.where(is_small, n, val_if_large)
    return nn.Parameter(ret, requires_grad=False)


# this is from TUPE
class PositionEmbedding(nn.Module):
    def __init__(
        self,
        token_size: int,
        num_heads: int,
        has_cls_token: bool,
        seq_max_len: int,
        rel_pos_embed: Optional[bool] = False,
        rel_pos_embed_buckets: Optional[int] = 32,
        rel_pos_embed_max: Optional[int] = 128,
        pos_embed_dropout: Optional[float] = 0.0,
        pos_scale_factor: Optional[int] = 1,
    ) -> None:
        super().__init__()
        self.token_size = token_size
        self.num_heads = num_heads
        self.seq_max_len = seq_max_len
        self.has_cls_token = has_cls_token
        self.dropout = nn.Dropout(pos_embed_dropout)
        if self.has_cls_token:
            # make room for [CLS]-to-others and others-to-[CLS]
            self.seq_max_len += 2
        self.abs_pos_embed = nn.Parameter(
            torch.randn(self.seq_max_len, self.token_size)
        )
        self.ln = nn.LayerNorm(self.token_size)
        self.in_proj = nn.Linear(self.token_size, self.token_size * 2)
        self.scaling = (token_size / num_heads * pos_scale_factor) ** -0.5

        self.rel_pos_embed = rel_pos_embed
        if self.rel_pos_embed:
            assert rel_pos_embed_buckets % 2 == 0
            self.rel_pos_embed_buckets = rel_pos_embed_buckets
            self.rel_pos_embed_max = rel_pos_embed_max
            self.rel_pos_embed = nn.Embedding(
                self.rel_pos_embed_buckets + 1, self.num_heads
            )
            self.rel_pos_embed_bucket = relative_position_bucket(
                seq_max_len=self.seq_max_len,
                num_buckets=self.rel_pos_embed_buckets,
                max_distance=self.rel_pos_embed_max,
            )

    def forward(self, src: Tensor, cls_token_index: Optional[Tensor] = None) -> Tensor:
        B, N, C = src.shape
        # 0 is for others-to-[CLS] 1 is for [CLS]-to-others
        # Assume the input is ordered. If your input token is permuted, you may need to update this accordingly
        if self.has_cls_token:
            # only plus 1 here since because [CLS] already plused 1
            N += 1
        weight = self.ln(self.abs_pos_embed[:N, :])
        q, k = (
            self.in_proj(weight)
            .reshape(N, 2, self.num_heads, C // self.num_heads)
            .permute(1, 2, 0, 3)
        )
        q = q * self.scaling
        pos_embed = torch.bmm(q, k.transpose(1, 2))
        if self.has_cls_token:
            # p_0 \dot p_0 is [CLS]-to-others
            cls_2_others = pos_embed[:, 0, 0]
            # p_1 \dot p_1 is others-to-[CLS]
            others_2_cls = pos_embed[:, 1, 1]
            # offset
            pos_embed = pos_embed[:, 1:, 1:]
            # if [CLS] is not the first token
            if cls_token_index is not None:
                pos_embed = pos_embed.repeat(B, 1, 1, 1)
                pos_embed[torch.arange(B), :, cls_token_index, :] = cls_2_others.expand(
                    B, -1
                ).unsqueeze(-1)
                pos_embed[torch.arange(B), :, :, cls_token_index] = others_2_cls.expand(
                    B, -1
                ).unsqueeze(-1)
            else:
                pos_embed[:, 0, :] = cls_2_others.unsqueeze(-1)
                pos_embed[:, :, 0] = others_2_cls.unsqueeze(-1)
            N -= 1
        rel_pos_embed = torch.zeros_like(pos_embed)
        if self.rel_pos_embed:
            rel_pos_embed_bucket = self.rel_pos_embed_bucket[:N, :N]
            if self.has_cls_token:
                if cls_token_index is not None:
                    rel_pos_embed_bucket = rel_pos_embed_bucket.repeat(B, 1, 1)
                    rel_pos_embed_bucket[torch.arange(B), cls_token_index, :] = (
                        self.rel_pos_embed_buckets // 2
                    )
                    rel_pos_embed_bucket[
                        torch.arange(B), :, cls_token_index
                    ] = self.rel_pos_embed_buckets
                    rel_pos_embed = self.rel_pos_embed(rel_pos_embed_bucket).permute(
                        0, 3, 1, 2
                    )
                else:
                    rel_pos_embed_bucket[0, :] = self.rel_pos_embed_buckets // 2
                    rel_pos_embed_bucket[:, 0] = self.rel_pos_embed_buckets
                    rel_pos_embed = self.rel_pos_embed(rel_pos_embed_bucket).permute(
                        2, 0, 1
                    )
            else:
                rel_pos_embed = self.rel_pos_embed(rel_pos_embed_bucket).permute(
                    2, 0, 1
                )
            pos_embed += rel_pos_embed

        pos_embed = (
            pos_embed.view(-1, *pos_embed.shape[2:])
            if cls_token_index is not None
            else pos_embed.repeat(B, 1, 1)
        )
        return self.dropout(pos_embed)
