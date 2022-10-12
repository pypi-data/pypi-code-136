from abc import ABC

import gym


class BaseEnv(gym.Env, ABC):
    def __init__(self):
        super(BaseEnv).__init__()

    def render(self):
        pass
