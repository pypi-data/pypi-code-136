#!/usr/bin/env python
from os.path import isfile
from os import system
import argh
import argparse
import json as js
#import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from irff.tools.vdw import vdw as Evdw
from irff.data.ColData import ColData
from irff.ml.data import get_data,get_bond_data,get_atoms_data #,get_md_data
# from irff.ml.gpfit import train
# tf.compat.v1.disable_eager_execution()

def get_parameters(ffield):
    with open(ffield,'r') as lf:
        j = js.load(lf)
        p = j['p']
        m = j['m']
    return p,m

def Ebond(bd, p, R,ro=1.6, rovdw=3.0, k=0.1):
    b = bd.split('-')
    gamma = np.sqrt(p['gamma_'+b[0]]*p['gamma_'+b[1]])
    gammaw = np.sqrt(p['gammaw_'+b[0]]*p['gammaw_'+b[1]])

    evdw = Evdw(R, Devdw=p['Devdw_'+bd]*4.3364432032e-2, gamma=gamma, gammaw=gammaw,
                vdw1=p['vdw1'], rvdw=p['rvdw_'+bd], alfa=p['alfa_'+bd])

    evdw_ro = Evdw(ro, Devdw=p['Devdw_'+bd]*4.3364432032e-2, gamma=gamma, gammaw=gammaw,
                   vdw1=p['vdw1'], rvdw=p['rvdw_'+bd], alfa=p['alfa_'+bd])
    evdw_rovdw = Evdw(rovdw, Devdw=p['Devdw_'+bd]*4.3364432032e-2, gamma=gamma, gammaw=gammaw,
                      vdw1=p['vdw1'], rvdw=p['rvdw_'+bd], alfa=p['alfa_'+bd])

    Eo = evdw_ro - evdw_rovdw + k*(ro-rovdw)**2
    Eb = []
    for i, r in enumerate(R):
        Eb.append(evdw_ro - evdw[i])

    Eb = np.array(Eb)
    Eb = Eb - Eo

    for i, r in enumerate(R):
        Eb[i] += k*(r-ro)**2
    return Eb,evdw

def harm(gen='gulp.traj',bonds=None,ro=2.17,rovdw=3.0,k_lo=5.0,k_up=4.75):
    D, Bp, B, R, E = get_atoms_data(gen=gen,bonds=bonds)
    # D, Bp, B, R, E = get_bond_data(i,j,images=None, traj=traj,bonds=bonds)
    p,_ = get_parameters('ffield.json') 
    for bd in bonds:
        for i,bp in enumerate(Bp[bd]):
            eb = - p['Desi_'+bd]* E[bd][i] * 4.3364432032e-2 
            print('id: {:3d} R: {:6.4f} '
                  'Di: {:7.4f} B\': {:6.4f} Dj: {:7.4f} B: {:7.5f} '
                  'Ebd: {:7.5f}'.format(i,R[bd][i],D[bd][i][0],D[bd][i][1],D[bd][i][2],
                                        np.sum(B[bd][i]),eb))
    # ro=2.17
    # rovdw= 3.0
    # k_lo = 5.0
    # k_up = 4.75
    eb1, evdw = Ebond(bd, p, R[bd], ro=ro, rovdw=rovdw, k=k_lo)
    eb2, evdw = Ebond(bd, p, R[bd], ro=ro, rovdw=rovdw, k=k_up)
    
    plt.figure()
    
    ebd_= np.array(E[bd])
    ebd = -p['Desi_'+bd]*ebd_*4.3364432032e-2  ## Bond-Energy

    #plt.plot(R[bd],evdw,alpha=0.8,linewidth=2,linestyle='-',color='r',
    #         label=r'$E_{vdw}$')
    plt.subplot(2,2,1) 
    plt.scatter(R[bd],evdw,alpha=0.8,marker='o',color='r',s=10,
                label=r'$E_{vdw}$')
    plt.legend(loc='best',edgecolor='yellowgreen')  

    plt.subplot(2,2,2) 
    plt.scatter(R[bd],ebd,alpha=0.8,marker='o',color='r',s=10,
               label=r'$E_{bond}$')
    plt.scatter(R[bd],eb1,alpha=0.8,marker='^',color='y',s=2)
    plt.scatter(R[bd],eb2,alpha=0.8,marker='v',color='c',s=2)
    plt.legend(loc='best',edgecolor='yellowgreen')

    plt.subplot(2,1,2) 
    plt.scatter(R[bd],evdw+ebd,alpha=0.8,marker='o',color='r',s=10,
                label=r'$E_{vdw}$ + $E_{bond}$')
    
    plt.scatter(R[bd],evdw+eb1,alpha=0.8,marker='^',color='y',s=2,
                label=r'$E_{bond+vdw}^l$')
    plt.scatter(R[bd],evdw+eb2,alpha=0.8,marker='v',color='c',s=2,
                label=r'$E_{bond+vdw}^u$')

    # diff = np.abs(pdft - preax)
    # plt.fill_between(R[bd], evdw+eb1, evdw+eb2, color='palegreen',
    #                  alpha=0.2)

    # plt.savefig('vdw_energy_{:s}.pdf'.format(bd))
    plt.legend(loc='best',edgecolor='yellowgreen')
    plt.show()
    plt.close() 


if __name__ == '__main__':
   ''' constrain the bond-energy according harmonic approximation
       Run with commond: ./be_harm.py  '''
   #bo(gen='gulp.traj',bonds=['O-Fe'],ro=2.17,rovdw=3.0,k_lo=5.0,k_up=4.8)
   harm(gen='gulp.traj',bonds=['Fe-Fe'],ro=2.45,rovdw=3.2,k_lo=4.2,k_up=3.8)
