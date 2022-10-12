'''
Implement Gaussian Copula model for tabular simulation
prediction in clinical trials.
'''
import os
import warnings
import joblib
from copulas.multivariate import GaussianMultivariate

from .base import TabularSimulationBase
from pytrial.data.patient_data import TabularPatientBase
from pytrial.utils.check import check_checkpoint_file, check_model_dir, check_model_config_file, make_dir_if_not_exist

warnings.filterwarnings('ignore')


class BuildModel:
    def __new__(self) -> GaussianMultivariate:
        return GaussianMultivariate()

class GaussianCopula(TabularSimulationBase):
    '''
    Implement Gaussian Copula model for tabular simulation
    prediction in clinical trials.

    Parameters
    ----------
    experiment_id: str, optional (default='test')
        The name of current experiment. Decide the saved model checkpoint name.
    '''
    def __init__(
        self,
        experiment_id='test',
    ) -> None:
        super().__init__(experiment_id=experiment_id)
        
    def fit(self, train_data):
        '''
        Train gaussian copula model to simulate patient outcome
        with tabular input data.
        
        Parameters
        ----------
        train_data: tabular data
        '''
        self._input_data_check(train_data)
        self._build_model()
        if isinstance(train_data, TabularPatientBase):
            dataset = train_data.df
        if isinstance(train_data, dict): 
            dataset = TabularPatientBase(train_data, transform=True)
            dataset = dataset.df
        self._fit_model(dataset)
        self.metadata = train_data.metadata
        self.raw_dataset = train_data

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
        ypred = self.raw_dataset.reverse_transform(ypred) # transform back
        return ypred # output: dataset, same as the input dataset

    def save_model(self, output_dir=None):
        '''
        Save the learned gaussian copula model to the disk.

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

        #self._save_config(self.config, output_dir=output_dir)
        ckpt_path = os.path.join(output_dir, 'GaussianCopula-tabular.model')
        joblib.dump(self.model, ckpt_path)

    def load_model(self, checkpoint=None):
        '''
        Save the learned gaussian copula model to the disk.

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
        #self.config = self._load_config(config_filename)

    def _build_model(self):
        self.model = BuildModel()

    def _fit_model(self, data):
        self.model.fit(data)

    # May need _save_config and _load_config
