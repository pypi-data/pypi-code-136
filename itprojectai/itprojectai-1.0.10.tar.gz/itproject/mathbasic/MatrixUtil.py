import numpy as np

"""
矩阵工具包，实现矩阵加减乘除等运算,切片思想，广播机制理解
"""


def getOnes(m, n):
    """获取m*n全是1的矩阵，exp：X = getOnes(3, 2)"""
    return np.ones(shape=(m, n))


def getZeros(m, n):
    """获取m行n列全是0的矩阵, exp:X = getZeros(3,3)"""
    return np.zeros(shape=(m, n))


def getEye(M):
    """获取N行的单位矩阵/对角矩阵, exp:X = getEye(3)"""
    return np.eye(M)


def getDiag(M, num):
    """获取N行的单位矩阵/对角矩阵, 可以指定对角线的元素, exp:getDiag(4, 4)"""
    return np.diag([num] * M)


def getMNMatrix(m, n):
    """获取一个M*N的矩阵，m=-1表示只指定列数，n=-1表示只指定行数"""
    return np.arange(m * n).reshape(m, n)


def getImgMatrix(count, rgb=3, width=None, height=None):
    """获取count张宽是width高是height的图像的矩阵,exp: getImgMatrix(3,width=10,height=10)"""
    return np.random.randn(count, rgb, width, height)


def add(np_flag, X1, X2, *args, **kwargs):
    """
    两个矩阵相加,np_flag=true将调用numpy封装的方法
    """
    if np_flag:
        return np.add(X1, X2, *args, **kwargs)
    else:
        return A + B


def subtract(X1, X2, *args, **kwargs):
    """两个矩阵相减"""
    return np.subtract(X1, X2, *args, **kwargs)


def multi(A, B):
    """两个矩阵相乘"""
    return A @ B


def getMax(X, axis=None):
    """获取矩阵某行或某列的最大值, 0代表按列，1代表按行 exp: getMax(X, axis=0)"""
    return np.array(X).max(axis=axis)


def getMaxIdx(X, axis=None):
    """获取矩阵某行或某列的最大值对应的索引, 0代表按列，1代表按行 exp: getMaxIdx(X, axis=1)"""
    return np.array(X).argmax(axis=axis)


def getSubMatrix(X, row=None, col=None):
    """
    矩阵切片：X[rfrom:rto,cfrom:cto]
    切片获取某一行或某一列,或者某个元素,如果row或col是负数，表示从后面开始算起
    exp:getSubMatrix(X,row=2), getSubMatrix(X, row=1,col=-1)行与列从1开始算"""
    if row is None and col is None:
        return X
    elif col is None:
        if row > 0:
            return np.array(X)[row - 1, :]
        else:
            return np.array(X)[row, :]
    elif row is None:
        if col > 0:
            return np.array(X)[:, col - 1]
        else:
            return np.array(X)[:, col]
    else:
        if row > 0 and col > 0:
            return np.array(X)[row - 1, col - 1]
        elif row < 0 and col < 0:
            return np.array(X)[row, col]
        elif row < 0 and col > 0:
            return np.array(X)[row, col - 1]
        else:
            return np.array(X)[row - 1, col]


def getSubMatrixRow(X, rowFrom, rowTo):
    """
    获取矩阵第rowFrom行到第rowTo行的数据"""
    return X[rowFrom - 1:rowTo - 1, ]


def getSubMatrixCol(X, colFrom, colTo):
    """获取矩阵第colFrom列到第colTo列的数据"""
    return X[::, colFrom - 1:colTo - 1]


X = getEye(10)
print(getSubMatrixCol(X, 1, 8))


def getMatrixT(arr):
    """获取转置矩阵,exp: getMatrixT(X)"""
    return np.array(arr).T
