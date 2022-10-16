def compute_cost(x, y, w, b): 
    """
    计算线性回归的损失函数
    
    参数:
      x (ndarray (m,)): m个数据
      y (ndarray (m,)): 目标值
      w,b (scalar)    : 模型参数
    
    返回值
      total_cost (float): 总损失
    """
    m = x.shape[0] 
    
    cost_sum = 0 
    for i in range(m): 
        f_wb = w * x[i] + b   
        cost = (f_wb - y[i]) ** 2  
        cost_sum = cost_sum + cost  
    total_cost = (1 / (2 * m)) * cost_sum  

    return total_cost