from cmath import inf
import numpy as np

class Linear_Classification:

  def fi(self, x, W, b):
    """
    线性分类器，计算权值向量f

    参数
      x (ndarray(m,)) : m个参数，n个特征
      W (ndarray(n,m)): n个类别，每个类别有m个权值
      b (ndarray(n))   : 每个类别的偏移量
    返回值
      f (ndarray(n,))
    案例
      x = [1, 2, 3, 4] # m = 4
      y = [0, 1, 2]
      W = [
        [.1, .2, .3, .4],
        [.5, .6, .7, .8],
        [.9, .0, .1, .2]] # (n,m) = (3,4)
      b = [0, 0, 0]
    """
    fi = np.dot(W, x) + b
    return fi
  

  def loss_i(self, x, yi, W, b):
    """
    线性分类器，计算单张图片的loss_function

    参数
      x (ndarray(m,))  : m个像素点
      yi (int)         : n类别中的一个
      W (ndarray(n,m)) : n个分类器，每个分类器有m个权值
      b (ndarray(n))   : 每个类别的偏移量
      lambda_    (int) : 正则化超参数
      R                : 计算正则化项
    中间值
      i        (int)   : 第i个分类器，范围是{0,1,...,n-1}
      s_yi     (int)   : 第i个样本真实类别的预测分数
      s_ij     (int)   : 第i个样本第j个类别的预测分数
    返回值
      loss_i   (int)   : 第i张图片的loss
    """
    n = W.shape[0]
    fi = self.fi(x,W,b)
    s_yi = fi[yi]
    loss_i = 0
    for j in range(n):
      s_ij = fi[j]
      loss_i += max(0, s_ij - s_yi + 1)
    return loss_i - 1


  def cost_j(self,X,y,W,b,lambda_=0):
    """
    参数
      X (ndarray(N,m)) : N个样图，m个像素
      y (ndarray(N))   : n个分类器
      W (ndarray(n,m)) : n个分类器，每个分类器有m个权值
      b (ndarray(n))   : 每个类别的偏移量
      lambda_    (int) : 正则化超参数
    """
    N = X.shape[0]
    cost_j = 0
    for k in range(N):
      xi = X[k]
      yi = y[k]
      cost_j += self.loss_i(xi,yi,W,b)
    cost_j = (1/N) * cost_j + lambda_ * np.sum(W**2)
    return cost_j
      

  def dj_dw(self, X, W, b, lambda_=0):
    """
    线性分类器，计算梯度

    参数
      X (ndarray(N,m)) : N个样图，m个像素
      y (ndarray(N))   : n个分类器
      W (ndarray(n,m)) : n个分类器，每个分类器有m个权值
    返回值
      dj_dw (ndarray(n,m)) : n个类别，每个类别有m个权值
    代办TODO
      未添加正则项目（没有成功）
    """
    n, m = W.shape
    N = X.shape[0]
    dj_dw = np.zeros((n,m))
    dj_db = np.zeros(n)
    tlr = 1e-4 # tolerance
    for k in range(N):
      xi = X[k]
      for i in range(n):
        dj_db[i] = 0 if b[i] <= tlr else 1
        for j in range(m):
          dj_dw[i][j] = 0 if W[i][j] < tlr else xi[j]
    dj_dw = dj_dw / N
    dj_db = dj_db / N
    return dj_dw,dj_db
    

  def learning(self, X, y, W, b, alpha, n):
    for i in range(n):
      J = self.cost_j(X,y,W,b)
      dj_dw,dj_db = self.dj_dw(X,W,b)
      W -= alpha * dj_dw
      b -= alpha * dj_db
    return W

    
if __name__ == "__main__":
  lc = Linear_Classification()
  # lc.test_compute_cost()
  
  x1 = np.array([1,2,3,4]) # m = 4
  y1 = 0
  x2 = np.array([2,2,4,5])
  y2 = 2
  y12 = np.array([y1,y2])
  x12 = np.stack((x1,x2), axis=0)
  W = np.array([
    [.1, .2, .3, .4],
    [.5, .6, .7, .8],
    [.9, .0, .1, .2]]) # (n,m) = (3,4)
  b = np.array([.0,.0,.0])
  
  # print(lc.fi(x1,W,b))
  # print(lc.loss_i(x1,y1,W,b))
  # print(lc.loss_i(x2,y2,W,b))
  # print(lc.cost_j(x12, y12, W, b, lambda_=0.0))


  print(W)
  print(lc.cost_j(x12,y12,W,b))
  W_new = lc.learning(x12,y12,W,b,alpha=0.1,n=1000)
  print(W_new)
  print(lc.cost_j(x12,y12,W_new,b))
  

    