import os
from PIL import Image
import jsonpickle as jsp
import matplotlib.pyplot as plt
from jjy.framework.cuda import xp as np
import numpy as np2

import cupy as cp

import time
import random
from tqdm import tqdm
import jjy.framework.initializer as Initializer
import jjy.framework.layer as Layer
import jjy.framework.optimizer as Optimizer
from jjy.framework.functions import *
# from functions import *
from jjy.framework.network import MultiLayerNet

from jjy.dataset.mnist import load_mnist
import datetime





net = MultiLayerNet()
net.load_model("./idol_result/idol_train_weight_2021-06-06 090301_8907.npz")

load_data = np2.load("./idol_images_gray_128_v2.npz", allow_pickle=True)

x_train = load_data["x_train"]
t_train = load_data["t_train"].astype(np2.int64)

x_test = load_data["x_test"]
t_test = load_data["t_test"].astype(np2.int64)


print(x_train.shape, t_train.shape, x_test.shape, t_test.shape)

x_test = x_test / 255

x_test2 = []
t_test2 = []



i = 0
for x, t in zip(x_test, t_test):
    i += 1
    # x_test2.append(x)
    # t_test2.append(t)

    predict_num = np.argmax(net.predict(cp.array([x]), train_flg=False), axis=1)[0]

    if t != predict_num:
        print(t, predict_num)
        transposed_array = np.transpose(x, (1, 2, 0))
        plt.imshow(transposed_array, cmap='gray')
        plt.show()
        print("Predict : ", ["IU", "Irene", "Arin"][int(predict_num)], "Real : ", ["IU", "Irene", "Arin"][int(t)])
        a = input()
        if a == "d":
            print("discard")
        else:
            x_test2.append(x)
            t_test2.append(t)
    else:
        x_test2.append(x)
        t_test2.append(t)

print(i)





# x_train = np2.array(x_train)
x_test = np2.array(x_test2)
# t_train = np2.array(t_train)
t_test = np2.array(t_test2)

x_test = x_test * 255

print(x_test.shape)
print(t_test.shape)
temp_data = {"x_train": x_train, "x_test": x_test, "t_train": t_train, "t_test": t_test}
np2.savez_compressed("./idol_images_gray_128_v4.npz", **temp_data)
