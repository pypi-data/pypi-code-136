import pickle
import os
import numpy as np
import cv2
import warnings
import tensorflow as tf

warnings.filterwarnings("ignore")
import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageDraw
import glob


def start_canny(image_path, is_save=True, save_path="../segmentation/map.jpg"):
    img = cv2.imread(image_path, 0)
    img = cv2.GaussianBlur(img, (3, 3), 0)

    v = np.median(img)
    # apply automatic Canny edge detection using the computed median
    sigma = 0.33
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    result_image = cv2.Canny(image=img, threshold1=lower, threshold2=upper)

    if is_save:
        cv2.imwrite(save_path, result_image)
    else:
        return result_image

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def start_add_mask(map_path, masks_path, treshold=0.8, colors=[(252, 66, 123),  # 'RO'
                                                              (192, 57, 43),  # 'RO sq'
                                                              (52, 152, 219),  # 'CT':
                                                              (52, 152, 219),  # 'CT sq
                                                              (52, 152, 219),  # 'CT vent
                                                              (39, 174, 96),  # 'Switch
                                                              (155, 89, 182),  # 'WPS'
                                                              (252, 66, 123),  # 'Turb'
                                                              (155, 89, 182),  # 'Spill'
                                                              (58, 53, 117),  # ER'
                                                              (255, 221, 89)]  # 'Parking'
                   ):
    masks = os.listdir(masks_path)

    for mask_path in masks:
        map = cv2.imread(map_path)
        map_shape = map.shape
        mask_name_list = mask_path.split(" ")
        cls = int(mask_name_list[2])
        score = mask_name_list[7].split('.')
        score = float(score[0] + "." + score[1])

        print("Cls {0:d} score {1:f}".format(cls, score))

        if score > treshold:
            fill = np.zeros((map_shape[0], map_shape[1], 3), np.uint8)
            fill[:] = colors[cls]

            mask = cv2.imread(os.path.join(masks_path,mask_path))

            mask = cv2.resize(mask, fill.shape[1::-1])

            dst = cv2.bitwise_and(fill, mask)

            dst = cv2.bitwise_or(map, dst)

            cv2.imwrite(map_path, dst)

    map = cv2.imread(map_path)
    map = cv2.cvtColor(map, cv2.COLOR_BGR2RGB)
    cv2.imwrite(map_path, map)

if __name__ == "__main__":
    map_path = "D:\python\object_detector\pyqt_sns\segmentation/4.jpg"
    # start_canny(map_path)
    mask_path = "D:\python\object_detector\pyqt_sns\detection\Mask-R-CNN-R101\masks/"
    fill_path = "D:\python\object_detector\pyqt_sns\segmentation/fill.jpg"
    start_add_mask(map_path, mask_path)
