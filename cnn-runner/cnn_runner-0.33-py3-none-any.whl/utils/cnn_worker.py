from cnn_runner.yolo.detect_yolo import YoloDetector
from cnn_runner.yolor.detect_yolor import YoloRDetector
from cnn_runner.mm_detector import run_mm_detection
import cnn_runner.mask_r_cnn.aes_visual_detect as mask_detector

from PyQt5 import QtCore
import os
import torch
from cnn_runner.utils.canny_edge import start_add_mask, start_canny
import cv2

class CNN_worker(QtCore.QThread):
    def __init__(self, parent=None, cnn_type="YOLOv5l6", conf_thres=0.7, iou_thres=0.5,
                 img_name="selected_area.png", img_path=None, save_path=None,
                 classes_names=None, mask_colors=None, is_mask_saved=False, is_map=False, map_path=None,
                 scanning=False, device='GPU'):
        QtCore.QThread.__init__(self, parent)
        self.conf_thres = conf_thres
        self.iou_thres = iou_thres
        self.cnn_type = cnn_type
        self.img_name = img_name
        self.img_path = img_path
        self.is_mask_saved = is_mask_saved
        self.is_map = is_map
        self.scanning = scanning
        self.device = device

        self.classes_names = classes_names
        self.mask_colors = mask_colors
        self.masks_path = None
        self.map_path = map_path

        if save_path:
            self.save_path = save_path
            if not os.path.exists(save_path):
                os.makedirs(save_path)

        else:
            proj_path = os.getcwd()
            det_path = os.path.join(proj_path, "detection")
            self.save_path = os.path.join(det_path, self.cnn_type)

    def run(self):

        torch.cuda.empty_cache()

        if self.img_path == None:
            print("img_path doesn't set. Stop detection")
            return

        else:
            img_path_full = os.path.join(self.img_path, self.img_name)

        is_detected = False

        if self.cnn_type == "YOLOv5l6":

            if not self.scanning:
                proj_path = os.getcwd()
                cfg_path = os.path.join(proj_path, "yolo//yamls//aes.yaml")
                weights_path = os.path.join(proj_path, 'yolo//yolo_weights//v5l6_1280//best.pt')

                dev_set = 'cpu'
                if self.device == "GPU":
                    dev_set = 0

                yolo_detector = YoloDetector(img_path_full, cfg_path, weights_path, self.save_path)
                yolo_detector.run(view_img=False, save_txt=True,
                                  exist_ok=True, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                                  box_colors=self.mask_colors, classes_names=self.classes_names, scanning=self.scanning,
                                  device=dev_set)
                is_detected = True
            else:
                # split image and safe to temp folder
                proj_path = os.getcwd()
                temp_path = os.path.join(proj_path, "temp")
                if not os.path.exists(temp_path):
                    print("Make temp folder...")
                    os.mkdir(temp_path)

        if self.cnn_type == "YOLOv5x6":

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 0

            if not self.scanning:
                proj_path = os.getcwd()
                cfg_path = os.path.join(proj_path, "yolo//yamls//aes.yaml")
                weights_path = os.path.join(proj_path, 'yolo//yolo_weights//v5x6_640//best.pt')

                yolo_detector = YoloDetector(img_path_full, cfg_path, weights_path, self.save_path)
                yolo_detector.run(view_img=False, save_txt=True,
                                  exist_ok=True, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                                  box_colors=self.mask_colors, classes_names=self.classes_names, device=dev_set)
                is_detected = True
            else:
                # split image and safe to temp folder
                cnn_shape = [640, 640]
                proj_path = os.getcwd()
                temp_path = os.path.join(proj_path, "temp")
                if not os.path.exists(temp_path):
                    print("Make temp folder...")
                    os.mkdir(temp_path)

                img = cv2.imread(img_path_full)
                shape = img.shape

                print("shape ", shape)

                # если изображение меньше или сравнимо с входом СНС - запустить один раз
                if shape[0] < cnn_shape[0] * 1.1 and shape[1] < cnn_shape[1] * 1.1:

                    print("Image with size {0:d}*{1:d} too small. Start detection with one shot...".format(shape[0],
                                                                                                           shape[1]))

                    proj_path = os.getcwd()
                    cfg_path = os.path.join(proj_path, "yolo//yamls//aes.yaml")
                    weights_path = os.path.join(proj_path, 'yolo//yolo_weights//v5x6_640//best.pt')

                    yolo_detector = YoloDetector(img_path_full, cfg_path, weights_path, self.save_path)
                    yolo_detector.run(view_img=False, save_txt=True,
                                      exist_ok=True, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                                      box_colors=self.mask_colors, classes_names=self.classes_names, device=dev_set)
                    is_detected = True
                else:
                    fragments_names = []
                    if shape[0] % cnn_shape[0] != 0:
                        x_parts = int(shape[0] / cnn_shape[0]) + 1
                    else:
                        x_parts = int(shape[0] / cnn_shape[0])

                    if shape[1] % cnn_shape[1] != 0:
                        y_parts = int(shape[1] / cnn_shape[1]) + 1
                    else:
                        y_parts = int(shape[1] / cnn_shape[1])

                    print("Split image with size {0:d}*{1:d} to {2:d}*{3:d} fragments...".format(shape[0], shape[1],
                                                                                                 x_parts, y_parts))

                    x_tek = 0
                    delta_x = cnn_shape[0]
                    for x in range(x_parts):
                        y_tek = 0
                        delta_y = cnn_shape[1]
                        if x == x_parts - 1:
                            delta_x = shape[0] - x * cnn_shape[0]
                            # print("Delta x: ", delta_x)

                        for y in range(y_parts):

                            if y == y_parts - 1:
                                delta_y = shape[1] - y * cnn_shape[1]
                                # print("Delta y: ", delta_y)

                            crop = img[x_tek:x_tek + delta_x, y_tek:y_tek + delta_y]

                            crop_path = os.path.join(temp_path, "frag_{0:d}_{1:d}.jpg".format(x + 1, y + 1))
                            fragments_names.append(crop_path)
                            cv2.imwrite(crop_path, crop)
                            y_tek += delta_y

                        x_tek += delta_x

                    print("Start fragments detection...")
                    proj_path = os.getcwd()
                    save_path = os.path.join(temp_path, "detected")
                    if not os.path.exists(save_path):
                        print("Make save dir folder...")
                        os.mkdir(save_path)

                    cfg_path = os.path.join(proj_path, "yolo//yamls//aes.yaml")
                    weights_path = os.path.join(proj_path, 'yolo//yolo_weights//v5x6_640//best.pt')

                    yolo_detector = YoloDetector(temp_path, cfg_path, weights_path, save_path)
                    yolo_detector.run(view_img=False, save_txt=True,
                                      exist_ok=True, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                                      box_colors=self.mask_colors, classes_names=self.classes_names, device=dev_set)

                    # print("Start fragments detection...")
                    # for i in tqdm(range(len(fragments_names))):
                    #     name = fragments_names[i]
                    #     proj_path = os.getcwd()
                    #     save_path = os.path.join(temp_path, "detected")
                    #     if not os.path.exists(save_path):
                    #         print("Make save dir folder...")
                    #         os.mkdir(save_path)
                    #
                    #     cfg_path = os.path.join(proj_path, "yolo//yamls//aes.yaml")
                    #     weights_path = os.path.join(proj_path, 'yolo//yolo_weights//v5x6_640//best.pt')
                    #
                    #     yolo_detector = YoloDetector(name, cfg_path, weights_path, save_path)
                    #     yolo_detector.run(view_img=False, save_txt=True,
                    #                       exist_ok=True, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                    #                       box_colors=self.mask_colors, classes_names=self.classes_names)

                    for name in fragments_names:
                        os.remove(name)
                    is_detected = True

        elif self.cnn_type == "YOLOR":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "yolor//cfg//yolor_p6.cfg")
            weights_path = os.path.join(proj_path, 'yolor//weights//best.pt')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = '0'

            yolo_detector = YoloRDetector(img_path_full, out=self.save_path, weights=weights_path, cfg=cfg_path)
            yolo_detector.run(view_img=False, conf_thres=self.conf_thres, iou_thres=self.iou_thres,
                              colors=self.mask_colors, classes_names=self.classes_names, device=dev_set)
            is_detected = True

        elif self.cnn_type == "YOLACT":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/yolact/yolact_r50_1x8_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/yolact_r50_1x8_coco/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "YOLOv3":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/yolo/yolov3_d53_mstrain-608_273e_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/yolov3_d53_mstrain-608_273e/epoch_270.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "YOLACT-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/yolact/yolact_r101_1x8_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/yolact_101/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "AutoAssign":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/autoassign/autoassign_r50_fpn_8x2_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/autoassign_r50_fpn_8x2_1x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "FCOS-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path,
                                    "mm_detector/configs/fcos/fcos_r101_caffe_fpn_gn-head_mstrain_640-800_2x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/fcos_r101_caffe_fpn_gn-head_mstrain_640-800_2x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "NAS-FCOS-R50":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path,
                                    "mm_detector/configs/nas_fcos/nas_fcos_nashead_r50_caffe_fpn_gn-head_4x4_1x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/nas_fcos_nashead_r50_caffe_fpn_gn-head_4x4_1x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "ATSS-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/atss/atss_r101_fpn_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/atss_r101_fpn_1x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "SSD":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/ssd/ssd512_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/ssd_512/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "DDOD-R50":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/ddod/ddod_r50_fpn_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/ddod/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "TOOD-R101-Dconv":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/tood/tood_r101_fpn_dconv_c3-c5_mstrain_2x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/tood_r101_fpn_dconv_c3-c5_mstrain_2x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Sparce-RCNN-R50-FPN-300prop-3x":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path,
                                    "mm_detector/configs/sparse_rcnn/sparse_rcnn_r50_fpn_300_proposals_crop_mstrain_480-800_3x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/sparce_50_300prop_3/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Sparce-RCNN-R101-FPN-3x":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path,
                                    "mm_detector/configs\sparse_rcnn\sparse_rcnn_r101_fpn_mstrain_480-800_3x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/sparse_rcnn_r101_fpn_mstrain_480-800_3x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Dynamic R-CNN":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/dynamic_rcnn/dynamic_rcnn_r50_fpn_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/dynamic_rcnn/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True


        elif self.cnn_type == "SOLOv2-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/solov2\solov2_r101_fpn_3x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/solov2_r101_fpn_3x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "SOLOv2-R50":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/solov2\solov2_r50_fpn_3x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/solov2_r50_fpn_3x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "HTC-R50-1":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/htc/htc_without_semantic_r50_fpn_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/htc-50-1/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "SCNet-R50-20e":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/scnet\scnet_r50_fpn_20e_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/scnet_r50_fpn_20e/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "MS-R-CNN-R50":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/ms_rcnn/ms_rcnn_r50_fpn_1x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/ms_rcnn_50/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "VerifocalNet-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path,
                                    "mm_detector/configs/vfnet/vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/vfnet_r101_fpn_mdconv_c3-c5_mstrain_2x/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "PAA-R101":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/paa/paa_r101_fpn_mstrain_3x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/paa_101_3/latest.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "TridentNet-R50":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/tridentnet/tridentnet_r50_caffe_mstrain_3x_coco.py")
            weights_path = os.path.join(proj_path,
                                        'mm_detector/checkpoints/tridentnet_r50_caffe_mstrain_3x/epoch_32.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Grid R-CNN":
            proj_path = os.getcwd()
            cfg_path = os.path.join(proj_path, "mm_detector/configs/grid_rcnn/grid_rcnn_r101_fpn_gn-head_2x_coco.py")
            weights_path = os.path.join(proj_path, 'mm_detector/checkpoints/grid_rcnn/epoch_33.pth')

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda:0'

            run_mm_detection.run_mmdet(img_full_path=img_path_full, out_dir=self.save_path, config_file=cfg_path,
                                       checkpoint_file=weights_path,
                                       classes_names=self.classes_names, score_thr=self.conf_thres,
                                       mask_colors=self.mask_colors, model_type=self.cnn_type, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Mask-R-CNN-R50":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/mask_config.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train/model_final.pth")

            if self.classes_names:
                class_dict = {}
                num = 1
                for name in self.classes_names:
                    class_dict[name] = num
                    num += 1
            else:
                class_dict = None

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Mask-R-CNN", class_names=class_dict,
                                 is_mask_saved=self.is_mask_saved, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Mask-R-CNN-R101":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/mask_config_101.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_mask_101/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Mask-R-CNN-101",
                                 is_mask_saved=self.is_mask_saved, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Mask-R-CNN-X101":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/mask_x_101_config.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_mask_x101/model_0063999.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Mask-R-CNN-X101",
                                 is_mask_saved=self.is_mask_saved, device=dev_set)
            is_detected = True

        elif self.cnn_type == "Retina-R50":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/mask_config_retina.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_retina/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Retina", device=dev_set)
            is_detected = True

        elif self.cnn_type == "Retina-R101":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/config_retina_101.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_retina_101/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Retina", device=dev_set)
            is_detected = True

        elif self.cnn_type == "R-CNN-Faster-R50":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/faster_config.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_faster/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="R-CNN-Faster", device=dev_set)
            is_detected = True

        elif self.cnn_type == "R-CNN-Faster-R101":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/config_faster_101.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_faster_101/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="R-CNN-Faster", device=dev_set)
            is_detected = True

        elif self.cnn_type == "R-CNN-Faster-X101":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/faster_x101_config.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_faster_x101/model_0054999.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="R-CNN-Faster", device=dev_set)
            is_detected = True

        elif self.cnn_type == "Cascade R-CNN":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/config_cascade.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_cascade/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Cascade R-CNN", is_mask_saved=self.is_mask_saved,
                                 device=dev_set)

            is_detected = True

        elif self.cnn_type == "GN":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/config_gn.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_gn/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="GN", is_mask_saved=self.is_mask_saved,
                                 device=dev_set)

            is_detected = True

        elif self.cnn_type == "Deformable-Conv":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn/config_def.yml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_def/model_final.pth")

            dev_set = 'cpu'
            if self.device == "GPU":
                dev_set = 'cuda'

            mask_detector.detect(image_name=self.img_name, image_path=self.img_path, config_yaml=config_yml,
                                 save_path=self.save_path, model_weigths_path=model_weigth_path,
                                 model_tresh=self.conf_thres,
                                 thing_colors_set=self.mask_colors,
                                 iou_thres=self.iou_thres, model_type="Deformable", is_mask_saved=self.is_mask_saved,
                                 device=dev_set)

            is_detected = True

        if is_detected:
            self.img_detected_path = os.path.join(self.save_path, self.img_name)
        else:
            self.img_detected_path = None

        if self.is_map:
            image_name = os.path.join(self.img_path, self.img_name)

            if not self.map_path:
                self.map_path = os.path.join(self.img_path, "map.jpg")
            else:
                self.map_path = os.path.join(self.map_path, self.img_name)

            start_canny(image_name, is_save=True, save_path=self.map_path)
            start_add_mask(self.map_path, os.path.join(self.save_path, "masks"), treshold=self.conf_thres,
                           colors=self.mask_colors)

            print("map created")
