import os

import shutil
import pytest

from pathlib import Path, PosixPath
from typing import Any, Optional, Tuple, Union, Dict

import numpy as np
import tensorflow as tf
import torch
from tensorflow.keras.layers import Dense

from cinnaroll_internal.constants import KERAS, PYTORCH, TENSORFLOW, VALID_FRAMEWORKS
from cinnaroll_internal.model import (
    MODEL_SAVE_PATH,
    create_model,
    ModelInputSampleError,
)


class MyDense(tf.Module):  # type: ignore
    """A dense unit initialised with randomised weights and ReLU activation function."""

    def __init__(self, input_dim: int, output_size: int, name: Optional[str] = None):
        super().__init__(name=name)
        self.w = tf.Variable(
            tf.random.normal([input_dim, output_size], dtype=tf.dtypes.float64),
            name=f"{name}.w",
        )
        self.b = tf.Variable(
            tf.random.normal([output_size], dtype=tf.dtypes.float64), name=f"{name}.b"
        )

    def __call__(self, x: tf.Tensor) -> tf.Tensor:
        y = tf.matmul(x, self.w) + self.b
        return tf.nn.relu(y)


class TensorFlowSimpleModel(tf.Module):  # type: ignore
    def __init__(
        self, input_dim: int, dense_layers: Tuple[int, int], name: Optional[str] = None
    ):
        super().__init__(name=name)
        self.dense_1 = MyDense(input_dim, dense_layers[0], name="layer1")
        self.dense_2 = MyDense(dense_layers[0], dense_layers[1], name="layer2")

    @tf.function  # type: ignore
    def __call__(self, x: tf.Tensor) -> tf.Tensor:
        x = tf.nn.relu(self.dense_1(x))
        return self.dense_2(x)

    @staticmethod
    def _MSEloss(y: tf.Tensor, y_pred: tf.Tensor) -> tf.Tensor:
        return tf.reduce_mean(tf.square(y - y_pred))

    def perform_training(
        self,
        X: np.ndarray,  # type: ignore
        Y: np.ndarray,  # type: ignore
        num_epochs: int = 10,
        learning_rate: float = 1e-3,
    ) -> None:
        for epoch in range(num_epochs):
            with tf.GradientTape(persistent=True) as t:
                current_loss = self._MSEloss(self(X), Y)

            print(f"Epoch {epoch + 1}, loss: {current_loss}")

            for layer in (self.dense_1, self.dense_2):
                for x in ("w", "b"):
                    attr = getattr(layer, x)
                    grad = t.gradient(current_loss, attr)
                    attr.assign_sub(learning_rate * grad)


class PyTorchSimpleModel(torch.nn.Module):  # type: ignore
    """A class representing a simple dense neural network in PyTorch."""

    def __init__(self, input_dim: int, dense_layers: Tuple[int, int]):
        super().__init__()
        self.fc1 = torch.nn.Linear(input_dim, dense_layers[0])
        self.fc2 = torch.nn.Linear(dense_layers[0], dense_layers[1])
        self.criterion = torch.nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.parameters(), lr=0.01)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = torch.nn.functional.relu(self.fc1(x))
        return self.fc2(x).squeeze(1)

    def perform_training(
        self, X: torch.Tensor, Y: torch.Tensor, num_epochs: int
    ) -> None:
        for epoch in range(num_epochs):
            # zero the parameter gradients
            self.optimizer.zero_grad()

            # forward + backward + optimize
            outputs = self.forward(X)
            loss = self.criterion(outputs, Y)
            print(f"Epoch: {epoch + 1}, loss: {loss.item():.4f}")
            loss.backward()
            self.optimizer.step()


def create_model_object(
    framework: str,
    input_dim: int,
    dense_layers: Tuple[int, int],
    weights: Optional[Dict[str, np.ndarray]] = None,  # type: ignore
) -> Any:
    """Create a dense neural network model_object. Optionally set weights of the newly created model."""
    assert framework in VALID_FRAMEWORKS

    if framework == KERAS:
        model_object = tf.keras.models.Sequential(
            [
                Dense(dense_layers[0], input_shape=(input_dim,), activation="relu"),
                Dense(dense_layers[1], activation=None),
            ]
        )
        model_object.compile(
            loss=tf.keras.losses.MeanSquaredError(),
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
        )

        if weights is not None:
            for j in range(2):
                model_object.layers[j].set_weights(
                    [weights[f"lay{j+1}.w"], weights[f"lay{j+1}.b"]]
                )

    elif framework == TENSORFLOW:
        model_object = TensorFlowSimpleModel(input_dim, dense_layers)

        if weights is not None:
            for j in range(1, 3):
                for var in ("w", "b"):
                    setattr(
                        getattr(model_object, f"dense_{j}"),
                        var,
                        weights[f"lay{j}.{var}"],
                    )

    elif framework == PYTORCH:
        model_object = PyTorchSimpleModel(input_dim, dense_layers)

        if weights is not None:
            for j in range(1, 3):
                model_object.state_dict()[f"fc{j}.weight"].data[:, :] = torch.Tensor(
                    weights[f"lay{j}.w"].T
                )
                model_object.state_dict()[f"fc{j}.bias"].data[:] = torch.Tensor(
                    weights[f"lay{j}.b"]
                )

    return model_object


def check_model_object(framework: str, model_object: Any, input_dim: int) -> None:
    """Check that model_object can be trained and can executed to make predictions."""
    assert framework in VALID_FRAMEWORKS

    num_samples = np.random.randint(10, 20)
    num_epochs = np.random.randint(10, 20)

    X, Y = generate_random_data(num_samples, input_dim)

    print("\n-- training")
    if framework == KERAS:
        model_object.fit(X, Y, epochs=num_epochs)
    elif framework == TENSORFLOW:
        model_object.perform_training(X, Y, num_epochs=num_epochs)
    elif framework == PYTORCH:
        model_object.perform_training(torch.Tensor(X), torch.Tensor(Y), num_epochs=10)

    print("\n-- making predictions")
    if framework == KERAS:
        print(model_object.predict(X))
    elif framework == TENSORFLOW:
        print(model_object(X))
    elif framework == PYTORCH:
        print(model_object.forward(torch.Tensor(X)))


def generate_random_data(
    num_samples: int, num_features: int
) -> Tuple[np.ndarray, np.ndarray]:  # type: ignore
    """Generate random data of specified dimension. Returns numpy.arrays."""
    X = np.random.rand(num_samples, num_features)
    Y = np.random.rand(num_samples)

    return X, Y


def clean(path: Union[Path, PosixPath]) -> None:
    """If a file or directory exists, remove it."""
    if path.exists():
        if path.is_file():
            os.remove(path)
        elif path.is_dir():
            shutil.rmtree(path)
        else:
            raise RuntimeWarning(f"Unknown object: {path}")


class TestSimpleNNModels:
    @pytest.mark.parametrize("framework", VALID_FRAMEWORKS)
    def test_model_object_creation(self, framework: str) -> None:
        """Test creating model_objects in all the frameworks and check their validity."""

        num_features = np.random.randint(5, 15)
        dense_layers = (np.random.randint(3, 10), 1)

        print(f"\nChecking {framework} model_object")
        model_object = create_model_object(
            framework, input_dim=num_features, dense_layers=dense_layers
        )
        check_model_object(framework, model_object, num_features)

    @pytest.mark.parametrize("framework", VALID_FRAMEWORKS)
    def test_cinnaroll_model_should_be_loaded(self, framework: str) -> None:
        num_features = np.random.randint(5, 15)
        dense_layers = (np.random.randint(3, 10), 1)

        print(f"\nTesting framework: {framework}")
        clean(MODEL_SAVE_PATH)
        model_object = create_model_object(
            framework, input_dim=num_features, dense_layers=dense_layers
        )

        print("Create a fresh model_object and save it")

        if framework == KERAS:
            model_object.save(MODEL_SAVE_PATH)
        elif framework == TENSORFLOW:
            tf.saved_model.save(
                model_object,
                MODEL_SAVE_PATH,
                signatures=model_object.__call__.get_concrete_function(
                    tf.TensorSpec([None, num_features], tf.float64)
                ),
            )
        elif framework == PYTORCH:
            torch.save(model_object, MODEL_SAVE_PATH)

        cinnaroll_model = create_model(model_object, framework)

        print(f"Should be loaded? {cinnaroll_model.should_be_loaded()}")
        assert (
            cinnaroll_model.should_be_loaded()
        ), "Saved model is compatible and should be loaded, but should_be_loaded() returned False."

        clean(MODEL_SAVE_PATH)

        print("Create a different model_object without saving")
        model_object = create_model_object(
            framework, input_dim=num_features + 1, dense_layers=dense_layers
        )
        cinnaroll_model = create_model(model_object, framework)
        print(f"Should be loaded? {cinnaroll_model.should_be_loaded()}")
        assert (
            not cinnaroll_model.should_be_loaded()
        ), "Saved model is not compatible and should not be loaded, but should_be_loaded() returned True."

    @pytest.mark.parametrize("framework", VALID_FRAMEWORKS)
    @pytest.mark.parametrize(
        "extra_features,expectation",
        [(0, None), (1, ModelInputSampleError)],
    )
    def test_cinnaroll_model_find_model_input_sample_error(
        self, framework: str, extra_features: int, expectation: Any
    ) -> None:
        num_features = np.random.randint(5, 15)
        dense_layers = (np.random.randint(3, 10), 1)

        X = generate_random_data(
            np.random.randint(3, 10), num_features + extra_features
        )[0]

        print(f"\nTesting framework: {framework}")
        print("Create a fresh model_object")
        model_object = create_model_object(
            framework, input_dim=num_features, dense_layers=dense_layers
        )

        cinnaroll_model = create_model(model_object, framework)

        out = cinnaroll_model.find_model_input_sample_error(X)

        if expectation is None:
            assert out is None
        else:
            assert isinstance(out, expectation)

    @pytest.mark.parametrize("framework", VALID_FRAMEWORKS)
    def test_cinnaroll_save_load(self, framework: str) -> None:
        """Generate a random simple NN model and save it. Then, load it and check that predictions on random data are consistent."""
        clean(MODEL_SAVE_PATH)
        # generate random model parameters
        num_features = np.random.randint(5, 15)
        dense_layers = (np.random.randint(3, 10), 1)

        # generate random input
        num_samples = np.random.randint(10, 20)
        X = np.random.rand(num_samples, num_features)

        print(f"\nTesting framework: {framework}")
        model_object = create_model_object(
            framework, input_dim=num_features, dense_layers=dense_layers
        )
        cinnaroll_model = create_model(model_object, framework)
        cinnaroll_model.save()

        if framework == KERAS:
            Y = model_object.predict(X).reshape(-1)
        elif framework == TENSORFLOW:
            Y = model_object(X).numpy().reshape(-1)
        elif framework == PYTORCH:
            with torch.no_grad():
                Y = model_object(torch.Tensor(X)).numpy()

        new_cinnaroll_model = create_model(None, framework)
        new_cinnaroll_model.load()

        if framework == KERAS:
            Y2 = model_object.predict(X).reshape(-1)
        elif framework == TENSORFLOW:
            Y2 = model_object(X).numpy().reshape(-1)
        elif framework == PYTORCH:
            with torch.no_grad():
                Y2 = model_object(torch.Tensor(X)).numpy()

        # verify that the results are the same
        np.testing.assert_allclose(Y, Y2, rtol=1e-6)  # type: ignore
