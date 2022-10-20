#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Multi-Armed Bandit family
'''
import math
import numpy as np
from copy import deepcopy
# internal imports
from oacde.tuners._base import __base



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
class __baseMAB(__base):
    ''' :class:`__baseMAB` is the base class for Multi-Armed Bandit family. '''

    def __init__(self, RS, feature_discrete, value_estimation_method, **kwargs):
        '''
        Create a Multi-Armed Bandit model

        Parameters
        ----------
        feature_discrete : list
            The collections of arms' name
        RS: rng of np.random
            Random state instance of np
        value_estimation_method: str
            Either be 'sliding_window_average' or 'sample_average'. The first
            calculates the moving average in contrast to the global arithmetic
            average
        sliding_window_size: int (optional)
            If 'sliding_window_average' is enabled in `value_estimation_method`,
            this value defines the rolling size of data-set
        '''
        self.RS = RS
        self.feature_discrete = feature_discrete
        self.value_estimation_method = value_estimation_method
        self.sw_size = kwargs.get("sliding_window_size")
        self.counts = {arm: 0 for arm in self.feature_discrete}
        self.values = {arm: 0.0 for arm in self.feature_discrete}

    @property
    def value_estimation_method(self):
        return self._value_estimation_method

    @value_estimation_method.setter
    def value_estimation_method(self, method):
        if isinstance(method, str):
            self._value_estimation_method = method.lower()
            if self._value_estimation_method == "sliding_window_average":
                self.rewards = {arm: [] for arm in self.feature_discrete}
        else:
            raise TypeError("`value_estimation_method` must be a str but '{}' "
                "is given".format(type(method)))

    @property
    def sw_size(self):
        return self._sw_size

    @sw_size.setter
    def sw_size(self, size):
        if self.value_estimation_method == "sliding_window_average":
            if isinstance(size, (int, float)):
                self._sw_size = int(size)
            else:
                raise TypeError("`sliding_window_size` must be a int but {} is"
                    " given".format(type(size)))
        else:
            self._sw_size = size

    def reset(self):
        if self.value_estimation_method == "sliding_window_average":
            self.rewards = {arm: [] for arm in self.feature_discrete}
        self.counts = {arm: 0 for arm in self.feature_discrete}
        self.values = {arm: 0.0 for arm in self.feature_discrete}

    def select_an_arm(self):
        raise NotImplementedError("<method select_an_arm> is not implemented")

    def select_multiple_arms(self, k):
        return [self.select_an_arm() for i in range(int(k))]

    def update(self, chosen_arm, reward):
        self.counts[chosen_arm] = self.counts[chosen_arm] + 1
        if self.value_estimation_method == "sample_average":
            self.values[chosen_arm] = (self.values[chosen_arm]
                                       + (reward - self.values[chosen_arm])
                                       / self.counts[chosen_arm])
        elif self.value_estimation_method == "sliding_window_average":
            self.rewards[chosen_arm].append(reward)
            if self.counts[chosen_arm] > self.sw_size:
                self.values[chosen_arm] = sum(
                    self.rewards[chosen_arm][-self.sw_size:])/self.sw_size
            else:
                self.values[chosen_arm] = sum(
                    self.rewards[chosen_arm])/self.counts[chosen_arm]
        else:
            raise ValueError("`value_estimation_method` must be either"
                             " 'sample_average' or 'sliding_window_average'")

    def update_batch(self, chosen_arms, rewards):
        for chosen_arm, reward in zip(chosen_arms, rewards):
            self.update(chosen_arm, reward)


class EpsilonGreedy(__baseMAB):
    '''Epsilon Greedy multi-armed bandit'''
    TUNER_NAME = "Epsilon-Greedy"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        epsilon = kwargs.get("epsilon")
        if epsilon is None:
            raise ValueError(
                "`epsilon` is required for EpsilonGreedy algorithm.")
        self.epsilon = kwargs.get("epsilon")

    def select_an_arm(self):
        if self.RS.rand() > self.epsilon:
            # Select the arm with maximum value
            selected_arm = max(self.values, key=self.values.get)
        else:
            # Randomly select an arm
            i_arm = self.RS.randint(0, len(self.feature_discrete))
            selected_arm = self.feature_discrete[i_arm]
        return selected_arm


class Softmax(__baseMAB):
    '''Softmax multi-armed bandit'''
    TUNER_NAME = "Softmax"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tau = kwargs.get("temperature")

    def select_an_arm(self):
        if self.tau is None:
            z = sum([math.exp(self.values[arm]) for arm in self.feature_discrete])
            probs = {arm: math.exp(self.values[arm]) / z for arm in self.feature_discrete}
        else:
            z = sum([math.exp(self.values[arm] / self.tau)
                     for arm in self.feature_discrete])
            probs = {arm: math.exp(
                self.values[arm] / self.tau) / z for arm in self.feature_discrete}
        # select one arm using Roulette selection
        r = self.RS.rand()
        cum_prob = 0.0
        for arm in self.feature_discrete:
            cum_prob += probs[arm]
            if cum_prob >= r:
                selected_arm = arm
                break
        return selected_arm


class SUS_Softmax(Softmax):
    ''' Stochastic Universal Selection (SUS) Softmax multi-armed bandit
        Reference
        ---------
        Book-Computational Itelligence: An Introduction. p.p.137
    '''
    TUNER_NAME = "SUS Softmax"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_multiple_arms(self, k):
        if self.tau is None:
            z = sum([math.exp(self.values[arm]) for arm in self.feature_discrete])
            probs = {arm: math.exp(self.values[arm]) / z for arm in self.feature_discrete}
        else:
            z = sum([math.exp(self.values[arm] / self.tau)
                     for arm in self.feature_discrete])
            probs = {arm: math.exp(
                self.values[arm] / self.tau) / z for arm in self.feature_discrete}
        spacing = 1.0/k
        r = self.RS.rand()/k
        cum_prob = 0.0
        selected_arms = []
        for arm in self.feature_discrete:
            cum_prob += probs[arm]
            while r < cum_prob:
                selected_arms.append(arm)
                r += spacing
        # randomly shuffle the list of strategy names
        # self.RS.shuffle(selected_arms)
        return selected_arms


class UCB(__baseMAB):
    '''Upper Confidence Bound (UCB) multi-armed bandit'''
    TUNER_NAME = "UCB"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def select_an_arm(self):
        for arm in self.feature_discrete:
            if self.counts[arm] == 0:
                return arm
        ucb_values = {arm: 0.0 for arm in self.feature_discrete}
        total_counts = sum(list(self.counts.values()))
        for arm in self.feature_discrete:
            bonus = math.sqrt(2 * math.log(total_counts) / self.counts[arm])
            ucb_values[arm] = self.values[arm] + bonus
        selected_arm = max(ucb_values, key=ucb_values.get)
        return selected_arm

    def select_multiple_arms(self, k):
        counts = deepcopy(self.counts)
        selected_arms = []
        for i in range(int(k)):
            ucb_values = {arm: 0.0 for arm in self.feature_discrete}
            total_counts = sum(list(counts.values()))
            for arm in self.feature_discrete:
                if counts[arm] == 0:
                    ucb_values[arm] = np.Inf
                else:
                    bonus = math.sqrt(2 * math.log(total_counts) / counts[arm])
                    ucb_values[arm] = self.values[arm] + bonus
            selected_arm = max(ucb_values, key=ucb_values.get)
            counts[selected_arm] = counts[selected_arm] + 1
            selected_arms.append(selected_arm)
        # self.RS.shuffle(selected_arms)
        return selected_arms



#!------------------------------------------------------------------------------
#!                                    FUNCTIONS
#!------------------------------------------------------------------------------



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    pass


if __name__ == "__main__":
    main()
