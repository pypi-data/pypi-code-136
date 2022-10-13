import numpy as np


class Memory:
    """
    记录一个episode数据
    """

    def __init__(self):
        self.obs = []
        self.actions = []
        self.rewards = []
        self.dones = []
        self.logprobs = []
        self.returns = []
        self.values = []

    def clear_memory(self):
        del self.obs[:]
        del self.actions[:]
        del self.rewards[:]
        del self.dones[:]
        del self.logprobs[:]
        del self.values[:]

    def append(self, obs, action, reward, done, logprob, value):
        if isinstance(obs, tuple):
            if len(self.obs) == 0:
                self.obs = [[] for _ in range(len(obs))]
            for i, item in enumerate(obs):
                self.obs[i].append(item)
        else:
            self.obs.append(obs)
        self.actions.append(action)
        self.rewards.append(reward)
        self.dones.append(done)
        self.logprobs.append(logprob)
        self.values.append(value)

    def compute_standard_returns(self, next_value, use_gae, gamma, gae_lambda):
        self.returns = [0 for _ in range(len(self.rewards))]
        if use_gae:
            self.values[-1] = next_value
            gae = 0
            for step in reversed(range(len(self.rewards))):
                delta = self.rewards[step] + gamma * self.values[step + 1] * self.dones[step + 1] - self.values[step]
                gae = delta + gamma * gae_lambda * self.dones[step + 1] * gae
                self.returns[step] = gae + self.values[step]
        else:
            self.returns[-1] = next_value
            for step in reversed(range(len(self.rewards))):
                self.returns[step] = self.returns[step + 1] * gamma * self.dones[step + 1] + self.rewards[step]

    def compute_monte_carlo_returns(self, gamma):
        rewards = []
        discounted_reward = 0
        for reward, is_terminal in zip(reversed(self.rewards), reversed(self.dones)):
            if is_terminal:
                discounted_reward = 0
            discounted_reward = reward + (gamma * discounted_reward)
            rewards.insert(0, discounted_reward)
        rewards = np.array(rewards, dtype=np.float32)
        self.returns = (rewards - rewards.mean()) / (rewards.std() + 1e-5)

    def sample(self, device):
        raise NotImplementedError("实现该函数，转为torch tensor")
