"""
Generate data to build aerodecks using SU2.
In future, this module may be rewritten to handle large-scale parallel sims on a
cluster.

Inputs:
+ Current geometry parameters pk
+ Sampling points XXk.

Outputs:
+ Aerodynamic data to build GPR (or other) aerdeck model.

TODO list:
+ Warning if CFD doesn't converge
+ Job IDs so we can scale to multiple cores
+ Detailed CFD settings (e.g., reference moment distance)
+ More generic version of this should take the following inputs for a given
  aerodynamics sampling point:
    - refine_level
    - parameters (array of values for shape parameters)
    - flight conditions (array of values for shape parameters)
"""

import csv
import itertools
import numpy as np
import os
import re
import subprocess

def sample_aero_su2(refine_level, mach, alpha, delta):
    # Run a simulation in SU2 for a given flight condition (Mach-alpha-delta-...).
    # Runs direct sim and an adjoint sim for each output.

    # TODO: Need a process ID at some point to match log files and output data
    #   (if we want to run on a cluster).
    # TODO: Do something w/ refine_level.
    # TODO: For 3D, will probably want to remove code duplication.

    print("Running CFD...")
    with open("./su2-files/cfd_job_template.cfg", "r") as f: # direct
        txt = f.read()
        txt = re.sub("INPUT_PROBLEM", "DIRECT", txt, 1)
        txt = re.sub("INPUT_MACH", str(mach), txt, 1)
        txt = re.sub("INPUT_ALPHA", str(alpha), txt, 1)
        txt = re.sub("INPUT_OBJECTIVE", "DRAG", txt, 1) # dummy
        txt = re.sub("INPUT_FNAME", "history", txt, 1)
    with open('./su2-files/cfd_job.cfg', 'w') as f: f.write(txt)
    subprocess.call("./run_su2.sh")
    os.system("mv ./su2-files/restart_flow.dat ./su2-files/solution_flow.dat")
    with open("./su2-files/cfd_job_template.cfg", "r") as f: # adjoint - drag
        txt = f.read()
        txt = re.sub("INPUT_PROBLEM", "CONTINUOUS_ADJOINT", txt, 1)
        txt = re.sub("INPUT_MACH", str(mach), txt, 1)
        txt = re.sub("INPUT_ALPHA", str(alpha), txt, 1)
        txt = re.sub("INPUT_OBJECTIVE", "DRAG", txt, 1)
        txt = re.sub("INPUT_FNAME", "history_adjoint_cd", txt, 1)
    with open('./su2-files/cfd_job.cfg', 'w') as f: f.write(txt)
    subprocess.call("./run_su2.sh")
    with open("./su2-files/cfd_job_template.cfg", "r") as f: # adjoint - lift
        txt = f.read()
        txt = re.sub("INPUT_PROBLEM", "CONTINUOUS_ADJOINT", txt, 1)
        txt = re.sub("INPUT_MACH", str(mach), txt, 1)
        txt = re.sub("INPUT_ALPHA", str(alpha), txt, 1)
        txt = re.sub("INPUT_OBJECTIVE", "LIFT", txt, 1)
        txt = re.sub("INPUT_FNAME", "history_adjoint_cl", txt, 1)
    with open('./su2-files/cfd_job.cfg', 'w') as f: f.write(txt)
    subprocess.call("./run_su2.sh")
    with open("./su2-files/cfd_job_template.cfg", "r") as f: # adjoint - z-moment
        txt = f.read()
        txt = re.sub("INPUT_PROBLEM", "CONTINUOUS_ADJOINT", txt, 1)
        txt = re.sub("INPUT_MACH", str(mach), txt, 1)
        txt = re.sub("INPUT_ALPHA", str(alpha), txt, 1)
        txt = re.sub("INPUT_OBJECTIVE", "MOMENT_Z", txt, 1)
        txt = re.sub("INPUT_FNAME", "history_adjoint_mz", txt, 1)
    with open('./su2-files/cfd_job.cfg', 'w') as f: f.write(txt)
    subprocess.call("./run_su2.sh")
    print("Done.")

    # Read results and add to GPR data
    outs = {}
    with open("./su2-files/history.csv", "r") as f: # direct results
        head = f.readline()
        head = head.replace('"', '').replace(' ', '').strip("\n").split(",")
        ind = dict(zip(head, list(range(len(head)))))
        last_line = f.readlines()[-1].replace('"', '').replace(' ', '').strip(
                "\n").split(",") # change history write frequency?
        outs['CL'] = last_line[ind['CL']]
        outs['CD'] = last_line[ind['CD']]
    with open("./su2-files/history_adjoint_cd.csv", "r") as f: # adjoint - drag
        head = f.readline()
        head = head.replace('"', '').replace(' ', '').strip("\n").split(",")
        ind = dict(zip(head, list(range(len(head)))))
        last_line = f.readlines()[-1].replace('"', '').replace(' ', '').strip(
                "\n").split(",") # change history write frequency?
        outs['CD*d/dMach'] = last_line[ind['Sens_Mach']]
        outs['CD*d/dalpha'] = last_line[ind['Sens_AoA']]
    with open("./su2-files/history_adjoint_cl.csv", "r") as f: # adjoint - lift
        head = f.readline()
        head = head.replace('"', '').replace(' ', '').strip("\n").split(",")
        ind = dict(zip(head, list(range(len(head)))))
        last_line = f.readlines()[-1].replace('"', '').replace(' ', '').strip(
                "\n").split(",") # change history write frequency?
        outs['CL*d/dMach'] = last_line[ind['Sens_Mach']]
        outs['CL*d/dalpha'] = last_line[ind['Sens_AoA']]
    with open("./su2-files/history_adjoint_cl.csv", "r") as f: # adjoint - moment-z
        head = f.readline()
        head = head.replace('"', '').replace(' ', '').strip("\n").split(",")
        ind = dict(zip(head, list(range(len(head)))))
        last_line = f.readlines()[-1].replace('"', '').replace(' ', '').strip(
                "\n").split(",") # change history write frequency?
        outs['MZ*d/dMach'] = last_line[ind['Sens_Mach']]
        outs['MZ*d/dalpha'] = last_line[ind['Sens_AoA']]
    return outs

def generate_aero_data(pdata, xdata):
    """
    For a given geometry, generates 2D aerodynamic maps, parameterized by
    Mach-alpha-delta, using SU2.
    The input data must match the ordering in the 'ins' array below.
    """
    ins = ['Mach', 'alpha', 'delta']
    outs = ['CD', 'CL', 'MZ']
    param_labels = [] # none yet
    header = ['refine_level'] + ins 
    for out in outs: header += [out] + [out+'*d/d'+inv for inv in ins]

    # TODO: Make a mesh corresponding to pdata.
    # TODO: this function is for 3DoF trimmed dynamics - check and generalize.

    # Sample the Mach-alpha space and store results
    # will support CL derivatives later
    index = dict(zip(header, list(range(len(header)))))
    data = np.hstack((xdata,
        np.zeros((xdata.shape[0], len(header)-xdata.shape[1]))))
    for i in range(data.shape[0]):
        inputs = data[i, 0:index[ins[-1]]+1]
        coeffs = sample_aero_su2(*inputs)
        for k, v in coeffs.items(): data[i, index[k]] = v
    save_header = 'x_labels: ' + ', '.join(ins) + \
            '\ny_labels: ' + ', '.join(outs) + \
            '\nparams: ' + ', '.join(param_labels) + \
            '\nheader: ' + ', '.join(header)
    np.savetxt("aero_data.txt", data, header=save_header)

if __name__ == "__main__":
    # Test-drive the SU2 deck generation
    pdata = None
    ref_lvl_arr = np.arange(0, 1, 1, dtype=np.int16) # these will be inputs
    mach_arr = np.linspace(1.2, 5.0, 7)
    alpha_arr = np.linspace(-10.0, 10.0, 7)
    delta_arr = np.linspace(0.0, 0.0, 1) # no delta currently
    # Order of points matches refine_level + ins(see generate_2D_aero_maps),
    # currently
    #   'refine_level', 'Mach', 'alpha', 'delta'
    xdata = np.array(list(itertools.product(ref_lvl_arr, mach_arr, alpha_arr,
        delta_arr)))
    # itertools.product will make a grid, probably want something better for
    # more realistic use.
    generate_aero_data(pdata, xdata)

    # TODO: dCD/dp, dG/dp?


    # Will use Kieran's batch job code for running CART3D.
    # This will need to be scalable... will need to do a similar thing here
    # eventually --> let individual codes handle batching.

    # There should be some shared code to work out what vars and outputs are
    # needed for each dynamics description.
    # How you go about getting this data is irrelevant.

    # Structure:
    # def generate_2D_aero_data(params, xdata):
    #   def prep_geom(params):
    #     ...
    #   def sample_aero(xdata):
    #     ...

    # params: vector of geometry parameters; specific to each geometry family
    #   that we will consider.
    # xdata: vector of sampling points (where each sampling point is a vector);
    #   specific to each vehicle dynamics model that we will consider.
    # ydata [implicit?]: aerodynamic outputs to store (specific to each vehicle
    #   dynamics model).

    # Code sharing:
    # Aerodynamics data must be written in standard format so that they can go
    # into the GPR.
    # Geometry is the easiest -- for each geometry family, we need to define
    # a prep_geom function that accepts the parameters associated w/ that family.

    # Define xdata, ydata for some models.
    # Trimmed 3DoF:
    #   x -- Mach, alpha, delta
    #   y -- CD, CL, MZ
    # All solvers then need a way of outputting y, dy/dx, and dy/dp.
    # Solvers create their own results files --> once you prep the geom and pass
    # in xdata, the solver will create its own output file with some headers.
    # Define mappings between x, y, and p.
    # Then, we can read the results from each solver into a unified format for
    # making the GPR.


