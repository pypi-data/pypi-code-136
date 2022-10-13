
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import MinMaxScaler
from copy import deepcopy
from multiprocessing import Pool, freeze_support
import os,sys


def get_differential_privacy_value(value, epsilon, seed=0):
    
    def pdf(x):
        b = 2 / (epsilon)
        c = 1 - 0.5 * (np.exp(-(value+1)/b) + np.exp(-(1 - value)/b))
        return (1 / (b * c * 2)) * np.exp(-np.absolute(x - value)/b)

    elements = np.linspace(-1, 1, 10**4)
    probabilities = pdf(elements)
    probabilities /= np.sum(probabilities)
    return np.random.choice(elements, size=1, p=probabilities.reshape(-1)).item()


def timeseries_dp(timeseries, epsilon):
    scaler = MinMaxScaler(feature_range=(-1,1))
    
    S = []
    
    for val_idx, value in enumerate(timeseries):
        if val_idx == 0 :
            ranges = np.array([value,timeseries[val_idx+1]]).reshape(-1,1)
            scaler.fit(ranges)
            scaled_value = scaler.transform(ranges)[0]
            dp_value = get_differential_privacy_value(scaled_value, epsilon) # 여기를 나중에 바꿔줄 것임
            # synthesized value : v'
            dp_value = np.array(dp_value).reshape(-1,1)
            print(dp_value)
            syn_value = scaler.inverse_transform(dp_value)
            S.append(syn_value.item())
    
    ## 2. get all values after index 0
        elif val_idx == len(timeseries)-1 :
            ranges = np.array([value,timeseries[val_idx-1]]).reshape(-1,1)
            scaler.fit(ranges)
            scaled_value = scaler.transform(ranges)[0]
            dp_value = get_differential_privacy_value(scaled_value, epsilon)
            dp_value = np.array(dp_value).reshape(-1,1)
            syn_value = scaler.inverse_transform(dp_value)
            S.append(syn_value.item())
            
        else :
            v_1, v_3 = timeseries[val_idx-1], timeseries[val_idx+1] # value index +1 을 v_3로 표현
            if (v_1 < value < v_3) | (v_1 > value > v_3) :
                ranges = np.array([v_1, v_3]).reshape(-1,1)
                scaler.fit(ranges)
                scaled_value = scaler.transform(np.array(value).reshape(-1,1))
                dp_value = get_differential_privacy_value(scaled_value, epsilon)
                dp_value = np.array(dp_value).reshape(-1,1)
                syn_value = scaler.inverse_transform(dp_value)
                S.append(syn_value.item())
                
            
            elif (v_1 < value) & (v_3 < value):
                _, second, first = sorted([v_1, value, v_3])
                ranges = np.array([first, second]).reshape(-1,1)
                scaler.fit(ranges)
                scaled_value = scaler.transform(np.array(value).reshape(-1,1))
                dp_value = get_differential_privacy_value(scaled_value, epsilon)
                dp_value = np.array(dp_value).reshape(-1,1)
                syn_value = scaler.inverse_transform(dp_value)
                S.append(syn_value.item())
                
            elif (v_1 > value) & (v_3 > value) :
                third, second, _ = sorted([v_1, value, v_3])
                ranges = np.array([third, second]).reshape(-1,1)
                scaler.fit(ranges)
                scaled_value = scaler.transform(np.array(value).reshape(-1,1))
                dp_value = get_differential_privacy_value(scaled_value, epsilon)
                dp_value = np.array(dp_value).reshape(-1,1)
                syn_value = scaler.inverse_transform(dp_value)
                S.append(syn_value.item())
                
            else :
                if (value == v_1 == v_3) :
                    # syn_value = get_differential_privacy_value(value, epsilon)
                    syn_value = 0
                    S.append(syn_value)
                else : 
                    val1, val2 = list(set([value, v_1, v_3]))
                    ranges = np.array([val1, val2]).reshape(-1,1)
                    scaler.fit(ranges)
                    scaled_value = scaler.transform(np.array(value).reshape(-1,1))
                    dp_value = get_differential_privacy_value(scaled_value, epsilon)
                    dp_value = np.array(dp_value).reshape(-1,1)
                    syn_value = scaler.inverse_transform(dp_value)
                    S.append(syn_value.item())
    return S
