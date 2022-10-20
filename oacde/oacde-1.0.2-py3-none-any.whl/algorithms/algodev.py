#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Algorithms in developping
    Vectorized version
'''
import numpy as np
from copy import deepcopy
# internal imports
import oacde.operators as oper
from oacde.algorithms.algoDE import DE
from oacde import tuners as tune
from oacde.publics import parameterize as para



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
## --------- Online Algorithm Configuration for Differential Evolution ---------
class OACDE(DE):
    ''' :class:`OACDE` refers to Online Algorithm Configuration for
        Differential Evolution algorithm

        Features
        --------
        - A MAB bndit model for mutation and crossover operator
        - Each pair of mutation and crossover has a KDE model for F and CR pair

        References
        ---------
        C. Huang, H. Bai, X. Yao, Online Algorithm Configuration for
        Differential Evolution Algorithm, 2021
    '''
    ALGO_NAME = "OACDE"
    # CONFIG_TYPE = para.DE

    def __init__(self,
                 opt_problem,
                 algo_parameters,
                 stop_conditions,
                 stagnation_gen, # 10
                 tuning_level,
                 model_utilization_strategy, # "strategy1", "strategy2"
                 KDE_kernel,
                 KDE_width,
                 KDE_max_size,
                 MAB_algo,
                 MAB_value_method,
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        #* Attributes
        self.STRATEGY_POOL = {
            "uniform": (self.__generate_by_uniform, lambda: None),
            "random": (self.__generate_by_random, lambda: None),
            "success": (self.__generate_by_success, lambda: None),
            "success_tau": (self.__generate_by_success,
                            self.__reconfig_tau),
            "success_reset_tau": (self.__generate_by_success,
                                  self.__reconfig_reset_tau),
            "success_resetKDE": (self.__generate_by_success,
                                 self.__reconfig_resetKDE),
            "success_resetKDE_tau": (self.__generate_by_success,
                                     self.__reconfig_resetKDE_tau),
            }
        #* Affect values to attributes
        self.stagnation_gen = stagnation_gen
        self.tuning_level = tuning_level
        self.model_utilization_strategy = model_utilization_strategy
        # Each arm is a combination of mutation and crossover operator, i.e., a generation strategy
        generation_strategies = []
        for mut in self.MUT_POOL:
            for cx in self.CX_POOL:
                # if mut == "de/current-to-rand/1":
                #     cx = "none"
                generation_strategies.append((mut, cx))
        self.generation_strategies = generation_strategies
        arms = sorted(set(generation_strategies),
                      key=generation_strategies.index)
        self.strategy_arms = arms
        self.MAB_algo = MAB_algo
        self.gen_effective = 0
        self.gen_ineffective = 0

        # A bandit model which focuses on the performance of each arm
        # self.success_bandit_values = {str(arm): [] for arm in arms}
        if self.model_utilization_strategy == "random" or self.model_utilization_strategy == "uniform":
            self.MUT_model = tune.initialize_model(
                model_name=self.model_utilization_strategy,
                RS=self.para.rng,
                feature_discrete=tuple(self.MUT_POOL.keys()))
            self.CX_model = tune.initialize_model(
                model_name=self.model_utilization_strategy,
                RS=self.para.rng,
                feature_discrete=tuple(self.CX_POOL.keys()))
            self.F_model = tune.initialize_model(
                model_name=self.model_utilization_strategy,
                RS=self.para.rng,
                feature_continued=self.F_RANGE)
            self.CR_model = tune.initialize_model(
                model_name=self.model_utilization_strategy,
                RS=self.para.rng,
                feature_continued=self.CR_RANGE)
        else:
            self.MUT_CX_model = tune.initialize_model(
                model_name=MAB_algo,
                RS=self.para.rng,
                feature_discrete=arms,
                value_estimation_method=MAB_value_method,
                **kwargs)
            F_CR_range = ((self.F_RANGE[0], self.CR_RANGE[0]),
                        (self.F_RANGE[1], self.CR_RANGE[1]))
            self.F_CR_model = {
                arm: tune.initialize_model(
                    model_name="KDE",
                    RS=self.para.rng,
                    feature_continued=F_CR_range,
                    kernel=KDE_kernel,
                    bandwidth=KDE_width,
                    feature_name=["F", "CR"],
                    max_training_size=KDE_max_size,)
                for arm in arms}

    @property
    def model_utilization_strategy(self):
        return self._model_utilization_strategy

    @model_utilization_strategy.setter
    def model_utilization_strategy(self, strategy_name):
        self._generate_configs = self.STRATEGY_POOL.get(strategy_name)[0]
        self._reconfig_models = self.STRATEGY_POOL.get(strategy_name)[1]
        if self._generate_configs is None:
            raise ValueError("`model_utilization_strategy` get an unexpected "
                             "strategy name '{}'. The allowable strategy names "
                             "are: {}"
                             .format(strategy_name, self.STRATEGY_POOL.keys()))
        else:
            self._model_utilization_strategy = strategy_name

    @property
    def MAB_algo(self):
        return self._MAB_algo

    @MAB_algo.setter
    def MAB_algo(self, MAB_name):
        if "tau" in self.model_utilization_strategy:
            if not "softmax" in MAB_name.lower():
                raise ValueError("When use `{}` strategy, the `MAB_algo` "
                                 "must be either 'Softmax' or 'SUS_Softmax', "
                                 "not '{}'"
                                 .format(self.model_utilization_strategy,
                                 MAB_name))
        self._MAB_algo = MAB_name

    # --------------------------- Internal Methods ---------------------------
    def _evolve_by_population(self):
        #* generate a set of configuration
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(
            min(self.pop.NP, self.stop.max_FES - self.pb.num_calls))
        self.configs_assignment = self._generate_configs(n_trials)
        #* adapt mutation
        mutate = self.MUT_POOL.get(self.pop.config_MUT[0])
        F = self.pop.config_F[0]
        self.pop.X_mutant = mutate(
            self.pop.X, F, self.pop.rng, fitness=self.pop.F)
        #* adapt crossover
        crossover = self.pop.config_CX[0]
        CR = self.pop.config_CR[0]
        self.pop.X_trial = crossover(
            self.pop.X, self.pop.X_mutant, CR, self.pop.rng,
            operator=oper.DEmat.bin)
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

    def _evolve_by_individual(self):
        #* Pre-step: update tuning model if necessary
        if self.gen_ineffective >= self.stagnation_gen:
            self._reconfig_models()  # change MAB or KDE models if necessary

        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        MUTs, CXs = self._generate_configs(n_trials)
        unique, counts = np.unique(MUTs, return_counts=True)
        self.pop.config_MUT = list(zip(unique, counts.cumsum()))
        unique, counts = np.unique(CXs, return_counts=True)
        self.pop.config_CX = list(zip(unique, counts.cumsum()))

        #* adapt mutation
        # initiate by using the 1st mutation operator
        mutate = self.MUT_POOL.get(self.pop.config_MUT[0][0])
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
            fitness=self.pop.F)
        _ = [pop[:self.pop.config_MUT[0][1], :], ]
        self.pop.used_MUT = [
            self.pop.config_MUT[0][0], ] * self.pop.config_MUT[0][1]
        #
        tmp = map(
            self.__mutate_individually, range(1,len(self.pop.config_MUT)))
        _.extend(list(tmp))
        self.pop.X_mutant = np.vstack(_)
        self.pop.used_MUT = np.array(self.pop.used_MUT)
        self.pop.used_F = np.array(self.pop.config_F)
        # print("Config_MUT:", self.pop.config_MUT)

        #* adapt crossover
        # initiate by using the 1st crossover operator
        crossover = self.CX_POOL.get(self.pop.config_CX[0][0])
        pop = crossover(self.pop.X, self.pop.X_mutant, self.pop.config_CR,
            self.pop.rng)
        _ = [pop[:self.pop.config_CX[0][1], :], ]
        self.pop.used_CX = [
            self.pop.config_CX[0][0], ] * self.pop.config_CX[0][1]
        #
        tmp = map(
            self.__crossover_individually,range(1, len(self.pop.config_CX)))
        _.extend(list(tmp))
        self.pop.X_trial = np.vstack(_)
        self.pop.used_CX = np.array(self.pop.used_CX)
        self.pop.used_CR = np.array(self.pop.config_CR)
        # print("Config_CX", self.pop.config_CX)

        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

        #* Add-step: update KDE and MAB models' training data
        self.update_models(self.survival_idx)
        # print("")


    # --------------------------- Overwrite Methods ---------------------------
    def update_models(self, idx):
        '''Update tuning model's training data based on index of individuals

        :param idx: index of individuals to be updated
        :type idx: ndarray
        '''
        if self.model_utilization_strategy == "random" or self.model_utilization_strategy == "uniform":
            pass
        else:
            # update bandits
            _ = zip(self.pop.used_MUT[idx], self.pop.used_CX[idx])
            used_bandits = deepcopy(list(_))
            length = self.pop.used_MUT[idx].shape[0]
            # print("used_bandit:", used_bandits, length)
            # print("BANDIT BEFORE:", self.MUT_CX_model.values)
            self.MUT_CX_model.update_batch(used_bandits, [1.0, ] * length)
            # print("BANDIT AFTER:",self.MUT_CX_model.values)
            # update KDEs
            __ = list(zip(self.pop.used_F[idx]/2, self.pop.used_CR[idx]))
            for i, elem in enumerate(used_bandits):
                self.F_CR_model[elem].add_data(__[i])

    def _update_pop_attribute(self):
        ''' Update best solution found so far'''
        super()._update_pop_attribute()
        if self.pop.F_best < (self.pb.f_opt - self.stop.delta_ftarget):
            self.gen_effective += 1
            self.gen_ineffective = 0
        else:
            self.gen_ineffective += 1
            self.gen_effective = 0


    # ---------------------------- Private Methods ----------------------------
    def __mutate_individually(self, i):
        ''' Mutate the entire population by a given configuration '''
        i0 = self.pop.config_MUT[i][0]
        i1 = self.pop.config_MUT[i][1]
        i1_prev = self.pop.config_MUT[i-1][1]
        mutate = self.MUT_POOL.get(i0)
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        used_MUT = [i0,] * (i1 - i1_prev)
        self.pop.used_MUT.extend(used_MUT)
        return pop[i1_prev:i1]

    def __crossover_individually(self, i):
        ''' Crossover the entire population by a given configuration '''
        i0 = self.pop.config_CX[i][0]
        i1 = self.pop.config_CX[i][1]
        i1_prev = self.pop.config_CX[i-1][1]
        crossover = self.CX_POOL.get(i0)
        pop = crossover(self.pop.X, self.pop.X_mutant, self.pop.config_CR,
                        self.pop.rng)
        used_CX = [i0, ] * (i1 - i1_prev)
        self.pop.used_CX.extend(used_CX)
        return pop[i1_prev:i1]

    def __generate_by_uniform(self, size):
        ''' Generate equally configurations '''
        array_MUT = self.MUT_model.generate_discrete(size)
        self.pop.config_F = self.F_model.generate_continued(size)
        array_CX = self.CX_model.generate_discrete(size)
        self.pop.config_CR = self.CR_model.generate_continued(size)
        return array_MUT, array_CX

    def __generate_by_random(self, size):
        ''' Randomize uniformly configurations '''
        array_MUT = self.MUT_model.generate_discrete(size)
        self.pop.config_F = self.F_model.generate_continued(size)
        array_CX = self.CX_model.generate_discrete(size)
        self.pop.config_CR = self.CR_model.generate_continued(size)
        return array_MUT, array_CX

    def __generate_by_success(self, size):
        ''' Randomize algorithmic configurations using KDE (for F and CR) and
            MAB (for MUT and CX) models that have created survival offsprings
            during the passed generations

            Remarks
            -------
            `F_RANGE` is normalized to [0.0, 1.0] in this configuration
        '''
        list_mut_cx = self.MUT_CX_model.select_multiple_arms(k=size)
        list_F_CR = [self.F_CR_model[(mut, cx)].sample(n_samples=1)[0]
                     for (mut, cx) in list_mut_cx]
        array_MUT = np.array([mut_cx[0] for mut_cx in list_mut_cx])
        self.pop.config_F = np.array([F_CR[0] * 2 for F_CR in list_F_CR])
        array_CX = np.array([mut_cx[1] for mut_cx in list_mut_cx])
        self.pop.config_CR = np.array([F_CR[1] for F_CR in list_F_CR])
        return array_MUT, array_CX

    def __reconfig_tau(self):
        non_zeros = [v for v in self.MUT_CX_model.values.values() if v > 0.0]
        if non_zeros != []:
            self.MUT_CX_model.tau = min(non_zeros)

    def __reconfig_reset_tau(self):
        self.MUT_CX_model.reset()  # reset MAB model

    def __reconfig_resetKDE(self):
        for arm in self.strategy_arms:  # reset KDE model
            self.F_CR_model[arm].reset()

    def __reconfig_resetKDE_tau(self):
        self.MUT_CX_model.reset() # reset MAB model
        for arm in self.strategy_arms: # reset KDE model
            self.F_CR_model[arm].reset()



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    from oacde.problems import problem as pb

    seed = 0  # ! HB: don't change this value
    # rng = np.random.RandomState(seed)
    # list_seed = tuple(rng.randint(0, 2**31-1, 25))
    case = "ALL"
    outputs = []

    ## 1. Problem Configuration
    benchmark = "bbob2015"
    D = 2
    funID = 15 # 8 9 Rosenbrock , 15 Rastrigin
    problem = pb.Benchmark(benchmark_set=benchmark, D=D, funID=funID,
        instanceID=1)

    ## 2. Algorithm Configuration
    NP = 24
    config = para.DE(seed = seed,
                     N = NP,
                     mutation='de/rand/1'
                     )
    stop = para.StopCondition(max_FES=100.*NP, max_iter=None, delta_ftarget=1e-8)

    ## 3. Aglorithm Selection: using DE random algorithm
    if case == "OACDE" or case == 1 or case == "ALL":
        print("--- Testing OACDE:")
        optimizer = OACDE(opt_problem=problem,
                          algo_parameters=config,
                          stop_conditions=stop,
                          mut_pool=[
                           "de/rand/1", # CoDE, SaDE, EPSDE, SAKPDE, jDE
                           "de/rand/2", # CoDE, SaDE, SAKPDE
                           "de/best/2", # EPSDE, SAKPDE
                           "de/current-to-best/2",  # SaDE, SAKPDE
                           "de/current-to-rand/1",  # CoDE, SaDE, EPSDE
                           "de/current-to-pbest/1", # JADE, SHADE
                           ],
                          cx_pool=["bin", "exp"],
                          tuning_level="individual_level",
                          F_range=(0.0, 1.0),
                          CR_range=(0.0, 1.0),
                          model_utilization_strategy="success",
                          stagnation_gen=10,
                          KDE_kernel="gaussian",
                          KDE_width=1/3,
                          KDE_max_size=None,
                          MAB_algo="ucb",
                          MAB_value_method="sample_average",
                          epsilon=0.2,
                          temperature=None,
                          sliding_window_size=None, # required for
                                                    # "sliding_window_average"
                          )
        results = optimizer.solve(disp=1)
        # 5. Post-processing
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    print(optimizer.history)

if __name__ == "__main__":
    main()
