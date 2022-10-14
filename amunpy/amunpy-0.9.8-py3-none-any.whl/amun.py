#-*- coding: utf-8 -*-
"""
================================================================================

  This file is part of the AMUN source code, a program to perform Newtonian or
  relativistic magnetohydrodynamical simulations on uniform or adaptive grid.

  Copyright (C) 2021-2022 Grzegorz Kowal <grzegorz@amuncode.org>

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

  The base class for Amun's snapshot formats.

--------------------------------------------------------------------------------
"""
class Amun:
    """AMUN snapshot base class"""

    def __init__(self, path, version=-1):

        import os

        if os.path.exists(path):
            if os.path.isdir(path):
                self.path_is_file = False
                self.dirname      = path
                self.filename     = None
            else:
                self.path_is_file = True
                self.dirname      = os.path.dirname(path)
                self.filename     = os.path.basename(path)
        else:
            raise Exception("Path '{}' does not exist!".format(path))

        self.path        = path
        self.dataformat  = None
        self.version     = version
        self.chunkname   = '{:d}'
        self.attributes  = dict()
        self.chunks      = dict()
        self.variables   = dict()

        self.__init_snapshot__()
        self.__fill_attributes__()
        self.__fill_chunks__()
        self.__fill_variables__()

        self.__check_attributes__()
        self.__check_chunks__()
        self.__check_variables__()

        self.__complete_attributes__()
        self.__complete_chunks__()
        self.__complete_variables__()


    def __init_snapshot__(self):
        """
            Initializes the snapshot object by checking the file's data format
            and setting the field 'self.dataformat' (string).
        """
        pass


    def __fill_attributes__(self):
        """
            Read attributes from the snapshot file and add all attributed to
            the dictionary 'self.attributes'.
        """
        pass


    def __fill_chunks__(self):
        """
            Retrieve metadata about data blocks stored in the snapshot's chunks.
        """
        pass


    def __fill_variables__(self):
        """
            Retrieve the variable names from the snapshot file and add them
            to the list 'self.variables'.
        """
        pass


    def __check_attributes__(self):
        """
            Check the presence of mandatory attributes.
        """
        mandatory_attributes = [ 'isnap', 'nchunks', 'ndims', 'maxlev', \
                'nleafs', 'ncells', 'nghosts', 'xmin', 'ymin', 'zmin', 'xmax', \
                'ymax', 'zmax', 'xblocks', 'yblocks', 'zblocks' ]

        for attr in mandatory_attributes:
            if not attr in self.attributes:
                raise Exception("Mandatory attribute '{}' not set!".format(attr))


    def __check_chunks__(self):
        """
            Check the presence of required field in chunks.
        """
        if not len(self.chunks) >= 1:
            raise Exception("The snapshot {} has no chunks!".format(self.path))

        mandatory_fields = [ 'filename', 'dblocks', 'levels', 'bounds', 'coords' ]

        for nc in range(self.attributes['nchunks']):
            for field in mandatory_fields:
                if not field in self.chunks[nc]:
                    raise Exception("Mandatory field '{}' not set in chunk no. {}!".format(field, nc))


    def __check_variables__(self):
        """
            Check the presence of variables.
        """
        if len(self.variables) < 1:
            raise Exception("The snapshot {} has no variables stored!".format(self.path))


    def __complete_attributes__(self):
        """
            Add additional attributes.
        """
        if not 'toplev' in self.attributes:
            self.attributes['toplev'] = max([max(chunk['levels']) if chunk['dblocks'] > 0 else 1 for chunk in self.chunks.values()])

        if not 'xlen' in self.attributes:
            self.attributes['xlen'] = self.attributes['xmax'] - self.attributes['xmin']
        if not 'ylen' in self.attributes:
            self.attributes['ylen'] = self.attributes['ymax'] - self.attributes['ymin']
        if not 'zlen' in self.attributes:
            self.attributes['zlen'] = self.attributes['zmax'] - self.attributes['zmin']

        if not 'bcells' in self.attributes:
            self.attributes['bcells'] = self.attributes['ncells'] + 2 * self.attributes['nghosts']

        if not 'resistivity' in self.attributes:
            self.attributes['resistivity'] = 0
        if not 'viscosity' in self.attributes:
            self.attributes['viscosity'] = 0

        self.cell_size = dict()
        for l in range(self.attributes['maxlev']):
            self.cell_size[l+1] = self.attributes['xlen'] / (self.attributes['xblocks'] * self.attributes['ncells'] * 2**l)


    def __complete_chunks__(self):
        """
            Add additional attributes to chunks.
        """
        for n in range(len(self.chunks)):
            if not 'dims' in self.chunks[n]:
                self.chunks[n]['dims'] = [ self.attributes['bcells'] ]*self.attributes['ndims']
                self.chunks[n]['dims'][:0] = [ self.chunks[n]['dblocks'] ]


    def __complete_variables__(self):
        """
            Add derived variables.
        """
        denflag = 'dens' in self.variables
        preflag = 'pres' in self.variables
        velflag = all(v in self.variables for v in ['velx','vely','velz'])
        magflag = all(v in self.variables for v in ['magx','magy','magz'])
        self.variables['refinement level']                  = 'mlev'
        if denflag:
            self.variables['density']                       = 'dens'
            self.variables['logarithm of density']          = 'logd'
        if preflag or self.attributes['eos'] == 'iso':
            self.variables['pressure']                      = 'pres'
            self.variables['logarithm of pressure']         = 'logp'
        if velflag:
            self.variables['velocity']                      = 'vvec'
            self.variables['velocity magnitude']            = 'velo'
            self.variables['x-velocity']                    = 'velx'
            self.variables['y-velocity']                    = 'vely'
            self.variables['z-velocity']                    = 'velz'
            self.variables['divergence of velocity']        = 'divv'
            self.variables['x-vorticity']                   = 'vorx'
            self.variables['y-vorticity']                   = 'vory'
            self.variables['z-vorticity']                   = 'vorz'
            self.variables['vorticity']                     = 'wvec'
            self.variables['vorticity magnitude']           = 'vort'
        if magflag:
            self.variables['magnetic field']                = 'bvec'
            self.variables['magnetic field magnitude']      = 'magn'
            self.variables['x-magnetic field']              = 'magx'
            self.variables['y-magnetic field']              = 'magy'
            self.variables['z-magnetic field']              = 'magz'
            self.variables['divergence of magnetic field']  = 'divb'
            self.variables['x-current density']             = 'curx'
            self.variables['y-current density']             = 'cury'
            self.variables['z-current density']             = 'curz'
            self.variables['current density']               = 'jvec'
            self.variables['current density magnitude']     = 'curr'
        if 'bpsi' in self.variables:
            self.variables['magnetic divergence potential'] = 'bpsi'
        if preflag and 'adiabatic_index' in self.attributes:
            self.variables['internal energy']               = 'eint'
        if denflag and preflag:
            self.variables['temperature']                   = 'temp'
        if self.attributes['eqsys'] in ['hd','mhd'] and denflag and velflag:
            self.variables['kinetic energy']                = 'ekin'
        if self.attributes['eqsys'] in ['mhd','srmhd'] and magflag:
            self.variables['magnetic energy']               = 'emag'
            self.variables['magnetic pressure']             = 'emag'
        if velflag and magflag:
            self.variables['electric field']                = 'evec'
            self.variables['electric field magnitude']      = 'elec'
            self.variables['x-electric field']              = 'elex'
            self.variables['y-electric field']              = 'eley'
            self.variables['z-electric field']              = 'elez'
        if self.attributes['eqsys'] in ['srhd','srmhd'] and velflag:
            self.variables['Lorentz factor']                = 'lore'

        delete_datasets = ['dens','pres','velx','vely','velz','magx','magy','magz','bpsi']
        for v in delete_datasets:
            if v in self.variables:
                del self.variables[v]


    def __read_binary_data__(self, dataset_name, chunk_number):
        """
            Get dataset array from the given snapshot's chunk.
        """
        pass


    def __get_dataset__(self, dataset_name, chunk_number):
        """
            Get dataset array of name dataset_name from the file n.
        """
        import numpy

        dataset = self.variables[dataset_name]

        if dataset == 'mlev':
            dset = numpy.zeros(self.chunks[chunk_number]['dims'])
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] = self.chunks[chunk_number]['levels'][p]
        elif dataset == 'logd':
            dset = numpy.log10(self.__read_binary_data__('dens', chunk_number))
        elif dataset == 'pres':
            if self.attributes['eos'] == 'iso':
                dset = self.__read_binary_data__('dens', chunk_number) * self.attributes['sound_speed']**2
            else:
                dset = self.__read_binary_data__('pres', chunk_number)
        elif dataset == 'logp':
            if self.attributes['eos'] == 'iso':
                dset = numpy.log10(self.__read_binary_data__('dens', chunk_number) * self.attributes['sound_speed']**2)
            else:
                dset = numpy.log10(self.__read_binary_data__('pres', chunk_number))
        elif dataset == 'velo':
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset += tmp**2
            dset = numpy.sqrt(dset)
        elif dataset == 'vvec':
            dset = [self.__read_binary_data__('velx', chunk_number), \
                    self.__read_binary_data__('vely', chunk_number), \
                    self.__read_binary_data__('velz', chunk_number)]
        elif dataset == 'magn':
            tmp = self.__read_binary_data__('magx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('magy', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('magz', chunk_number)
            dset += tmp**2
            dset = numpy.sqrt(dset)
        elif dataset == 'bvec':
            dset = [self.__read_binary_data__('magx', chunk_number), \
                    self.__read_binary_data__('magy', chunk_number), \
                    self.__read_binary_data__('magz', chunk_number)]
        elif dataset == 'ekin':
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('dens', chunk_number)
            dset *= tmp
            dset *= 0.5
        elif dataset == 'emag':
            tmp = self.__read_binary_data__('magx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('magy', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('magz', chunk_number)
            dset += tmp**2
            dset *= 0.5
        elif dataset == 'elex':
            by = self.__read_binary_data__('magy', chunk_number)
            bz = self.__read_binary_data__('magz', chunk_number)
            vy = self.__read_binary_data__('vely', chunk_number)
            vz = self.__read_binary_data__('velz', chunk_number)
            dset = vy * bz - vz * by
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(by,  1, axis=1) - numpy.roll(by, -1, axis=1))
                    tmp += (numpy.roll(bz, -1, axis=2) - numpy.roll(bz,  1, axis=2))
                else:
                    tmp  = (numpy.roll(bz, -1, axis=1) - numpy.roll(bz,  1, axis=1))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dset -= 0.5 * self.attributes['resistivity'] * tmp
        elif dataset == 'eley':
            bx = self.__read_binary_data__('magx', chunk_number)
            bz = self.__read_binary_data__('magz', chunk_number)
            vx = self.__read_binary_data__('velx', chunk_number)
            vz = self.__read_binary_data__('velz', chunk_number)
            dset = vz * bx - vx * bz
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(bx, -1, axis=1) - numpy.roll(bx,  1, axis=1))
                    tmp += (numpy.roll(bz,  1, axis=3) - numpy.roll(bz, -1, axis=3))
                else:
                    tmp  = (numpy.roll(bz,  1, axis=2) - numpy.roll(bz, -1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dset -= 0.5 * self.attributes['resistivity'] * tmp
        elif dataset == 'elez':
            bx = self.__read_binary_data__('magx', chunk_number)
            by = self.__read_binary_data__('magy', chunk_number)
            vx = self.__read_binary_data__('velx', chunk_number)
            vy = self.__read_binary_data__('vely', chunk_number)
            dset = vx * by - vy * bx
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(bx,  1, axis=2) - numpy.roll(bx, -1, axis=2))
                    tmp += (numpy.roll(by, -1, axis=3) - numpy.roll(by,  1, axis=3))
                else:
                    tmp  = (numpy.roll(bx,  1, axis=1) - numpy.roll(bx, -1, axis=1))
                    tmp += (numpy.roll(by, -1, axis=2) - numpy.roll(by,  1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dset -= 0.5 * self.attributes['resistivity'] * tmp
        elif dataset == 'elec':
            b1 = self.__read_binary_data__('magy', chunk_number)
            b2 = self.__read_binary_data__('magz', chunk_number)
            v1 = self.__read_binary_data__('vely', chunk_number)
            v2 = self.__read_binary_data__('velz', chunk_number)
            dtmp = v1 * b2 - v2 * b1
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1,  1, axis=1) - numpy.roll(b1, -1, axis=1))
                    tmp += (numpy.roll(b2, -1, axis=2) - numpy.roll(b2,  1, axis=2))
                else:
                    tmp  = (numpy.roll(b2, -1, axis=1) - numpy.roll(b2,  1, axis=1))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dtmp -= 0.5 * self.attributes['resistivity'] * tmp
            dset  = dtmp**2

            b1 = self.__read_binary_data__('magx', chunk_number)
            v1 = self.__read_binary_data__('velx', chunk_number)
            dtmp = v2 * b1 - v1 * b2
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1, -1, axis=1) - numpy.roll(b1,  1, axis=1))
                    tmp += (numpy.roll(b2,  1, axis=3) - numpy.roll(b2, -1, axis=3))
                else:
                    tmp  = (numpy.roll(b2,  1, axis=2) - numpy.roll(b2, -1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dtmp -= 0.5 * self.attributes['resistivity'] * tmp
            dset += dtmp**2

            b2 = self.__read_binary_data__('magy', chunk_number)
            v2 = self.__read_binary_data__('vely', chunk_number)
            dtmp = v1 * b2 - v2 * b1
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1,  1, axis=2) - numpy.roll(b1, -1, axis=2))
                    tmp += (numpy.roll(b2, -1, axis=3) - numpy.roll(b2,  1, axis=3))
                else:
                    tmp  = (numpy.roll(b1,  1, axis=1) - numpy.roll(b1, -1, axis=1))
                    tmp += (numpy.roll(b2, -1, axis=2) - numpy.roll(b2,  1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                dtmp -= 0.5 * self.attributes['resistivity'] * tmp
            dset += dtmp**2
            dset = numpy.sqrt(dset)
        elif dataset == 'evec':
            b1 = self.__read_binary_data__('magy', chunk_number)
            b2 = self.__read_binary_data__('magz', chunk_number)
            v1 = self.__read_binary_data__('vely', chunk_number)
            v2 = self.__read_binary_data__('velz', chunk_number)
            wx = v1 * b2 - v2 * b1
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1,  1, axis=1) - numpy.roll(b1, -1, axis=1))
                    tmp += (numpy.roll(b2, -1, axis=2) - numpy.roll(b2,  1, axis=2))
                else:
                    tmp  = (numpy.roll(b2, -1, axis=1) - numpy.roll(b2,  1, axis=1))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                wx -= 0.5 * self.attributes['resistivity'] * tmp

            b1 = self.__read_binary_data__('magx', chunk_number)
            v1 = self.__read_binary_data__('velx', chunk_number)
            wy = v2 * b1 - v1 * b2
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1, -1, axis=1) - numpy.roll(b1,  1, axis=1))
                    tmp += (numpy.roll(b2,  1, axis=3) - numpy.roll(b2, -1, axis=3))
                else:
                    tmp  = (numpy.roll(b2,  1, axis=2) - numpy.roll(b2, -1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                wy -= 0.5 * self.attributes['resistivity'] * tmp

            b2 = self.__read_binary_data__('magy', chunk_number)
            v2 = self.__read_binary_data__('vely', chunk_number)
            wz = v1 * b2 - v2 * b1
            if self.attributes['resistivity'] > 0:
                if self.attributes['ndims'] == 3:
                    tmp  = (numpy.roll(b1,  1, axis=2) - numpy.roll(b1, -1, axis=2))
                    tmp += (numpy.roll(b2, -1, axis=3) - numpy.roll(b2,  1, axis=3))
                else:
                    tmp  = (numpy.roll(b1,  1, axis=1) - numpy.roll(b1, -1, axis=1))
                    tmp += (numpy.roll(b2, -1, axis=2) - numpy.roll(b2,  1, axis=2))

                for p in range(self.chunks[chunk_number]['dblocks']):
                    tmp[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
                wz -= 0.5 * self.attributes['resistivity'] * tmp

            dset = [wx, wy, wz]
        elif dataset == 'eint':
            dset = self.__read_binary_data__('pres', chunk_number)
            dset *= 1.0 / (self.attributes('adiabatic_index') - 1)
        elif dataset == 'temp':
            dset = self.__read_binary_data__('pres', chunk_number) / self.__read_binary_data__('dens', chunk_number)
        elif dataset == 'etot':
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('dens', chunk_number)
            dset *= tmp
            tmp = self.__read_binary_data__('pres', chunk_number)
            dset += 2.0 / (self.attributes('adiabatic_index') - 1) * tmp
            if 'magn' in self.variables:
                tmp = self.__read_binary_data__('magx', chunk_number)
                dset = tmp**2
                tmp = self.__read_binary_data__('magy', chunk_number)
                dset += tmp**2
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset += tmp**2
            dset *= 0.5
        elif dataset == 'lore':
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = tmp**2
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset += tmp**2
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset += tmp**2
            dset = 1.0 / numpy.sqrt(1.0 - dset)
        elif dataset == 'divv':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset  = (numpy.roll(tmp, -1, axis=p) \
                   - numpy.roll(tmp,  1, axis=p))
            p -= 1
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset += (numpy.roll(tmp, -1, axis=p) \
                   - numpy.roll(tmp,  1, axis=p))
            p -= 1
            if p >= 0:
                tmp = self.__read_binary_data__('velz', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=p) \
                       - numpy.roll(tmp,  0, axis=p))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'vorx':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('vely', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=1) \
                       - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('velz', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=2) \
                       - numpy.roll(tmp,  1, axis=2))
            else:
                tmp = self.__read_binary_data__('velz', chunk_number)
                dset  = (numpy.roll(tmp, -1, axis=1) \
                       - numpy.roll(tmp,  1, axis=1))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'vory':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('velx', chunk_number)
                dset  = (numpy.roll(tmp, -1, axis=1) \
                       - numpy.roll(tmp,  1, axis=1))
                tmp = self.__read_binary_data__('velz', chunk_number)
                dset += (numpy.roll(tmp,  1, axis=3) \
                       - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('velz', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=2) \
                       - numpy.roll(tmp, -1, axis=2))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'vorz':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('velx', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=2) \
                       - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('vely', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=3) \
                       - numpy.roll(tmp,  1, axis=3))
            else:
                tmp = self.__read_binary_data__('velx', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=1) \
                       - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('vely', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=2) \
                       - numpy.roll(tmp,  1, axis=2))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'wvec':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('velx', chunk_number)
                wy  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wz  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('vely', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=3) \
                     - numpy.roll(tmp,  1, axis=3))
                wx  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('velz', chunk_number)
                wx += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                wy += (numpy.roll(tmp,  1, axis=3) \
                     - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('velx', chunk_number)
                wz  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('vely', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                tmp = self.__read_binary_data__('velz', chunk_number)
                wx  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wy  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))

            for p in range(self.chunks[chunk_number]['dblocks']):
                h = 2 * self.cell_size[self.chunks[chunk_number]['levels'][p]]
                wx[p,...] /= h
                wy[p,...] /= h
                wz[p,...] /= h

            dset = [wx, wy, wz]
        elif dataset == 'vort':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('velx', chunk_number)
                wy  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wz  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('vely', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=3) \
                     - numpy.roll(tmp,  1, axis=3))
                wx  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('velz', chunk_number)
                wx += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                wy += (numpy.roll(tmp,  1, axis=3) \
                     - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('velx', chunk_number)
                wz  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('vely', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                tmp = self.__read_binary_data__('velz', chunk_number)
                wx  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wy  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))

            dset = 0.5 * numpy.sqrt(wx**2 + wy**2 + wz**2)
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvxdx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvxdy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('velx', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvxdz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('velx', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        elif dataset == 'dvydx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvydy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('vely', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvydz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('vely', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        elif dataset == 'dvzdx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvzdy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('velz', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dvzdz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('velz', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        elif dataset == 'divb':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('magx', chunk_number)
            dset  = (numpy.roll(tmp, -1, axis=p) \
                   - numpy.roll(tmp,  1, axis=p))
            p -= 1
            tmp = self.__read_binary_data__('magy', chunk_number)
            dset += (numpy.roll(tmp, -1, axis=p) \
                   - numpy.roll(tmp,  1, axis=p))
            p -= 1
            if p >= 0:
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=p) \
                       - numpy.roll(tmp,  0, axis=p))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'curx':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('magy', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=1) \
                       - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=2) \
                       - numpy.roll(tmp,  1, axis=2))
            else:
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset  = (numpy.roll(tmp, -1, axis=1) \
                       - numpy.roll(tmp,  1, axis=1))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'cury':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('magx', chunk_number)
                dset  = (numpy.roll(tmp, -1, axis=1) \
                       - numpy.roll(tmp,  1, axis=1))
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset += (numpy.roll(tmp,  1, axis=3) \
                       - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('magz', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=2) \
                       - numpy.roll(tmp, -1, axis=2))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'curz':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('magx', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=2) \
                       - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('magy', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=3) \
                       - numpy.roll(tmp,  1, axis=3))
            else:
                tmp = self.__read_binary_data__('magx', chunk_number)
                dset  = (numpy.roll(tmp,  1, axis=1) \
                       - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magy', chunk_number)
                dset += (numpy.roll(tmp, -1, axis=2) \
                       - numpy.roll(tmp,  1, axis=2))

            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'jvec':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('magx', chunk_number)
                wy  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wz  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('magy', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=3) \
                     - numpy.roll(tmp,  1, axis=3))
                wx  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magz', chunk_number)
                wx += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                wy += (numpy.roll(tmp,  1, axis=3) \
                     - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('magx', chunk_number)
                wz  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magy', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                tmp = self.__read_binary_data__('magz', chunk_number)
                wx  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wy  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))

            for p in range(self.chunks[chunk_number]['dblocks']):
                h = 2 * self.cell_size[self.chunks[chunk_number]['levels'][p]]
                wx[p,...] /= h
                wy[p,...] /= h
                wz[p,...] /= h

            dset = [wx, wy, wz]
        elif dataset == 'curr':
            if self.attributes['ndims'] == 3:
                tmp = self.__read_binary_data__('magx', chunk_number)
                wy  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wz  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))
                tmp = self.__read_binary_data__('magy', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=3) \
                     - numpy.roll(tmp,  1, axis=3))
                wx  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magz', chunk_number)
                wx += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                wy += (numpy.roll(tmp,  1, axis=3) \
                     - numpy.roll(tmp, -1, axis=3))
            else:
                tmp = self.__read_binary_data__('magx', chunk_number)
                wz  = (numpy.roll(tmp,  1, axis=1) \
                     - numpy.roll(tmp, -1, axis=1))
                tmp = self.__read_binary_data__('magy', chunk_number)
                wz += (numpy.roll(tmp, -1, axis=2) \
                     - numpy.roll(tmp,  1, axis=2))
                tmp = self.__read_binary_data__('magz', chunk_number)
                wx  = (numpy.roll(tmp, -1, axis=1) \
                     - numpy.roll(tmp,  1, axis=1))
                wy  = (numpy.roll(tmp,  1, axis=2) \
                     - numpy.roll(tmp, -1, axis=2))

            dset = 0.5 * numpy.sqrt(wx**2 + wy**2 + wz**2)
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbxdx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('magx', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbxdy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('magx', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbxdz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('magx', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        elif dataset == 'dbydx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('magy', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbydy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('magy', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbydz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('magy', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        elif dataset == 'dbzdx':
            p = self.attributes['ndims']
            tmp = self.__read_binary_data__('magz', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbzdy':
            p = self.attributes['ndims'] - 1
            tmp = self.__read_binary_data__('magz', chunk_number)
            dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
            dset *= 0.5
            for p in range(self.chunks[chunk_number]['dblocks']):
                dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
        elif dataset == 'dbzdz':
            p = self.attributes['ndims'] - 2
            tmp = self.__read_binary_data__('magz', chunk_number)
            if p >= 0:
                dset = numpy.roll(tmp, -1, axis=p) - numpy.roll(tmp,  1, axis=p)
                dset *= 0.5
                for p in range(self.chunks[chunk_number]['dblocks']):
                    dset[p,...] /= self.cell_size[self.chunks[chunk_number]['levels'][p]]
            else:
                dset = numpy.zeros_like(tmp)
        else:
            dset = self.__read_binary_data__(dataset, chunk_number)

        return dset


    def dataset(self, dataset_name, extent=None, maxlev=None, shrink=1, \
                           interpolation='rebin', order=3, progress=False):
        """
            Function returns dataset of the requested variable resampled to
            the uniform mesh.
        """
        from .interpolation import interpolate
        import numpy, sys

        if self.dataformat == None:
            raise Exception("Snapshot object has not been properly initialized!")

        if not dataset_name in self.variables:
            raise Exception("Dataset '{}' is not available!\nAvailable datasets: {}\n".format(dataset_name, list(self.variables.keys())))

        dlo = numpy.array([self.attributes['xmin'], self.attributes['ymin']])
        dup = numpy.array([self.attributes['xmax'], self.attributes['ymax']])
        dln = numpy.array([self.attributes['xlen'], self.attributes['ylen']])
        if self.attributes['ndims'] == 3:
            dlo = numpy.append(dlo, self.attributes['zmin'])
            dup = numpy.append(dup, self.attributes['zmax'])
            dln = numpy.append(dln, self.attributes['zlen'])

        slo = numpy.array(dlo)
        sup = numpy.array(dup)
        if extent != None:
            if len(extent) != 2 * self.attributes['ndims']:
                raise Exception("Wrong dimensions of the argument 'extent'!")
            slo = numpy.array(extent)[0::2]
            sup = numpy.array(extent)[1::2]
            if any(slo > dup) or any(sup < dlo) or any (slo >= sup):
                raise Exception("Wrong order of the dimensions in the argument 'extent'!")

        if maxlev != None:
            if isinstance(maxlev, (int, numpy.int32)):
                if 1 <= maxlev <= self.attributes['maxlev']:
                    shrink = 2**(self.attributes['maxlev']-maxlev)
                elif maxlev > self.attributes['maxlev']:
                    raise Exception("Argument 'maxlev' should be between 1 and {}.\n".format(self.attributes['maxlev']))
            else:
                raise Exception("Argument 'maxlev' must be an integer between 1 and {}.\n".format(self.attributes['maxlev']))

        bm = numpy.array([ self.attributes['ncells'] ]*self.attributes['ndims'])

        if self.attributes['ndims'] == 3:
            rm = numpy.array([self.attributes['zblocks'], self.attributes['yblocks'], self.attributes['xblocks']])
        else:
            rm = numpy.array([self.attributes['yblocks'], self.attributes['xblocks']])

        dm = rm * self.attributes['ncells'] * 2**(self.attributes['toplev'] - 1) // shrink
        ll = numpy.array(numpy.floor(dm[::-1] * (slo - dlo) / dln), dtype='int')
        uu = numpy.array( numpy.ceil(dm[::-1] * (sup - dlo) / dln), dtype='int')
        dm  = (uu - ll)[::-1]
        if dataset_name in [ 'velocity', 'vorticity', 'magnetic field', 'current density', 'electric field']:
            arr = [ numpy.zeros(dm[:]), numpy.zeros(dm[:]), numpy.zeros(dm[:]) ]
        else:
            arr = numpy.zeros(dm[:])

        if progress:
            sys.stdout.write("Snapshot's path:\n  '{}'\n".format(self.path))
            m = 0

        for n in range(self.attributes['nchunks']):

            if self.chunks[n]['dblocks'] > 0:

                dset = self.__get_dataset__(dataset_name, n)

                for p in range(self.chunks[n]['dblocks']):
                    nl = 2**(self.attributes['toplev'] - self.chunks[n]['levels'][p])
                    if nl <= shrink:
                        method = 'rebin'
                    else:
                        method = interpolation
                    cm = bm[0:self.attributes['ndims']] * nl // shrink
                    il = self.chunks[n]['coords'][p,:][0:self.attributes['ndims']] * cm[0:self.attributes['ndims']]
                    iu = il + cm[0:self.attributes['ndims']]

                    if all(iu[:] > ll[:]) and all(il[:] < uu[:]):
                        nb = il[:] - ll[:]
                        ne = iu[:] - ll[:]
                        ib = numpy.maximum(nb[:], 0)
                        ie = numpy.minimum(ne[:], uu[:] - ll[:])
                        jb = ib[:] - nb[:]
                        je = ie[:] - ne[:] + cm[:]

                        if isinstance(dset, (list, tuple)):
                            for di in range(3):
                                if self.attributes['ndims'] == 3:
                                    arr[di][ib[2]:ie[2],ib[1]:ie[1],ib[0]:ie[0]] = interpolate(dset[di][p,:,:,:], cm, self.attributes['nghosts'], method=method, order=order)[jb[2]:je[2],jb[1]:je[1],jb[0]:je[0]]
                                else:
                                    arr[di][ib[1]:ie[1],ib[0]:ie[0]] = interpolate(dset[di][p,:,:], cm, self.attributes['nghosts'], method=method, order=order)[jb[1]:je[1],jb[0]:je[0]]
                        else:
                            if self.attributes['ndims'] == 3:
                                arr[ib[2]:ie[2],ib[1]:ie[1],ib[0]:ie[0]] = interpolate(dset[p,:,:,:], cm, self.attributes['nghosts'], method=method, order=order)[jb[2]:je[2],jb[1]:je[1],jb[0]:je[0]]
                            else:
                                arr[ib[1]:ie[1],ib[0]:ie[0]] = interpolate(dset[p,:,:], cm, self.attributes['nghosts'], method=method, order=order)[jb[1]:je[1],jb[0]:je[0]]

                    if progress:
                        cfile = self.chunkname.format(n)
                        m += 1
                        sys.stdout.write('\r')
                        sys.stdout.write("Reading '{}' from '{}': block {} of {}".format(dataset_name, cfile, m, self.attributes['nleafs']))
                        sys.stdout.flush()

        if (progress):
            sys.stdout.write('\n')
            sys.stdout.flush()

        return arr


    def dataset_to_vtk(self, dataset_name, label=None, compression=None, compression_level=19, progress=False):
        """
            Function converts dataset of the requested variable to AMR VTK file.
        """
        import numpy, os, sys
        from .octree import OcBase, OcNode
        from .vtkio import WriteVTK

        if self.dataformat == None:
            raise Exception("Snapshot object has not been properly initialized!")

        if not dataset_name in self.variables:
            raise Exception("Dataset '{}' is not available!\nAvailable datasets: {}\n".format(dataset_name, list(self.variables.keys())))

        if label == None:
            label = dataset_name

        if self.attributes['ndims'] < 3:
            raise Exception("Conversion to OverlappedAMR works only with 3D snapshots!")

        base = OcBase([self.attributes['xmin'], self.attributes['ymin'], self.attributes['zmin']], \
                      [self.attributes['xlen'], self.attributes['ylen'], self.attributes['zlen']], \
                      [self.attributes['xblocks'], self.attributes['yblocks'], self.attributes['zblocks']])

        ng = self.attributes['nghosts']

        if progress:
            sys.stdout.write("Snapshot's path:\n  '{}'\n".format(self.path))
            m = 0

        for n in range(self.attributes['nchunks']):

            if self.chunks[n]['dblocks'] > 0:

                dset = self.__get_dataset__(dataset_name, n)

                for p in range(self.chunks[n]['dblocks']):

                    lv = self.chunks[n]['levels'][p] - 1

                    center = (self.chunks[n]['bounds'][p,0,:] + self.chunks[n]['bounds'][p,1,:]) / 2
                    base.createNodeBranch(center, lv)
                    if isinstance(dset, (list, tuple)):
                        base.setNodeData(center, lv, (dset[0][p,ng:-ng,ng:-ng,ng:-ng], dset[1][p,ng:-ng,ng:-ng,ng:-ng], dset[2][p,ng:-ng,ng:-ng,ng:-ng]))
                    else:
                        base.setNodeData(center, lv, dset[p,ng:-ng,ng:-ng,ng:-ng])

                    if progress:
                        cfile = self.chunkname.format(n)
                        m += 1
                        sys.stdout.write('\r')
                        sys.stdout.write("Reading '{}' from '{}': block {} of {}".format(dataset_name, cfile, m, self.attributes['nleafs']))
                        sys.stdout.flush()

        if (progress):
            sys.stdout.write('\n')
            sys.stdout.flush()

        if progress:
            sys.stdout.write("Populating AMR structure\n")
        base.populateNodeData()

        if progress:
            sys.stdout.write("Generating OverlappingAMR VTK files\n")

        bm = numpy.array([ self.attributes['ncells'] ]*self.attributes['ndims'])

        if self.attributes['ndims'] == 3:
            rm = numpy.array([self.attributes['zblocks'], self.attributes['yblocks'], self.attributes['xblocks']])
        else:
            rm = numpy.array([self.attributes['yblocks'], self.attributes['xblocks']])

        ofile = "{}_{:06d}.vthb".format(dataset_name, self.attributes['isnap'])
        opath = "{}_{:06d}".format(dataset_name, self.attributes['isnap'])
        if not os.path.exists(opath):
            os.makedirs(opath)
        with open(ofile, 'w') as vtk:
            vtk.write('<VTKFile type="vtkOverlappingAMR" version="1.1" ' + \
                        'byte_order="LittleEndian" header_type="UInt64">\n')
            vtk.write('  <vtkOverlappingAMR ' + \
                        'origin="{} {} {}" '.format(*base.lower) + \
                        'grid_description="XYZ">\n')

            fmt = '{}_{:0' + str(len(str(self.attributes['toplev']))) + '}_{:0' + str(len(str(base.nodes))) + 'd}.vti'

            m = 0
            for lv in range(self.attributes['toplev']):

                sm = rm[::-1] * 2**lv
                bw = base.size / sm
                cw = bw / self.attributes['ncells']
                vtk.write('    <Block level="{}"'.format(lv) + \
                                ' spacing="{} {} {}">\n'.format(*cw))

                no = 0
                for item in base.getNodesFromLevel(lv):
                    lo = numpy.array(item.index) * bm
                    up = lo + bm - 1
                    ll = numpy.stack((lo,up)).T.flatten()
                    if item.hasData:
                        vfile = os.path.join(opath, fmt.format(dataset_name, lv, no))
                        WriteVTK(vfile, label, item.data, \
                            origin = (item.lower[0], item.lower[1], item.lower[2]), \
                            spacing = (cw[0], cw[1], cw[2]), \
                            compression=compression, compression_level=compression_level)
                        vtk.write('      <DataSet index="{}"'.format(no) + \
                                    ' amr_box = "{} {} {} {} {} {}"'.format(*ll) + \
                                        ' file = "{}"></DataSet>\n'.format(vfile))
                        no += 1
                    else:
                        vtk.write('      <DataSet index="{}"'.format(no) + \
                                    ' amr_box = "{} {} {} {} {} {}"'.format(*ll) + \
                                        '></DataSet>\n')
                    m += 1

                    if progress:
                        sys.stdout.write('\r')
                        sys.stdout.write("Storing AMR block {} of {}".format(m, base.nodes))
                        sys.stdout.flush()

                vtk.write('    </Block>\n')
            vtk.write('  </vtkOverlappingAMR>\n')
            vtk.write('</VTKFile>')

        if (progress):
            sys.stdout.write('\n')
            sys.stdout.flush()
