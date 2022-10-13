import gym
from abc import ABC
from jssp_tool.env.data.data_generator import gen_instance_uniformly


class BaseEnv(gym.Env, ABC):
    def __init__(self):
        super(BaseEnv).__init__()

        self.n_j = None
        self.n_m = None
        self.op_processing_times = None
        self.op_machines = None

        self.operations = None

        # 记录用
        self.step_count = 0

    def reset(self, **kwargs):
        self.step_count = 0
        if "data" in kwargs:
            # 加载案例
            self.op_processing_times, self.op_machines = kwargs.get("data")
            self.n_j, self.n_m = len(self.op_processing_times), len(self.op_processing_times[0])
        else:
            # 生成一个新的案例
            self.n_j, self.n_m = kwargs.get("n_j"), kwargs.get("n_m")
            dur_low, dur_high = kwargs.get("low"), kwargs.get("high")
            self.op_processing_times, self.op_machines = gen_instance_uniformly(self.n_j, self.n_m, dur_low, dur_high)

    def render(self):
        pass
