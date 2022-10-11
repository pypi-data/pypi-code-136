# ADC 
# mV
# ke-
# MeV (include work function, recombination and lifetime correction)
import numpy as np

from LarpixParser import units
from LarpixParser import charge_calibration as Cali

def get_charge_ADC(packets_arr):
    return packets_arr['dataword']

def get_charge_mV(packets_arr, run_config):
    packet_mv = []
    packet_mV = packets_arr['dataword'] / run_config['ADC_COUNTS'] * (run_config['V_REF'] - run_config['V_CM']) + run_config['V_CM'] - run_config['V_PEDESTAL']
    return packet_mV

def get_charge_ke(packets_arr, run_config):
    packet_mV = get_charge_mV(packets_arr, run_config)
    packet_ke = packet_mV / run_config['GAIN']
    return packet_ke

def get_charge_MeV(packets_arr, t_drift_arr, run_config):
    ## recombination require truth matching
    # W_ion [MeV/e]
    lifetime_red = Cali.lifetime(t_drift_arr, run_config) 
    recomb = Cali.recombination(2, run_config)
    packet_MeV = get_charge_ke(packets_arr, run_config) * 1000 / recomb / lifetime_red * run_config['W_ion']
    return packet_MeV    
