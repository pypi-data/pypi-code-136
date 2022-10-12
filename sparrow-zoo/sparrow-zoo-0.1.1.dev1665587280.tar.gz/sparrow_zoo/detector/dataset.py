import torch


def detector_collate_fn(
    samples: list[dict[str, torch.Tensor]]
) -> tuple[torch.Tensor, list[dict[str, torch.Tensor]]]:
    """
    Collate samples for a sparrow-zoo detector.

    Parameters
    ----------
    samples
        A list of dicts with "image", "boxes" keys

    Returns
    -------
    images, targets
        A tuple with a batch of images and a list of dicts with
        "boxes" and "labels". Each dict in the targets list is
        associated with a single image.
    """
    images: list[torch.Tensor] = []
    targets: list[dict[str, torch.Tensor]] = []
    for sample in samples:
        images.append(sample["image"])
        targets.append({"boxes": sample["boxes"], "labels": sample["labels"]})
    return torch.stack(images), targets
