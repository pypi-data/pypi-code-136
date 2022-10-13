from torch.distributions.categorical import Categorical

from jssp_tool.rl.ppo import PPO


class PPODiscrete(PPO):
    def sample_action(self, p, candidate):
        dist = Categorical(p.squeeze())
        index = dist.sample()
        action = candidate.squeeze()[index]
        return action, index, dist.log_prob(index)

    def greedy_select_action(self, p, candidate):
        _, index = p.squeeze().max(0)
        action = candidate.squeeze()[index]
        return action

    def evaluate_actions(self, p, actions):
        dist = Categorical(p)
        action_log_probs = dist.log_prob(actions)
        dist_entropy = dist.entropy().mean()

        return action_log_probs, dist_entropy
