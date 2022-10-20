#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Validation of modules and functions
'''
import time
import oacde



tik = time.time()
#! -----------------------------------------------------------------------------
seed = 0 #! Please don't change this value

## 1. Problem Configuration
print("--- Step 1")
print("Let's start by selecting a testing function from bbob benchmark, "
    "you'll get an object of `<class Benchmark>`:")
benchmark = "bbob2015"
D = 10
funID = 7 # 8 9 Rosenbrock , 15 Rastrigin
problem = oacde.problem.Benchmark(benchmark_set=benchmark, D=D, funID=funID,
    instanceID=1)
print(problem)


## 2. Algorithm Configuration
print("\n--- Step 2")
print("Next, we need to initialize the DE's hyperparameters:")
NP = 24
config = oacde.publics.parameterize.DE(seed = seed,
                                       N = NP,
                                       mutation='de/rand/1'
                                       )
print(config)
print("As well as stop conditions:")
stop = oacde.publics.parameterize.StopCondition(max_FES=1e3*NP, max_iter=None, delta_ftarget=1e-8)
print(stop)


## 3. Aglorithm Execution: using OAC-DE algorithm
print("\n--- Step 3")
print("Now, you can personalize the OAC-DE's parameters such as the "
    "mutation operators, the crossover operators, ...")
optimizer = oacde.OACDE(opt_problem=problem,
                        algo_parameters=config,
                        stop_conditions=stop,
                        mut_pool=[
                        "de/rand/1",
                        "de/rand/2",
                        "de/best/2",
                        "de/current-to-best/2",
                        "de/current-to-rand/1",
                        "de/current-to-pbest/1",
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
print("You can solve the optimization problem by running `solve()` method. "
    "If you want to follow the result step by step, you can set "
    "`solve(disp=True)`:")
results = optimizer.solve()
#! -----------------------------------------------------------------------------
tok = time.time()


## 4. (Optional) Save results to disk
print("\n--- Step 4 (Optional)")
print("If you want to save the results permanently, you can use `save()` "
    "method. It will save the configurations, the stop conditions, "
    "the iteration history, and the final optimum to a json file.")
optimizer.save()


## 5. (Optional) Post-processing
print("\n--- Step 5 (Optional)")
print("Or you can just view the results on your screen like:")
print("\tElapsed Time: {:.2f}s".format(tok-tik))
print("\tCalculated results:", results)
print("\tTheoretical optimal value:", problem.f_opt_theory)
print("\tRelative error:", results[1]-problem.f_opt_theory)
print("\tEvolved Generations:", optimizer.data.get("nth_hist")[-1])

print(optimizer.history)