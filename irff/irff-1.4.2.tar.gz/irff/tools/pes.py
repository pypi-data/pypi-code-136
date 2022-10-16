#!/usr/bin/env python
# coding: utf-8
from ase.visualize import view
from ase.io import read
from ase.io.trajectory import TrajectoryWriter,Trajectory
from ase.calculators.singlepoint import SinglePointCalculator
from irff.AtomDance import AtomDance
# get_ipython().run_line_magic('matplotlib', 'inline')


atoms  = read('h2o.gen',index=-1)
ad     = AtomDance(atoms=atoms,rmax=1.33)
zmat   = ad.InitZmat
# zmat[2][1] = 109.0


#images = []
his    = TrajectoryWriter('md.traj',mode='w')
ang    = 90.0

for i in range(30):
    r   = 0.7
    ang += 3.0
    zmat[2][1] = ang
    atoms  = ad.zmat_to_cartation(atoms,zmat)
    for j in range(20):
        r += 0.03
        zmat[2][0] = r
        atoms  = ad.zmat_to_cartation(atoms,zmat)
        ad.ir.calculate(atoms)
        calc = SinglePointCalculator(atoms,energy=ad.ir.E)
        atoms.set_calculator(calc)
        his.write(atoms=atoms)
    # images.append(atoms.copy())

his.close()
# view(images)
ad.close()
# view(images)



