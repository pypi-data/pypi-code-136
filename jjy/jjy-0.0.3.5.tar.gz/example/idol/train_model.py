import os
from PIL import Image
import jsonpickle as jsp
import matplotlib.pyplot as plt
from jjy.framework.cuda import xp as np
import numpy as np2

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


class Timer(object):

    def __init__(self, name=""):
        self.name = name

    def __enter__(self):
        self.t = datetime.datetime.now()
        return self

    def __exit__(self, type, value, traceback):
        self.t = datetime.datetime.now() - self.t
        print(f"{self.name} Time : ", self.t)


# Open the image form working directory

def img_to_array(fname):
    image = Image.open(fname)
    image = image.resize((64, 64))
    image = np.reshape(image.convert("L"), (1, 64, 64))
    # show_img_by_array(np.asarray(image))
    return np.asarray(image)
    # return np.transpose(np.asarray(image), (2, 1, 0))


def show_img_by_array(img_array):
    transposed_array = np.transpose(img_array, (1, 2, 0))
    plt.imshow(transposed_array, cmap='gray')
    plt.show()





def make_net1():
    net = MultiLayerNet(is_use_dropout=False)
    net.add_layer(Layer.Conv2D(16, (4, 4), pad=1, input_size=(1, 128, 128)), initializer=Initializer.He())
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(32, (4, 4), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(64, (3, 3), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(128, (3, 3), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Dense(512, initializer=Initializer.He(), activation=Layer.Relu()))
    net.add_layer(Layer.Dropout(0.4))
    net.add_layer(Layer.Dense(512, initializer=Initializer.He(), activation=Layer.Relu()))
    net.add_layer(Layer.Dropout(0.4))
    net.add_layer(Layer.Dense(3))
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.SoftmaxWithLoss())
    return net


def make_net3():
    net = MultiLayerNet(is_use_dropout=False)
    net.add_layer(Layer.Conv2D(16, (3, 3), pad=1, input_size=(3, 128, 128)), initializer=Initializer.He())
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.2))
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(32, (3, 4), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(64, (3, 3), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Conv2D(128, (3, 3), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Dense(512 , initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Dense(1024, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Dense(3))
    net.add_layer(Layer.SoftmaxWithLoss())
    return net



def make_net4():
    net = MultiLayerNet(is_use_dropout=False, weight_decay_lambda=0.1)
    net.add_layer(Layer.Conv2D(16, (3, 3), pad=1, input_size=(3, 128, 128)), initializer=Initializer.He())
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Conv2D(32, (3, 3), pad=1, initializer=Initializer.He()))
    net.add_layer(Layer.BatchNormalization())
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Dropout(0.5))

def make_net5():
    net = MultiLayerNet(is_use_dropout=False)
    net.load_model("./idol_result/idol_train_weight_2021-06-06 090301_8907.npz")
    return net






def make_net2():

    # net.add_layer(Layer.Conv2D(16, (3, 3), pad=1, input_size=(1, 128, 128)), initializer=Initializer.He())
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Relu())
    # net.add_layer(Layer.Dropout(0.2))
    # net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    # net.add_layer(Layer.Conv2D(32, (3, 3), pad=1, initializer=Initializer.He()))
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Relu())
    # net.add_layer(Layer.Dropout(0.2))
    # net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    # net.add_layer(Layer.Conv2D(64, (3, 3), pad=1, initializer=Initializer.He()))
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Relu())
    # net.add_layer(Layer.Dropout(0.2))
    # net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    # net.add_layer(Layer.Conv2D(128, (3, 3), pad=1, initializer=Initializer.He()))
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Relu())
    # net.add_layer(Layer.Dropout(0.2))
    # net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    # net.add_layer(Layer.Dense(512, initializer=Initializer.He()))
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Relu())
    # net.add_layer(Layer.Dropout(0.5))
    net = MultiLayerNet(is_use_dropout=False)
    net.add_layer(Layer.Conv2D(32,(3,3), input_size=(1, 128, 128)), initializer=Initializer.He(), activation=Layer.Relu())
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    net.add_layer(Layer.Dropout(0.5))
    net.add_layer(Layer.Dense(3))
    net.add_layer(Layer.SoftmaxWithLoss())
    return net


# def make_net2():
#     net = MultiLayerNet(is_use_dropout=False)
#     net.add_layer(Layer.Conv2D(32, (3, 3), pad=1, input_size=(1, 64, 64)), initializer=Initializer.He(),
#                   activation=Layer.Relu())
#     net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
#     net.add_layer(Layer.Dense(128, initializer=Initializer.He(), activation=Layer.Relu()))
#     net.add_layer(Layer.Dense(2, initializer=Initializer.He()))
#     net.add_layer(Layer.SoftmaxWithLoss())
#
#     return net


def shuffle_dataset(x, t):
    from sklearn.utils import shuffle
    x, t = shuffle(x, t)
    return x, t

print("Loading Dataset..")

load_data = np2.load("./idol_images_gray_128_v2.npz", allow_pickle=True)
x_train = load_data["x_train"]

t_train = load_data["t_train"].astype(np.int64)

x_test = load_data["x_test"]
t_test = load_data["t_test"].astype(np.int64)

x_train, t_train = shuffle_dataset(x_train, t_train)
x_test, t_test = shuffle_dataset(x_test, t_test)



x_train = x_train / 255
x_test = x_test / 255


def train_model():
    net = make_net5()

    for k, v in net.params.items():
        print(k, v.shape)
    print(net.layers)
    print(net.hiddenSizeList)

    result = net.train(
        x_train, t_train, x_test, t_test, batch_size=6, iters_num=30, print_epoch=1, evaluate_limit=50,
        is_use_progress_bar=True, save_model_each_epoch=1, save_model_path="./idol_result",
        optimizer=Optimizer.Adam(lr=0.0001))

    import pickle
    import datetime
    #
    ## Save pickle
    with open(f"train_data_{str(datetime.datetime.now())[:-7].replace(':', '')}.pickle", "wb") as fw:
        pickle.dump(result, fw)
    net.save_model("weight_idol_f55.npz")

    print("============================================")


train_model()



# load_trained_model()