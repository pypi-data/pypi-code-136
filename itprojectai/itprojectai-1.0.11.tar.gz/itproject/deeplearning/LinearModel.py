import torch

"""线性模型"""


def linear_regression(X, w, b):
    """
       模型定义: y=Ax+b
    """
    return X @ w + b


def loss_fn(y_train, y_pred):
    """
        采用 MSE 均方误差来衡量预测结果的好坏
    """
    return ((y_train - y_pred) ** 2).mean()


def train(X_train, y_train, weights, learning_rate=1e-2):
    """训练过程，默认训练1000次，学习率为10的-2次方（学习率过大容易造成梯度左右摇摆，要注意调整学习率）"""
    # weights个权重
    w = torch.randn(weights, 1, dtype=torch.float32, requires_grad=True)
    # 1个偏置
    b = torch.randn(1, dtype=torch.float32, requires_grad=True)

    # 以下是训练过程
    # 正向传播(预测一次)
    y_pred = linear_regression(X_train, w, b)
    # 计算损失
    loss = loss_fn(y_train=y_train, y_pred=y_pred)
    # 反向传播
    loss.backward()
    # 更新参数
    w.data -= learning_rate * w.grad.data
    b.data -= learning_rate * b.grad.data
    # 清空梯度
    w.grad.data.zero_()
    b.grad.data.zero_()
    # 过程监控（向上管理）
    print(loss.item())

