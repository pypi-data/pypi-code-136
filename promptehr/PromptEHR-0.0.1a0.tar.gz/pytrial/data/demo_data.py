'''
Provide an easy-to-acess function to load ready-to-use demo data
from './demo_data' folder.
'''
import pdb
import os
import dill

import pandas as pd

from .patient_data import TabularPatientBase
from ..utils.trial_utils import ClinicalTrials

__all__ = [
    'load_mimic_ehr_sequence',
    'load_trial_patient_sequence',
    'load_trial_outcome_data',
    'load_trial_document_data',
]

def load_mimic_ehr_sequence(input_dir='./demo_data/demo_patient_sequence/ehr', n_sample=None):

    visit = dill.load(open(os.path.join(input_dir, 'visits.pkl'), 'rb'))
    voc = dill.load(open(os.path.join(input_dir, 'voc.pkl'), 'rb'))

    # make some simple processing
    feature = pd.read_csv(os.path.join(input_dir, 'feature.csv'), index_col=0)
    label = feature['MORTALITY'].values
    x = feature[['AGE','GENDER','ETHNICITY']]
    tabx = TabularPatientBase(x)
    x = tabx.df.values # get processed patient features in matrix form

    if n_sample is not None:
        # cut to get smaller demo data
        visit = visit[:n_sample]
        label = label[:n_sample]
        x = x[:n_sample]

    n_num_feature = 1
    cat_cardinalities = []
    for i in range(n_num_feature, x.shape[1]):
        cat_cardinalities.append(len(list(set(x[:,i]))))

    return {
        'visit':visit,
        'voc':voc,
        'order':['diag','prod','med'],
        'mortality':label,
        'feature':x,
        'n_num_feature':n_num_feature,
        'cat_cardinalities':cat_cardinalities,
        }

def load_trial_patient_sequence(input_dir='./demo_data/demo_patient_sequence/trial'):
    # load patient data
    print("#"*5+'Demo Data Folder'+"#"*5)
    print(os.listdir(input_dir))
    print("#"*20)
    visit = dill.load(open(os.path.join(input_dir,'visit.pkl'), 'rb'))
    vocs = dill.load(open(os.path.join(input_dir,'voc.pkl'), 'rb'))
    feature = pd.read_csv(os.path.join(input_dir, 'feature.csv'))
    v_stage = dill.load(open(os.path.join(input_dir,'visit_stage.pkl'), 'rb'))
    orders = list(vocs.keys())
    # data preprocessing
    label_relapse = feature['num relapse']
    label_mortality = feature['death'].values
    x = feature.drop(['num relapse','death','RUSUBJID'], axis=1)
    x['weight'] = x['weight'].replace({'>= 125':'125'}).astype(float)
    tabx = TabularPatientBase(x)
    x = tabx.df.values # get processed patient features in matrix form
    return {
        'feature':x,
        'visit':visit,
        'voc':vocs,
        'order':orders,
        'visit_stage':v_stage,
        'relapse':label_relapse,
        'mortality':label_mortality,
    }

def load_trial_outcome_data(input_dir='./demo_data/demo_trial_data'):
    df = pd.read_csv(os.path.join(input_dir, 'phase_i_clinical_trials.csv'))
    return {'data':df}

def load_trial_document_data(input_dir='./demo_data/demo_trial_document', n_sample=None):

    filepath = os.path.join(input_dir, 'clinical_trials.csv')
    label_filepath = os.path.join(input_dir, 'TrialSim-data.xlsx')
    
    if not os.path.exists(filepath):
        # download demo data
        client = ClinicalTrials()
        client.download(date='20221001', output_dir=input_dir)

    if not os.path.exists(label_filepath):
        # download demo label
        import wget
        wget.download('https://uofi.box.com/shared/static/n8md2ixd4wkzo3w3towr848uippr6ax7.xlsx', out=label_filepath)

    df = pd.read_csv(filepath, index_col=0)
    df_tr = df # all data
    df_val = pd.read_excel(label_filepath, index_col=0)

    df_v = pd.DataFrame({'nct_id':df_val.iloc[:,:11].to_numpy().flatten()})
    df_v = df_v.merge(df, on='nct_id', how='inner')
    df_tr = pd.concat([df_tr, df_v], axis=0).drop_duplicates()

    if n_sample is not None:
        # cut to get smaller demo data
        df_tr = df_tr.iloc[:n_sample]

    return {
        'x': df_tr,
        'fields':['title','intervention_name','disease','keyword'],
        'ctx_fields':['description','criteria'],
        'tag': 'nct_id',
        'x_val':df_val.iloc[:,:11],
        'y_val':df_val.iloc[:,11:],
    }