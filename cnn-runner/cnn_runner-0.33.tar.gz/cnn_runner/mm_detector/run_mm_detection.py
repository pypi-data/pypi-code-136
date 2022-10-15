from mmdet.apis import init_detector, inference_detector
from mmcv.runner import load_checkpoint
# import mmcv
import os
import cv2

mask_models = ["YOLACT-R101", "SOLOv2-R50", "SOLOv2-R101", "HTC-R50-1",
               "MS-R-CNN-50", "SCNet-R50-20e"]
import numpy as np


def run_mmdet(img_full_path, out_dir, config_file, checkpoint_file, score_thr=0.3, thickness=None, fontsize=None,
              classes_names=None, mask_colors=None, model_type="YOLACT-R101", is_mask_saved=False, device='cuda:0'):
    # Specify the path to model config and checkpoint file
    # config_file = 'configs/yolact/yolact_r50_1x8_coco.py'
    # checkpoint_file = 'checkpoints/yolact_r50_1x8_coco/latest.pth'

    # build the model from a config file and a checkpoint file
    model = init_detector(config_file, checkpoint_file, device=device)

    # test a single image and show the results
    result = inference_detector(model, img_full_path)

    # print(result)

    # or save the visualization results to image files
    img_name = os.path.basename(img_full_path)

    out_path = os.path.join(out_dir, img_name)

    labels_path = os.path.join(out_dir, "labels")
    if not os.path.exists(labels_path):
        os.makedirs(labels_path)

    if is_mask_saved:
        masks_path = os.path.join(out_dir, "masks")
        if not os.path.exists(masks_path):
            os.makedirs(masks_path)

    labels_name = img_name.split('.')[0] + str(".txt")
    # masks_name = img_name.split('.')[0] + str(".txt")

    # if is_mask_saved:
    #     mask_file = open(os.path.join(masks_path, masks_name), 'w')

    with open(os.path.join(labels_path, labels_name), 'w') as outfile:

        for k in range(len(classes_names)):
            # print("Class {0:s}".format(classes_names[k]))
            # print(result[k])
            if model_type in mask_models:
                box_results = result[0]
            else:
                box_results = result

            pred_num = 0
            for prediction in box_results[k]:
                if prediction[4] > score_thr:
                    line = "Class {0} score {5:f} boxes: {1:5.5f}, {2:5.5f}, {3:5.5f}, {4:5.5f}\n".format(
                        k,
                        prediction[0],
                        prediction[1],
                        prediction[2],
                        prediction[3],
                        prediction[4])

                    outfile.write(line)

                    if is_mask_saved:
                        if model_type in mask_models:
                            # mask_tensor = result[1][k][pred_num]
                            head_str = "class {1:d} mask {0:d} with score {2:0.3f}".format(pred_num, k,
                                                                                           prediction[4])
                            mask_tensor = result[1][0][k][pred_num]
                            #
                            # heigth = len(mask_tensor)
                            # width = len(mask_tensor[0])
                            #
                            # # print(heigth, width)

                            image_name = img_name.split('.')[0] + " " + head_str + str(".png")

                            cv2.imwrite(os.path.join(masks_path, image_name), mask_tensor * 255)

                pred_num += 1

    # if is_mask_saved:
    #     mask_file.close()
    # Load checkpoint
    # checkpoint = load_checkpoint(model, checkpoint_file, map_location=device)

    # Set the classes of models for inference
    model.CLASSES = classes_names
    # print(classes_names)

    if not thickness or not fontsize:
        im = cv2.imread(img_full_path)
        if not thickness:
            thickness = max(round(sum(im.shape) / 2 * 0.003), 2)
            # print("Img shape: ", im.shape)
            # thickness = 2
        if not fontsize:
            fontsize = max(round(sum(im.shape) / 2 * 0.01), 12)
            # print("Img size: ", im.size)
            # fontsize = 13

    model.show_result(img_full_path, result,
                      score_thr=score_thr, thickness=thickness, mask_color=mask_colors, bbox_color=mask_colors,
                      font_size=fontsize, out_file=out_path)

    # # test a video and show the results
    # video = mmcv.VideoReader('video.mp4')
    # for frame in video:
    #     result = inference_detector(model, frame)
    #     model.show_result(frame, result, wait_time=1)
