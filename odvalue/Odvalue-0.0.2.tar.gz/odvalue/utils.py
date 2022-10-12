import numpy as np


class Desolver():
    def __init__(self, deter_func, rand_func, y0, slvtype='RK4', tspan=10, h=0.01, rand_open=True, **kwargs):
        # 建议func_list传进来后在内部重新构造一个func_list

        self.rand_open = rand_open # 是否涉及到随机模拟

        self.__dict__.update(kwargs) #这个基本没用，太大

        self.tspan = tspan # 时间总步长

        self.h = h
        self.grid = int(1 / self.h)  # 求解步长

        self.deter_func = deter_func
        self.rand_func = rand_func

        self.y0 = y0
        self.slvtype = slvtype

        # self.args = kwargs # 构造一个参数字典
        # self.args['h'] = self.h # 加个h

    def RK4_solver(self, **kwargs):
        # 默认为f(t,y)的形式，如果不用t可以设置为0
        solve_data = np.zeros((len(self.y0), self.tspan * self.grid))
        solve_data[:, 0] = self.y0 # 赋予初值

        # 不需要区分自变量t,y, t,y 都有

        for i in range(1, self.tspan * self.grid):
            tep_tn = self.h * (i - 1)
            tep_yn = solve_data[:, i - 1]


            k1 = self.deter_func(tep_tn, tep_yn, **self.__dict__)
            k2 = self.deter_func(tep_tn + self.h / 2, tep_yn + k1 * self.h / 2, **self.__dict__)
            k3 = self.deter_func(tep_tn + self.h / 2, tep_yn + k2 * self.h / 2, **self.__dict__)
            k4 = self.deter_func(tep_tn + self.h, tep_yn + k3 * self.h, **self.__dict__)

            if self.rand_open == True: # 这种做法属于蒙特卡洛模拟了
                solve_data[:, i] = tep_yn + (k1 + 2 * k2 + 2 * k3 + k4) * self.h / 6 + self.rand_func(tep_tn, tep_yn, **self.__dict__)
            else:
                solve_data[:, i] = tep_yn + (k1 + 2 * k2 + 2 * k3 + k4) * self.h / 6

        return solve_data

    def solver(self, **kwargs):
        solve_data = None
        if self.slvtype == 'RK4':
            solve_data = self.RK4_solver()

        return solve_data


