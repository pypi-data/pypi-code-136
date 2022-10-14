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

 module: VTKIO

  Module provides a function to store given dataset in the VTK image file.

--------------------------------------------------------------------------------
"""

def WriteVTK(vtkfile, vname, data, \
            origin=(0, 0, 0), spacing=(1, 1, 1), \
            compression=None, compression_level=19, encode=True, \
            lz4mode='default', lz4acceleration=1, block_size=32768, \
            points=False, verbose=False):

    import base64, numpy, struct, zlib, lz4.block, lzma

    if isinstance(data, (list, tuple)):

        if not all(isinstance(d, (numpy.ndarray)) for d in data):
            raise Exception('All input data components in WriteVTK must be arrays!')

        if not all(data[0].shape == d.shape for d in data):
            raise Exception('All input data components in WriteVTK must have the same dimensions!')

        dtype = 'vector'
        ncomp = len(data)
        ndims = data[0].ndim
        dims  = data[0].shape

    elif isinstance(data, (numpy.ndarray)):

        dtype = 'scalar'
        ncomp = 1
        ndims = data.ndim
        dims  = data.shape

    else:
        raise Exception('Unknown type of the input data in WriteVTK!')

    with open(vtkfile, 'wb') as vt:
        offset = 0
        sdims  = '"'
        if points:
            for i in range(ndims - 1, 0, -1):
                sdims +='%d %d ' % (0, dims[i] - 1)
            sdims += '%d %d" ' % (0, dims[0] - 1)
        else:
            for i in range(ndims - 1, 0, -1):
                sdims +='%d %d ' % (0, dims[i])
            sdims += '%d %d" ' % (0, dims[0])

        string  = '<?xml version="1.0"?>\n<VTKFile type="ImageData" version="1.0" byte_order="LittleEndian" header_type="UInt64"'
        if compression == 'zlib':
            string  += ' compressor="vtkZLibDataCompressor"'
            compression_level = min(max(compression_level, 0), 9)
        elif compression == 'lzma':
            string  += ' compressor="vtkLZMADataCompressor"'
            compression_level = min(max(compression_level, 0), 9)
        elif compression == 'lz4':
            string  += ' compressor="vtkLZ4DataCompressor"'
            compression_level = min(max(compression_level, 0), 12)
            lz4acceleration = max(lz4acceleration, 1)
        string += '>\n  <ImageData WholeExtent=%s' % sdims
        string += 'Origin="%e %e %e" ' % origin
        string += 'Spacing="%e %e %e">\n' % spacing
        string += '    <Piece Extent=%s>\n' % sdims
        if points:
            string += '      <PointData %ss="%s">\n' % (dtype, vname)
        else:
            string += '      <CellData %ss="%s">\n' % (dtype, vname)
        if ncomp == 1:
            dmin = data.min()
            dmax = data.max()
        else:
            dd   = numpy.zeros(data[0].shape)
            for dc in data:
                dd += dc**2
            dmin = numpy.sqrt(dd.min())
            dmax = numpy.sqrt(dd.max())
        string += '        <DataArray '
        if ncomp > 1:
            string += 'NumberOfComponents="{:d}" '.format(ncomp)
        string += 'type="Float32" Name="{}" RangeMin="{:e}" RangeMax="{:e}" format="appended" offset="{}">\n'.format(vname, dmin, dmax, offset)
        string += "        </DataArray>\n"
        if points:
            string += '      </PointData>\n'
        else:
            string += '      </CellData>\n'
        string += '    </Piece>\n'
        string += '  </ImageData>\n'
        vt.write(string.encode())

        if encode:
            string  = '  <AppendedData encoding="base64">\n'
        else:
            string  = '  <AppendedData encoding="raw">\n'
        string += '   _'
        vt.write(string.encode())

        if dtype == 'vector':
            qt = numpy.zeros([ dims[0], dims[1], dims[2], ncomp ], dtype=numpy.float32)
            for n, d in enumerate(data[:]):
                qt[:,:,:,n] = numpy.float32(d)
        else:
            qt = numpy.float32(data)

        barr = qt.tobytes()

        if compression != None:
            if len(barr) < block_size:
                if compression == 'zlib':
                    carr = zlib.compress(barr, compression_level)
                elif compression == 'lz4':
                    carr = lz4.block.compress(barr, mode=lz4mode, acceleration=lz4acceleration, compression=compression_level, store_size=False)
                elif compression == 'lzma':
                    carr = lzma.compress(barr)

                head = struct.pack("QQQQ", 1, len(barr), 0, len(carr))

            else:
                nblocks = len(barr) // block_size
                rsize   = len(barr) % block_size
                if verbose:
                    print("Number of blocks:\t {}\nBlock size:\t\t {}\nRemaining size:\t\t {}".format(nblocks, block_size, rsize))

                head = struct.pack("QQQ", nblocks, block_size, rsize)

                carr = bytearray(b'')
                ib = 0
                if compression == 'zlib':
                    cctx = zlib
                    for i in range(nblocks):
                        ie = min(len(barr), ib + block_size)
                        cblk = cctx.compress(barr[ib:ie], compression_level)
                        head += struct.pack("Q", len(cblk))
                        carr += cblk
                        ib = ie

                elif compression == 'lzma':
                    cctx = lzma
                    for i in range(nblocks):
                        ie = min(len(barr), ib + block_size)
                        cblk = cctx.compress(barr[ib:ie], preset=compression_level)
                        head += struct.pack("Q", len(cblk))
                        carr += cblk
                        ib = ie

                elif compression == 'lz4':
                    cctx = lz4.block
                    for i in range(nblocks):
                        ie = min(len(barr), ib + block_size)
                        cblk = cctx.compress(barr[ib:ie], mode=lz4mode, acceleration=lz4acceleration, compression=compression_level, store_size=False)
                        head += struct.pack("Q", len(cblk))
                        carr += cblk
                        ib = ie

            if encode:
                vt.write(base64.b64encode(head)+base64.b64encode(carr))
            else:
                vt.write(head+carr)

        else:
            head = struct.pack("Q", len(barr))
            if encode:
                vt.write(base64.b64encode(head+barr))
            else:
                vt.write(head+barr)

        string  = '\n  </AppendedData>\n'
        string += '</VTKFile>\n'
        vt.write(string.encode())
