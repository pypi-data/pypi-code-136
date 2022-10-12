'''
Implement TVAE model for tabular simulation
prediction in clinical trials.
'''
import os
import warnings
import joblib
from ctgan import TVAESynthesizer

from .base import TabularSimulationBase
from pytrial.data.patient_data import TabularPatientBase
from pytrial.utils.check import check_checkpoint_file, check_model_dir, check_model_config_file, make_dir_if_not_exist

warnings.filterwarnings('ignore')


class BuildModel:
    def __new__(self, config) -> TVAESynthesizer:
        model = TVAESynthesizer(
            embedding_dim=config['embedding_dim'],
            compress_dims=config['compress_dims'],
            decompress_dims=config['decompress_dims'],
            l2scale=config['l2scale'],
            batch_size=config['batch_size'],
            epochs=config['epochs'],
            loss_factor=config['loss_factor'],
            cuda=config['cuda'],
            )

        return model


class TVAE(TabularSimulationBase):
    '''
    Implement TVAE model for tabular simulation
    prediction in clinical trials.

    Parameters
    ----------
    embedding_dim (int):
        Size of the random sample passed to the Generator. Defaults to 128.

    compress_dims (tuple or list of ints):
        Size of each hidden layer in the encoder. Defaults to (128, 128).
    
    decompress_dims (tuple or list of ints):
       Size of each hidden layer in the decoder. Defaults to (128, 128).
    
    l2scale (int):
        Regularization term. Defaults to 1e-5.
    
    batch_size (int):
        Number of data samples to process in each step.
    
    epochs (int):
        Number of training epochs. Defaults to 300.
    
    loss_factor (int):
        Multiplier for the reconstruction error. Defaults to 2.
    
    cuda (bool or str):
        If ``True``, use CUDA. If a ``str``, use the indicated device.
        If ``False``, do not use cuda at all.

    experiment_id: str, optional (default='test')
        The name of current experiment. Decide the saved model checkpoint name.
    '''
    def __init__(
        self,
        embedding_dim=128,
        compress_dims=(128, 128),
        decompress_dims=(128, 128),
        l2scale=1e-5,
        batch_size=500,
        epochs=300,
        loss_factor=2,
        cuda=False,
        experiment_id='test',
    ) -> None:
        super().__init__(experiment_id=experiment_id)
        self.config = {
            'embedding_dim' : embedding_dim,
            'compress_dims' : compress_dims,
            'decompress_dims' : decompress_dims,
            'l2scale' : l2scale,
            'batch_size': batch_size,
            'epochs': epochs,
            'loss_factor' : loss_factor,
            'cuda' : cuda,
            'experiment_id': experiment_id,
            'model_name': 'tvae',
        }
        self._save_config(self.config)

    def fit(self, train_data):
        '''
        Train TVAE model to simulate patient outcome
        with tabular input data.

        Parameters
        ----------
        train_data: tabular data
        '''
        self._input_data_check(train_data)
        self._build_model()
        if isinstance(train_data, TabularPatientBase): # transform=True
            dataset = train_data.df
        if isinstance(train_data, dict): 
            dataset = TabularPatientBase(train_data, transform=True)
            dataset = dataset.df

        self.metadata = train_data.metadata
        self.raw_dataset = train_data

        dataset = self.raw_dataset.reverse_transform() # transform back

        categoricals = []
        fields_before_transform = self.metadata['sdtypes']
        for field in dataset.columns:
            field_name = field.replace('.value', '')
            if field_name in fields_before_transform:
                meta = fields_before_transform[field_name]
                if meta == 'categorical':
                    categoricals.append(field)

        self._fit_model(dataset, categoricals) 

    def predict(self, number_of_predictions=200):
        '''
        simulate a new tabular data with number_of_predictions.

        Parameters
        ----------
        number_of_predictions: number of predictions

        Returns
        -------
        ypred: dataset, same as the input dataset
            A new tabular data simulated by the model
        '''
        ypred = self.model.sample(number_of_predictions) # build df
        return ypred # output: dataset, same as the input dataset not transform back

    def save_model(self, output_dir=None):
        '''
        Save the learned TVAE model to the disk.

        Parameters
        ----------

        output_dir: str or None
            The dir to save the learned model.
            If set None, will save model to `self.checkout_dir`.
        '''
        if output_dir is not None:
            output_dir = os.path.join(output_dir, 'checkpoints')
            make_dir_if_not_exist(output_dir)
        else:
            output_dir = self.checkout_dir

        self._save_config(self.config, output_dir=output_dir)
        ckpt_path = os.path.join(output_dir, 'TVAE-tabular.model')
        joblib.dump(self.model, ckpt_path)

    def load_model(self, checkpoint=None):
        '''
        Save the learned TVAE model to the disk.

        Parameters
        ----------
        
        checkpoint: str or None
            If a directory, the only checkpoint file `.model` will be loaded.
            If a filepath, will load from this file;
            If None, will load from `self.checkout_dir`.
        '''
        if checkpoint is None:
            checkpoint = self.checkout_dir

        checkpoint_filename = check_checkpoint_file(checkpoint, suffix='model')
        config_filename = check_model_config_file(checkpoint)
        self.model = joblib.load(checkpoint_filename)
        self.config = self._load_config(config_filename)

    def _build_model(self):
        self.model = BuildModel(self.config)

    def _fit_model(self, data, discrete_columns):
        self.model.fit(data, discrete_columns=discrete_columns)
