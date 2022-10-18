"""
Implementation:
+ Look into effects of matrix rank for LMC index kernel (start with 'Kernels for
  vector-valued functions').
+ `Multifidelity' data:
  - load current 'aero_data.txt' file (or something)
  - select data (Ma, alpha) values to be copied as hifi (index 1) data
  - copy all data as lofi (index 0) data with transformation
+ Trial the following transformations:
  - linear scaling of outputs -- scale outputs by factor
  - linear scaling of inputs  -- scale inputs by factor
  - translation of outputs, inputs
  - translation and linear scaling of outputs, inputs
  - add in some nonlinearity to make it harder
"""

import numpy as np
import pandas as pd
import re

Ma_range = [2.5, 4.1, 5.0, 6.1, 7.5] # can crash on certain Mach (eg 4.0, 6.0)
alpha_range = [-0.08727, -0.04363,  0., 0.04363, 0.08727]
Ma_hi = [4.1, 6.1]
alpha_hi = [-0.04363, 0.04363]

data_file = './datafiles/aero_data.txt'
header_lines = []
with open(data_file) as f:
    while True:
        line = f.readline()
        if line.startswith('# header: '): 
            raw_header = re.sub(' ', '', re.sub('# header: ', '', line)).strip(
                    '\n').split(',')
            header_lines.append(line)
            break
        elif line.startswith('# '): 
            header_lines.append(line)
        else:
            raise Exception("Reading data file at " + data_path + " went bad.")

raw_data = np.loadtxt(data_file)
lofi_df = pd.DataFrame(raw_data, columns=raw_header)
hifi_df = lofi_df[lofi_df['Mach'].isin(Ma_hi) & lofi_df['alpha'].isin(alpha_hi)].copy()
lofi_df['refine_level'] = 1.0

# Apply input / output scaling to lofi data.
# Derivative scaling via chain rule:
#    y' = y * y_s --> dy'/dy = y_s
#    x' = x * x_s --> dx/dx' = 1/x_s
#   dy'   dy   dy'   dx
#   --- = -- * --- * --- = dy/dx * y_s / x_s
#   dx'   dx   dy    dx'
# cd_s = 1.0
cd_s = 1.2
ma_s = 1.0
alpha_s = 1.0
delta_s = 1.0
scale_map = {
    'CD'          : cd_s,
    'Mach'        : ma_s,
    'alpha'       : alpha_s,
    'delta'       : delta_s,
    'CD*d/dMach'  : cd_s / ma_s,
    'CD*d/dalpha' : cd_s / alpha_s,
    'CD*d/ddelta' : cd_s / delta_s,
}
for k in scale_map: lofi_df[k] *= scale_map[k]
# cd_t = 0.0
cd_t = 0.01
ma_t = 0.0
alpha_t = 0.0
delta_t = 0.0
trans_map = {
    'CD'          : cd_t,
    'Mach'        : ma_t,
    'alpha'       : alpha_t,
    'delta'       : delta_t,
}
for k in trans_map: lofi_df[k] += trans_map[k]

# Add noise to CD
noise_scale_lo = 0.03
noise_scale_hi = 0.03
xvars = ['Mach', 'alpha', 'delta']
outvars = ['CD'] + ['CD*d/d' + var for var in xvars]
for var in outvars:
    noise_lo = np.sqrt(sum(lofi_df[var]**2) / len(lofi_df[var])) * noise_scale_lo
    lofi_df[var] += np.random.normal(size=len(lofi_df[var])) *  noise_lo
    noise_hi = np.sqrt(sum(hifi_df[var]**2) / len(hifi_df[var])) * noise_scale_hi
    hifi_df[var] += np.random.normal(size=len(hifi_df[var])) *  noise_hi

df = pd.concat([lofi_df, hifi_df]).reset_index(drop=True)

f = open('./datafiles/aero_data_mf_test.txt', 'w')
f.write(''.join(header_lines))
df.to_csv(f, header=False, index=False, sep=' ')
f.close()

