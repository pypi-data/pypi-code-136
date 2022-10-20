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
from . import multi_armed_bandit
from . import non_parameter
from . import distribution


def initialize_model(model_name, *args, **kwargs):
    ''' Initialize a tuning model

    :param model_name: Name of a hyperparameter tuner model
    :type model_name: str
    '''
    model_name = model_name.lower()
    # Multi-Armed Bandit family
    if model_name == "EpsilonGreedy".lower():
        return multi_armed_bandit.EpsilonGreedy(*args, **kwargs)
    elif model_name == "Softmax".lower():
        return multi_armed_bandit.Softmax(*args, **kwargs)
    elif model_name == "SUS_Softmax".lower():
        return multi_armed_bandit.SUS_Softmax(*args, **kwargs)
    elif model_name == "UCB".lower():
        return multi_armed_bandit.UCB(*args, **kwargs)
    # Non-Parametric family
    elif model_name == "KDE".lower():
        return non_parameter.KDE(*args, **kwargs)
    # Heuristic distribution family
    elif model_name == "Uniform".lower():
        return distribution.Uniform(*args, **kwargs)
    elif model_name == "Random".lower():
        return distribution.Roulette(*args, **kwargs)
    elif model_name == "Normal".lower():
        return distribution.Normal(*args, **kwargs)
    elif model_name == "Cauchy".lower():
        return distribution.Cauchy(*args, **kwargs)
    elif model_name == "Roulette".lower():
        return distribution.Roulette(*args, **kwargs)
    else:
        raise ValueError("Unsupported '{}' for `model_name`, it must be one of "
                         "'EpsilonGreedy', 'Softmax', 'SUS_Softmax', 'UCB', "
                         "'KDE', 'Uniform', 'Random', 'Normal', 'Cauchy', or "
                         "'Roulette'".format(model_name))
