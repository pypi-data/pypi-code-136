import pandas as pd
import json as js
import csv
import numpy as np
from irff.tools.vdw import vdw as Evdw

def make_fluct(fluct=0.1,bond=['C-C','H-H','O-O'],csv='fluct'):
    beup = {}
    belo = {}
    vup = {}
    vlo = {}
    for bd in bond:
        csv_ = csv+'_'+bd+'.csv'
        d    = pd.read_csv(csv_)
        r    = d['r']
        eb   = d['ebond']
        ev   = d['evdw']

        beup[bd] = []
        belo[bd] = []
        vup[bd]  = []
        vlo[bd]  = []

        for r_,eb_,ev_ in zip(r,eb,ev):
            up = 1.0+fluct
            lo = 1.0-fluct
            beup[bd].append((r_,eb_*lo))
            belo[bd].append((r_,eb_*up))

            vup[bd].append((r_,ev_*up))
            vlo[bd].append((r_,ev_*lo))
    return belo,beup,vlo,vup

def bo_fluct(fluct=0.1,bond=['C-C','H-H','O-O'],csv='bo_fluct'):
    boup = {}
    bolo = {}
    for bd in bond:
        csv_ = csv+'_'+bd+'.csv'
        d   = pd.read_csv(csv_)
        r   = d['r']
        bsi = d['bosi1']
        bpi = d['bopi1']
        bpp = d['bopp1']
        boup[bd] = []
        bolo[bd] = []
         
        for r_,bsi_,bpi_,bpp_ in zip(r,bsi,bpi,bpp):
            up = 1.0+fluct
            boup[bd].append((r_,bsi_*up,bpi_*up,bpp_*up))
            lo = 1.0-fluct
            bolo[bd].append((r_,bsi_*lo,bpi_*lo,bpp_*lo))
    return bolo,boup

def get_parameters(ffield):
    with open(ffield,'r') as lf:
        j = js.load(lf)
        p = j['p']
        m = j['m']
    return p,m

def harmonic(bd,ro=2.45,rst=2.1,red=2.8,rovdw=3.0,k=0.1,
             Di=None,Dj=None,
             npoints=7):
    p,_ = get_parameters('ffield.json')
    b  = bd.split('-')
    gamma  = np.sqrt(p['gamma_'+b[0]]*p['gamma_'+b[1]])
    gammaw = np.sqrt(p['gammaw_'+b[0]]*p['gammaw_'+b[1]])
    
    R = np.linspace(rst, red, num=npoints)
    evdw       = Evdw(R,Devdw=p['Devdw_'+bd]*4.3364432032e-2,gamma=gamma,gammaw=gammaw,
                      vdw1=p['vdw1'],rvdw=p['rvdw_'+bd],alfa=p['alfa_'+bd])
    evdw_ro    = Evdw(ro,Devdw=p['Devdw_'+bd]*4.3364432032e-2,gamma=gamma,gammaw=gammaw,
                      vdw1=p['vdw1'],rvdw=p['rvdw_'+bd],alfa=p['alfa_'+bd])
    evdw_rovdw = Evdw(rovdw,Devdw=p['Devdw_'+bd]*4.3364432032e-2,gamma=gamma,gammaw=gammaw,
                      vdw1=p['vdw1'],rvdw=p['rvdw_'+bd],alfa=p['alfa_'+bd])

    Eo = evdw_ro - evdw_rovdw + k*(rovdw-ro)**2
    Eb = []
    for i,r in enumerate(R):
        Eb.append(evdw_ro - evdw[i])
    
    Eb = np.array(Eb)
    Eb = Eb - Eo

    for i,r in enumerate(R):
        Eb[i] += k*(r-ro)**2

    be = []
    for r_,eb_ in zip(R,Eb):
        if Di is None:
           Di = (0,100)
        if Dj is None:
           Dj = (0,100)
        be.append((r_,Di[0],Di[1],Dj[0],Dj[1],eb_))
    return be 

