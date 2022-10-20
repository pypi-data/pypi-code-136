#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Distribution based family
'''
import numpy as np
import scipy.stats as ss
# internal imports
from oacde.tuners._base import __base



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
class __DistCommonProp(__base):
    '''Define some common properties for all distributions'''

    def __init__(self, RS, feature_discrete=None, feature_continued=None,
        lower_bound="truncate", upper_bound="truncate"):
        '''Initialize a distribution-like model

        :param RS: random number generator
        :type RS: np.RandomState
        :param feature_discrete: list of discrete features
        :type feature_discrete: list, tuple or ndarray
        :param feature_continued: min and max of continued features
        :type feature_continued: list, tuple or ndarray
        :param lower_bound: method to use when value is less than lower bound
        :type lower_bound: str
        :param upper_bound: method to use when value is higher than upper bound
        :type upper_bound: str
        '''
        self.RS = RS
        self.feature_discrete = feature_discrete
        self.feature_continued = feature_continued
        self.clip_lower_bound = lower_bound
        self.clip_upper_bound = upper_bound

    @property
    def clip_lower_bound(self):
        return self._clip_lower_bound

    @clip_lower_bound.setter
    def clip_lower_bound(self, name):
        if name.lower() == "truncate":
            self._clip_lower_bound = self.truncate_lower_bound
        elif name.lower() == "regenerate":
            self._clip_lower_bound = self.regenerate_lower_bound
        else:
            raise ValueError("`lower_bound` method must be either 'truncate' or"
                             "'regenerate'")

    @property
    def clip_upper_bound(self):
        return self._clip_upper_bound

    @clip_upper_bound.setter
    def clip_upper_bound(self, name):
        if name.lower() == "truncate":
            self._clip_upper_bound = self.truncate_upper_bound
        elif name.lower() == "regenerate":
            self._clip_upper_bound = self.regenerate_upper_bound
        else:
            raise ValueError("`upper_bound` method must be either 'truncate' or"
                             " 'regenerate'")

    def regenerate_lower_bound(self, array):
        flag = array < self.feature_continued[0]
        while flag.any() == True:
            array[flag] = self.sample_method(len(array[flag]))
            flag = array < self.feature_continued[0]
        return array

    def regenerate_upper_bound(self, array):
        flag = array > self.feature_continued[1]
        while flag.any() == True:
            array[flag] = self.sample_method(len(array[flag]))
            flag = array > self.feature_continued[1]
        return array

    def truncate_lower_bound(self, array):
        array[array < self.feature_continued[0]] = self.feature_continued[0]
        return array

    def truncate_upper_bound(self, array):
        array[array > self.feature_continued[1]] = self.feature_continued[1]
        return array

    def sample_method(self, size):
        '''To be defined by each distribution'''
        return self.dist.rvs(loc=self.loc, scale=self.scale, size=size,
                             random_state=self.RS)

    def generate_discrete(self, size):
        pass

    def generate_continued(self, size):
        _ = self.sample_method(size)
        _ = self.clip_lower_bound(_)
        _ = self.clip_upper_bound(_)
        return _

    def update(self, **kwargs):
        self.loc = kwargs.get("loc", self.loc)
        self.scale = kwargs.get("scale", self.scale)


## ------------------------------ Uniform Random ------------------------------
class Uniform(__DistCommonProp):
    '''Uniform Random tuner'''
    TUNER_NAME = "Uniform Random"

    def __init__(self, RS, feature_discrete=None, feature_continued=None,
        lower_bound="truncate", upper_bound="truncate", *args, **kwargs):
        '''Initialize an Uniform Random model

        :param RS: random number generator
        :type RS: np.RandomState
        :param feature_discrete: list of discrete features
        :type feature_discrete: list, tuple or ndarray
        :param feature_continued: min and max of continued features
        :type feature_continued: list, tuple or ndarray
        '''
        super().__init__(RS, feature_discrete, feature_continued, lower_bound,
            upper_bound)

    def generate_discrete(self, size):
        return np.array(self.feature_discrete * size)[:size]

    def generate_continued(self, size):
        return self.RS.uniform(
            self.feature_continued[0], self.feature_continued[1], size)

    def update(self, **kwargs):
        raise NotImplementedError()


## --------------------------- Roulette Wheel Random ---------------------------
class Roulette(__DistCommonProp):
    '''Roulette Wheel Random tuner'''
    TUNER_NAME = "Roulette Wheel Random"

    def __init__(self, RS, feature_discrete=None, feature_continued=None,
        lower_bound="truncate", upper_bound="truncate", *args, **kwargs):
        '''Initialize a Roulette Wheel Random model

        :param RS: random number generator
        :type RS: np.RandomState
        :param feature_discrete: list of discrete features
        :type feature_discrete: list, tuple or ndarray
        :param feature_continued: min and max of continued features
        :type feature_continued: list, tuple or ndarray
        :param prob_discrete: probability of each corresponding feature
        :type prob_discrete: list, tuple or ndarray
        '''
        super().__init__(RS, feature_discrete, feature_continued, lower_bound,
            upper_bound)
        self.prob_discrete = kwargs.get("prob_discrete")

    #// HB: old implementation
    # @property
    # def prob_discrete(self):
    #     return self._prob_discrete

    # @prob_discrete.setter
    # def prob_discrete(self, list_prob):
    #     if not self.feature_discrete is None:
    #         if list_prob is None:
    #             length = len(self.feature_discrete)
    #             self._prob_discrete = [1/length, ] * length
    #         else:
    #             self._prob_discrete = list_prob

    # def generate_discrete(self, size, *args, **kwargs):
    #     _ = []
    #     for __ in range(size):
    #         i = 0
    #         cumul_prob = self.prob_discrete[i]
    #         r = self.RS.rand()
    #         while cumul_prob < r:
    #             i += 1
    #             cumul_prob += self.prob_discrete[i]
    #         _.append(self.feature_discrete[i])
    #     return np.array(_)

    def generate_discrete(self, size):
        return self.RS.choice(self.feature_discrete, size, p=self.prob_discrete)

    def generate_continued(self, size):
        return self.RS.rand(size) \
                * (self.feature_continued[1]-self.feature_continued[0]) \
                + self.feature_continued[0]

    def update(self, **kwargs):
        raise NotImplementedError()

## --------------------------- Normal Random ---------------------------
class Normal(__DistCommonProp):
    '''Normal Random tuner'''
    TUNER_NAME = "Normal Random"

    def __init__(self, RS, feature_discrete=None, feature_continued=None,
        lower_bound="truncate", upper_bound="truncate", *args, **kwargs):
        '''Initialize a Normal Random model

        :param RS: random number generator
        :type RS: np.RandomState
        :param feature_discrete: list of discrete features
        :type feature_discrete: list, tuple or ndarray
        :param feature_continued: min and max of continued features
        :type feature_continued: list, tuple or ndarray

        Reference
        --------
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html?highlight=norm
        '''
        super().__init__(RS, feature_discrete, feature_continued, lower_bound,
            upper_bound)
        self.loc = kwargs.get("loc", 0)
        self.scale = kwargs.get("scale", 1)
        # Additional attributes
        self.dist = ss.norm  # ! careful: ss.norm ≠ ss.norm()

    def generate_discrete(self, size, *args, **kwargs):
        raise NotImplementedError()


## --------------------------- Cauchy Random ---------------------------
class Cauchy(__DistCommonProp):
    '''Cauchy Random tuner'''
    TUNER_NAME = "Cauchy Random"

    def __init__(self, RS, feature_discrete=None, feature_continued=None,
        lower_bound="truncate", upper_bound="truncate", *args, **kwargs):
        '''Initialize a Cauchy Random model

        :param RS: random number generator
        :type RS: np.RandomState
        :param feature_discrete: list of discrete features
        :type feature_discrete: list, tuple or ndarray
        :param feature_continued: min and max of continued features
        :type feature_continued: list, tuple or ndarray

        Reference
        --------
        https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.cauchy.html?highlight=cauchy
        '''
        super().__init__(RS, feature_discrete, feature_continued, lower_bound,
            upper_bound)
        self.loc = kwargs.get("loc", 0)
        self.scale = kwargs.get("scale", 1)
        # Additional attributes
        self.dist = ss.cauchy #! careful: ss.cauchy ≠ ss.cauchy()

    def generate_discrete(self, size, *args, **kwargs):
        raise NotImplementedError()



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
