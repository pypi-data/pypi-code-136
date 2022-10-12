# Basic trial dataset loader
from collections import defaultdict
import pdb
import os
from typing import Any, Callable, Dict, List, NewType, Optional, Tuple, Union
import re

import pandas as pd
from torch.utils.data import Dataset, DataLoader

from ..utils.trial_utils import ClinicalTrials
from ..utils.tabular_utils import read_csv_to_df
from ..data.vocab_data import Vocab
from ..utils.trial_outcome_pred_utils import trial_collate_fn as trialoutcome_collate_fn 


import torch, csv
from torch.utils.data.dataloader import default_collate


class TrialDatasetBase(Dataset):
    '''
    The basic trial datasets loader.

    Parameters
    ----------
    data: pd.DataFrame
        Contain the trial document in tabular format.
    '''
    inc_ec_embedding = None # inclusion criteria embedding
    inc_vocab = None # inclusion criteria vocab
    exc_ec_embedding = None # exclusion criteria embedding
    exc_vocab = None # exclusion criteria vocab

    def __init__(self, data):
        self.df = data
        self._process_ec()
        self._collect_cleaned_sentence_set()
    
    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        return self.df.iloc[index:index+1]
    
    def get_ec_sentence_embedding(self):
        '''
        Process the eligibility criteria of each trial,
        get the criterion-level emebddings stored in dict.
        '''
        self._get_ec_emb()

    def _process_ec(self):
        res = self.df['criteria'].apply(lambda x: self._split_protocol(x))
        self.df['inclusion_criteria'] = res.apply(lambda x: x[0])
        self.df['exclusion_criteria'] = res.apply(lambda x: x[1])

    def _get_ec_emb(self):
        # create EC embedding with indexed ECs
        from pytrial.model_utils.bert import BERT
        bert_model = BERT(device='cuda:0')
        self.inc_ec_embedding = bert_model.encode(self.inc_vocab.words, batch_size=64)
        self.exc_ec_embedding = bert_model.encode(self.exc_vocab.words, batch_size=64)
        self.inc_ec_embedding = self.inc_ec_embedding.cpu()
        self.exc_ec_embedding = self.exc_ec_embedding.cpu()
        

    def _collect_cleaned_sentence_set(self):
        # create a vocab for ec sentences
        self.inc_vocab = Vocab()
        self.exc_vocab = Vocab()
        self.inc_vocab.add_sentence(['[PAD]']) # 0 belongs to the pad token
        self.exc_vocab.add_sentence(['[PAD]']) # 0 belongs to the pad token

        inc_index_set, exc_index_set = [], []
        for idx, row in self.df.iterrows():
            row_inc_set, row_exc_set = [], []
            inc = row['inclusion_criteria']
            exc = row['exclusion_criteria']
            for sent in inc:
                self.inc_vocab.add_sentence(sent)
                row_inc_set.append(self.inc_vocab.word2idx[sent])
            for sent in exc:
                self.exc_vocab.add_sentence(sent)
                row_exc_set.append(self.exc_vocab.word2idx[sent])
            inc_index_set.append(list(set(row_inc_set)))
            exc_index_set.append(list(set(row_exc_set)))
        self.df['inclusion_criteria_index'] = inc_index_set
        self.df['exclusion_criteria_index'] = exc_index_set

    def _clean_protocol(self, protocol):
        protocol = protocol.lower()
        protocol_split = protocol.split('\n')
        filter_out_empty_fn = lambda x: len(x.strip())>0
        strip_fn = lambda x: x.strip()
        protocol_split = list(filter(filter_out_empty_fn, protocol_split))	
        protocol_split = list(map(strip_fn, protocol_split))
        return protocol_split

    def _split_protocol(self, protocol):
        protocol_split = self._clean_protocol(protocol)
        inclusion_idx, exclusion_idx = len(protocol_split), len(protocol_split)	
        for idx, sentence in enumerate(protocol_split):
            if "inclusion" in sentence:
                inclusion_idx = idx
                break
        for idx, sentence in enumerate(protocol_split):
            if "exclusion" in sentence:
                exclusion_idx = idx 
                break 		
        if inclusion_idx + 1 < exclusion_idx + 1 < len(protocol_split):
            inclusion_criteria = protocol_split[inclusion_idx:exclusion_idx]
            exclusion_criteria = protocol_split[exclusion_idx:]
            if not (len(inclusion_criteria) > 0 and len(exclusion_criteria) > 0):
                print(len(inclusion_criteria), len(exclusion_criteria), len(protocol_split))
                exit()
            return inclusion_criteria, exclusion_criteria ## list, list 
        else:
            return protocol_split, []


class TrialDataset(Dataset):
    '''
    Basic trial datasets loader.

    Parameters
    ----------
    input_dir: str
        The path to the trial dataset in tabular form (.csv).
        If a directory is given, the code will automatically pick the only '.csv' file under this dir.
    '''
    def __init__(self, input_dir=None) -> None:
        if os.path.isfile(input_dir):
            self.df = read_csv_to_df(input_dir, index_col=0)

        if os.path.isdir(input_dir):
            csv_names = [name for name in os.listdir(input_dir) if name.endswith('.csv')]
            if len(csv_names) > 1:
                raise Exception(f'`input_dir` {input_dir} is given where more than one csv files are found under this path.')
            if len(csv_names) == 0:
                raise Exception(f'`input_dir` {input_dir} is given where no csv file is found under this path.')
            self.df = read_csv_to_df(os.path.join(input_dir, csv_names[0]), index_col=0)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        return self.df.iloc[index:index+1]

class TrialDataCollator:
    '''The basic trial data collator.
    Subclass it and override the `__init__` & `__call__` function if need operations inside this step.

    Returns
    -------
    batch_df: pd.DataFrame
        A dataframe contains multiple fields for each trial.
    '''
    def __init__(self) -> None:
        # subclass to add tokenizer
        # subclass to add feature preprocessor
        pass

    def __call__(self, examples):
        batch_df = pd.concat(examples, 0)
        batch_df.fillna('none',inplace=True)
        return batch_df


class TrialOutcomeDatasetBase(Dataset):
    '''
    Trial dataset for trial outcome prediction 

    Parameters
    ----------      
    data: a tuple of length 5, 
    containing nctid list, label list, smiles string list, icd-codes list and criteria list
    ''' 
    def __init__(self, data):
        nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst = data 
        self.nctid_lst = nctid_lst 
        self.label_lst = label_lst 
        self.smiles_lst = smiles_lst 
        self.icdcode_lst = icdcode_lst 
        self.criteria_lst = criteria_lst 

    def __len__(self):
        return len(self.nctid_lst)

    def __getitem__(self, index):
        return self.nctid_lst[index], self.label_lst[index], self.smiles_lst[index], \
                self.icdcode_lst[index], self.criteria_lst[index]
    #### smiles_lst[index] is list of smiles

def csvfile2dataloader(csvfile):
    '''
    Transform the csvfile (data file) into dataloader 
    '''
    with open(csvfile, 'r') as csvfile:
        rows = list(csv.reader(csvfile, delimiter=','))[1:]
    ## nctid,status,why_stop,label,phase,diseases,icdcodes,drugs,smiless,criteria
    nctid_lst = [row[0] for row in rows]
    label_lst = [row[3] for row in rows]
    icdcode_lst = [row[6] for row in rows]
    drugs_lst = [row[7] for row in rows]
    smiles_lst = [row[8] for row in rows]
    criteria_lst = [row[9] for row in rows] 

    data = nctid_lst, label_lst, smiles_lst, icdcode_lst, criteria_lst 
    dataset = TrialOutcomeDatasetBase(data)
    data_loader = DataLoader(dataset, batch_size = 32, shuffle = True, collate_fn = trialoutcome_collate_fn)
    return data_loader







def test():
    trialdata = TrialDataset('./datasets/AACT-ClinicalTrial/')
    trial_collate_fn = TrialDataCollator()
    trialoader = DataLoader(trialdata, batch_size=10, shuffle=False, collate_fn=trial_collate_fn)
    batch = next(iter(trialoader))
    print(batch)

if __name__ == '__main__':
    test()
