#!/usr/bin/env python
from os import system, getcwd, chdir,listdir
from os.path import isfile,exists,isdir
import numpy as np
import json as js
import matplotlib.pyplot as plt
from ase import Atoms
from ase.io import read,write
from ase.io.trajectory import TrajectoryWriter,Trajectory
from irff.dft.cpmd import get_lattice
from irff.reax_data import get_data


dataset = {'test':'FeO.traj'}
atoms = read('FeO.traj')
with open('ffield.json','r') as lf:
     j = js.load(lf)
     p = j['p']

data_ =  get_data(structure='test',
                    direc=dataset['test'],
                        dft='ase',
                    atoms=atoms,
                    vdwcut=10.0,
                        rcut={'Fe-Fe':3.2,'Fe-O':3.0,'O-O':2.5},
                    rcuta={'Fe-Fe':3.2,'Fe-O':3.0,'O-O':2.5},
                    hbshort=6.75,
                    hblong=7.5,
                    batch=50,
                    p=p,
                    spec=('Fe','O'),
                    bonds=('Fe-Fe','Fe-O','O-O'))



