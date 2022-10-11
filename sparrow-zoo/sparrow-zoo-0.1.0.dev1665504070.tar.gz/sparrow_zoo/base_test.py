import os
import tempfile
from pathlib import Path

import numpy as np
import onnxruntime as ort
import pytest
import torch

from .base import SparrowModel


class FakeModel(SparrowModel):
    output_names: tuple[str] = ("fake",)

    def __init__(self) -> None:
        super().__init__()
        self.fake_intercept = torch.nn.Parameter(torch.randn(1), requires_grad=False)

    def forward(self, x: torch.Tensor) -> dict[str, torch.Tensor]:
        return x + self.fake_intercept


def test_base_model_lazily_requires_output_names():
    model = SparrowModel()
    with pytest.raises(NotImplementedError):
        model.output_names


def test_base_model_lazily_requires_forward():
    model = SparrowModel()
    with pytest.raises(NotImplementedError):
        model(torch.randn(1, 3, 64, 64))


def test_serde_for_fake_model():
    x = torch.randn(10)
    model = FakeModel().eval()
    yhat1 = model(x)
    with tempfile.TemporaryDirectory() as dir:
        path = os.path.join(dir, "model.pth")
        model.save(path)
        model2 = FakeModel().eval()
        model2.load(path)
    yhat2 = model2(x)
    np.testing.assert_equal(yhat1.numpy(), yhat2.numpy())


def test_onnx_export():
    x = torch.randn(10)
    model = FakeModel()
    yhat1 = model(x)
    with tempfile.TemporaryDirectory() as dir:
        path = os.path.join(dir, "model.onnx")
        model.export(path, (10,))
        sess = ort.InferenceSession(path)
        (yhat2,) = sess.run(model.output_names, {"input": x.numpy()})
    np.testing.assert_equal(yhat1.numpy(), yhat2)


@pytest.mark.skipif(os.getenv("FAST") == "1", reason="Skip slow tests")
def test_tensorrt_export():
    model = FakeModel()
    with tempfile.TemporaryDirectory() as dir:
        path = Path(dir) / "fakemodel.engine"
        model.export_tensorrt(path, (10,))
        assert path.exists()
