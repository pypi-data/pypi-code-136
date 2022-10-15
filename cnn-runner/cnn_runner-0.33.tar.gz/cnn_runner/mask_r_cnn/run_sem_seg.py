from detectron2.utils.logger import setup_logger
import os
import cv2
import matplotlib.pyplot as plt
from detectron2.engine import DefaultPredictor
from cnn_runner.utils.my_vizualizer import MyVisualizer
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode, Visualizer, VisImage
from detectron2.data import DatasetCatalog, MetadataCatalog
from tqdm import tqdm
import torch
import numpy as np
import tensorflow as tf
import matplotlib.colors as mplc

setup_logger()

_SMALL_OBJECT_AREA_THRESH = 1000
_LARGE_MASK_AREA_THRESH = 120000
_OFF_WHITE = (1.0, 1.0, 240.0 / 255)
_BLACK = (0, 0, 0)
_RED = (1.0, 0, 0)


# helper function for data visualization
def visualize(**images):
    """
    Plot images in one row
    """
    n_images = len(images)
    plt.figure(figsize=(10, 10))
    for idx, (name, image) in enumerate(images.items()):
        plt.subplot(1, n_images, idx + 1)
        plt.xticks([]);
        plt.yticks([])
        # get title from the parameter names
        plt.title(name.replace('_', ' ').title(), fontsize=20)
        plt.imshow(image)
    plt.show()


# Perform one hot encoding on label
def one_hot_encode(label, label_values):
    """
    Convert a segmentation image label array to one-hot format
    by replacing each pixel value with a vector of length num_classes
    # Arguments
        label: The 2D array segmentation image label
        label_values

    # Returns
        A 2D array with the same width and hieght as the input, but
        with a depth size of num_classes
    """
    semantic_map = []
    for colour in label_values:
        equality = np.equal(label, colour)
        class_map = np.all(equality, axis=-1)
        semantic_map.append(class_map)
    semantic_map = np.stack(semantic_map, axis=-1)
    return semantic_map


# Perform reverse one-hot-encoding on labels / preds
def reverse_one_hot(image):
    """
    Transform a 2D array in one-hot format (depth is num_classes),
    to a 2D array with only 1 channel, where each pixel value is
    the classified class key.
    # Arguments
        image: The one-hot format image

    # Returns
        A 2D array with the same width and hieght as the input, but
        with a depth size of 1, where each pixel value is the classified
        class key.
    """
    x = np.argmax(image, axis=-1)
    return x


# Perform colour coding on the reverse-one-hot outputs
def colour_code_segmentation(image, label_values):
    """
    Given a 1-channel array of class keys, colour code the segmentation results.
    # Arguments
        image: single channel array where each value represents the class key.
        label_values

    # Returns
        Colour coded image for segmentation visualization
    """
    colour_codes = np.array(label_values)
    x = colour_codes[image.astype(int)]

    return x


def make_image(img, selected_labels=None):
    height, width = img.shape[:2]
    color = np.zeros((*(height, width), 3), dtype=np.uint8)

    # ['urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land', 'unknown']
    colors = []
    colors.append([0, 255, 255])  # urban_land
    colors.append([255, 255, 0])  # agriculture_land
    colors.append([255, 0, 255])  # rangeland
    colors.append([0, 255, 0])  # forest_land
    colors.append([0, 0, 255])  # water
    colors.append([255, 255, 255])  # barren_land
    colors.append([0, 0, 0])  # unknown

    if not selected_labels:
        for cls in range(7):
            color[img == cls] = colors[cls]
    else:
        for cls in range(7):
            if cls not in selected_labels:
                color[img == cls] = [0, 0, 0]
            else:
                color[img == cls] = colors[cls]

    color = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

    return color


def draw_text(image,
              text,
              position, color, thickness=None, font_scale=1):
    x, y = position
    # cv2.putText(image, text, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, thickness, cv2.LINE_AA)

    tl = thickness or round(0.0012 * (image.shape[0] + image.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1 = (int(x), int(y))
    tf = max(tl - 1, 1)  # font thickness
    t_size = cv2.getTextSize(text, 0, fontScale=tl / 3, thickness=tf)[0]
    c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
    cv2.rectangle(image, c1, c2, [0,0,0], -1, cv2.LINE_AA)  # filled
    cv2.putText(image, text, (c1[0], c1[1] - 2), cv2.FONT_HERSHEY_COMPLEX, tl / 3, [225, 255, 255], thickness=tf,
                lineType=cv2.LINE_AA,
                )

    return image


def make_image_with_text(img, labels, selected_labels=None, thickness=None, font_scale=None):
    height, width = img.shape[:2]
    if not thickness:
        thickness = max(round(sum(img.shape) / 2 * 0.00001), 2)
    if not font_scale:
        font_scale = max(round(sum(img.shape) / 2 * 0.0001), 1)

    color = np.zeros((*(height, width), 3), dtype=np.uint8)

    # ['urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land', 'unknown']
    colors = []
    colors.append([0, 255, 255])  # urban_land
    colors.append([255, 255, 0])  # agriculture_land
    colors.append([255, 0, 255])  # rangeland
    colors.append([0, 255, 0])  # forest_land
    colors.append([0, 0, 255])  # water
    colors.append([255, 255, 255])  # barren_land
    colors.append([0, 0, 0])  # unknown

    if not selected_labels:
        for cls in range(7):
            color[img == cls] = colors[cls]
    else:
        for cls in range(7):
            if cls not in selected_labels:
                color[img == cls] = [0, 0, 0]
            else:
                color[img == cls] = colors[cls]

    image_output = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

    for cls in range(6):
        binary_mask = np.zeros((*(height, width), 1), dtype=np.uint8)
        binary_mask[img == cls] = 1
        _num_cc, cc_labels, stats, centroids = cv2.connectedComponentsWithStats(binary_mask, 8)
        if stats[1:, -1].size == 0:
            return
        largest_component_id = np.argmax(stats[1:, -1]) + 1

        # draw text on the largest component, as well as other very large components.
        for cid in range(1, _num_cc):
            if cid == largest_component_id or stats[cid, -1] > _LARGE_MASK_AREA_THRESH:
                # median is more stable than centroid
                # center = centroids[largest_component_id]
                center = np.median((cc_labels == cid).nonzero(), axis=1)[::-1]
                # inv_color = colors[cls]
                # for ch in range(len(inv_color)):
                #     inv_color[ch] = 255 - inv_color[ch]
                yellow_color = [255, 255, 255]
                if selected_labels:
                    if cls in selected_labels:
                        draw_text(image_output, labels[cls], center, color=yellow_color, thickness=None,
                                  font_scale=font_scale)
                else:
                    draw_text(image_output, labels[cls], center, color=yellow_color, thickness=None,
                          font_scale=font_scale)

    return image_output


def prediction2color(img, output_path, labels, original_img, selected_labels=None):
    height, width = img.shape[:2]

    color = np.zeros((*(height, width), 3), dtype=np.uint8)

    # ['urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land', 'unknown']
    colors = []
    colors.append([0, 255, 255])  # urban_land
    colors.append([255, 255, 0])  # agriculture_land
    colors.append([255, 0, 255])  # rangeland
    colors.append([0, 255, 0])  # forest_land
    colors.append([0, 0, 255])  # water
    colors.append([255, 255, 255])  # barren_land
    colors.append([0, 0, 0])  # unknown

    if not selected_labels:
        for cls in range(7):
            color[img == labels[cls]] = colors[cls]
    else:
        for cls in range(7):
            if cls not in selected_labels:
                color[img == labels[cls]] = [0, 0, 0]
            else:
                color[img == labels[cls]] = colors[cls]

    color = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

    added_image = cv2.addWeighted(original_img, 0.4, color, 0.6, 0)

    # cv2.imwrite('combined.png', added_image)

    cv2.imwrite(output_path, added_image)

    # v.save(os.path.join(save_path, image_name))


def get_base_img_name(name_with_dir):
    return os.path.basename(name_with_dir)


def detect(image_path, image_name,
           save_path="segmentation",
           config_yaml="mask_config.yml",
           model_tresh=0.7,
           iou_thres=0.5,
           classes=['urban_land', 'agriculture_land', 'rangeland', 'forest_land', 'water', 'barren_land', 'unknown'],
           selected_labels=None,
           model_weigths_path=None):
    from os import listdir
    from os.path import isfile, join

    torch.cuda.empty_cache()

    DatasetCatalog.clear()

    num_of_classes = len(classes)

    aes_metadata = MetadataCatalog.get("sat_data_test/val").set(stuff_classes=classes)
    # MetadataCatalog.get("sat_data_test/val").set(stuff_colors=stuff_colors_set)
    MetadataCatalog.get("sat_data_test/val").set(ignore_label="unknown")

    # Create Model Configuration object
    mrcnn_model = config_yaml

    # Create Model Configuration object
    cfg = get_cfg()

    # Add model architecture config, which we set earlier
    cfg.merge_from_file(mrcnn_model)

    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 512
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = len(classes)
    cfg.MODEL.SEM_SEG_HEAD.NUM_CLASSES = len(classes)
    cfg.MODEL.SEM_SEG_HEAD.IGNORE_VALUE = 255
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = iou_thres
    cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = iou_thres
    cfg.DATASETS.TEST = ("sat_data_test/val")
    cfg.OUTPUT_DIR = "run_train_semseg"

    # Add model architecture config, which we set earlier

    # load weights
    if not model_weigths_path:
        cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    else:
        cfg.MODEL.WEIGHTS = model_weigths_path

    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = model_tresh  # set the testing threshold for this model

    predictor = DefaultPredictor(cfg)

    print("Start detection {0:s}...".format(image_name))
    im = cv2.imread(os.path.join(image_path, image_name))
    outputs = predictor(im)["sem_seg"].to('cpu')
    pred_mask = outputs.numpy().astype(int)

    # pred_mask = pred_mask.detach().squeeze().cpu().numpy()
    # Convert pred_mask from `CHW` format to `HWC` format
    pred_mask = np.transpose(pred_mask, (1, 2, 0))
    # Get prediction channel corresponding to foreground
    # pred_urban_land_heatmap = pred_mask[:, :, select_classes.index('urban_land')]
    # pred_mask = colour_code_segmentation(reverse_one_hot(pred_mask), classes)

    pred_mask = reverse_one_hot(pred_mask)

    colored_mask = make_image_with_text(pred_mask, classes, selected_labels=selected_labels, thickness=None,
                                        font_scale=None)

    added_image = cv2.addWeighted(im, 0.6, colored_mask, 0.6, 0)

    cv2.imwrite(os.path.join(save_path, image_name), added_image)

    print("Segmentation done")


if __name__ == '__main__':
    img_name = "1 biver-valli.jpg"
    image_path = "D:/MyPythonProjects/det2/images"
    model_weights_path = "D:\MyPythonProjects\det2/run_train_semseg/model_0003999.pth"

    detect(image_name=img_name, image_path=image_path,
           save_path="D:\MyPythonProjects\det2\segment_results",
           config_yaml="semantic_R_50_FPN_1x.yaml",
           model_tresh=0.7,
           iou_thres=0.5,
           model_weigths_path=model_weights_path)
