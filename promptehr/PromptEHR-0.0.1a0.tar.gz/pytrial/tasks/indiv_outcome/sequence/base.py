import abc
import pdb
import os

import torch
from torch import nn

from pytrial.utils.check import check_model_dir
from pytrial.utils.check import make_dir_if_not_exist
from pytrial.tasks.indiv_outcome.data import SequencePatient


class SequenceIndivBase(abc.ABC):
    '''Abstract class for all individual outcome predictions
        based on sequential patient data.

    Parameters
    ----------
    experiment_id: str, optional (default = 'test')
        The name of current experiment.
    '''
    _mode_list = ['binary','multiclass','multilabel','regression']
    training=False
    @abc.abstractmethod
    def __init__(self, experiment_id='test', mode=None, output_dim=None):
        check_model_dir(experiment_id)
        self.checkout_dir = os.path.join('./experiments_records', experiment_id,
                                         'checkpoints')
        self.result_dir = os.path.join('./experiments_records', experiment_id,
                                       'results')
        make_dir_if_not_exist(self.checkout_dir)
        make_dir_if_not_exist(self.result_dir)
        self._check_mode_and_output_dim(mode, output_dim)

    @abc.abstractmethod
    def fit(self, train_data, valid_data):
        raise NotImplementedError

    @abc.abstractmethod
    def predict(self, test_data):
        raise NotImplementedError

    @abc.abstractmethod
    def load_model(self, checkpoint):
        raise NotImplementedError

    @abc.abstractmethod
    def save_model(self, output_dir):
        raise NotImplementedError

    def train(self, mode=True):
        self.training = mode
        self.model.train()
        return self
    
    def eval(self, mode=False):
        self.training = mode
        self.model.eval()
        return self

    def _input_data_check(self, inputs):
        assert isinstance(inputs, SequencePatient), 'Wrong input type.'

    def _check_mode_and_output_dim(self, mode, output_dim):
        mode = mode.lower()
        assert mode in self._mode_list, f'Input mode `{mode}` does not belong to the supported mode list {self._mode_list}.'
        if output_dim is None:
            if mode not in ['binary','regression']:
                raise ValueError('`output_dim` should be given when `mode` is not `binary` or `regression`.')
            else:
                output_dim = 1
        self.mode = mode
        self.output_dim = output_dim

class InputEventEmbedding(nn.Module):
    def __init__(self, orders, vocab_size, emb_size, padding_idx) -> None:
        super().__init__()
        # build input embeddings
        emb_dict = {}
        for i, order in enumerate(orders):
            emb_dict[order] = nn.Embedding(vocab_size[i], embedding_dim=emb_size, padding_idx=padding_idx)
        self.embeddings = nn.ModuleDict(emb_dict)
    
    def forward(self, inputs):
        emb_list = []
        for k, v in inputs['v'].items():
            emb = self.embeddings[k](v)
            emb_list.append(emb)
        embs = torch.cat(emb_list, 1)
        return embs

class RNNModel(nn.Module):
    RNN_TYPE = {
        'rnn':nn.RNN,
        'lstm':nn.LSTM,
        'gru':nn.GRU,
    }
    def __init__(self, 
        rnn_type,
        emb_size,
        num_layer,
        bidirectional,
        ) -> None:
        super().__init__()
        self.model = self.RNN_TYPE[rnn_type](
            input_size=emb_size,
            hidden_size=emb_size,
            num_layers=num_layer,
            bidirectional=bidirectional,
            batch_first=True,
        )
        self.bidirectional = bidirectional
    
    def forward(self, x):
        outputs = self.model(x)[0]
        return outputs