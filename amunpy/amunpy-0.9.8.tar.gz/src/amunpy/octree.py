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

 submodule: octree.py

  Python module to handle the octree structure of blocks used by
  the AMUN's code adaptive mesh representation of the domain.

  This submodule provides two classes:
   OcBase - the base of the structure
   OcNode - the node can be any node with or without data

  The only requirements for this package are:

     - numpy

--------------------------------------------------------------------------------
"""
import itertools

class OcBase(object):
    ''' Octree base '''

    def __init__(self, position, size, dims):
        self.level    = -1
        self.lower    = position
        self.upper    = [p + s for p, s in zip(position, size)]
        self.size     = size
        self.dims     = dims
        self.nodes    = 0
        self.children = []

        blkSize = [s / d for s, d in zip(size, dims)]

        for k, j, i in itertools.product(range(dims[2]), range(dims[1]), range(dims[0])):
            idx = [i, j, k]
            pos = [l + i * s for l, i, s in zip(self.lower, idx, blkSize)]
            self.children.append(OcNode(idx, pos, blkSize, self.level + 1))
            self.nodes += 1


    ''' Function creates the branch of leafs at given position down to the given level'''
    def createNodeBranch(self, position, level):

        for n in range(len(self.children)):
            self.nodes += self.children[n].createNodeBranch(position, level)


    ''' Function assigns data to the node '''
    def setNodeData(self, position, level, data):

        for n in range(len(self.children)):
            self.children[n].setNodeData(position, level, data)


    ''' Function populates all nodes at lower levels with data from higher levels '''
    def populateNodeData(self):

        for n in range(len(self.children)):
            self.children[n].populateNodeData()


    ''' Function returns the list of nodes from the given level '''
    def getNodesFromLevel(self, level):

        items = []

        for n in range(len(self.children)):
            items = items + self.children[n].getNodesFromLevel(level)

        return items


    ''' Function prints the node properties '''
    def printNodes(self, l):

        print(self.lower, self.upper, self.size, self.level)

        for n in range(len(self.children)):
            self.children[n].printNodes(1, l)



class OcNode(object):
    ''' Octree node '''

    def __init__(self, index, position, size, level):
        self.isLeaf   = True
        self.hasData  = False
        self.level    = level
        self.index    = index
        self.lower    = position
        self.upper    = [p + s for p, s in zip(position, size)]
        self.size     = size
        self.children = []
        self.data     = None


    ''' Functions creates the subnodes '''
    def __refine(self):

        newnodes = 0

        if self.isLeaf:

            newSize  = ( self.size[0] / 2, self.size[1] / 2, self.size[2] / 2 )

            for k, j, i in itertools.product(range(2), range(2), range(2)):

                idx = [i, j, k]
                pos = [l + i * s for l, i, s in zip(self.lower, idx, newSize)]
                idx = [2 * l + i for l, i in zip(self.index, idx)]

                self.children.append(OcNode(idx, pos, newSize, self.level + 1))

                newnodes += 1

            self.isLeaf = False

        return newnodes


    ''' Function creates the branch of leafs at given position down to the given level'''
    def createNodeBranch(self, position, level):
        flag = [(l < p and p < u) \
               for l, p, u in zip(self.lower, position, self.upper)]

        newnodes = 0

        if all(flag):
            if self.level < level:
                if self.isLeaf:
                    newnodes = self.__refine()
                for n in range(len(self.children)):
                    newnodes += self.children[n].createNodeBranch(position, level)

        return newnodes


    ''' Function assigns data to the node '''
    def setNodeData(self, position, level, data):

        flag = [(l < p and p < u) \
               for l, p, u in zip(self.lower, position, self.upper)]

        if all(flag):
            if self.isLeaf:
                self.data = data
                self.hasData = True
            else:
                for n in range(len(self.children)):
                    self.children[n].setNodeData(position, level, data)


    ''' Function populates all nodes at lower levels with data from higher levels '''
    def populateNodeData(self):
        from .interpolation import rebin
        import numpy

        if not self.isLeaf:
            for n in range(len(self.children)):
                self.children[n].populateNodeData()

            if isinstance(self.children[0].data, (list, tuple)):

                self.data = []

                for m, comp in enumerate(self.children[0].data):

                    bm  = comp.shape
                    dm  = [ 2 * d for d in bm ]

                    arr = numpy.zeros(dm, dtype=comp.dtype)

                    for k, j, i in itertools.product(range(2), range(2), range(2)):
                        n = (k * 2 + j) * 2 + i
                        ib, jb, kb =  0 + i * bm[0],  0 + j * bm[1],  0 + k * bm[2]
                        ie, je, ke = ib +     bm[0], jb +     bm[1], kb +     bm[2]
                        arr[kb:ke,jb:je,ib:ie] = self.children[n].data[m][:,:,:]

                    self.data.append(rebin(arr, bm))


            else:
                bm  = self.children[0].data.shape
                dm  = [ 2 * d for d in bm ]

                arr = numpy.zeros(dm, dtype=self.children[0].data.dtype)

                for k, j, i in itertools.product(range(2), range(2), range(2)):
                    n = (k * 2 + j) * 2 + i
                    ib, jb, kb =  0 + i * bm[0],  0 + j * bm[1],  0 + k * bm[2]
                    ie, je, ke = ib +     bm[0], jb +     bm[1], kb +     bm[2]
                    arr[kb:ke,jb:je,ib:ie] = self.children[n].data[:,:,:]

                self.data = rebin(arr, bm)

            self.hasData = True


    ''' Function returns the list of nodes from the given level '''
    def getNodesFromLevel(self, level):

        items = []

        if self.level == level:
            items.append(self)
        elif self.level < level:
            for n in range(len(self.children)):
                items = items + self.children[n].getNodesFromLevel(level)

        return items


    ''' Function prints the node properties '''
    def printNodes(self, s, l):

        if self.level <= l:
            print(s*'  ', "[{:6.3f} {:6.3f} {:6.3f}]".format(*self.lower), \
                    "-> [{:6.3f} {:6.3f} {:6.3f}]".format(*self.upper), \
                    ", size: [{:6.3f} {:6.3f} {:6.3f}]".format(*self.size), \
                    ", level: {}".format(self.level), \
                    ", leaf: {}, data: {}".format(self.isLeaf, self.hasData))

            for n in range(len(self.children)):
                self.children[n].printNodes(s+1, l)
