#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Algorithms common attributes and methods
    Vectorized version
'''
import numpy as np
import pandas as pd
from copy import deepcopy
# internal imports
from oacde.publics import tools
from oacde.publics import parameterize as para



#!------------------------------------------------------------------------------
#!                                     CLASSES
#!------------------------------------------------------------------------------
class __base(object):
    ''' :class:`__base` is the base class for defining an optimization method.
    '''
    _HIST_ITEMS = ["nth", "FES", "x_best", "f_best", "f_mean", "x_opt", "f_opt",
        "used_MUT", "used_F", "used_CX", "used_CR"]

    def __init__(self, opt_problem, algo_parameters, stop_conditions):
        '''
        Creates a new :class:`__base` for optimization methods.

        Parameters
        ----------
        opt_problem : instance of problem.SingleObject
            The optimization problem that will be solved by the current
            algorithm
        algo_parameters : dict | instance of option.
            The parameter setting/configuration of the current algorithm
        stop_conditions : dict | instance of option.StopCondition
            Stopping conditions which determine when the algorithm terminates.
        '''
        self.pb = opt_problem
        self.para = algo_parameters
        self.stop = stop_conditions
        self._ALL_initial_schemes = {
            "latin_hypercube": tools.latin_hypercube_sampling,
            "random": tools.uniform_random_sampling}

    # ----------------------------- Setter/Getter ------------------------------
    @property
    def pb(self):
        return self._pb

    @pb.setter
    def pb(self, problem):
        if problem is not None:
            self._pb = problem
        else:
            raise TypeError("The optimization problem must be an instance of"
                " problem.SingleObject, not an instance of {}"
                .format(type(problem).__name__))

    @property
    def para(self):
        return self._para

    @para.setter
    def para(self, hyperparameters):
        if isinstance(hyperparameters, self.CONFIG_TYPE):
            self._para = hyperparameters
        else:
            raise TypeError("The {} algorithm's configuration (i.e.,"
                " hyperparameters) must be an instance of {}, not an instance"
                " of {}".format(type(self).__name__, self.CONFIG_TYPE,
                type(hyperparameters)))
        if self._para.record_position == True:
            self.HIST_ITEMS = self._HIST_ITEMS + ["pop_X", "pop_F"]
        else:
            self.HIST_ITEMS = self._HIST_ITEMS

    @property
    def stop(self):
        return self._stop

    @stop.setter
    def stop(self, stop_cond):
        if isinstance(stop_cond, para.StopCondition):
            if stop_cond.ftarget is None:
                stop_cond.ftarget = self.pb.f_opt_theory+stop_cond.delta_ftarget
            self._stop = stop_cond
            self._stop.cond_array = np.array([stop_cond.max_FES,
                                              stop_cond.max_iter,
                                              -stop_cond.ftarget])
        else:
            raise TypeError("The algorithm's stopping condition must be an"
                " instance of {}, not an instance of {}"
                .format(para.StopCondition, type(stop_cond)))

    # ----------------------------- Public Methods -----------------------------
    def initialize_X0(self, initial_scheme, pop_size, criterion="classic",
        iterations=5):
        ''' Initialize decision variables '''
        func = self._ALL_initial_schemes.get(initial_scheme)
        if func is None:
            raise ValueError("The `initial_scheme` must be one of"
                " 'latin_hypercube' or 'random', not {}".format(initial_scheme))
        else:
            X0 = func(pop_size, self.pb.D,
                      self.pb.init_lower_bound, self.pb.init_upper_bound,
                      self.para.rng, criterion, iterations)
        return X0

    def _initiate_generation_0(self):
        ''' Initialize population '''
        self.reset() # Initialize the algorithm configuration
        X0 = self.initialize_X0(initial_scheme=self.para.initial_scheme,
                                pop_size=self.para.N)
        self.pop.initialize(X0) # Initialize the population
        # Update the best solution (equivalent to self._update_pop_attribute())
        self.pop.find_best_individual()
        self.pb.update_opt(self.pop.X_best, self.pop.F_best)
        # Avoid errors in recording history
        self.pop.used_MUT = ""
        self.pop.used_F = np.nan
        self.pop.used_CX = ""
        self.pop.used_CR = np.nan

    def solve(self, disp=False, plot=False):
        self._initiate_generation_0()
        self._write_to_history(self.HIST_ITEMS)
        # self._write_to_propagation()
        self._display_result(disp)
        # Main loop of evolution
        while not self.terminate():
            self._evolve_a_generation()
            self._update_pop_attribute()
            self.pop.nth_generation += 1
            self._write_to_history(self.HIST_ITEMS)
            # self._write_to_propagation()
            self._display_result(disp)
        # Collect result data for output
        self.output = self._collect_output()
        return self.pb.x_opt, self.pb.f_opt

    def terminate(self):
        ''' Check whether termination conditions are satisfied or not.

        Returns
        -------
        termination : boolean
            If any stop condition is met, return True; Otherwise, return False.
        '''
        self.stop.current_array = np.array(
            [self.pb.num_calls, self.pop.nth_generation, -self.pop.F_best])
        termination = self.stop.current_array >= self.stop.cond_array
        return termination.any()

    def evaluate(self, X):
        self.pb.num_calls += self.pop.NP
        return self.pb.fobj(X)

    def reset(self):
        ''' Reset the attributes of the optimizer.

        All variables/atributes will be re-initialized.
        '''
        # Initialize history lists
        self.history = pd.DataFrame(columns=self.HIST_ITEMS)
        # Reset some counters used in optimization process
        self.pb.num_calls = 0
        self.pop.nth_generation = 0
        self.pb.x_opt = None
        self.pb.f_opt = None

    def save(self, filestring="", replace=True):
        ''' Save output to file

        Parameters
        ----------
        filestring : string
            File path or filename.
            - If not specified, the output is JSON file
            - If extension is not specified, a JSON file and a binary file will
                be created
            - If extension ".json" is included, the output is JSON file
            - if extension ".rng" is included, the output is binary file
        '''
        if ".json" in filestring:
            stem = filestring.split(".")[0]
            tools.to_json(self.output, filestring, replace)
        elif filestring == "":
            stem = self.pb.name + "_" + self.ALGO_NAME
            tools.to_json(self.output, stem+".json", replace)
        else:
            stem = str(filestring)
            tools.to_json(self.output, stem+".json", replace)

    # ----------------------------- Private Methods ----------------------------
    def _display_result(self, flag):
        if flag:
            print("Generation {0:5d}: f(x) = {1:.20f}, objective function has"
                  " been called {2} times".format(self.pop.nth_generation,
                  self.pop.F_best, self.pb.num_calls))

    def _update_pop_attribute(self):
        ''' Update best solution found so far'''
        self.pop.find_best_individual()
        self.pb.update_opt(self.pop.X_best, self.pop.F_best)

    def _write_to_history(self, keys_list):
        available_items = {"nth": self.pop.nth_generation,
                           "FES": self.pb.num_calls,
                           "x_best": self.pop.X_best,
                           "f_best": self.pop.F_best,
                           "f_mean": self.pop.F_mean,
                           "x_opt": self.pb.x_opt,
                           "f_opt": self.pb.f_opt,
                           "pop_state": deepcopy(self.pop.state),
                           "used_MUT": self.pop.used_MUT,
                           "used_F": self.pop.used_F,
                           "used_CX": self.pop.used_CX,
                           "used_CR": self.pop.used_CR,
                           "pop_X": self.pop.X,
                           "pop_F": self.pop.F,
                           }
        request_items = {k: available_items.get(k) for k in keys_list}
        df_request_items = pd.Series(request_items)
        self.history = pd.concat(
            [self.history, df_request_items.to_frame().T], ignore_index=True)

    def _collect_output(self):
        result = {}
        result["problem"] = self.pb.name
        result["config"] = self.para.current()
        result["stop_conditions"] = self.stop.current()
        result["stop_status"] = self.stop.current_array
        result["consumed_FES"] =  self.pb.num_calls
        if self.stop.current_array[-1] == True:
            result["success"] = True
        else:
            result["success"] = False
        result["f_opt_theory"] = self.pb.f_opt_theory
        # history information
        result["x_best"] = self.history["x_best"].iloc[-1]
        result["f_best"] = self.history["f_best"].iloc[-1]
        result["x_opt"] = self.history["x_opt"].iloc[-1]
        result["f_opt"] = self.history["f_opt"].iloc[-1]
        if self.pb.f_opt_theory is not None:
            self.history["f_error"] = self.history["f_opt"]-self.pb.f_opt_theory
            result["f_error"] = self.history["f_error"].iloc[-1]
        result["history"] = self.history.to_json()
        return result



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
