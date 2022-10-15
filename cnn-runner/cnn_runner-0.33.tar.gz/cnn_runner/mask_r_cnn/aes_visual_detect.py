from detectron2.utils.logger import setup_logger
import os
import cv2
import matplotlib.pyplot as plt
from detectron2.engine import DefaultPredictor
from cnn_runner.utils.my_vizualizer import MyVisualizer
from detectron2.config import get_cfg
from detectron2.utils.visualizer import ColorMode
from detectron2.data import DatasetCatalog, MetadataCatalog
from tqdm import tqdm

CLASS_NAME = {'реактор': 1, 'реактор кв': 2, 'градирня': 3, 'градирня кв': 4,
              'градирня вент': 5, 'РУ': 6, 'ВНС': 7, 'турбина': 8, 'БСС': 9, 'машинный зал': 10, 'парковка': 11}

setup_logger()

# model_types = ["mask-r-cnn", "retina", "faster",
#                "faster_101", "retina_101", "panoptic",
#                "mask-101", "cascade", "deformable",
#                "gn", "SyncBN"]

mask_models = ["Mask-R-CNN", "Mask-R-CNN-101", "Cascade R-CNN", "Deformable",
               "GN", "SyncBN"]


def get_base_img_name(name_with_dir):
    return os.path.basename(name_with_dir)


def detect(image_name, image_path,
           save_path="detect",
           config_yaml="mask_config.yml",
           model_tresh=0.7,
           visualizer_scale=1,
           iou_thres=0.5,
           visualizer_mode=ColorMode.IMAGE,
           class_names=CLASS_NAME,
           thing_colors_set=[(252, 66, 123),  # 'RO'
                             (192, 57, 43),  # 'RO sq'
                             (52, 152, 219),  # 'CT':
                             (52, 152, 219),  # 'CT sq
                             (52, 152, 219),  # 'CT vent
                             (39, 174, 96),  # 'Switch
                             (155, 89, 182),  # 'WPS'
                             (252, 66, 123),  # 'Turb'
                             (155, 89, 182),  # 'Spill'
                             (58, 53, 117),  # ER'
                             (255, 221, 89)],  # 'Parking'
           model_weigths_path=None,
           model_type="Mask-R-CNN", is_mask_saved=False, device='cuda'):
    from os import listdir
    from os.path import isfile, join

    if not class_names:
        class_names = CLASS_NAME

    classes = [key for key in class_names]

    num_of_classes = len(classes)

    aes_metadata = MetadataCatalog.get("aes_data_test/val").set(thing_classes=classes)
    MetadataCatalog.get("aes_data_test/val").set(thing_colors=thing_colors_set)

    # Create Model Configuration object
    mrcnn_model = config_yaml

    # Create Model Configuration object
    cfg = get_cfg()

    # Add model architecture config, which we set earlier
    cfg.merge_from_file(mrcnn_model)

    cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 512
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 11
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = iou_thres
    cfg.MODEL.ROI_HEADS.NMS_THRESH_TEST = iou_thres
    cfg.MODEL.DEVICE = device
    cfg.DATASETS.TEST = ("aes_data_test/val")
    cfg.OUTPUT_DIR = "run_train"

    # Add model architecture config, which we set earlier

    # load weights
    if not model_weigths_path:
        cfg.MODEL.WEIGHTS = os.path.join(cfg.OUTPUT_DIR, "model_final.pth")
    else:
        cfg.MODEL.WEIGHTS = model_weigths_path

    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = model_tresh  # set the testing threshold for this model
    if model_type == "Retina":
        cfg.MODEL.RETINANET.SCORE_THRESH_TEST = model_tresh
        cfg.MODEL.RETINANET.NUM_CLASSES = num_of_classes

    predictor = DefaultPredictor(cfg)

    print("Start detection {0:s}...".format(image_name))
    im = cv2.imread(os.path.join(image_path, image_name))
    outputs = predictor(im)

    labels_path = os.path.join(save_path, "labels")
    if not os.path.exists(labels_path):
        os.makedirs(labels_path)

    masks_path = os.path.join(save_path, "masks")
    if not os.path.exists(masks_path):
        os.makedirs(masks_path)
    else:
        masks = os.listdir(masks_path)
        for m in masks:
            os.remove(os.path.join(masks_path, m))

    labels_name = image_name.split('.')[0] + str(".txt")

    pred_per_classes_num = [0] * len(class_names)

    with open(os.path.join(labels_path, labels_name), 'w') as outfile:
        for k in range(len(outputs['instances'].scores)):

            class_num = outputs['instances'].pred_classes.tolist()[k]
            pred_num = pred_per_classes_num[class_num]
            pred_per_classes_num[class_num] += 1
            score = outputs['instances'].scores[k]

            tensor = outputs['instances'].pred_boxes[k].tensor
            line = "Class {0} score {5:f} boxes: {1:5.5f}, {2:5.5f}, {3:5.5f}, {4:5.5f}\n".format(
                outputs['instances'].pred_classes.tolist()[k],
                tensor[0][1],
                tensor[0][1],
                tensor[0][2],
                tensor[0][3], score)

            outfile.write(line)

            if is_mask_saved:
                if model_type in mask_models:
                    # mask_tensor = result[1][k][pred_num]
                    head_str = "class {1:d} mask {0:d} with score {2:0.3f}".format(pred_num, class_num,
                                                                                   score)
                    mask_tensor = outputs['instances'].pred_masks.to('cpu').numpy()[k]
                    #
                    # heigth = len(mask_tensor)
                    # width = len(mask_tensor[0])
                    #
                    # # print(heigth, width)

                    mask_img_name = image_name.split('.')[0] + " " + head_str + str(".png")

                    cv2.imwrite(os.path.join(masks_path, mask_img_name), mask_tensor * 255)

                    # mask_tensor =
                    # h_w_mask_list = []
                    # heigth = len(mask_tensor)
                    # width = len(mask_tensor[0])
                    # for h in range(heigth):
                    #     for w in range(width):
                    #         if mask_tensor[h][w]:
                    #             h_w_mask_list.append([h, w])
                    #
                    # line2 = "Instance pred mask: "
                    #
                    # for inst in h_w_mask_list:
                    #     line2 += "({0:5.5f}, {1:5.5f}) ".format(inst[0], inst[1])
                    #
                    # outfile.write(line2 + "\n")


    v = MyVisualizer(im[:, :, ::-1],
                     metadata=aes_metadata,
                     scale=visualizer_scale,
                     instance_mode=visualizer_mode)
    v = v.draw_instance_predictions(outputs["instances"].to("cpu"))

    v.save(os.path.join(save_path, image_name))

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect(image_name="image.jpg", image_path="",
           save_path="detect",
           config_yaml="mask_config.yml",
           model_tresh=0.7,
           visualizer_scale=1,
           visualizer_mode=ColorMode.IMAGE,
           iou_thres=0.5,
           class_names=CLASS_NAME,
           model_weigths_path=None)

