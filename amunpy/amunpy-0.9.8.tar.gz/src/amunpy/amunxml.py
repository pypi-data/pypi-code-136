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

 module: AMUNXML

  This module implements an interface class to read attributes, coordinates,
  and datasets stored in AmunXML format snapshots.

--------------------------------------------------------------------------------
"""
from .amun import Amun

class AmunXML(Amun):
    """AMUN XML snapshot class"""

    def __init_snapshot__(self):
        """
            Sets the data format after verifying if the snapshot is stored
            in AmunXML format.
        """
        import os
        import xml.etree.ElementTree as ET

        if not self.path_is_file:
            self.filename = "metadata.xml"

        mfile = os.path.join(self.dirname, self.filename)
        if os.path.exists(mfile):
            tree = ET.parse(mfile)
            root = tree.getroot()
            if self.version < 0:
                if 'version' in root.attrib:
                        self.version = int(float(root.attrib['version']))
            if root.tag == 'AMUNFile':
                self.dataformat = 'AmunXML'
            else:
                raise Exception("{} does not seem to be an AmunXML snapshot!".format(mfile))
        else:
            raise Exception("{} does not exist!".format(mfile))


    def __fill_attributes__(self):
        """
            Reads attributes from the snapshot file and adds them to
            the attributes' dictionary.
        """
        import os
        import xml.etree.ElementTree as ET

        exclude_list = ['nproc']

        tree = ET.parse(os.path.join(self.dirname, self.filename))
        root = tree.getroot()
        for child in root:
            if not child.tag == 'BinaryFiles':
                for item in child:
                    if item.tag == 'Attribute':
                        if not item.attrib['name'] in exclude_list:
                            if item.attrib['type'] == 'double':
                                self.attributes[item.attrib['name']] = float(item.text)
                            elif item.attrib['type'] == 'integer':
                                self.attributes[item.attrib['name']] = int(item.text)
                            else:
                                self.attributes[item.attrib['name']] = item.text

        if not 'nchunks' in self.attributes and 'nprocs' in self.attributes:
            self.attributes['nchunks'] = self.attributes['nprocs']
            del self.attributes['nprocs']

        if not 'zmin' in self.attributes:
            self.attributes['zmin'] = 0
        if not 'zmax' in self.attributes:
            self.attributes['zmax'] = 1
        if not 'zblocks' in self.attributes:
            self.attributes['zblocks'] = 1


    def __fill_variables__(self):
        """
            Reads the names of datasets stored in the snapshot and adds them
            to the variables' dictionary.
        """
        if 'variables' in self.attributes:
            for v in self.attributes['variables'].split():
                self.variables[v] = v
        else:
            raise Exception("No attribute 'variables' in {}!".format(self.filename))


    def __fill_chunks__(self):
        """
            Retrieves metadata about datablocks stored in the snapshot's chunks
            and adds them to the chunks' dictionary.
        """
        import numpy, os
        import xml.etree.ElementTree as ET

        self.binaries = dict()

        fname = os.path.join(self.dirname, self.filename)
        tree  = ET.parse(fname)
        root  = tree.getroot()
        for child in root:
            if child.tag == 'BinaryFiles':
                for item in child:
                    self.binaries[item.attrib['name']]         = item.attrib
                    self.binaries[item.attrib['name']]['file'] = item.text

        self.chunkname = 'datablocks_{:06d}.xml'
        for n in range(self.attributes['nchunks']):
            self.chunks[n] = dict()
            self.chunks[n]['filename'] = self.chunkname.format(n)
            fname = os.path.join(self.dirname, self.chunks[n]['filename'])
            if os.path.exists(fname):
                tree = ET.parse(fname)
                root = tree.getroot()
                for item in root.findall('./BinaryFiles/Attribute'):
                    self.chunks[n][item.attrib['name']]         = item.attrib
                    self.chunks[n][item.attrib['name']]['file'] = item.text
                for item in root.findall('./DataBlocks/Attribute'):
                    if item.attrib['name'] == 'dblocks':
                        self.chunks[n]['dblocks'] = int(item.text)
            else:
                raise Exception("Snapshot's chunk '{}' does not exist!".format(fname))

        mset = self.__read_binary_meta('fields')

        n     = mset.size // self.attributes['nleafs']
        if self.version > 0:
            mset  = numpy.reshape(mset, [self.attributes['nleafs'],n])
        else:
            mset  = self.__swap__(numpy.reshape(mset, [n, self.attributes['nleafs']]))

        index = dict()
        level = dict()
        coord = dict()
        for n in range(self.attributes['nleafs']):
            index[mset[n,0]] = n
            level[mset[n,0]] = mset[n,  1]
            coord[mset[n,0]] = mset[n,2:5]

        bounds = self.__read_binary_meta('bounds', dtype='float64')
        if self.version > 0:
            bounds = numpy.reshape(bounds, [self.attributes['nleafs'], 2, 3])
        else:
            bounds = self.__swap__(numpy.reshape(bounds, [2, 3, self.attributes['nleafs']]))

        for n in range(self.attributes['nchunks']):
            nblk = self.chunks[n]['dblocks']
            if nblk > 0:
                ids = self.__read_binary_data('ids', n, dtype='int32')

                self.chunks[n]['levels'] = numpy.array([level[ids[p]] for p in range(nblk)])
                self.chunks[n]['coords'] = numpy.array([coord[ids[p]] for p in range(nblk)])

                ii  = [ index[ids[p]] for p in range(nblk) ]

                self.chunks[n]['bounds'] = numpy.array([bounds[ii[p],:,:] for p in range(nblk)])
            else:
                self.chunks[n]['levels'] = None
                self.chunks[n]['coords'] = None
                self.chunks[n]['bounds'] = None


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
        import numpy

        dims = self.chunks[chunk_number]['dims']
        if self.version < 1:
            dims = numpy.roll(self.chunks[chunk_number]['dims'], -1)
        dset = numpy.reshape(self.__read_binary_data(dataset_name, chunk_number), dims)
        return self.__swap__(dset)


    def __check_digest(self, filename, hash_type, digest, data):
        '''
            Verifies if the provided digest matches the data.
        '''
        import xxhash

        failed = False
        if hash_type == 'xxh64':
            failed = digest.lower() != xxhash.xxh64(data).hexdigest()
        elif hash_type == 'xxh3':
            failed = digest.lower() != xxhash.xxh3_64(data).hexdigest()
        if failed:
            print("File '{}' seems to be corrupted! Proceeding anyway...".format(filename))


    def __read_binary_meta(self, dataset, dtype='int32'):
        '''
            Reads binary data of metadata.
        '''
        import numpy, os
        import zstandard as zstd
        import lz4.frame as lz4
        import lzma

        fname = os.path.join(self.path, self.binaries[dataset]['file'])
        if os.path.exists(fname):
            with open(fname, mode ='rb') as f:
                stream = f.read()

            if 'compression_format' in self.binaries[dataset]:
                if 'compressed_digest' in self.binaries[dataset]:
                    htype = self.binaries[dataset]['digest_type']
                    dhash = self.binaries[dataset]['compressed_digest']
                    self.__check_digest(fname, htype, dhash, stream)

                comp = self.binaries[dataset]['compression_format']
                if comp == 'zstd':
                    data = zstd.ZstdDecompressor().decompress(stream)
                elif comp == 'lz4':
                    data = lz4.decompress(stream)
                elif comp == 'lzma':
                    data = lzma.decompress(stream)
                else:
                    raise Exception("Binary file '{}' compressed in unsupported format {}!".format(fname, comp))

                if 'digest' in self.binaries[dataset]:
                    htype = self.binaries[dataset]['digest_type']
                    dhash = self.binaries[dataset]['digest']
                    self.__check_digest(fname, htype, dhash, data)

                return numpy.frombuffer(data, dtype=dtype)
            else:
                if 'digest' in self.binaries[dataset]:
                    htype = self.binaries[dataset]['digest_type']
                    dhash = self.binaries[dataset]['digest']
                    self.__check_digest(fname, htype, dhash, stream)

                return numpy.frombuffer(stream, dtype=dtype)
        else:
            raise Exception("Binary file '{}' does not exist!".format(fname))


    def __read_binary_data(self, dataset_name, chunk_number, dtype='float64'):
        '''
            Reads binary data of provided dataset name from a given chunk.
        '''
        import numpy, os
        import zstandard as zstd
        import lz4.frame as lz4
        import lzma

        fname = os.path.join(self.path, self.chunks[chunk_number][dataset_name]['file'])
        if os.path.exists(fname):
            with open(fname, mode ='rb') as f:
                stream = f.read()

            if 'compression_format' in self.chunks[chunk_number][dataset_name]:
                if 'compressed_digest' in self.chunks[chunk_number][dataset_name]:
                    htype = self.chunks[chunk_number][dataset_name]['digest_type']
                    dhash = self.chunks[chunk_number][dataset_name]['compressed_digest']
                    self.__check_digest(fname, htype, dhash, stream)

                comp = self.chunks[chunk_number][dataset_name]['compression_format']
                if comp == 'zstd':
                    dctx = zstd.ZstdDecompressor()
                    data = dctx.decompress(stream)
                elif comp == 'lz4':
                    data = lz4.decompress(stream)
                elif comp == 'lzma':
                    data = lzma.decompress(stream)
                else:
                    raise Exception("Binary file '{}' compressed in unsupported format {}!".format(fname, comp))

                if 'digest' in self.chunks[chunk_number][dataset_name]:
                    htype = self.chunks[chunk_number][dataset_name]['digest_type']
                    dhash = self.chunks[chunk_number][dataset_name]['digest']
                    self.__check_digest(fname, htype, dhash, data)

                return numpy.frombuffer(data, dtype=dtype)
            else:
                if 'digest' in self.chunks[chunk_number][dataset_name]:
                    htype = self.chunks[chunk_number][dataset_name]['digest_type']
                    dhash = self.chunks[chunk_number][dataset_name]['digest']
                    self.__check_digest(fname, htype, dhash, stream)

                return numpy.frombuffer(stream, dtype=dtype)
        else:
            raise Exception("Binary file '{}' does not exist!".format(fname))
