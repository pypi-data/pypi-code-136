import sys

import matplotlib.pyplot as plt
from jjy.framework.functions import *
from PIL import Image
import os
#
import jjy.framework.layer as Layer
import jjy.framework.optimizer as Optimizer
import jjy.framework.initializer as Initializer
from jjy.framework.functions import *
from jjy.framework.network import MultiLayerNet
import random

import numpy as np2
import cupy as np

# import pickle
# with open("train_data_2021-04-20 060758.pickle","rb") as fr:
#     result = pickle.load(fr)
#
# for k,v in result.items():
#     result[k] = np.asnumpy(result[k])


color_list = ["red", "blue", "green", "yellow", "purple"]

marker_list = ["o", "s", "^", "v", "x"]

plt.figure(figsize=(9, 5))


def show_loss():
    plt.xlabel("step")
    plt.ylabel("loss")

    x = np2.arange(len(result["train_loss_list"]))
    plt.plot(x, result["train_loss_list"], label="loss", color=color_list[0], marker=None)

    plt.legend(loc='upper right')

    plt.show()


def show_acc():
    plt.xlabel("epoch")
    plt.ylabel("acc")

    x = np2.arange(len(result["train_acc_list"]))
    plt.plot(x, result["train_acc_list"], label="train_acc", color=color_list[0], marker=None)
    plt.plot(x, result["test_acc_list"], label="test_acc", color=color_list[1], marker="o")

    for i, v in enumerate(result["test_acc_list"]):
        plt.text(i, v + 0.0005, round(float(v), 2),  # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
                 fontsize=9,
                 color='blue',
                 horizontalalignment='center',  # horizontalalignment (left, center, right)
                 verticalalignment='bottom')
    plt.legend(loc='lower right')

    plt.show()


def show_img(img, t, ax):
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.imshow(img.get())
    ax.set_title(t, fontsize=20)


def plot_grid(imgs, title_list, nrows, ncols, figsize=(10, 10)):
    assert len(imgs) == nrows * ncols, f"Number of images should be {nrows}x{ncols}"
    _, axs = plt.subplots(nrows, ncols, figsize=figsize)
    axs = axs.flatten()
    for i, (img, ax) in enumerate(zip(imgs, axs)):
        show_img(img, title_list[i], ax)


def show_img_predict(net):
    # net = MultiLayerNet()
    # net.load_model("./idol_result/idol_train_weight_2021-06-06 090301_8907.npz")
    #
    # print(net.layers["BatchNormal9"])
    # # print(net.params)
    # return

    base_dir = 'D:\\google-image-crawler\\crop'

    # 테스트에 사용되는 고양이/개 이미지 경로
    test_iu_dir = os.path.join(base_dir, 'iu')
    test_irene_dir = os.path.join(base_dir, 'irene')
    test_arin_dir = os.path.join(base_dir, 'arin')

    test_iu_fnames = [os.path.join(test_iu_dir, x) for x in os.listdir(test_iu_dir)]
    test_irene_fnames = [os.path.join(test_irene_dir, x) for x in os.listdir(test_irene_dir)]
    test_arin_fnames = [os.path.join(test_arin_dir, x) for x in os.listdir(test_arin_dir)]

    def img_to_array(fname, original=False):

        image = Image.open(fname)

        if original is False:
            image = image.resize((128, 128))
            image = np2.reshape(image.convert("L"), (1, 128, 128))
        # show_img_by_array(np.asarray(image))
        return np.asarray(image)

    random.shuffle(test_iu_fnames)
    random.shuffle(test_irene_fnames)
    random.shuffle(test_arin_fnames)

    img_list = []
    predict_list = []
    for fname in test_iu_fnames[:8] + test_irene_fnames[:8] + test_arin_fnames[:8]:
        # fname = os.path.join(test_arin_dir, fname)

        img_original_array = img_to_array(fname, original=True)
        img_array = img_to_array(fname)
        img_array = img_array / 255.0

        img_list.append(img_original_array)
        print(net.predict(np.array([img_array])))

        predict_num = np.argmax(net.predict(np.array([img_array]), train_flg=False), axis=1)[0]
        # print(net.predict(np.array([img_array]), train_flg=False))
        # print(predict_num)

        predict_list.append(["IU", "Irene", "Arin"][int(predict_num)])

    plot_grid(np.asnumpy(img_list), predict_list, 3, 8, figsize=(16, 10))
    plt.show()


net = MultiLayerNet()
net.load_model("./idol_result/idol_train_weight_2021-06-06 090301_8907.npz")

load_data = np.load("./idol_images_gray_128_v4.npz", allow_pickle=True)

x_test = load_data["x_test"]
t_test = load_data["t_test"].astype(np.int64)

# print(x_test.max())
# exit()

# x_test = x_test / 255

# for x, t in zip(x_test, t_test):
#     # print(x.shape)
#     # print(net.predict(np.array([x])))
#     predict_num = np.argmax(net.predict(np.array([x]), train_flg=False), axis=1)[0]
#     if t != predict_num:
#         print(t, predict_num)
#         transposed_array = np.transpose(x.get(), (1, 2, 0))
#         plt.imshow(transposed_array, cmap='gray')
#         plt.show()
#         print("Predict : ", ["IU", "Irene", "Arin"][int(predict_num)], "Real : ", ["IU", "Irene", "Arin"][int(t)])
#         input()




for k, v in net.params.items():
    print(k, v.shape)



# for k, v in net.layers.items():
#     if type(v) == Layer.BatchNormalization:
#         net.layers[k].trainable = False
#     if isinstance(v, Layer.Dropout):
#         # net.layers[k].dropout_ratio = net.layers[k].dropout_ratio - 0.15
# # net.trainable_param_keys = ["W39", "b39", "W42", "b42", "W45", "b45"]


def shuffle_dataset(x, t):
    from sklearn.utils import shuffle
    x, t = shuffle(x, t)
    return x, t


x_test, t_test = shuffle_dataset(x_test, t_test)
#
x_test = x_test / 255
#
print("Test Acc : ", net.accuracy(x_test, t_test, batch_size=1))

# for k, v in net.layers.items():
#     if type(v) == Layer.BatchNormalization:
#         print(v.running_mean, v.running_var)

# print(net.layers)
show_img_predict(net)

# show_loss()
# show_acc()
