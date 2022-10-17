from matplotlib import pyplot as plt

"""数据可视化工具，可以用于预测结果定性分析"""


def plot(X, y):
    """绘制折线图"""
    plt.plot(X, y)
    plt.show()


def scatter(X, y):
    """绘制散点图"""
    plt.scatter(X, y)
    plt.show()


def scatterX(X):
    """绘制散点图, 只需要传入某个特征"""
    # plt.title(label="y_pred VS y_test")
    # plt.xlabel(xlabel="y_pred")
    # plt.ylabel(ylabel="y_test")
    plt.scatter(range(X.size), X)
    plt.show()


def showImage(imgArr):
    """根据图片的三维矩阵，绘制图像"""
    plt.imshow(X=imgArr)
    plt.show()
