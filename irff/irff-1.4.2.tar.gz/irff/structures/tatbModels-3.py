#!/usr/bin/env python
# coding: utf-8
from ase.visualize import view
from ase.io import read
from ase.io.trajectory import TrajectoryWriter,Trajectory
from irff.structures import structure
from irff.molecule import Molecules,SuperCell,moltoatoms
import numpy as np


# <font color=blue size=4>构建超晶</font>


A = structure('tatb')
x = A.get_positions()
m = np.min(x,axis=0)
x_ = x - m
A.set_positions(x_)

M = Molecules(A)
nmol = len(M)
print('\nnumber of molecules:',nmol)

cell = A.get_cell()
m,A = SuperCell(M,cell=cell,supercell=[15,15,2])
natom = len(A)
print('\nnumber of atoms:',natom)
nmol = len(m)
print('\nnumber of molecules in super-cell:',nmol)
# view(A)


cell = A.get_cell()
print(cell)


# <font color=blue size=4> 如果分子在方形区域内</font>
# 
# x ~ (0,90)
# 
# y ~ (0,50)

mol_in_region = []
for m_ in m:
    # print(m_.center)
    c = m_.center
    if c[0]>0 and c[0]<90:
       if c[1]>0 and c[1]<90:
          mol_in_region.append(m_)
    
A = moltoatoms(mol_in_region)
print('number of atoms in region:',len(A))
A.set_cell([[92.0, 0.0, 0.0],
            [0.0, 94.0, 0.0], 
            [0.0,0.0, 12.559967994689941]])

# view(A)
# <font color=blue size=4>PDA聚合物</font>

P = structure('pda')
# P.set_cell([[4.60, 0.0, 0.0],
#             [0.0, 10.0, 0.0], 
#             [0.0,0.0, 3.5]])
P = P*[20,9,1]
#P.set_pbc([True,True,True])
#P.write('pda.pdb')
print(P.get_cell())


# view(P)
# <font color=blue size=4>合并两个结构</font>

# mol_in_region = []
P_mol = Molecules(P)
for m_ in P_mol:
    m_.move([0.0,0.0,13.0])
    mol_in_region.append(m_)
    
B = moltoatoms(mol_in_region)
B.set_cell([92.0, 90.0, 18.0])
view(B)


