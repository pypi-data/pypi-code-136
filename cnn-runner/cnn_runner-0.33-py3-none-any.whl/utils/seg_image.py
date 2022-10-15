import pickle
import os
import numpy as np
import cv2
import warnings
import tensorflow as tf
warnings.filterwarnings("ignore")


def start_seg(
        reg_model,
        poly_pipeline, image_path, is_save=True, is_pooling=True, pool_size=2):

    img = cv2.imread(image_path)

    scale_percent = 50  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    img = cv2.resize(img, dim)

    colors = [[13, 240, 150], [78, 167, 255], [160, 160, 160]]  # forest water aes
    shape = img.shape

    new_img = np.zeros(shape)

    print("Start image segmentation...")

    X = []
    for x in range(shape[0]):
        for y in range(shape[1]):
            pixel = img[x, y]
            X.append([pixel[0], pixel[1], pixel[2]])

    X = poly_pipeline.transform(X)
    pred_val = reg_model.predict(X)

    i = 0
    for x in range(shape[0]):
        for y in range(shape[1]):
            new_img[x, y] = colors[int(pred_val[i])]
            i += 1

    tek_path = os.getcwd()
    dest = os.path.join(tek_path, '../seg_datasets')
    ImgPath = os.path.join(dest, 'seg_image.png')
    if not os.path.exists(dest):
        os.makedirs(dest)
    # img.save(self.selectedImgPath)
    print("Область изображения помещена в " + ImgPath)

    cv2.imwrite(ImgPath, new_img)

    img = cv2.imread(ImgPath)

    scale_percent = 100 * (100 / scale_percent)  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize back to original scale
    img = cv2.resize(img, dim)

    result_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    if is_pooling:
        result_image = tf.keras.layers.MaxPooling1D(pool_size=pool_size, strides=1)(result_image)
        result_image = result_image.numpy()

    if is_save:
        cv2.imwrite(ImgPath, result_image)
    else:
        return result_image

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    reg_models_path = os.path.join('../seg_datasets/', 'reg_models')
    random_forest = pickle.load(open(os.path.join(reg_models_path, 'random_forest_reg.pkl', ), 'rb'))
    # ada_boost = pickle.load(open(os.path.join(reg_models_path + degree, 'ada_boost_reg.pkl',), 'rb'))
    # bagging_forest = pickle.load(open(os.path.join(reg_models_path, 'bagging_reg.pkl',), 'rb'))
    poly_pipeline = pickle.load(open(os.path.join(reg_models_path, 'poly_pipeline.pkl', ), 'rb'))

    img_path = "D:\python\object_detector\pyqt_sns/aes_imgs/new/fanchangan1.jpg"
    start_seg(random_forest, poly_pipeline, img_path)
