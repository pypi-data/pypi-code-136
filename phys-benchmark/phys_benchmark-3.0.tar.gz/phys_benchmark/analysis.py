import glob
import numpy as np
import pandas as pd
import os
#from .delete import deleting
import subprocess
import sys
from .delete import wrong


def analyze():
    wrong()
    my_path=(os.getcwd())
    print(my_path)
    filenames=glob.glob(my_path + '/*/md.log', recursive=True)
    filenames2=glob.glob(my_path + '/*/job_script_*', recursive=True)
    
    #x=[]
    #for f in filenames:
    #    outfile = open(f,'r')
    #    data = outfile.readlines()
    #    outfile.close()
    #    for line in data:
    #        if 'Performance:' in line:
    #            energy_line = line
    #            words = energy_line.split()
    #            energy = float(words[1])
    #            #print(energy)
    #            x.append(energy)
 
    x=[]
    
    for f in filenames:
        outfile = open(f,'r')
        data = outfile.readlines()
        outfile.close()
        for line in data:
            if 'Performance:' in line:
                energy_line = line
                words = energy_line.split()
                energy = float(words[1])
        u=[]
        u.append(energy)
    
        x.append(u)
       
    
    y=[]
    z=[]
    u=[]
    d=[]
    for f in filenames2:
        outfile2 = open(f,'r')
        data2 = outfile2.readlines()
        outfile2.close()
        for line in data2:
            if '--ntasks-per-node=' in line:
                energy_line2 = line
                words2 = energy_line2.split()
                energy2 = (words2[1])
                y.append(energy2)
            if '--cpus-per-task=' in line:
                energy_line3 = line
                words3 = energy_line3.split()
                energy3 = (words3[1])
                z.append(energy3)
            if '--gres=gpu:' in line:
                energy_line4 = line
                words4 = energy_line4.split()
                energy4 = (words4[1])
                u.append(energy4)
            if '--nodes=' in line:
                energy_line5 = line
                words5 = energy_line5.split()
                energy5 = (words5[1])
                d.append(energy5)
        
    df = pd.DataFrame(
    {'Perfomance': x,
     'Ntasks': y,
     'CPUs': z,
     'GPUs': u,
     'Nodes': d
    })
    df

    df['Ntasks'] = df['Ntasks'].astype(str).str.split('=').str[1]
    df['CPUs'] = df['CPUs'].astype(str).str.split('=').str[1]
    df['GPUs'] = df['GPUs'].astype(str).str.split(':').str[1]
    df['Nodes'] = df['Nodes'].astype(str).str.split('=').str[1]

    pd.set_option('display.max_colwidth',1000)
    pd.set_option('display.max_rows', df.shape[0]+1)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('max_colwidth', -1)

    df = df.sort_values(by=['Perfomance'], ascending=False)
    df = df.reset_index()
    df = df.reset_index(drop=True)
    df_new=df.drop(['index'],axis=1)
   # pd.set_option('display.max_colwidth',1000)
   # pd.set_option('display.max_rows', 1000)
   # pd.set_option('display.expand_frame_repr', False)
   # pd.set_option('display.max_columns', None)
   # pd.display.max_colwidth
   # pd.display.max_rows
   # pd.display.max_columns
    with open('./Benchmark_Perfomance.png', 'a') as fo:
        fo.write(df_new.__repr__())

    
