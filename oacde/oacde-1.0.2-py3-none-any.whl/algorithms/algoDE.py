#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Differential evolution (DE) algorithm family
    Vectorized version
'''
import numpy as np
from collections import OrderedDict
# internal imports
from oacde import tuners as tune
from oacde import operators as oper
from oacde.algorithms._algo import __base
from oacde.architectures.population import popDE
from oacde.publics import parameterize as para



#!------------------------------------------------------------------------------
#!                          Basic DE and Randomized DE
#!------------------------------------------------------------------------------
## ----------------------- Differential Evolution basic -----------------------
class DE(__base):
    ''' :class:`DE` refers the basic/standard Differential Evolution (DE)

        Reference
        ---------
        R. Storn et al., Differential Evolution – A Simple and Efficient
        Heuristic for Global Optimization over Continuous Spaces, 1997
    '''
    ALGO_NAME = "Basic DE"
    CONFIG_TYPE = para.DE

    _MUT_POOL = {"de/rand/1": oper.DEmat.rand_1, # 3),
                 "de/rand/2": oper.DEmat.rand_2, # 5),
                 "de/best/1": oper.DEmat.best_1, # 2),
                 "de/best/2": oper.DEmat.best_2, # 4),
                 "de/rand-to-best/1": oper.DEmat.rand_to_best_1, # 3),
                 "de/rand-to-pbest/1": oper.DEmat.rand_to_pbest_1, # 3),
                 "de/current/1": oper.DEmat.current_1, # 2),
                 "de/current-to-rand/1": oper.DEmat.current_to_rand_1, # 3),
                 "de/current-to-best/1": oper.DEmat.current_to_best_1, # 2),
                 "de/current-to-best/2": oper.DEmat.current_to_best_2, # 4),
                 "de/current-to-pbest/1": oper.DEmat.current_to_pbest_1, # 2),
                }
    _CX_POOL = {"bin": oper.DEmat.bin,
                "exp": oper.DEmat.exp,
                "eig": oper.DEmat.eig,
                "none": oper.DEmat.none
               }
    _F_RANGE = (0.0, 2.0)
    _CR_RANGE = (0.0, 1.0)

    def __init__(self, opt_problem,
                 algo_parameters=para.DE(),
                 stop_conditions=para.StopCondition(),
                 **kwargs):
        super().__init__(opt_problem, algo_parameters, stop_conditions)
        self.pop = popDE(
            opt_problem.fobj, random_number_generator=self.para.rng)
        self.MUT_POOL = kwargs.get("mut_pool",)
        self.CX_POOL = kwargs.get("cx_pool",)
        self.F_RANGE = kwargs.get("F_range",)
        self.CR_RANGE = kwargs.get("CR_range",)
        self.mutate = self.para.mutation
        self.crossover = self.para.crossover

    @property
    def MUT_POOL(self):
        return self._MUT_POOL

    @MUT_POOL.setter
    def MUT_POOL(self, name_list):
        if not name_list is None:
            self._MUT_POOL = {k: self._MUT_POOL.get(k) for k in name_list}

    @property
    def CX_POOL(self):
        return self._CX_POOL

    @CX_POOL.setter
    def CX_POOL(self, name_list):
        if not name_list is None:
            self._CX_POOL = {k: self._CX_POOL.get(k) for k in name_list}

    @property
    def F_RANGE(self):
        return self._F_RANGE

    @F_RANGE.setter
    def F_RANGE(self, value_range):
        if not value_range is None:
            self._F_RANGE = value_range

    @property
    def CR_RANGE(self):
        return self._CR_RANGE

    @CR_RANGE.setter
    def CR_RANGE(self, value_range):
        if not value_range is None:
            self._CR_RANGE = value_range

    @property
    def mutate(self):
        return self._mutate

    @mutate.setter
    def mutate(self, name):
        self._mutate = self.MUT_POOL.get(name)
        if self._mutate is None:
            raise ValueError("Mutation operator '{}' is not supported in {}"
                             " algorithm, available options are:\n{}"
                             .format(name, type(self).__name__,
                             self.MUT_POOL.keys()))

    @property
    def crossover(self):
        return self._crossover

    @crossover.setter
    def crossover(self, name):
        self._crossover = self.CX_POOL.get(name)
        if self._crossover is None:
            raise ValueError("Crossover operator '{}' is not supported in {}"
                             " algorithm, available options are:\n{}"
                             .format(name, type(self).__name__,
                             self.CX_POOL.keys()))

    # --------------------- Methods reserved for variants ---------------------
    @property
    def tuning_level(self):
        return self._tuning_level

    @tuning_level.setter
    def tuning_level(self, level):
        if isinstance(level, str):
            if level == "population_level":
                self._evolve_a_generation = self._evolve_by_population
            elif level == "individual_level":
                self._evolve_a_generation = self._evolve_by_individual
            else:
                raise NameError("`tuning_level` get an unexpected level name "
                                "'{}'. The allowable level names are: "
                                "'individual_level' or 'population_level'"
                                .format(level))
        else:
            raise TypeError("The level, at which hyperparameters are randomly "
                            "assigned, must be a string, not a {}"
                            .format(type(level).__name__))
        self._tuning_level = level

    def survive(self):
        self.pop.X_last, self.pop.F_last = self.pop.X, self.pop.F
        self.pop.X, self.pop.F, self.survival_idx = oper.select(
            self.pop.X, self.pop.F, self.pop.X_trial, self.pop.F_trial)

    def _evolve_a_generation(self):
        #* adapt mutation
        self.pop.X_mutant = self.mutate(
            self.pop.X, self.para.F, self.pop.rng, fitness=self.pop.F)
        self.pop.used_MUT, self.pop.used_F = self.para.mutation, self.para.F
        #* adapt crossover
        self.pop.X_trial = self.crossover(
            self.pop.X, self.pop.X_mutant, self.para.CR, self.pop.rng,
            operator=oper.DEmat.bin)
        self.pop.used_CX, self.pop.used_CR = self.para.crossover, self.para.CR
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        #* compare parents to offsprings
        self.survive()


## ----------------------- Random Control Parameters DE -----------------------
class RandomDE(DE):
    ''' :class:`RandomDE` refers to randomly generate hyperparameters for each
        Population or Individual
        Two options are available:
            - "population_level": at each generation, new parameter setting is
                sampled for generating new population.
            - "individual_level": new parameter setting is sampled when
                generating each new individual
    '''
    ALGO_NAME = "Random DE"
    # CONFIG_TYPE = para.DE

    def __init__(self, opt_problem,
                 algo_parameters=para.DE(),
                 stop_conditions=para.StopCondition(),
                 tuning_level="individual_level",
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self.tuning_level = tuning_level
        # generate random values for hyperparameter
        if self.tuning_level == "population_level":
            size = int(self.stop.max_FES/self.para.N)
        elif self.tuning_level == "individual_level":
            size = int(self.stop.max_FES)
        self.mut_candidate = self.para.rng.choice(
            list(self.MUT_POOL.keys()), size=size, replace=True)
        self.F_candidate = self.para.rng.uniform(
            self.F_RANGE[0], self.F_RANGE[1], size)
        self.cx_candidate = self.para.rng.choice(
            list(self.CX_POOL.keys()), size=size, replace=True)
        self.CR_candidate = self.para.rng.uniform(
            self.CR_RANGE[0], self.CR_RANGE[1], size)

    def _evolve_by_population(self):
        #* adapt mutation
        mutate = self.MUT_POOL.get(self.mut_candidate[0])
        F, self.F_candidate = self.F_candidate[0], self.F_candidate[1:]
        self.pop.X_mutant = mutate(
            self.pop.X, F, self.pop.rng, fitness=self.pop.F)
        self.pop.used_MUT, self.pop.used_F = self.mut_candidate[0], F
        self.mut_candidate = self.mut_candidate[1:]
        #* adapt crossover
        crossover = self.CX_POOL.get(self.cx_candidate[0])
        CR, self.CR_candidate = self.CR_candidate[0], self.CR_candidate[1:]
        self.pop.X_trial = crossover(
            self.pop.X, self.pop.X_mutant, CR, self.pop.rng,
            operator=oper.DEmat.bin)
        self.pop.used_CX, self.pop.used_CR = self.cx_candidate[0], CR
        self.cx_candidate = self.cx_candidate[1:]
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

    def _evolve_by_individual(self):
        #* adapt mutation
        self.__config_mutation()
        # initiate by using the 1st mutation operator
        mutate = self.MUT_POOL.get(self.pop.config_MUT[0][0])
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
            fitness=self.pop.F)
        _ = [pop[:self.pop.config_MUT[0][1], :], ]
        tmp = map(self.__mutate_individually, range(1,len(self.pop.config_MUT)))
        _.extend(list(tmp))
        self.pop.X_mutant = np.vstack(_)
        self.pop.used_F = self.pop.config_F
        #* adapt crossover
        self.__config_crossover()
        # initiate by using the 1st crossover operator
        crossover = self.CX_POOL.get(self.pop.config_CX[0][0])
        pop = crossover(self.pop.X, self.pop.X_mutant, self.pop.config_CR,
            self.pop.rng)
        _ = [pop[:self.pop.config_CX[0][1], :], ]
        tmp=map(self.__crossover_individually,range(1, len(self.pop.config_CX)))
        _.extend(list(tmp))
        self.pop.X_trial = np.vstack(_)
        self.pop.used_CR = self.pop.config_CR
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

    # ---------------------------- Private Methods ----------------------------
    def __config_mutation(self,):
        ''' Select mutation operators and associate F '''
        array_MUT = self.mut_candidate[:self.para.N]
        self.mut_candidate = self.mut_candidate[self.para.N:]
        self.pop.config_F = self.F_candidate[:self.para.N]
        self.F_candidate = self.F_candidate[self.para.N:]
        unique, counts = np.unique(array_MUT, return_counts=True)
        self.pop.config_MUT = list(zip(unique, counts.cumsum()))
        self.pop.used_MUT = array_MUT

    def __config_crossover(self,):
        ''' Select crossover operators and associate CR '''
        array_CX = self.cx_candidate[:self.para.N]
        self.cx_candidate = self.cx_candidate[self.para.N:]
        self.pop.config_CR = self.CR_candidate[:self.para.N]
        self.CR_candidate = self.CR_candidate[self.para.N:]
        unique, counts = np.unique(array_CX, return_counts=True)
        self.pop.config_CX = list(zip(unique, counts.cumsum()))
        self.pop.used_CX = array_CX

    def __mutate_individually(self, i):
        ''' Mutate the entire population by a given configuration '''
        mutate = self.MUT_POOL.get(self.pop.config_MUT[i][0])
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        return pop[self.pop.config_MUT[i-1][1]:self.pop.config_MUT[i][1]]

    def __crossover_individually(self, i):
        ''' Crossover the entire population by a given configuration '''
        crossover = self.CX_POOL.get(self.pop.config_CX[i][0])
        pop = crossover(self.pop.X, self.pop.X_mutant, self.pop.config_CR,
                        self.pop.rng)
        return pop[self.pop.config_CX[i-1][1]:self.pop.config_CX[i][1]]



#!------------------------------------------------------------------------------
#!      Operators (mutation and crossover) & Control parameters (F and CR)
#!------------------------------------------------------------------------------
## DE with Composite Trial Vector Generation Strategies and Control Parameters
class CoDE(DE):
    ''' :class:`CoDE` refers to DE with Composite Trial Vector Generation
        Strategies and Control Parameters algorithm

        Reference
        ---------
        Y. Wang, Z. Cai and Q. Zhang, "Differential Evolution With Composite
        Trial Vector Generation Strategies and Control Parameters",
        in IEEE Transactions on Evolutionary Computation,
        vol. 15, no. 1, pp. 55-66, Feb. 2011
    '''
    ALGO_NAME = "CoDE"

    _MUT_CX_POOL = np.array([("de/rand/1", "bin"),
                             ("de/rand/2", "bin"),
                             ("de/current-to-rand/1", "none")])
    _F_CR_POOL = np.array([(1.0, 0.1), (1.0, 0.9), (0.8, 0.2)])

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(),
                 stop_conditions=para.StopCondition(),
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        # Attributes
        self._evolve_a_generation = self._evolve_by_individual
        self.mutates = [
            self.MUT_POOL.get(self.MUT_CX_POOL[i, 0]) for i in range(3)]
        self.crossovers = [
            self.CX_POOL.get(self.MUT_CX_POOL[i, 1]) for i in range(3)]

    @property
    def MUT_CX_POOL(self,):
        return self._MUT_CX_POOL

    @property
    def F_CR_POOL(self,):
        return self._F_CR_POOL

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        self.pop.X_last, self.pop.F_last = self.pop.X, self.pop.F

        used_MUT, used_F, used_CX, used_CR = [], [], [], []
        for i in range(3):
            #* generate configuration for hyperparameters
            # Find how many trial individuals can be generated:
            if self.stop.max_FES < self.pb.num_calls: #! need to reimplement
                self.pop.used_MUT, self.pop.used_F = used_MUT, used_F
                self.pop.used_CX, self.pop.used_CR = used_CX, used_CR
                break
            else:
                self.__generate_configs(self.pop.NP)
            #* adapt mutation
            X_mutant = self.mutates[i](
                self.pop.X_last, self.pop.config_F, self.pop.rng,
                fitness=self.pop.F)
            used_MUT.append(self.MUT_CX_POOL[i, 0])
            used_F.extend(self.pop.config_F)
            #* adapt crossover
            X_trial = self.crossovers[i](
                self.pop.X_last, X_mutant, self.pop.config_CR, self.pop.rng,
                operator=oper.DEmat.bin)
            used_CX.append(self.MUT_CX_POOL[i, 1])
            used_CR.extend(self.pop.config_CR)
            #* evaluate
            F_trial = self.evaluate(X_trial)
            #* environmenet selection
            self.survive(X_trial, F_trial)
        self.pop.used_MUT, self.pop.used_F = used_MUT, used_F
        self.pop.used_CX, self.pop.used_CR = used_CX, used_CR


    # ---------------------------- Private Methods ----------------------------
    def __generate_configs(self, size):
        ''' Generate control parameters F and CR '''
        idx = self.para.rng.choice(self.F_CR_POOL.shape[0], size)
        array_F_CR = self.F_CR_POOL[idx]
        self.pop.config_F = array_F_CR[:, 0]
        self.pop.config_CR = array_F_CR[:, 1]

    # --------------------------- Overwrite Methods ---------------------------
    def survive(self, X_trial, F_trial):
        self.pop.X, self.pop.F, self.survival_idx = oper.select(
            self.pop.X, self.pop.F, X_trial, F_trial)


## ---- DE with strategy adaptation and knowledge-based control parameters ----
class SAKPDE(DE):
    ''' :class:`SAKPDE` refers to DE with Strategy Adaptation and
        Knowledge-based control Parameters

        Reference
        ---------
        Q. Fan, W. Wang and X. Yan, "Differential evolution algorithm with
        strategy adaptation and knowledge-based control parameters", in
        Artificial Intelligence Review, vol. 51, no. 2, pp. 219-253, 2019
    '''
    ALGO_NAME = "SAKPDE"

    _MUT_POOL = OrderedDict()
    _MUT_POOL["de/rand/1"] = oper.DEmat.rand_1
    _MUT_POOL["de/rand/2"] = oper.DEmat.rand_2
    _MUT_POOL["de/current-to-best/1"] = oper.DEmat.current_to_best_1
    _MUT_POOL["de/current-to-best/2"] = oper.DEmat.current_to_best_2
    _MUT_POOL["de/best/2"] = oper.DEmat.best_2

    _CX_POOL = OrderedDict()
    _CX_POOL["bin"] = oper.DEmat.bin
    _CX_POOL["exp"] = oper.DEmat.exp

    _F_RANGE = (0.4, 1.0)
    _CR_RANGE = (0.3, 0.9)

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(),
                 stop_conditions=para.StopCondition(),
                 forgetting_factor=0.7,
                 opposition_learning_ratio=0.8,
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self.forgetting_factor = forgetting_factor
        self.op_learning_ratio = opposition_learning_ratio
        # Internal attributes
        self._evolve_a_generation = self._evolve_by_individual
        if self.stop.max_iter != None:
            self.Gmax = int(self.stop.max_iter)
        else:
            self.Gmax = int(self.stop.max_FES/self.para.N)
        self.Gs = int(0.3 * self.Gmax)
        #* models for hyperparameter
        self.MUT_model = tune.initialize_model(
            model_name="Roulette",
            RS=self.para.rng,
            feature_discrete=list(self.MUT_POOL.keys()),
            prob_discrete=[1/5,]*5)
        self.CX_model = tune.initialize_model(
            model_name="Roulette",
            RS=self.para.rng,
            feature_discrete=list(self.CX_POOL.keys()),
            prob_discrete=[1/3,]*3)
        self.F_model = tune.initialize_model(
            model_name="Cauchy",
            RS=self.para.rng,
            feature_continued=self.F_RANGE,
            lower_bound="regenerate",
            upper_boudn="regenerate",
            loc=1.0,
            scale=0.2)
        self.CR_model = tune.initialize_model(
            model_name="Normal",
            RS=self.para.rng,
            feature_continued=self.CR_RANGE,
            lower_bound="regenerate",
            upper_boudn="regenerate",
            loc=0.3,
            scale=0.2)

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        MUTs, CXs = self.__generate_configs(n_trials)
        unique, counts = np.unique(MUTs, return_counts=True)
        self.pop.config_MUT = list(zip(unique, counts.cumsum()))
        unique, counts = np.unique(CXs, return_counts=True)
        self.pop.config_CX = list(zip(unique, counts.cumsum()))

        #* adapt mutation
        mutate = self.MUT_POOL.get(self.pop.config_MUT[0][0])
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        _ = [pop[:self.pop.config_MUT[0][1], :], ]
        self.pop.used_MUT = [
            self.pop.config_MUT[0][0], ] * self.pop.config_MUT[0][1]
        #
        tmp = map(
            self.__mutate_individually, range(1, len(self.pop.config_MUT)))
        _.extend(list(tmp))
        self.pop.X_mutant = np.vstack(_)
        self.pop.used_MUT = np.array(self.pop.used_MUT)
        self.pop.used_F = self.pop.config_F

        #* adapt crossover
        crossover = self.CX_POOL.get(self.pop.config_CX[0][0])
        pop = crossover(self.pop.X, self.pop.X_mutant, self.pop.config_CR,
                        self.pop.rng)
        _ = [pop[:self.pop.config_CX[0][1], :], ]
        self.pop.used_CX = [
            self.pop.config_CX[0][0], ] * self.pop.config_CX[0][1]
        #
        tmp = map(
            self.__crossover_individually, range(1, len(self.pop.config_CX)))
        _.extend(list(tmp))
        self.pop.X_trial = np.vstack(_)
        self.pop.used_CX = np.array(self.pop.used_CX)
        self.pop.used_CR = self.pop.config_CR

        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

        #* update model
        self.update_models()

    # ---------------------------- Private Methods ----------------------------
    def __generate_configs(self, size):
        ''' Generate control parameters F and CR '''
        #* mutation operator & crossover operator
        if self.pop.nth_generation < self.Gs:
            array_MUT = np.array(["de/rand/1",] * size)
            array_CX = np.array(["bin",] * size)
        else:
            array_MUT = self.MUT_model.generate_discrete(size)
            array_CX = self.CX_model.generate_discrete(size)

        #* F
        cond = self.para.rng.rand(size) > self.op_learning_ratio
        num_true = np.count_nonzero(cond)
        # true cases (opposition learning)
        _t = np.abs(1 - self.F_model.generate_continued(num_true))
        # false cases
        _f = np.abs(self.F_model.generate_continued(size-num_true))
        self.pop.config_F = np.hstack([_t, _f])

        #* CR
        # true cases (opposition learning)
        _t = 1 - self.CR_model.generate_continued(num_true)
        # false cases
        _f = self.CR_model.generate_continued(size-num_true)
        self.pop.config_CR = np.hstack([_t, _f])
        return array_MUT, array_CX

    def __mutate_individually(self, i):
        ''' Mutate the entire population by a given configuration '''
        i0 = self.pop.config_MUT[i][0]
        i1 = self.pop.config_MUT[i][1]
        i1_prev = self.pop.config_MUT[i-1][1]
        mutate = self.MUT_POOL.get(i0)
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        used_MUT = [i0, ] * (i1 - i1_prev)
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

    # --------------------------- Overwrite Methods ---------------------------
    def update_models(self,):
        ''' Update each strategy '''
        if self.pop.nth_generation >= self.Gs + 1: #? HB: 经检查后任然不理解why +1
            MUT_diff, CX_diff = [], []
            fx_diff = np.abs(self.pop.F - self.pop.F.max())
            # mutation operator
            for operator in self.MUT_POOL.keys():
                pos = self.pop.used_MUT == operator
                MUT_diff.append(fx_diff[pos].sum())
            _ = np.array(MUT_diff)
            _[_.argmax()] = _.max() * self.forgetting_factor
            self.MUT_model.prob_discrete = _ / _.sum()
            # crossover operator
            for operator in self.CX_POOL.keys():
                pos = self.pop.used_CX == operator
                CX_diff.append(fx_diff[pos].sum())
            _ = np.array(CX_diff)
            _[_.argmax()] = _.max() * self.forgetting_factor
            self.CX_model.prob_discrete = _ / _.sum()

        # F
        self.F_model.loc = 1.0 - 0.6*self.pop.nth_generation/self.Gmax
        self.F_model.scale = 0.8 - 0.6*(1.0
            - (self.pop.nth_generation/self.Gmax)**2)
        # CR
        self.CR_model.loc = 1.0 - 0.7*(1.0 - self.pop.nth_generation/self.Gmax)
        self.CR_model.scale = 0.8 - 0.6*(1.0
            - (self.pop.nth_generation/self.Gmax)**2)


## ------ DE with Ensemble of mutation strategies and control parameters ------
class EPSDE(DE):
    ''' :class:`EPSDE` refers to DE with Ensemble of mutation strategies and
        control parameters

        Reference
        ---------
        Mallipeddi, R., Suganthan, P. N., Pan, Q. K., & Tasgetiren, M. F., 2011,
        Differential evolution algorithm with ensemble of parameters and
        mutation strategies. Applied soft computing, 11(2), 1679-1696
    '''
    ALGO_NAME = "EPSDE"

    _MUT_CX_POOL = np.array([("de/best/2", "bin"),
                             ("de/rand/1", "bin"),
                             ("de/current-to-rand/1", "none")])
    _F_POOL = (0.4, 0.5, 0.6, 0.7, 0.8, 0.9)
    _CR_POOL = (0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9)

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(),
                 stop_conditions=para.StopCondition(),
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self._evolve_a_generation = self._evolve_by_individual
        # Attributes
        self.success_config = None
        self.survival_idx = None

    @property
    def MUT_CX_POOL(self,):
        return self._MUT_CX_POOL

    @property
    def F_POOL(self,):
        return self._F_POOL

    @property
    def CR_POOL(self,):
        return self._CR_POOL

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        MUTs, CXs = self.__generate_configs(n_trials)
        unique, counts = np.unique(MUTs, return_counts=True)
        self.pop.config_MUT = list(zip(unique, counts.cumsum()))
        unique, counts = np.unique(CXs, return_counts=True)
        self.pop.config_CX = list(zip(unique, counts.cumsum()))

        #* adapt mutation
        mutate = self.MUT_POOL.get(self.pop.config_MUT[0][0])
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        _ = [pop[:self.pop.config_MUT[0][1], :], ]
        self.pop.used_MUT = [
            self.pop.config_MUT[0][0], ] * self.pop.config_MUT[0][1]
        #
        tmp = map(
            self.__mutate_individually, range(1, len(self.pop.config_MUT)))
        _.extend(list(tmp))
        self.pop.X_mutant = np.vstack(_)
        self.pop.used_MUT = np.array(self.pop.used_MUT)
        self.pop.used_F = np.array(self.pop.config_F)

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
            self.__crossover_individually, range(1, len(self.pop.config_CX)))
        _.extend(list(tmp))
        self.pop.X_trial = np.vstack(_)
        self.pop.used_CX = np.array(self.pop.used_CX)
        self.pop.used_CR = np.array(self.pop.config_CR)

        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

        #* update model
        self.update_models(self.survival_idx)

    # ---------------------------- Private Methods ----------------------------
    def __mutate_individually(self, i):
        ''' Mutate the entire population by a given configuration '''
        i0 = self.pop.config_MUT[i][0]
        i1 = self.pop.config_MUT[i][1]
        i1_prev = self.pop.config_MUT[i-1][1]
        mutate = self.MUT_POOL.get(i0)
        pop = mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                     fitness=self.pop.F)
        used_MUT = [i0, ] * (i1 - i1_prev)
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

    def __generate_configs(self, size):
        ''' Generate control parameters F and CR '''
        idx = self.para.rng.choice(len(self.MUT_CX_POOL), size)
        list_mut_cx = self.MUT_CX_POOL[idx]
        array_MUT = np.array([mut_cx[0] for mut_cx in list_mut_cx])
        array_CX = np.array([mut_cx[1] for mut_cx in list_mut_cx])
        self.pop.config_F = self.para.rng.choice(self.F_POOL, size)
        self.pop.config_CR = self.para.rng.choice(self.CR_POOL, size)
        if not self.survival_idx is None: # HB: 成功演化时生效（非第0代）
            idx1 = ~self.survival_idx
            rand = self.para.rng.rand(np.nonzero(idx1)[0].shape[0])
            idx2 = rand > 0.5
            idx3 = self.para.rng.choice(
                self.success_config.shape[0], size=idx2.nonzero()[0].shape[0])
            array_MUT[idx1][idx2] = self.success_config[idx3, 0]
            array_CX[idx1][idx2] = self.success_config[idx3, 1]
            self.pop.config_F[idx1][idx2] = self.success_config[idx3, 2]
            self.pop.config_CR[idx1][idx2] = self.success_config[idx3, 3]
        return array_MUT, array_CX

    # --------------------------- Overwrite Methods ---------------------------
    def update_models(self, idx):
        #? F 确认self.success_F是所有成功的F历史，还是只有当代成功的F
        _ = np.vstack(
            [self.pop.used_MUT[idx], self.pop.used_CX[idx],
            self.pop.config_F[idx,], self.pop.config_CR[idx]]).T
        if self.success_config is None:
            self.success_config = _
        else:
            self.success_config = np.vstack([self.success_config, _])



#!------------------------------------------------------------------------------
#!                          Control parameters (F and CR)
#!------------------------------------------------------------------------------
## -------- Self-Adapting Control Parameters in Differential Evolution --------
class jDE(DE):
    ''' :class:`jDE` refers to DE with self-adaptive parameters.

        Reference
        ---------
        J. Brest, S. Greiner, B. Boskovic, M. Mernik and V. Zumer,
        "Self-Adapting Control Parameters in Differential Evolution: A
        Comparative Study on Numerical Benchmark Problems", in IEEE
        Transactions on Evolutionary Computation, vol. 10, no. 6, pp. 646-657,
        Dec. 2006
    '''
    ALGO_NAME = "jDE"

    _F_RANGE = (0.1, 1.0)
    _CR_RANGE = (0.0, 1.0)

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(
                    mutation="de/rand/1",
                    crossover="bin",
                    F=0.5,
                    CR=0.9),
                 stop_conditions=para.StopCondition(),
                 F_lower=0.1,
                 F_upper=0.9,
                 tau_F=0.1,
                 tau_CR=0.1,
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self.F_lower = F_lower
        self.F_upper = F_upper
        self.tau_F = tau_F
        self.tau_CR = tau_CR
        self._evolve_a_generation = self._evolve_by_individual

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        self.__generate_configs(n_trials)
        #* adapt mutation
        self.pop.X_mutant = self.mutate(self.pop.X, self.pop.config_F,
            self.pop.rng, fitness=self.pop.F)
        self.pop.used_MUT = self.para.mutation
        self.pop.used_F = self.pop.config_F
        #* adapt crossover
        self.pop.X_trial = self.crossover(self.pop.X, self.pop.X_mutant,
            self.pop.config_CR, self.pop.rng)
        self.pop.used_CX = self.para.crossover
        self.pop.used_CR = self.pop.config_CR
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()

    # ---------------------------- Private Methods ----------------------------
    def __generate_configs(self, size):
        ''' Generate control parameters F and CR '''
        r = self.para.rng.rand(size, 4)
        self.pop.config_F = np.ones(size) * self.para.F
        flag = r[:, 1] < self.tau_F
        self.pop.config_F[flag] = self.F_lower + r[flag, 0] * self.F_upper
        self.pop.config_CR = np.ones(size) * self.para.CR
        flag = r[:, 3] < self.tau_CR
        self.pop.config_CR[flag] = r[flag, 2]


## ------ Adaptive Differential Evolution With Optional External Archive ------
class JADE(DE):
    ''' :class:`JADE` refers to Adaptive Differential Evolution with
        Optional External Archive.

        Reference
        ---------
        J. Zhang and A. C. Sanderson, "JADE: Adaptive Differential Evolution
        With Optional External Archive", in IEEE Transactions on Evolutionary
        Computation, vol. 13, no. 5, pp. 945-958, Oct. 2009
    '''
    ALGO_NAME = "JADE"

    _F_RANGE = (0.0, 1.0)
    _CR_RANGE = (0.0, 1.0)

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(mutation="de/current-to-pbest/1",
                                         crossover="bin"),
                 stop_conditions=para.StopCondition(),
                 c=0.1, # constant
                 p=0.05, # probability
                #  ext_archive=True,
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self.c = c
        self.p = p
        self.pop_archive = []
        # self.ext_archive = ext_archive
        # Internal attributes
        self.F_mean = 0.5
        self.CR_mean = 0.5
        self.success_F = np.array([])
        self.success_CR = np.array([])
        self.F_model = tune.initialize_model(
            model_name="Cauchy",
            RS=self.para.rng,
            feature_continued=self.F_RANGE,
            lower_bound="regenerate",
            upper_bound="truncate",
            loc=self.F_mean,
            scale=0.1)
        self.CR_model = tune.initialize_model(
            model_name="Normal",
            RS=self.para.rng,
            feature_continued=self.CR_RANGE,
            loc=self.CR_mean,
            scale=0.1)
        self._evolve_a_generation = self._evolve_by_individual

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        self.__generate_configs(n_trials)
        #* adapt mutation
        self.pop.X_mutant = self.mutate(self.pop.X, self.pop.config_F,
                self.pop.rng, fitness=self.pop.F, pop_archive=self.pop_archive,)
        self.pop.used_MUT = self.para.mutation
        self.pop.used_F = self.pop.config_F
        #* adapt crossover
        self.pop.X_trial = self.crossover(self.pop.X, self.pop.X_mutant,
                                          self.pop.config_CR, self.pop.rng)
        self.pop.used_CX = self.para.crossover
        self.pop.used_CR = self.pop.config_CR
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()
        #* update tuning model if necessary
        self.update_models(self.survival_idx)

    # --------------------------- Overwrite Methods ---------------------------
    def update_models(self, idx):
        #? F 确认self.success_F是所有成功的F历史，还是只有当代成功的F
        self.success_F = np.hstack([self.success_F, self.pop.config_F[idx]])
        L_mean = np.sum(self.success_F**2) / np.sum(self.success_F)
        self.F_mean = (1.0 - self.c) * self.F_mean + self.c * L_mean
        # CR
        self.success_CR = np.hstack([self.success_CR, self.pop.config_CR[idx]])
        A_mean = np.mean(self.success_CR)
        self.CR_mean = (1.0 - self.c) * self.CR_mean + self.c * A_mean
        # archived population
        self.pop_archive.extend(self.pop.X[idx].tolist())
        if len(self.pop_archive) > self.para.N:
            self.para.rng.shuffle(self.pop_archive)
            self.pop_archive = self.pop_archive[:self.para.N]

    # ---------------------------- Private Methods ----------------------------
    def __generate_configs(self, size):
        self.pop.config_F = self.F_model.generate_continued(size)
        self.pop.config_CR = self.CR_model.generate_continued(size)


## --------------------- Success-History based Adaptive DE ---------------------
class SHADE(DE):
    ''' :class:`SHADE` refers to Success-History based Adaptive DE.

        Reference
        ---------
        R. Tanabe and A. Fukunaga, "Success-history based parameter adaptation
        for Differential Evolution", 2013 IEEE Congress on Evolutionary
        Computation, Cancun, 2013, pp. 71-78
    '''
    ALGO_NAME = "SHADE"

    _F_RANGE = (0.0, 1.0)
    _CR_RANGE = (0.0, 1.0)

    def __init__(self,
                 opt_problem,
                 algo_parameters=para.DE(mutation="de/current-to-pbest/1",
                                         crossover="bin"),
                 stop_conditions=para.StopCondition(),
                 memory_size = None,
                 p_min = None,
                 p_max = None,
                 **kwargs):
        super().__init__(
            opt_problem, algo_parameters, stop_conditions, **kwargs)
        self.memory_size = memory_size
        self.p_min = p_min
        self.p_max = p_max
        self.pop_archive = []
        # Internal attributes
        self.F_mean = [0.5,] * self.memory_size
        self.CR_mean = [0.5,] * self.memory_size
        self.success_F = np.array([])
        self.success_CR = np.array([])
        self.F_model = tune.initialize_model(
            model_name="Cauchy",
            RS=self.para.rng,
            feature_continued=self.F_RANGE,
            lower_bound="regenerate",
            upper_bound="truncate",
            loc=self.F_mean,
            scale=0.1)
        self.CR_model = tune.initialize_model(
            model_name="Normal",
            RS=self.para.rng,
            feature_continued=self.CR_RANGE,
            loc=self.CR_mean,
            scale=0.1)
        self._evolve_a_generation = self._evolve_by_individual

    @property
    def memory_size(self,):
        return self._memory_size

    @memory_size.setter
    def memory_size(self, value):
        if value is None:
            self._memory_size = self.para.N
        elif value > 0:
            self._memory_size = int(value)
        else:
            raise ValueError("`memory_size` must be a positive integer")

    @property
    def p_min(self,):
        return self._p_min

    @p_min.setter
    def p_min(self, value):
        if value is None:
            self._p_min = 2 / self.para.N
        elif 0 < value and value < 1:
            self._p_min = float(value)
        else:
            raise ValueError("`p_min` must be a numeric between 0 and 1")

    @property
    def p_max(self,):
        return self._p_max

    @p_max.setter
    def p_max(self, value):
        if value is None:
            value = 0.2
        if self.p_min < value:
            self._p_max = float(value)
        else:
            raise ValueError("`p_max` must be a numeric between `p_min` and 1")

    def _evolve_by_population(self):
        raise NotImplementedError()

    def _evolve_by_individual(self):
        #* generate configuration for hyperparameters
        # Find how many trial individuals can be generated in this generation:
        n_trials = int(min(self.pop.NP, self.stop.max_FES-self.pb.num_calls))
        self.__generate_configs(n_trials)
        #* adapt mutation
        _ = list(map(self.__mutate_individually, range(self.para.N)))
        self.pop.X_mutant = np.array(_)
        self.pop.used_MUT = self.para.mutation
        self.pop.used_F = self.pop.config_F
        #* adapt crossover
        self.pop.X_trial = self.crossover(self.pop.X, self.pop.X_mutant,
                                          self.pop.config_CR, self.pop.rng)
        self.pop.used_CX = self.para.crossover
        self.pop.used_CR = self.pop.config_CR
        #* evaluate
        self.pop.F_trial = self.evaluate(self.pop.X_trial)
        self.survive()
        #* update tuning model if necessary
        self.update_models(self.survival_idx)

    # --------------------------- Overwrite Methods ---------------------------
    def update_models(self, idx):
        Fit_improve = (self.pop.F_last - self.pop.F)[idx]
        somme = Fit_improve.sum()
        position = self.pop.nth_generation % self.memory_size
        if somme != 0:
            weights = Fit_improve / Fit_improve.sum()
            # F
            self.success_F = self.pop.config_F[idx]
            WL_mean = np.sum(weights*self.success_F**2) / np.sum(self.success_F)
            self.F_mean[position] = WL_mean
            # CR
            self.success_CR = self.pop.config_CR[idx]
            WA_mean = np.average(self.success_CR, weights=weights)
            self.CR_mean[position] = WA_mean
            # archived population
            self.pop_archive.extend(self.pop.X[idx].tolist())
            if len(self.pop_archive) > self.para.N:
                self.para.rng.shuffle(self.pop_archive)
                self.pop_archive = self.pop_archive[:self.para.N]
        # else:
        #     self.F_mean[position] = self.F_mean[position-1]
        #     self.CR_mean[position] = self.CR_mean[position-1]

    # ---------------------------- Private Methods ----------------------------
    def __mutate_individually(self, i):
        ''' Mutate the entire population by a given configuration '''
        pop = self.mutate(self.pop.X, self.pop.config_F, self.pop.rng,
                          p=self.pop.config_p[i], fitness=self.pop.F,
                          pop_archive=self.pop_archive,)
        return pop[i]

    def __generate_configs(self, size):
        # F
        r_idx = self.para.rng.randint(
            low=0, high=self.memory_size, size=size)
        _ = []
        for i in r_idx:
            self.F_model.update(loc=self.F_mean[i])
            _.append(self.F_model.generate_continued(size=1))
        self.pop.config_F = np.squeeze(_)
        # CR
        r_idx = self.para.rng.randint( #? 检查是否该用和F一样的r_idxs
            low=0, high=self.memory_size, size=size)
        _ = []
        for i in r_idx:
            self.CR_model.update(loc=self.CR_mean[i])
            _.append(self.CR_model.generate_continued(size=1))
        self.pop.config_CR = np.squeeze(_)
        # p
        self.pop.config_p = self.para.rng.uniform(self.p_min, self.p_max, size)



#!------------------------------------------------------------------------------
#!                                     TESTING
#!------------------------------------------------------------------------------
def main():
    from oacde.problems import problem as pb

    seed = 1226332587  # ! HB: don't change this value
    # rng = np.random.RandomState(seed)
    # list_seed = tuple(rng.randint(0, 2**31-1, 25))

    case = "CoDE"

    outputs = []

    ## 1. Problem Configuration
    benchmark = "bbob2015"
    D = 2
    funID = 23 # 8 9 Rosenbrock , 15 Rastrigin
    problem = pb.Benchmark(benchmark_set=benchmark, D=D, funID=funID,
        instanceID=9)

    ## 2. Algorithm Configuration
    NP = 30
    config1 = para.DE(seed = seed,
                      N = NP,
                      F = 0.3,
                      CR = 0.5,
                      mutation="de/rand/1",
                      crossover="eig",
                      initial_scheme = "latin_hypercube",
                      update_scheme = "deferred",
                      record_position = True)
    stop = para.StopCondition(max_FES=1e4*D, max_iter=None, delta_ftarget=1e-8)

    ## 3. Aglorithm Selection: using DE basic algorithm
    if case == "DE" or case == 1 or case == "ALL":
        print("\n--- Testing DE Basic:")
        optimizer = DE(opt_problem=problem,
                       algo_parameters=config1,
                       stop_conditions=stop)
        results = optimizer.solve(disp=1)
        # 5. Post-processing
        # outputs.append(optimizer.data)
        # print("Initial f_best:", output.get("f_best_hist")[0])
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)
        # Plot.convergence_curve(optimizer)
        # Plot.F_and_CR(optimizer)
        optimizer.save()

    ## 3. Aglorithm Selection: using DE random algorithm
    if case == "DE Random" or case == 2 or case == "ALL":
        print("\n--- Testing DE Random: on population level")
        optimizer = RandomDE(opt_problem=problem,
                             algo_parameters=config1,
                             stop_conditions=stop,
                             tuning_level="population_level",
                             )
        results = optimizer.solve(disp=0)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

        print("\n--- Testing DE Random: on individual level")
        optimizer = RandomDE(opt_problem=problem,
                             algo_parameters=config1,
                             stop_conditions=stop,
                             tuning_level="individual_level",
                             )
        results = optimizer.solve(disp=0)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)
        optimizer.save()

    ## 3. Aglorithm Selection: using jDE algorithm
    if case == "jDE" or case == 3 or case == "ALL":
        config1.mutation = "de/rand/1"
        config1.crossover = "bin"
        config1.F = 0.5
        config1.CR = 0.9
        print("\n--- Testing jDE:")
        optimizer = jDE(opt_problem=problem,
                        algo_parameters=config1,
                        stop_conditions=stop,
                        )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    ## 3. Aglorithm Selection: using JADE algorithm
    if case == "JADE" or case == 4 or case == "ALL":
        config1.mutation = "de/current-to-pbest/1"
        config1.crossover = "bin"
        print("\n--- Testing JADE:")
        optimizer = JADE(opt_problem=problem,
                         algo_parameters=config1,
                         stop_conditions=stop,
                         )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    ## 3. Aglorithm Selection: using SHADE algorithm
    if case == "SHADE" or case == 5 or case == "ALL":
        config1.mutation = "de/current-to-pbest/1"
        config1.crossover = "bin"
        print("\n--- Testing SHADE:")
        optimizer = SHADE(opt_problem=problem,
                          algo_parameters=config1,
                          stop_conditions=stop,
                         )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    ## 3. Aglorithm Selection: using EPSDE algorithm
    if case == "EPSDE" or case == 6 or case == "ALL":
        print("\n--- Testing EPSDE:")
        optimizer = EPSDE(opt_problem=problem,
                          algo_parameters=config1,
                          stop_conditions=stop,
                          )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    ## 3. Aglorithm Selection: using CoDE algorithm
    if case == "CoDE" or case == 7 or case == "ALL":
        print("\n--- Testing CoDE:")
        optimizer = CoDE(opt_problem=problem,
                         algo_parameters=config1,
                         stop_conditions=stop,
                         )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    ## 3. Aglorithm Selection: using SAKPDE algorithm
    if case == "SAKPDE" or case == 9 or case == "ALL":
        config1.mutation = "de/rand/1"
        print("\n--- Testing SAKPDE:")
        optimizer = SAKPDE(opt_problem=problem,
                           algo_parameters=config1,
                           stop_conditions=stop,
                           )
        results = optimizer.solve(disp=1)
        # Plot.convergence_curve(optimizer)
        print("Calculated results:", results)
        print("Theoretical optimal value:", problem.f_opt_theory)
        print("Relative error:", results[1]-problem.f_opt_theory)

    print(optimizer.history)

if __name__ == "__main__":
    main()
