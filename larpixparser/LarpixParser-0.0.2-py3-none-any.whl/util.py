import yaml
from LarpixParser import units

def get_data_packets(packets):

    mask = packets['packet_type'] == 0
    packets_arr = packets[mask]

    return packets_arr

def get_run_config(run_config_path):

    run_config = {}

    with open(run_config_path) as infile:
        run_yaml = yaml.load(infile, Loader=yaml.FullLoader)

    run_config['y_offset'] = run_yaml['tpc_offsets'][0][1] * units.cm

    run_config['GAIN'] = run_yaml['GAIN']  # mV/ke-
    run_config['V_CM'] = run_yaml['V_CM']  # mV
    run_config['V_REF'] = run_yaml['V_REF']  # mV
    run_config['V_PEDESTAL'] = run_yaml['V_PEDESTAL']  # mV
    run_config['ADC_COUNTS'] = run_yaml['ADC_COUNTS']

    run_config['efield'] = run_yaml['e_field'] / (units.kV / units.cm) # kV/cm # the input from the yaml should be in kV/mm
    run_config['temp'] = run_yaml['temperature'] / (units.K) #K

    run_config['response_sampling'] = run_yaml['response_sampling'] #us

    run_config['lar_density'] = run_yaml['lar_density'] # g/cm^3

    run_config['box_alpha'] = run_yaml['box_alpha'] 
    run_config['box_beta'] = run_yaml['box_beta'] 
    run_config['birks_Ab'] = run_yaml['birks_Ab'] 
    run_config['birks_kb'] = run_yaml['birks_kb'] 

    run_config['W_ion'] = run_yaml['W_ion'] #MeV

    run_config['lifetime'] = run_yaml['lifetime'] #us

    return run_config
