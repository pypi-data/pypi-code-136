# Copyright (c) OpenMMLab. All rights reserved.
from typing import Optional

import torch
from mmdet.structures.bbox.transforms import bbox_xyxy_to_cxcywh
from torch import Tensor


def quad2bbox_cxcywh(quad: torch.Tensor):
    """Convert quadrilateral to axis aligned box in [cx, cy, w, h] format.

    Args:
        quad (torch.Tensor): of shape (N, 8), (8, ), (N, 4) or (4, ). The
            coordinates are in [x1, y1, x2, y2, x3, y3, x4, y4] or
            [tl_x, tl_y, br_x, br_y] format.
    Returns:
        torch.Tensor: in [cx, cy, w, h] format.
    """
    if len(quad.shape) == 1:
        quad = quad.unsqueeze(0)
    length = quad.shape[1]
    if length == 8:
        cx = torch.mean(quad[:, 0::2], dim=-1)
        cy = torch.mean(quad[:, 1::2], dim=-1)
        x1 = torch.min(quad[:, 0::2], dim=-1)[0]
        x2 = torch.max(quad[:, 0::2], dim=-1)[0]
        y1 = torch.min(quad[:, 1::2], dim=-1)[0]
        y2 = torch.max(quad[:, 1::2], dim=-1)[0]
        area1 = torch.norm(quad[:, 0:2] - quad[:, 2:4], dim=1) * \
            torch.norm(quad[:, 2:4] - quad[:, 4:6], dim=1)
        area2 = (x2 - x1) * (y2 - y1)
        scale_factor = torch.sqrt(area1 / area2)
        w = scale_factor * (x2 - x1)
        h = scale_factor * (y2 - y1)
        bbox = torch.stack((cx, cy, w, h), dim=-1).squeeze(0)
    elif length == 4:
        bbox = bbox_xyxy_to_cxcywh(quad).squeeze(0)
    else:
        NotImplementedError(f'The length of quadrilateral: {length} is \
                 not supported')
    return bbox


def bbox_cxcywh_to_x1y1wh(bbox: torch.Tensor) -> torch.Tensor:
    """Convert bbox coordinates from (cx, cy, w, h) to (x1, y1, w, h).

    Args:
        bbox (torch.Tensor): Shape (n, 4) or (4, ) for bboxes.

    Returns:
        torch.Tensor: Converted bboxes.
    """
    cx, cy, w, h = bbox.split((1, 1, 1, 1), dim=-1)
    bbox_new = [(cx - 0.5 * w), (cy - 0.5 * h), w, h]
    return torch.cat(bbox_new, dim=-1)


def bbox_xyxy_to_x1y1wh(bbox: torch.Tensor) -> torch.Tensor:
    """Convert bbox coordinates from (x1, y1, x2, y2) to (x1, y1, w, h).

    Args:
        bbox (torch.Tensor): Shape (n, 4) or (4, ) for bboxes.

    Returns:
        torch.Tensor: Converted bboxes.
    """
    x1, y1, x2, y2 = bbox.split((1, 1, 1, 1), dim=-1)
    bbox_new = [x1, y1, (x2 - x1), (y2 - y1)]
    return torch.cat(bbox_new, dim=-1)


def bbox_xyxy_to_cxcyah(bboxes: torch.Tensor) -> torch.Tensor:
    """Convert bbox coordinates from (x1, y1, x2, y2) to (cx, cy, ratio, h).

    Args:
        bbox (Tensor): Shape (n, 4) for bboxes.

    Returns:
        Tensor: Converted bboxes.
    """
    cx = (bboxes[:, 2] + bboxes[:, 0]) / 2
    cy = (bboxes[:, 3] + bboxes[:, 1]) / 2
    w = bboxes[:, 2] - bboxes[:, 0]
    h = bboxes[:, 3] - bboxes[:, 1]
    xyah = torch.stack([cx, cy, w / h, h], -1)
    return xyah


def bbox_cxcyah_to_xyxy(bboxes: torch.Tensor) -> torch.Tensor:
    """Convert bbox coordinates from (cx, cy, ratio, h) to (x1, y1, x2, y2).

    Args:
        bbox (Tensor): Shape (n, 4) for bboxes.

    Returns:
        Tensor: Converted bboxes.
    """
    cx, cy, ratio, h = bboxes.split((1, 1, 1, 1), dim=-1)
    w = ratio * h
    x1y1x2y2 = [cx - w / 2.0, cy - h / 2.0, cx + w / 2.0, cy + h / 2.0]
    return torch.cat(x1y1x2y2, dim=-1)


def bbox_xywh_to_rel_cxcywh(bboxes: Tensor,
                            size_norm: Optional[Tensor] = None) -> Tensor:
    """Convert standard rectangular parametrization of the bounding box.

        [x, y, w, h] to relative parametrization [cx/sw, cy/sh, log(w), log(h)]
        , where [cx, cy] is the center coordinate.

    Args:
        bboxes (Tensor): of shape (N, 4) in [x, y, w, h] format.
        size_norm (Tensor, optional): It contains values of [sw, sh] and it's
            of shape (N, 2).

    Returns:
        Tensor: The converted bbox.
    """

    c = bboxes[..., :2] + 0.5 * bboxes[..., 2:]
    if size_norm is None:
        c_rel = c / bboxes[..., 2:]
    else:
        c_rel = c / size_norm

    sz_rel = torch.log(bboxes[..., 2:])
    return torch.cat((c_rel, sz_rel), dim=-1)


def bbox_rel_cxcywh_to_xywh(bboxes: Tensor,
                            size_norm: Optional[Tensor] = None) -> Tensor:
    """Inverts the effect of `bbox_xywh_to_rel_cxcywh`.

    Args:
        bboxes (Tensor): of shape (N, 4) in [cx/sw, cy/sh, log(w), log(h)]
            format.
        size_norm (Tensor, optional): It contains values of [sw, sh] and it's
            of shape (N, 2).

    Returns:
        Tensor: The converted bbox.
    """

    sz = torch.exp(bboxes[..., 2:])
    if size_norm is None:
        c = bboxes[..., :2] * sz
    else:
        c = bboxes[..., :2] * size_norm
    tl = c - 0.5 * sz
    return torch.cat((tl, sz), dim=-1)
