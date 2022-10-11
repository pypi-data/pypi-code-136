import os
import tempfile
from pathlib import Path

import numpy as np
import onnxruntime as ort
import pytest
import torch

from .fcos import FCOS


def test_compute_loss():
    x = torch.randn(2, 3, 224, 224)
    model = FCOS(10).train()
    outputs = model(x)
    targets = [
        {
            "boxes": torch.rand((n_boxes, 4)) * 224,
            "labels": torch.randint(0, 10, (n_boxes,)),
        }
        for n_boxes in [5, 7]
    ]
    for loss in model.compute_loss(targets, outputs).values():
        assert loss > 0


def test_onnx_export():
    input_shape = (1, 3, 224, 224)
    x = torch.randn(input_shape)
    model = FCOS(10)
    result = model(x)
    boxes1 = result["boxes"].detach().numpy()
    scores1 = result["scores"].detach().numpy()
    labels1 = result["labels"].detach().numpy()
    with tempfile.TemporaryDirectory() as dir:
        path = os.path.join(dir, "model.onnx")
        model.export(path, input_shape)
        sess = ort.InferenceSession(path)
        (boxes2, scores2, labels2) = sess.run(model.output_names, {"input": x.numpy()})
    assert np.linalg.norm(boxes1 - boxes2) / np.linalg.norm(boxes1) < 0.1
    assert scores1.shape == scores2.shape
    assert labels1.shape == labels2.shape


@pytest.mark.skipif(os.getenv("FAST") == "1", reason="Skip slow tests")
def test_tensorrt_export():
    model = FCOS(10)
    with tempfile.TemporaryDirectory() as dir:
        path = Path(dir) / "fcos.engine"
        model.export_tensorrt(path, (1, 3, 224, 224))
        assert path.exists()
