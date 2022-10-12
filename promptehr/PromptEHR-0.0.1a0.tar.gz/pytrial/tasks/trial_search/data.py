'''
Implement dataset for trial search model training.
'''
import pdb

import pandas as pd
from transformers import AutoTokenizer
from torch import Tensor, device

from pytrial.data.trial_data import TrialDataCollator

class TrialSearchCollator(TrialDataCollator):
    '''
    The basic collator for trial search tasks.
    '''
    def __init__(self,
        bert_name,
        max_seq_length,
        ) -> None:
        super().__init__()
        self.tokenizer = AutoTokenizer.from_pretrained(bert_name)
        self.max_length = max_seq_length

    def __call__(self, features):
        batch = self.tokenizer.pad(
            features,
            padding=True,
            max_length=self.max_length,
            return_tensors='pt',
        )
        return batch

def batch_to_device(batch, target_device: device):
    """
    send a pytorch batch to a device (CPU/GPU)
    """
    for key in batch:
        if isinstance(batch[key], Tensor):
            if 'cuda' in target_device:
                batch[key] = batch[key].cuda()
    return batch
