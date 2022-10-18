"""
Generate aerodynamic data to build aerodecks (i.e., continuous surfaces that can
be sampled at any flight condition) using some fitting method (e.g., Gaussian
process regression).
Top-level code that creates datasets in a unified format using any one of the
supported aerodynamics solvers, currently
  - CART3D
  - SU2
  - analytical.
Builds aerodecks that are compatible with the chosen vehicle dynamics model, one
of
  - trimmed 3DoF
  - trimmed 6DoF [in future]
  - 6DoF         [in future]
[TODO] x-states could actually be specific to certain geometries, for
example, we may have a single flap (delta) or two flaps (delta1, delta2) to
provide actuator redundancy.

TODOs:
+ The 'generate_aero_data' functions for the different solvers are currently
  specific to 3DoF trimmed.
+ Have check in 'generate_aero_data' to enforce correct ordering of xdata (and
  maybe pdata)
"""

from itertools import product
import numpy as np
import pandas as pd
import re
# from hypersonic_vehicle_hanger.Vehicle_2D.vehicle_2D import generate_aero_data

from gpr import GprModel
# from gpr_aerodecks.gpr import GprModel

# import importlib
# gpr = importlib.import_module("gpr", package="gpr-aerodecks")

class GeoFamily:
    def __init__(self, param_list):
        self.param_list = param_list
        self.params = {
            k:v for k,v in zip(param_list, list(range(len(param_list))))
        }

class TwoDWithFlap(GeoFamily):
    """
    VEHICLE -
                            ________-----------T1
          ________----------                   /
        P0____                                /
              ----____                       /
                      ----____              /
                              B1----------B2
        P0 = (0, 0)
        T1 = P0 + rt0
        B1 = P0 + rb0
        B2 = P0 + rb0 + rb1

    FLAP - The flap is treated independently.
                 ___----F1
            F0---
        F0 = P0 + rf0
        F1 = P0 + rf0 + rf1
    """
    def __init__(self):
        param_list = [
            "rt0", # [m] - length vector P0 to T0
            "at0", # [rad] - angle vector P0 to T0
            "rb0", # [m] - length vector P0 to B0
            "ab0", # [rad] - angle vector P0 to B0
            "rb1", # [m] - length vector B0 to B1
            "ab1", # [rad] - angle vector B0 to B1

            "rf0", # [m] - length vector P0 to F0
            "af0", # [rad] - angle vector P0 to F0
            "rf1", # [m] - length vector F0 to F1

            "rc0", # [m] - length vector P0 to CoM
            "ac0", # [rad] - angle vector P0 to CoM
        ]
        super().__init__(param_list)

class DynamicsModel:
    def __init__(self, model_type, xlist, ylist):
        self.model_type = model_type
        self.xlist = xlist
        self.ylist = ylist
        self.xdict = {k:v for k,v in zip(xlist, list(range(len(xlist))))}
        self.ydict = {k:v for k,v in zip(ylist, list(range(len(ylist))))}

class Trimmed3DoF(DynamicsModel):
    def __init__(self):
        xlist = ["Mach", "alpha", "delta"]
        ylist = ["CD", "CL", "CMz"]
        super().__init__("Trimmed3DoF", xlist, ylist)

def generate_aero_deck(solver, geo, model, pdata, xdata, fname, **kwargs):
    """
    Inputs:
      solver -- Analytical2D, SU2, CART3D
      geo    -- geometry model object, derived from 'GeoFamily'
      model  -- rigid-body dynamics model, specifies states and outputs, derived
                from 'DynamicsModel'
      pdata  -- vector of parameter values, ordering defined by 'geo'
      xdata  -- matrix, rows are vectors of x sampling points with ordering
                defined by 'model'
    KWInputs:
      x_nom  -- list of nominal values for each x variable, ordering as
                per xvars in 'DynamicsModel' class
      y_nom  -- as per x_nom for outputs
      p_nom  -- as per x_nom for parameters, ordering as per 'GeoFamily' class
    """
    if fname.split('/')[0] != "./datafiles/": fname = "./datafiles/" + fname
    raw_name = fname.split(".")[0] + "_raw.txt"
    if solver == "Analytical2D":
        import sys
        sys.path.append('/home/max/hypersonics/hsv-2d-model/hypersonic_vehicle_hanger/Vehicle_2D')
        from vehicle_2D import generate_aero_data
        generate_aero_data(pdata, xdata, geo.param_list, model.model_type, raw_name)
    else:
        raise Exception("Solver {} not supported.")

    # Load the file and rename to standard format
    with open(raw_name) as f:
        i = 0
        while True:
            i = i+1
            line = f.readline()
            if line.startswith('# x_labels: '): 
                xraw = re.sub('# x_labels: ', '', line).strip('\n').split(', ')
            elif line.startswith('# y_labels: '): 
                yraw = re.sub('# y_labels: ', '', line).strip('\n').split(', ')
            elif line.startswith('# params: '): 
                paramsraw = re.sub('# params: ', '', line).strip('\n').split(', ')
            elif line.startswith('# header: '): 
                raw_header = re.sub(' ', '', re.sub('# header: ', '', line)).strip(
                        '\n').split(',')
                break
    raw_data = pd.read_csv(raw_name, skiprows=i)
    raw_data.columns = raw_header
    if solver == "Analytical2D": raw_data['refine_level'] = 0
    cols = ['refine_level'] + model.xlist + model.ylist
    # TODO: different derivative formatting for different solvers?
    for y in model.ylist:
        cols += [y+'*d/d'+x for x in model.xlist]
        cols += [y+'*d/d'+p for p in geo.param_list]
    raw_data[raw_data.columns.intersection(cols)]
    raw_data = raw_data.reindex(columns=cols)
    # TODO: use parameters in block below
    save_header = 'x_labels: ' + ', '.join(model.xlist) + \
            '\ny_labels: ' + ', '.join(model.ylist) + \
            '\nparams: ' + ', '.join(geo.param_list)
    if "x_nom" in kwargs:
        assert len(x_nom) == len(model.xlist)
        save_header += '\nx_nom: ' + ', '.join(map(str, x_nom))
    if "y_nom" in kwargs:
        assert len(y_nom) == len(model.ylist)
        save_header += '\ny_nom: ' + ', '.join(map(str, y_nom))
    if "p_nom" in kwargs:
        assert len(p_nom) == len(geo.params)
        save_header += '\np_nom: ' + ', '.join(map(sr, p_nom))
    save_header += '\nheader: ' + ', '.join(cols)
    try:
        np.savetxt(fname, raw_data.to_numpy(), header=save_header)
    except TypeError as ex:
        print(raw_data)
        raise TypeError from ex
    # Done; aero_data.txt is in generic form, ready to be read by GPR code.

if __name__ == "__main__":
    # 1. Specify the model and geo parameters
    # Test using Ingo's analytical aero model
    geo = TwoDWithFlap()
    model = Trimmed3DoF()
    solver = "Analytical2D"

    # 2. Specify the geometry and sampling points, then compute data
    # Ordering of xdata and pdata must match ordering in 'model' and 'geo'
    pdata = np.array((1, np.deg2rad(5), 0.5, np.deg2rad(-10), 0.25,
        np.deg2rad(0.), 0.7, np.deg2rad(0.), 0.1, 0.3, np.deg2rad(0.)))
    M_range = [2.5, 4.1, 5.0, 6.1, 7.5] # can crash on certain Mach (eg 4.0, 6.0)
    alpha_range = np.deg2rad([-5, -2.5, 0, 2.5, 5])
    # M_range = [2.5, 3.0, 3.5, 4.1, 4.5, 5.0, 5.5, 6.1, 6.5, 7.1, 7.5] # Dense
    # alpha_range = np.deg2rad([-5, -3.75, -2.5, -1.25, 0, 1.25, 2.5, 3.75, 5])
    delta_range = np.deg2rad([-20, -10, 0, 10, 20])
    xdata = np.array(list(product(M_range, alpha_range, delta_range)))
    x_nom = [10, 0.1, 0.35] # list input
    y_nom = [0.15, 0.3, 0.12]

    # Generate aero data
    fname = "aero_data_aerodexx.txt"
    generate_aero_deck(solver, geo, model, pdata, xdata, fname,
            x_nom=x_nom, y_nom=y_nom)

    # 3. Train the GPR model
    # For the tests we use a really small learning rate as the initial guess is
    # very good and I want the stochastic optimization to converge deeply.
    gpr_ops = {
        "train_iters" : 50,
        "learn_rate"  : 0.005,
        "min_noise"   : 1E-8,
        "fit_params"  : ["rt0", "at0"], # fit derivatives for these params only
        "fit_x"       : ["Mach", "alpha"], # fit derivatives for these states only
        "data_path"   : fname,
        # "save_name"   : "aerodexx_model",
        "load_dir"    : "aerodexx_model_multi_fidelity",
    }
    gpr_model = GprModel(gpr_ops)

    # Test some single outputs
    # Stochastic optimization, results vary slightly, so use isclose with rel_tol
    # IMPORTANT: for these asserts to work, we still need a moderate amount of
    # training iterations -- due to adam optimization, there will be some
    # changes in hyperparams over first ~25 iterations.
    from math import isclose
    x_test = np.array([2.7, np.deg2rad(4), 0]) # Ma=2.7, alpha=4deg, delta=0deg
    i_test = 0 # ref_lvl=0
    out = 'CD' # predict drag coefficient
    cd_out = gpr_model.eval(out, x_test, i_test)
    assert isclose(float(cd_out), 0.06282498, rel_tol=1e-3)
    dCLdMach = gpr_model.eval('CL*d/dMach', [2.7, np.deg2rad(-3), 0], 0) # x list
    assert isclose(float(dCLdMach), 0.07687314, rel_tol=1e-3)
    dCMzdrt0 = gpr_model.eval('CMz*d/drt0', np.array([5.0, np.deg2rad(6), 0]), 0)
    assert isclose(float(dCMzdrt0), -0.0059426, rel_tol=1e-3)

    # Plot a slice with uncertainty bounds
    plot_slice = { # Mach-alpha slice
        'Mach'  : 'all',
        'alpha' : np.deg2rad(3),
        'delta' : 0.0,
    }
    plot_output = 'CL*d/dMach'
    plot_index = 0 # plot for first refinement level
    gpr_model.plot(plot_output, plot_slice, plot_index, ns=51)

    # Plot a surface with uncertainty bounds
    plot_surf = { # Mach-alpha slice
        'Mach'  : 'all',
        'alpha' : 'all',
        'delta' : 0.0,
    }
    plot_output = 'CD'
    plot_index = 0 # plot for first refinement level
    gpr_model.plot(plot_output, plot_surf, plot_index, ns=30)

