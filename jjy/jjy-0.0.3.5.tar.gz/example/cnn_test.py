import sys
import jjy.framework.initializer as Initializer
import jjy.framework.layer as Layer
import jjy.framework.optimizer as Optimizer
from jjy.framework.functions import *
# from functions import *
from jjy.framework.network import MultiLayerNet

from jjy.dataset.mnist import load_mnist
import matplotlib.pyplot as plt
import random


def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(flatten=False)
    # print(x_train.shape, t_train.shape)
    # print(t_train[0])
    # net.load_model("train_weight_2021-06-06 200548.npz")

    net = MultiLayerNet(is_use_dropout=False)
    net.add_layer(Layer.Dense(256, input_size=(1, 28, 28), initializer=Initializer.He()))
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dense(256, initializer=Initializer.He()))
    net.add_layer(Layer.Relu())
    net.add_layer(Layer.Dense(512, initializer=Initializer.He()))
    # net.add_layer(Layer.Conv2D(16, (3, 3), pad=1, input_size=(1, 28, 28), ),
    #               initializer=Initializer.He(),
    #               activation=Layer.Relu())
    # net.add_layer(Layer.BatchNormalization())
    # net.add_layer(Layer.Conv2D(32, (3, 3), pad=1, initializer=Initializer.He(), activation=Layer.Relu()))
    # net.add_layer(Layer.Pooling(pool_h=2, pool_w=2, stride=2))
    # net.add_layer(Layer.Dropout(0.2))
    # net.add_layer(Layer.Dense(10))
    net.add_layer(Layer.SoftmaxWithLoss())
    result = net.train(
        x_train, t_train, x_test, t_test, batch_size=100, iters_num=1000, print_epoch=1, evaluate_limit=100,
        is_use_progress_bar=True,
        optimizer=Optimizer.Adam(lr=0.001))

    # for k, v in net.params.items():
    # print(k, v.shape)

    # for i in range(5):
    #     img_idx = random.randrange(0, 10000)
    #
    #     plt.imshow(x_test[img_idx].reshape(28, 28), cmap='gray')
    #
    #     predict_num = np.argmax(net.predict(np.array([x_test[img_idx]]), train_flg=False), axis=1)[0]
    #     correct_num = t_test[img_idx]
    #
    #     plt.title(f"Predict : {predict_num}, Correct : {correct_num}",)
    #     plt.show()
    #     print(f"Predict : {predict_num}, Correct : {correct_num}")
    #
    # import pickle
    # import datetime
    # # Save pickle
    #
    # with open(f"train_data_{str(datetime.datetime.now())[:-7].replace(':', '')}.pickle", "wb") as fw:
    #     pickle.dump(result, fw)
    # net.save_model()

    print("============================================")


main()

print("done!")
