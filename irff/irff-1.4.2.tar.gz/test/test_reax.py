#!/usr/bin/env python
from os import system, getcwd, chdir,listdir
# from train_reaxff import test_reax
from irff.reax import test_reax

#system('rm *.pkl')
#system('./r2l<ffield>reax.lib')
dataset={'md':'md.traj'}
test_reax(dataset=dataset,dft='siesta',batch_size=100)


