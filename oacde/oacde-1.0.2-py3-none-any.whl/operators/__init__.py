#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Online algorithm configuration for differential evolution algorithm (OAC-DE)

    Copyright 2022 Changwu Huang, Hao Bai and Xin Yao

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''
import numpy as np

def select(pop, F, pop_trial, F_trial):
    ''' Compare target population and trial population and select survivals

        Return
        ------
        pop : 2D-array
            survival population
        F : 1D-array
            survival fitness corresponding to the survival population
    '''
    NP, D = pop.shape
    flag = np.array(F_trial <= F).reshape(-1, NP)
    cond = np.tile(np.transpose(flag), (1, D))
    pop = np.where(cond, pop_trial, pop)
    flag = np.squeeze(flag)
    F = np.where(flag, F_trial, F)
    return pop, F, flag #TODO needs to adapt the last output to all algos
