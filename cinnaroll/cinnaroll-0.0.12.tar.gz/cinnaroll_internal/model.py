import abc
import importlib
import os
from pathlib import Path
from typing import Any, Callable, Dict, Tuple, Optional

import tensorflow as tf
import torch

from cinnaroll_internal import utils
from cinnaroll_internal.constants import (
    KERAS,
    KERAS_PACKAGE_NAME,
    TENSORFLOW,
    TENSORFLOW_PACKAGE_NAME,
    PYTORCH,
    PYTORCH_PACKAGE_NAME,
    UNKNOWN_FRAMEWORK,
)


class ModelLoadingError(Exception):
    ...


class ModelSavingError(Exception):
    ...


class ModelInputSampleError(Exception):
    ...


# where to save the model
# todo: e2es on real filesystem to check multiplatform compatibility
MODEL_SAVE_PATH = Path(os.getcwd()) / "saved_model"


# container for framework-specific logic for saving and loading model and for running model's prediction method
class CinnarollModel(abc.ABC):
    def __init__(self, model_object: Any, framework_package_name: str):
        self.model_object = model_object
        self.framework_package = importlib.import_module(framework_package_name)

    @abc.abstractmethod
    def save(self) -> None:
        """
        throws a ModelSavingError if something fails
        """
        pass

    @abc.abstractmethod
    def load(self) -> None:
        """
        throws a ModelLoadingError if something fails
        """

    @abc.abstractmethod
    def find_model_input_sample_error(self, input_sample: Any) -> Optional[Exception]:
        """
        test if passing model_input_sample to model_object's prediction function
        (eg. model_object.predict(input) in Keras or model_object(input) in PyTorch
        doesn't raise any errors
        return if everything is ok, raise ModelInputSampleError otherwise
        """
        pass

    @abc.abstractmethod
    def get_metadata(self) -> Any:
        pass

    @abc.abstractmethod
    def should_be_loaded(self) -> bool:
        """when both of these are true:
        1. there’s a saved model on disk
        2. saved model’s metadata are the same as model_object’s
        """
        pass


# https://www.tensorflow.org/guide/keras/save_and_serialize
class CinnarollKerasModel(CinnarollModel):
    def save(self) -> None:
        try:
            self.model_object.save(MODEL_SAVE_PATH)
        except Exception as e:
            raise ModelSavingError(f"Could not save model: {repr(e)}")

    def load(self) -> None:
        try:
            self.model_object = tf.keras.models.load_model(MODEL_SAVE_PATH)
        except Exception as e:
            raise ModelLoadingError(f"Could not load model: {repr(e)}")

    def find_model_input_sample_error(self, input_sample: Any) -> Optional[Exception]:
        try:
            self.model_object.predict(input_sample)
        except ValueError as e:
            return ModelInputSampleError(
                f"Provided input_sample is not a valid input to the model.\n{repr(e)}"
            )

        return None

    def should_be_loaded(self) -> bool:
        if MODEL_SAVE_PATH.exists():
            try:
                saved_model = tf.keras.models.load_model(MODEL_SAVE_PATH)
            except Exception as e:
                raise ModelLoadingError(
                    f"Error occurred while trying to load model from {MODEL_SAVE_PATH}: {repr(e)}"
                )
            return bool(saved_model.to_json() == self.model_object.to_json())
        else:
            return False

    def get_metadata(self) -> Any:
        pass


# https://www.tensorflow.org/guide/saved_model
class CinnarollTensorflowModel(CinnarollModel):
    def save(self) -> None:
        try:
            tf.saved_model.save(
                self.model_object,
                MODEL_SAVE_PATH,
                signatures=self.model_object.__call__.get_concrete_function(
                    tf.TensorSpec(None, tf.float64)
                ),
            )
        except Exception as e:
            raise ModelSavingError(f"Could not save model: {repr(e)}")

    def load(self) -> None:
        try:
            self.model_object = tf.saved_model.load(MODEL_SAVE_PATH)
        except Exception as e:
            raise ModelLoadingError(f"Could not load model: {repr(e)}")

    def find_model_input_sample_error(self, input_sample: Any) -> Optional[Exception]:
        try:
            self.model_object(input_sample)
        except ValueError as e:
            return ModelInputSampleError(
                f"Provided input_sample is not a valid input to the model.\n{repr(e)}"
            )

        return None

    def should_be_loaded(self) -> bool:
        def _model_to_dict(model_object: Any) -> Dict[str, Tuple[Any, Any]]:
            """Converts a model into a dictionary where keys are labels of layers and values contain shape and type."""
            return {x.name: (x.shape, x.dtype) for x in model_object.variables}

        if MODEL_SAVE_PATH.exists():
            try:
                saved_model = tf.saved_model.load(MODEL_SAVE_PATH)
            except Exception as e:
                raise ModelLoadingError(
                    f"Error occurred while trying to load model from {MODEL_SAVE_PATH}: {repr(e)}"
                )
            return _model_to_dict(
                saved_model.signatures["serving_default"]
            ) == _model_to_dict(self.model_object)
        else:
            return False

    def get_metadata(self) -> Any:
        pass


# https://pytorch.org/tutorials/beginner/saving_loading_models.html
class CinnarollPyTorchModel(CinnarollModel):
    def save(self) -> None:
        try:
            torch.save(self.model_object, MODEL_SAVE_PATH)
        except Exception as e:
            raise ModelSavingError(f"Could not save model: {repr(e)}")

    def load(self) -> None:
        try:
            self.model_object = torch.load(MODEL_SAVE_PATH)
        except Exception as e:
            raise ModelLoadingError(f"Could not load model: {repr(e)}")

    def find_model_input_sample_error(self, input_sample: Any) -> Optional[Exception]:
        try:
            self.model_object(torch.Tensor(input_sample))
        except RuntimeError as e:
            return ModelInputSampleError(
                f"Provided input_sample is not a valid input to the model.\n{repr(e)}"
            )

        return None

    def should_be_loaded(self) -> bool:
        def _model_to_dict(model_object: Any) -> Dict[str, torch.Size]:
            """Converts a model into a dictionary where keys are labels of layers and values are shapes."""
            return {k: v.size() for k, v in model_object.state_dict().items()}

        if MODEL_SAVE_PATH.exists():
            try:
                saved_model = torch.load(MODEL_SAVE_PATH)
            except Exception as e:
                raise ModelLoadingError(
                    f"Error occurred while trying to load model from {MODEL_SAVE_PATH}: {repr(e)}"
                )
            return _model_to_dict(saved_model) == _model_to_dict(self.model_object)
        else:
            return False

    def get_metadata(self) -> Any:
        pass


# when train func contains actual code and not just pass or ...
def is_trained_in_script(train_func: Callable[[], None]) -> bool:
    return utils.is_function_implemented(train_func)


# todo: unit test
def infer_framework(model_object: Any) -> str:
    if isinstance(model_object, (tf.keras.models.Sequential, tf.keras.Model)):
        return KERAS
    elif isinstance(model_object, tf.Module):
        return TENSORFLOW
    elif isinstance(model_object, torch.nn.Module):
        return PYTORCH
    else:
        return UNKNOWN_FRAMEWORK


def create_model(model_object: Any, framework: str) -> CinnarollModel:
    if framework == KERAS:
        return CinnarollKerasModel(model_object, KERAS_PACKAGE_NAME)
    elif framework == TENSORFLOW:
        return CinnarollTensorflowModel(model_object, TENSORFLOW_PACKAGE_NAME)
    elif framework == PYTORCH:
        return CinnarollPyTorchModel(model_object, PYTORCH_PACKAGE_NAME)
    else:
        raise NotImplementedError("Unknown machine learning library used.")
