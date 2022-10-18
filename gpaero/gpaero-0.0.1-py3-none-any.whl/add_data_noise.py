"""
Add noise to existing aerodynamic data file.
Sample usage:
  py3 add_data_noise.py \
        --data_file=./datafiles/aero_data.txt \
        --outfile_name=./datafiles/aero_data_noisy.txt \
        --noise_scale=0.03 \
        --overwrite
"""

from getopt import getopt
import numpy as np
import os
import pandas as pd
import re
import sys

short_options = ""
long_options = ["data_file=", "outfile_name=", "noise_scale=", "overwrite"]

if __name__ == '__main__':
    user_options = getopt(sys.argv[1:], short_options, long_options)
    uo_dict = dict(user_options[0])

    if "--data_file" not in uo_dict:
        raise Exception("Must specify '--data_file=' input")
    else:
        data_file = uo_dict["--data_file"]
    if "--outfile_name" not in uo_dict:
        raise Exception("Must specify '--outfile_name=' input")
    else:
        outfile_name = uo_dict["--outfile_name"]
        if os.path.exists(outfile_name) and "--overwrite" not in uo_dict:
            raise Exception("Output file {} already exists, specify "
                "'--ovewrite' to overwrite.".format(outfile_name))
    if "--noise_scale" not in uo_dict:
        raise Exception("Must specify '--noise_scale=' input")
    else:
        noise_scale = np.double(uo_dict["--noise_scale"])
    if uo_dict["--data_file"] == uo_dict["--outfile_name"]:
        raise Exception("Aborting, this will overwrite input data.")

    save_hdr = ''
    with open(data_file) as f:
        while True:
            line = f.readline()
            if line.startswith('# x_labels: '):
                save_hdr += line.split('# ')[1]
                xvars = re.sub('# x_labels: ', '', line).strip('\n').split(', ')
                x_nom = np.ones(len(xvars))
            elif line.startswith('# y_labels: '):
                save_hdr += line.split('# ')[1]
                yvars = re.sub('# y_labels: ', '', line).strip('\n').split(', ')
                y_nom = np.ones(len(yvars))
            elif line.startswith('# params: '):
                save_hdr += line.split('# ')[1]
                params = re.sub('# params: ', '', line).strip('\n').split(', ')
                p_nom  = np.ones(len(params))
            elif line.startswith('# header: '):
                save_hdr += line.split('# ')[1]
                raw_header = re.sub(' ', '', re.sub('# header: ', '', line)).strip(
                        '\n').split(',')
                break
            elif line.startswith('#'):
                save_hdr += line.split('# ')[1]
            else:
                raise Exception("Reading data file " + data_file + " went bad.")
    raw_data = np.loadtxt(data_file)
    raw_df = pd.DataFrame(raw_data, columns=raw_header)
    outvars = yvars.copy()
    for yi in yvars:
        outvars += [yi+'*d/d'+xi for xi in xvars]
        outvars += [yi+'*d/d'+pi for pi in params]
    for var in outvars:
        noise = np.sqrt(sum(raw_df[var]**2) / len(raw_df[var])) * noise_scale
        raw_df[var] += np.random.normal(size=len(raw_df[var])) * noise
    np.savetxt(outfile_name, raw_df.to_numpy(), header=save_hdr.strip('\n'))

