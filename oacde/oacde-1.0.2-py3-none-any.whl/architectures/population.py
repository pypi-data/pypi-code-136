#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Populations of evolutionary algorithms (EA)
    Vectorized version
'''
import numpy as np
from copy import deepcopy
# internal imports
from oacde.operators import PSO
from oacde.operators import DEmat as DE



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
class __base(object):
    ''' :class:`__base` is the base class for defining other population classes.
    '''

    def __init__(self, evaluate_func, nth_generation, random_number_generator):
        '''
        Creates a new :class:`__base` for populations.

        Parameters
        ----------
            To be specified in its successors

        Returns
        -------
        A population object.
        '''
        self._fobj = evaluate_func #! 禁止在外部使用此方法
        self.nth_generation = nth_generation
        self.rng = random_number_generator
        self.state = {"explore":None, "exploit":None, "neutral":None}
        # self._sum_distance = None
        # self._avg_distance = None
        # Attributes
        self.X, self.F = np.array([]), np.array([]),
        self.X_last, self.F_last = np.array([]), np.array([])
        self.X_hist, self.F_hist = [], []


    def __repr__(self):
        line1 = "A {} including {} individuals of {} dimensions:\n{}".format(
            type(self).__name__, self.shape[0], self.shape[1], self.X)
        return line1

    def __len__(self):
        return self.NP

    @property
    def NP(self):
        return self.shape[0]

    @property
    def evaluate(self,):
        return self._evaluate

    @evaluate.setter
    def evaluate(self, func):
        if callable(func):
            self._evaluate = func
        else:
            raise TypeError("The objective function must be collable, not a "
                            "type of {}".format(type(func)))

    @property
    def shape(self):
        return self.X.shape

    @property
    def rng(self):
        return self._rng

    @rng.setter
    def rng(self, value):
        if value is None or isinstance(value, np.random.RandomState):
            self._rng = value
        else:
            raise TypeError("{} object's `random_number_generator` attribute"
                " must be None or an instance of np.random.RandomState, not an"
                " instance of {}".format(type(self).__name__, type(value)))

    @property
    def X_last(self):
        return self._X_last

    @X_last.setter
    def X_last(self, array):
        self._X_last = deepcopy(array)

    @property
    def F_last(self):
        return self._F_last

    @F_last.setter
    def F_last(self, array):
        self._F_last = deepcopy(array)

    @property
    def X_mean(self):
        return np.mean(self.X, axis=0)

    @property
    def F_mean(self):
        return np.mean(self.F)

    @property
    def X_best(self):
        return self._X_best

    @property
    def F_best(self):
        return self._F_best

    # @property
    # def distance(self):
    #     return self._distance

    # @distance.setter
    # def distance(array):
    #     self._distance = array

    def find_best_individual(self):
        min_idx = np.argmin(self.F)
        self._X_best = self.X[min_idx, :]
        self._F_best = self.F[min_idx]


#! -------------------------- Differential Evolution --------------------------
class popDE(__base):
    ''' :class:`popDE` is the definition of population in DE methods.
    '''

    def __init__(self, evaluate_func, nth_generation=0,
        random_number_generator=None):
        '''
        Creates a new :class:`popDE` of DE algorithm.

        Parameters
        ----------
        nth_generation : int [default=0]
            A integer number to indicate the N-th generation of population. (If
            this value is -1, it represents a temporary population that shoud
            be eliminated after usage)
        random_number_generator : instance of np.random.RandomState
            [default=None]
            A random number generator.
        '''
        super().__init__(evaluate_func, nth_generation, random_number_generator)
        # Attributes
        # self._gen_hist = {"mutation": [], "crossover": [], "F": [], "CR": []}
        self.used_MUT = []
        self.used_CX = []

    def initialize(self, X0):
        self.X = X0
        self.F = self._fobj(X0)


#! ----------------------- Particle Swarm Optimization -----------------------
class popPSO(__base):
    ''' :class:`popPSO` is the definition of population in PSO methods.
    '''

    def __init__(self, evaluate_func, nth_generation=0,
                 random_number_generator=None,):
        '''
        Creates a new :class:`popPSO` of PSO algorithm.

        Parameters
        ----------
        evaluate_func : function
            Objective function of the optimization problem
        nth_generation : int [default=0]
            A integer number to indicate the N-th generation of population. (If
            this value is -1, it represents a temporary population that shoud
            be eliminated after usage)
        random_number_generator : instance of np.random.RandomState
            [default=None]
            A random number generator.
        '''
        super().__init__(evaluate_func, nth_generation, random_number_generator)
        # Attributes
        # self._gen_hist = {"topology": [],}

    #  ----------- Three Mainly used methods of popPSO class -----------
    def initialize(self, X0):
        self.X = X0
        self.F = self._fobj(X0)
        self.X_cog_best = deepcopy(X0)
        self.F_cog_best = deepcopy(self.F)
        self.V = np.zeros(X0.shape)


#! ----------------------- Mixture -----------------------
class popPSO_DE(popPSO, popDE):
    ''' :class:`PSO_DE` is the definition of population in PSO-DE methods.
    '''

    def __init__(self, evaluate_func, nth_generation=0,
                 random_number_generator=None,):
        '''
        Creates a new :class:`PSO_DE` of PSO_DE algorithm.

        Parameters
        ----------
        evaluate_func : function
            Objective function of the optimization problem
        nth_generation : int [default=0]
            A integer number to indicate the N-th generation of population. (If
            this value is -1, it represents a temporary population that shoud
            be eliminated after usage)
        random_number_generator : instance of np.random.RandomState
            [default=None]
            A random number generator.
        '''
        super().__init__(evaluate_func, nth_generation, random_number_generator)
        # Attributes
        # self._gen_hist = {"topology": [], "mutation": [], "crossover": [],
        #     "F": [], "CR": []}

    def initialize(self, X0):
        popPSO.initialize(self, X0)



#!------------------------------------------------------------------------------
#!                                    FUNCTIONS
#!------------------------------------------------------------------------------
def get_f(object):
    return object.fvalue



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
        main()
