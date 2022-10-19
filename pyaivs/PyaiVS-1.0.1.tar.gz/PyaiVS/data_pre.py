import os.path

import pandas as pd
from rdkit.Chem import AllChem
import numpy as np
from sklearn import preprocessing
def saltremover(i):
    l = i.split('.')
    d = {len(a):a for a in l }
    smile = d[max(d.keys())]
    return smile
def stand_smiles(smiles):
    try:
        smiles = AllChem.MolToSmiles(AllChem.MolFromSmiles(smiles))
    except:
        smiles = ''
    return smiles
def process(file,content,cpu=10):
    if content == 'cano':
        data = pd.read_csv(file)
        start =len(data)
        data['Smiles'] = data['Smiles'].apply(saltremover)
        data['Smiles'] = data['Smiles'].apply(stand_smiles)
        output = file.split('.csv')[0] + '_pro.csv'
        if os.path.exists(output):
            pass
        else:
            data.to_csv(output,index=False)
            print('we meet some smiles which cannot revert to cano_smiles and the number is',start-len(data))
    if content == 'descriptor':
        from padelpy import padeldescriptor
        output = file.split('.csv')[0] + '_pro.csv'
        data = pd.read_csv(output)
        data['activity'] = data['Smiles']
        data=data[['Smiles','activity']]
        smi = file.split('.csv')[0] +'.smi'
        des = file.split('.csv')[0] +'_23d.csv'
        if os.path.exists(des):
            pass
        else:
            data.to_csv(smi,index=False,sep='\t',header=None)
            padeldescriptor(mol_dir=smi, d_2d=True, d_3d=True, d_file=des,threads=50)
            # print('done 2d3d',end=' ')
    if content == 'pubchem':
        from padelpy import padeldescriptor
        output = file.split('.csv')[0] + '_pro.csv'
        data = pd.read_csv(output)
        data['activity'] = data['Smiles']
        data=data[['Smiles','activity']]
        smi = file.split('.csv')[0] +'.smi'
        des = file.split('.csv')[0] +'_pubchem.csv'
        if os.path.exists(des):
            pass
        else:
            data.to_csv(smi,index=False,sep='\t',header=None)
            padeldescriptor(mol_dir=smi, fingerprints=True, d_file=des,threads=30)
            # print('done punchem',end=' ')
    if content == 'adj_23d':
        des = file.split('.csv')[0] + '_23d.csv'
        name = file.split('.csv')[0] + '_23d_adj.csv'
        if os.path.exists(name):
            pass
        else:
            des = pd.read_csv(des).iloc[:,:1445]   # save pre 1444 features
            des = des.replace([np.inf,-np.inf],np.nan)  # trans inf to nan
            des = des.dropna(thresh=int(des.shape[1]/2),axis =0)  #drop that row all 0 how ='all'
            des = des.dropna(thresh=int(des.shape[0]/2),axis =1)
            des = des.fillna(0)  # fill nan by mean col
            min_max_scaler = preprocessing.MinMaxScaler()
            adj = min_max_scaler.fit_transform(des.drop(['Name'], axis=1))  # scaler
            adj = pd.DataFrame(adj,columns=list(des.columns)[1:])
            adj['Name']=des['Name']
            adj.to_csv(name,index=False)
            # print('done scaler',end =' ')
def start(file,des= None):
    content = ['cano']
    if '2d-3d' in des:
        content.extend(['descriptor','adj_23d'])
    if 'pubchem' in des:
        content.append('pubchem')
    for pro in content:
        process(file,pro)

