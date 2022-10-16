import numpy as np
from ase import Atoms
from ase.io import read,write
# from ase.io.trajectory import TrajectoryWriter


def graphene(supercell=[3,3,1]):
    radius = 1.420 
    pi = 3.1415926535897932
    h  = 3.40
    hb=radius*np.cos(pi/6.0)

    coord = np.zeros([4,3])
    pos   = np.zeros([4*supercell[0]*supercell[1]*supercell[2],3])


    coord[0] = [0.5*radius,0.0,0.0]
    coord[1] = [1.5*radius,0.0,0.0]
    coord[2] = [0.0,hb,0.0]
    coord[3] = [2.0*radius,hb,0.0]

    a = np.array([[3.0*radius,0.0,0.0]])
    b = np.array([[0.0,2.0*hb,0.0]])
    c = np.array([[0.0,0.0,h]])
    cell = [a[0]*supercell[0],b[0]*supercell[1],c[0]*supercell[2]]

    for i in range(supercell[0]):
        for j in range(supercell[1]):
            for k in range(supercell[2]):
                natm = i*supercell[1]*supercell[2]*4+j*supercell[2]*4+k*4
                pos[natm:natm+4] = coord + a*i + b*j + c*k

    specs = ['C' for i in range(4*supercell[0]*supercell[1]*supercell[2])]

    atoms = Atoms(specs,pos,pbc=[True,True,True],cell=cell)
    # atoms.write('graphene.gen')
    return atoms



if __name__ == '__main__':
   atoms = graphene(supercell=[1,1,1])
   atoms.write('graphene.gen')

