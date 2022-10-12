import torch


def decode_box_offsets(
    box_offsets: torch.Tensor, anchors: torch.Tensor
) -> torch.Tensor:
    anchors_center_x = 0.5 * (anchors[:, 0] + anchors[:, 2])
    anchors_center_y = 0.5 * (anchors[:, 1] + anchors[:, 3])
    anchors_w = anchors[:, 2] - anchors[:, 0]
    anchors_h = anchors[:, 3] - anchors[:, 1]
    anchors_scale = torch.stack((anchors_w, anchors_h, anchors_w, anchors_h), dim=1)
    box_offsets = box_offsets * anchors_scale
    boxes1 = anchors_center_x - box_offsets[..., 0]
    boxes2 = anchors_center_y - box_offsets[..., 1]
    boxes3 = anchors_center_x + box_offsets[..., 2]
    boxes4 = anchors_center_y + box_offsets[..., 3]
    boxes = torch.stack((boxes1, boxes2, boxes3, boxes4), dim=-1)
    return boxes
