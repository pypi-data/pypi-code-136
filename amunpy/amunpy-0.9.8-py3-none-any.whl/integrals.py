"""
================================================================================

  This file is part of the AMUN source code, a program to perform
  Newtonian or relativistic magnetohydrodynamical simulations on uniform or
  adaptive mesh.

  Copyright (C) 2018-2022 Grzegorz Kowal <grzegorz@amuncode.org>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

 module: AMUN

  Python module with subroutines to read AMUN code HDF5 files.

  The only requirements for this package are:

     - numpy

--------------------------------------------------------------------------------
"""
def amun_integrals(field, filename, pathlist):
    '''
        get_integral: iterate over pathlist and read and merge field values from filename files in the provided paths
    '''
    # Initiate the return values with empty array and file number.
    #
    vals = np.array([])
    num  = 1

    # Iterate over all paths provided in the list 'pathlist'.
    #
    for path in pathlist:

      # Iterate over all files in the current path.
      #
      while True:

        # Generate file name.
        #
        dfile = path + '/' + filename + '_' + str(num).zfill(2) + '.dat'

        # Check if the file exists.
        #
        if op.isfile(dfile):

          # Read values from the current integrals file.
          #
          lvals = read_integrals(dfile, field)

          # Append to the return array.
          #
          vals = np.append(vals, lvals)

          # Increase the number file.
          #
          num = num + 1

        else:

          # File does not exists, so go to the next path.
          #
          break

    # Return appended values.
    #
    return vals


def read_integrals(filename, column):
    '''
        read_integrals: reads a given column from an integral file.
    '''
    # Open the given file and check if it is text file.
    #
    f = open(filename, 'r')

    # Read fist line and store it in h, since it will be used to obtain the
    # column headers.
    #
    l = f.readline()
    h = l

    # Read first line which is not comment in order to determine the number of
    # columns and store the number of columns in nc.  Calculate the column width
    # and store it in wc.
    #
    while l.startswith('#'):
        l = f.readline()
    nc = len(l.rsplit())
    wc = int((len(l) - 9) / (nc - 1))

    # Split header line into a list.
    #
    lh = [h[1:9].strip()]
    for i in range(nc - 1):
      ib = i * wc + 10
      ie = ib + wc - 1
      lh.append(h[ib:ie].strip())


    ic = lh.index(column)

    # Read given column.
    #
    if (ic > -1):
      lc = [float(l.split()[ic])]
      for l in f:
        lc.append(float(l.split()[ic]))

    # Close the file.
    #
    f.close()

    # Return values.
    #
    return(np.array(lc))
