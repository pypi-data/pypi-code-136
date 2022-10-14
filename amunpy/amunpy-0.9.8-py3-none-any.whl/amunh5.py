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

  This module implements an interface class to read attributes, coordinates,
  and datasets stored in AmunH5 format snapshots.

--------------------------------------------------------------------------------
"""
from .amun import Amun

class AmunH5(Amun):
    """AMUN H5 snapshot class"""

    def __init_snapshot__(self):
        """
            Sets the data format after verifying if the snapshot is stored
            in AmunH5 format.
        """
        import h5py

        if not self.path_is_file:
            raise Exception("AmunH5 requires a file not directory as the argument!")

        with h5py.File(self.path, 'r') as h5:
            if 'codes' in h5.attrs:
                if h5.attrs['code'].astype(str) == "AMUN":
                    self.dataformat = 'AmunH5'
                else:
                    raise Exception("'{}' contains attribute 'code', but its content is not 'AMUN'!".format(self.path))
            elif 'attributes' in h5 and 'coordinates' in h5 and 'variables' in h5:
                self.dataformat = 'AmunH5'
            else:
                raise Exception("{} misses one of these groups: 'attributes', 'coordinates' or 'variables'!".format(self.path))
            if 'version' in h5.attrs:
                if h5.attrs['version'].dtype == 'float32':
                    self.version = int(h5.attrs['version'])


    def __fill_attributes__(self):
        """
            Reads attributes from the snapshot file and adds them to
            the attributes' dictionary.
        """
        import h5py
        import numpy

        exclude_list = ['nseeds', 'seeds', 'dblocks', 'nproc', 'dims', 'dtn', 'last_id', 'mblocks']

        with h5py.File(self.path, 'r') as h5:
            for aname in h5['attributes'].attrs:
                if not aname in exclude_list:
                    attr = h5['attributes'].attrs[aname]
                    if attr.dtype in [ 'float64', 'float32', 'int64', 'int32' ]:
                        if isinstance(attr, numpy.ndarray):
                            self.attributes[aname] = numpy.squeeze(attr).tolist()
                        else:
                            self.attributes[aname] = attr
                    else:
                        self.attributes[aname] = numpy.squeeze(attr).astype(str)

        if not 'nchunks' in self.attributes and 'nprocs' in self.attributes:
            self.attributes['nchunks'] = self.attributes['nprocs']
            del self.attributes['nprocs']
        if 'rdims' in self.attributes:
            self.attributes['xblocks'] = self.attributes['rdims'][0]
            self.attributes['yblocks'] = self.attributes['rdims'][1]
            if self.attributes['ndims'] == 3:
                self.attributes['zblocks'] = self.attributes['rdims'][2]
            del self.attributes['rdims']


    def __fill_variables__(self):
        """
            Reads the names of datasets stored in the snapshot and adds them
            to the variables' dictionary.
        """
        import h5py

        with h5py.File(self.path, 'r') as h5:
            for variable in h5['variables']:
                v = variable.strip()
                self.variables[v] = v


    def __fill_chunks__(self):
        """
            Retrieves metadata about datablocks stored in the snapshot's chunks
            and adds them to the chunks' dictionary.
        """
        import h5py, numpy, os

        self.chunkname = 'p{:06d}'.format(self.attributes['isnap']) + '_{:05d}.h5'
        for n in range(self.attributes['nchunks']):
            self.chunks[n] = dict()
            self.chunks[n]['filename'] = self.chunkname.format(n)
            cname = os.path.join(self.dirname, self.chunks[n]['filename'])
            if os.path.exists(cname):
                with h5py.File(cname, 'r') as h5:
                    self.chunks[n]['dblocks'] = numpy.squeeze(h5['attributes'].attrs['dblocks'])
                    if self.chunks[n]['dblocks'] > 0:
                        self.chunks[n]['levels'] = numpy.array(h5['coordinates']['levels'])
                        self.chunks[n]['bounds'] = self.__swap__(numpy.array(h5['coordinates']['bounds']))
                        self.chunks[n]['coords'] = self.__swap__(numpy.array(h5['coordinates']['coords']))
                    else:
                        self.chunks[n]['levels'] = None
                        self.chunks[n]['coords'] = None
                        self.chunks[n]['bounds'] = None
            else:
                raise Exception("Snapshot's chunk '{}' not present!".format(cname))


    def __swap__(self, arr):
        """
            Function swaps the array for version before 1.0.
        """
        pass
        import numpy

        if self.version < 1:
            return numpy.transpose(arr, numpy.roll(numpy.arange(arr.ndim), 1))
        else:
            return arr


    def __read_binary_data__(self, dataset_name, chunk_number):
        """
            Gets the dataset array from a given snapshot's chunk.
        """
        import h5py, numpy, os

        cname = os.path.join(self.dirname, self.chunks[chunk_number]['filename'])
        with h5py.File(cname, 'r') as h5:
            return self.__swap__(numpy.squeeze(numpy.array(h5['variables'][dataset_name])))
