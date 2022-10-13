from pathlib import Path
import numpy as np
import skimage.io as io
import skimage.transform as trans
from skimage import img_as_ubyte


def testGenerator(full_path: Path, target_size: tuple = (256,256)) -> np.ndarray:
    """
    Generator to feed the images to the neural network.

    Args:
        full_path (Path): path to eyeballs/patient/original,
                          where preprocessed png are stored
        target_size (tuple): size of the final image

    Return:
        img (np.ndarray): numpy array of the png image with the desired property
    """
    for filename in full_path.iterdir():
        img = io.imread(str(filename), as_gray = True)
        img = img / 255.
        img = trans.resize(img,target_size)
        img = np.reshape(img,img.shape+(1,))
        img = np.reshape(img,(1,)+img.shape)
        yield img


def saveResult(output_path: Path, npyfile: np.ndarray, list_name: list) -> None:
    """
    Save the results of the model prediction as png in output_path.

    Args:
        output_path (Path): Path to where the png segmentation will be stored
        npyfile (np.ndarray): numpy array of the model prediction
        list_name (list): list containing strings of the desired output filename
    """
    for name in list_name:
        output_path.mkdir(parents=True, exist_ok=True)
        for i, item in enumerate(npyfile):
            if list_name.index(name) == i:
                img = item[:,:,0]
                io.imsave(str(output_path / name), img_as_ubyte(img),
                                                           check_contrast=False)
