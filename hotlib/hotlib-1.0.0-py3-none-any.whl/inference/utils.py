# Standard library imports
import os
from typing import List

# Third party imports
import numpy as np
from PIL import Image
from tensorflow import keras

IMAGE_SIZE = 256


def open_images(paths: List[str]) -> np.ndarray:
    """Open images from some given paths."""
    images = []
    for path in paths:
        image = keras.preprocessing.image.load_img(
            path, target_size=(IMAGE_SIZE, IMAGE_SIZE)
        )
        image = np.mean(image, axis=-1) / 255.0
        images.append(image)

    return np.array(images)


def save_mask(mask: np.ndarray, filename: str) -> None:
    """Save the mask array to the specified location."""
    reshaped_mask = mask.reshape((IMAGE_SIZE, IMAGE_SIZE)) * 255
    result = Image.fromarray(reshaped_mask.astype(np.uint8))
    result.save(filename)


def get_model(checkpoint_path: str) -> keras.Model:
    """Get keras model from architecture and weights.
    
    Args:
        checkpoint_path: Path where the architecture and weights of the model can be found. 
    """
    architecture_path = os.path.join(checkpoint_path, "model.json")
    with open(architecture_path, "r") as json_file:
        model_architecture = json_file.read()
        model = keras.models.model_from_json(model_architecture)
        weight_path = os.path.join(checkpoint_path, "model.h5")
        model.load_weights(weight_path)

    return model
