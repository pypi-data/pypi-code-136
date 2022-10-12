from ..base import SparrowModel


class SparrowDetector(SparrowModel):
    """Sparrow object detection model."""

    output_names: tuple[str, str, str] = ("boxes", "scores", "labels")
