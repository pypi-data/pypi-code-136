import numpy as np
import cv2
from skimage.filters import threshold_otsu
from PyQt5 import QtCore
import os
import cnn_runner.mask_r_cnn.run_sem_seg as sem_segmentator
import cnn_runner.utils.seg_image
import pickle
import cnn_runner.utils.start_ml


class StartML(QtCore.QThread):

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        tek_path = os.getcwd()

        dataset_url = os.path.join(tek_path, 'seg_datasets/sem_seg_data.csv')
        reg_models_path = os.path.join(tek_path, 'seg_datasets/reg_models')
        start_ml.create_models(dataset_url, reg_models_path)


class Segmentator(QtCore.QThread):

    def __init__(self, parent=None, img_path="", seg_method="k-means", clusters_num=2, k_means_attempts=10,
                 iou_thres=0.5,
                 k_means_criteria=None, save_path=None, is_crazy_colors=True,
                 semseg_classes=["город", "с/x земля", "пастбищные угодья", "лес", "вода", "бесплодная земля",
                                 "unknown"],
                 selected_labels=None):

        QtCore.QThread.__init__(self, parent)
        self.img_path = img_path
        self.seg_method = seg_method
        self.clusters_num = clusters_num
        self.k_means_attempts = k_means_attempts
        self.iou_thres = iou_thres
        self.is_crazy_colors = is_crazy_colors
        self.semseg_classes = semseg_classes
        self.selected_labels = selected_labels

        if k_means_criteria == None:
            self.k_means_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
        else:
            self.k_means_criteria = k_means_criteria

        if save_path:
            self.save_path = save_path
            if not os.path.exists(save_path):
                os.makedirs(save_path)

        else:
            proj_path = os.getcwd()
            det_path = os.path.join(proj_path, "segmentation")
            self.save_path = os.path.join(det_path, self.seg_method)

    def filter_image(self, image, mask):
        r = image[:, :, 0] * mask
        g = image[:, :, 1] * mask
        b = image[:, :, 2] * mask
        return np.dstack([r, g, b])

    def make_crazy_centers(self, num_of_clustars):
        centers = []
        color_depth = 255
        channel_num = 0  # red
        combs_num = 0

        for k in range(num_of_clustars):
            centers.append([0, 0, 0])

            if channel_num > 2:
                if channel_num < 6:
                    combs = [[0, 1], [0, 2], [1, 2]]
                    channel_num_1 = combs[combs_num][0]
                    channel_num_2 = combs[combs_num][1]
                    color_depth_1 = 255
                    color_depth_2 = 255
                    combs_num += 1
                    centers[k][channel_num_1] = color_depth_1
                    centers[k][channel_num_2] = color_depth_2
                else:
                    for ch in range(3):
                        centers[k][ch] = np.random.randint(low=0, high=255)
            else:
                centers[k][channel_num] = color_depth

            channel_num += 1

        return centers

    def run(self):

        img = cv2.imread(self.img_path)
        result_image = None

        img_basename = os.path.basename(self.img_path)

        is_segmented = False

        if self.seg_method == "CNN SemSeg":
            proj_path = os.getcwd()
            config_yml = os.path.join(proj_path, "mask_r_cnn\semantic_R_50_FPN_1x.yaml")
            model_weigth_path = os.path.join(proj_path, "mask_r_cnn/run_train_semseg/model_0038999.pth")

            sem_segmentator.detect(image_path=os.path.dirname(self.img_path),
                                   image_name=os.path.basename(self.img_path),
                                   save_path=self.save_path,
                                   iou_thres=self.iou_thres,
                                   config_yaml=config_yml,
                                   classes=self.semseg_classes,
                                   selected_labels=self.selected_labels,
                                   model_weigths_path=model_weigth_path)

            is_segmented = True

        if self.seg_method == "K-means":

            # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            twoDimage = img.reshape((-1, 3))
            twoDimage = np.float32(twoDimage)

            ret, label, center = cv2.kmeans(twoDimage, self.clusters_num, None, self.k_means_criteria,
                                            self.k_means_attempts, cv2.KMEANS_PP_CENTERS)
            if not self.is_crazy_colors:
                center = np.uint8(center)
            else:
                center = self.make_crazy_centers(self.clusters_num)
                print(center)
                center = np.array(center)

            res = center[label.flatten()]
            result_image = res.reshape((img.shape))

            is_segmented = True

        elif self.seg_method == "Contour Detection":
            img_shape = img.shape
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            _, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
            edges = cv2.dilate(cv2.Canny(thresh, 0, 255), None)
            cnt = sorted(cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2], key=cv2.contourArea)[
                -1]
            mask = np.zeros((img_shape[0], img_shape[1]), np.uint8)
            masked = cv2.drawContours(mask, [cnt], -1, 255, -1)

            dst = cv2.bitwise_and(img, img, mask=mask)
            result_image = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

            is_segmented = True

        elif self.seg_method == "RandomForest":

            proj_path = os.getcwd()
            reg_models_path = os.path.join(proj_path, 'seg_datasets/reg_models')
            random_forest = pickle.load(open(os.path.join(reg_models_path, 'random_forest_reg.pkl', ), 'rb'))
            poly_pipeline = pickle.load(open(os.path.join(reg_models_path, 'poly_pipeline.pkl', ), 'rb'))

            result_image = seg_image.start_seg(random_forest, poly_pipeline, self.img_path, is_save=False)

            is_segmented = True

        elif self.seg_method == "Thresholding":
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)

            thresh = threshold_otsu(img_gray)
            img_otsu = img_gray < thresh
            result_image = self.filter_image(img, img_otsu)

            is_segmented = True

        elif self.seg_method == "Color Masking":
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            hsv_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2HSV)

            light_blue = (90, 70, 50)
            dark_blue = (128, 255, 255)
            # You can use the following values for green
            # light_green = (40, 40, 40)
            # dark_greek = (70, 255, 255)
            mask = cv2.inRange(hsv_img, light_blue, dark_blue)
            result_image = cv2.bitwise_and(img, img, mask=mask)

            is_segmented = True

        if is_segmented:
            img_file_path = os.path.join(self.save_path, img_basename)
            self._img_save_path = img_file_path

            if self.seg_method != "CNN SemSeg":
                cv2.imwrite(img_file_path, result_image)

        else:
            print("segmenation not done. Please check seg_method or img path")
            self._img_save_path = None
