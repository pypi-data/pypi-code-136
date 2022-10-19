import os
import shutil
from PIL import Image


def replicate(image, destination):
    """
    Copy an image to a designated destination folder
    Args:
        image (str) : path of the image to copy
        destination (str) : directory where the image should be copied
    Returns:
        None
    """
    # Verify image points to a file
    image_abs_path = os.path.abspath(image)
    if os.path.isfile(image_abs_path) != True:
        raise FileNotFoundError("image must point to a valid file")

    # Verify destination points to a folder
    destination_abs_path = os.path.abspath(destination)
    if os.path.isdir(destination_abs_path) != True:
        raise NotADirectoryError("destination must point to a valid directory folder")

    # Verify image does not exist in destination folder
    image_file_name = image.split("/")[-1]
    new_image_path = os.path.join(destination_abs_path, image_file_name)
    if os.path.exists(new_image_path):
        raise FileExistsError(
            "File with name "
            + image_file_name
            + " already exists in "
            + destination
        ) 

    # Open Image
    try:
        img = Image.open(image_abs_path)
    except Exception as e:
        raise ValueError(image + "is not a valid image")

    print("Copying ", image_abs_path, " to ", destination_abs_path)

    # Copy Image to new path
    shutil.copy(image_abs_path, destination_abs_path)

    print(image, "has been successfully replicated in", destination)
