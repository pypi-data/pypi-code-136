import matplotlib.pyplot as plt
from jjy.framework.network import MultiLayerNet
import jjy.framework.layer as Layer
import random
from jjy.dataset.mnist import load_mnist
from jjy.framework.cuda import xp as np
import numpy as np2
import matplotlib.pyplot as plt



def filter_show(filters, nx=8, margin=3, scale=10, title=None):
    """
    c.f. https://gist.github.com/aidiary/07d530d5e08011832b12#file-draw_weight-py
    """
    # FN, C, FH, FW = filters.shape
    FN, FH, FW = filters.shape

    FN = min(FN, 32)
    ny = int(np.ceil(FN / nx))

    fig = plt.figure()
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

    fig.suptitle(title)
    for i in range(FN):
        ax = fig.add_subplot(ny, nx, i + 1, xticks=[], yticks=[])
        ax.imshow(filters[i], cmap=plt.cm.viridis, interpolation='nearest')

    plt.show()


# (x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)
load_data = np2.load("D:\\develop\\deep-learning-without-tensorflow\\src\\jjy\\example\\idol\\idol_images_gray_128_v2.npz", allow_pickle=True)
x_train = load_data["x_train"]


net = MultiLayerNet()
# net.load_model("D:\\develop\\deep-learning-without-tensorflow\\src\\jjy\\example\\train_weight_2021-06-06 202331.npz")
net.load_model("D:\\develop\\deep-learning-without-tensorflow\\src\\jjy\\example\\idol\\idol_result\\idol_train_weight_2021-06-06 090301_8907.npz")

img_idx = random.randrange(0, 10000)
target_img = x_train[img_idx]
print(target_img.shape)

x = np.array([target_img])

i = 0
for layer_name, layer in net.layers.items():
    # print(x.shape)
    if isinstance(layer, Layer.BatchNormalization) or isinstance(layer, Layer.Dropout):

        x = layer.forward(x, False)
    else:
        print(layer)
        x = layer.forward(x)
    if type(layer) == Layer.Convolution or type(layer) == Layer.Affine or type(layer)==Layer.Pooling:
        if len(np.asnumpy(x)[0].shape) >= 3:
            filter_show(np.asnumpy(x)[0], title=f"{layer_name}")
            i += 1

# for k, v in net.params.items():
#     print(k, v.shape)


# filter_show(np.asnumpy(net.params["W0"]))
