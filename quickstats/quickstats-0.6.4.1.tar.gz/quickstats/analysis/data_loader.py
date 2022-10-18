import os
from typing import List, Dict, Union, Optional

import pandas as pd
import numpy as np

from sklearn import preprocessing
from quickstats import semistaticmethod, GeneralEnum
from bbyy_analysis_framework.components import AnalysisBase

class DataType(GeneralEnum):
    TRAIN = 0
    VAL   = 1
    TEST  = 2

class TrainMethod(GeneralEnum):
    DEFAULT = 0
    KFOLD   = 1

class DataLoader(AnalysisBase):
    
    def __init__(self, analysis_config_path:str, array_dir:Optional[str]=None,
                 model_dir:Optional[str]=None, outdir:Optional[str]=None,
                 verbosity:Optional[Union[int, str]]="INFO",
                 **kwargs):
        super().__init__(analysis_config=analysis_config_path,
                         array_dir=array_dir,
                         model_dir=model_dir,
                         outdir=outdir,
                         verbosity=verbosity,
                         **kwargs)

    @staticmethod
    def fix_negative_weights(data, mode:int=0):
        if mode == 1:
            data['weight'][data['weight'] < 0] = 0
        elif mode == 2:
            data['weight'][data['weight'] < 0] = abs(data['weight'][data['weight'] < 0])
            
    @semistaticmethod
    def _load_sample_df(self, sample_path:str, selection:Optional[str]=None) -> pd.DataFrame:
        """
            Load csv data for a training sample
            
            Arguments:
                sample_path: string
                    Path to the csv data.
                selection: (optional) str
                    Selection applied to the csv data (via pandas.DataFrame.query)
        """
        if not os.path.exists(sample_path):
            raise FileNotFoundError(f'sample csv file "{sample_path}" does not exist')
        df = pd.read_csv(sample_path)
        if selection not in [None, "1", 1]:
            df = df.query(selection)
        return df

    def load_sample_df(self, sample:str, selection:Optional[str]=None)->pd.DataFrame:
        sample_path = self.get_file("train_sample", sample=sample)
        self.stdout.info(f'INFO: Loading inputs for the sample "{sample}" from {sample_path}')
        return self._load_sample_df(sample_path, selection=selection)
    
    @semistaticmethod
    def _load_sample_data(self, input_path:str, samples:List[str], train_variables:List[str],
                          weight_variable:str, class_labels:Dict, selection:Optional[str]=None):
        """
        Arguments:
            weight_variable: str
                Name of weight variable in the csv input
            selection: str
                Apply selection to the data.
        """ 
        x = {}
        y = {}
        weight = {}
        # for non-numeric class labels
        class_label_encodings = self._get_class_label_encodings(list(class_labels.values()))
        class_label_map = {raw_label:encoded_label for raw_label, encoded_label in \
                           zip(class_label_encodings['raw'], class_label_encodings['encoded'])}
        if not isinstance(samples, list):
            samples = [samples]
        for sample in samples:
            resolved_input_path = input_path.format(sample=sample)
            data = pd.read_csv(resolved_input_path)
            if selection not in [None, '1', 1]:
                data = data.query(selection)

            x[sample] = data[train_variables].reset_index(drop=True)
            weight[sample] = data[[weight_variable]].reset_index(drop=True)
            class_label = class_label_map[class_labels[sample]]
            input_size = len(x[sample])
            y[sample] = pd.DataFrame(np.full((input_size,), class_label), columns=['true_label'])
        return x, y, weight
    
    @semistaticmethod
    def _combine_sample_data(self, x, y, weight, scale_factors:Optional[Dict]=None,
                             normalize_weight:bool=True, scale_weight_by_mean:bool=True,
                             negative_weight_mode:int=0):
        """
        
        Arguments:
            scale_factors: Dict[str, float]
                A dictionary with sample name as the key and the corresponding scale factor as the value for scaling
                the weight of specific samples. This is done after weight normalization.         
            normalize_weight: bool
                (only if concatenate = True) Normalize the weight of each sample to unity.
            scale_weight_by_mean: bool
                (only if concatenate = True) Scale the weight by the average weight after concatenation.
            negative_weight_mode: int
                (only if concatenate = True) Fix negative weights in data depending on the mode below
                    0: do nothing
                    1: set weight to 0
                    2: set to absolute value of original weight
        """
        samples = list(x.keys())
        for sample in samples:
            # Normalize weight of each sample to unity
            if normalize_weight:
                weight[sample] = weight[sample] / weight[sample].sum()
            # multiply the yield by appropriate scale factors
            scale_factor = scale_factors.get(sample, None)
            if (scale_factor is not None):
                    weight[sample] = weight[sample] * scale_factor
        # concatenate samples
        x      = pd.concat([x[sample] for sample in samples], ignore_index = True)
        y      = pd.concat([y[sample] for sample in samples], ignore_index = True)
        weight = pd.concat([weight[sample] for sample in samples], ignore_index = True)
        if scale_weight_by_mean:
            weight = weight / weight['weight'].mean()
            self.fix_negative_weights(weight, mode=negative_weight_mode)
        return x, y, weight
    
    @semistaticmethod
    def _load_combined_data(self, input_path:str, samples:List[str], train_variables:List[str], weight_variable:str,
                            class_labels:Dict, scale_factors:Optional[Dict]=None, selection:Optional[str]=None,
                            concatenate:bool=True, normalize_weight:bool=True, scale_weight_by_mean:bool=True,
                            negative_weight_mode:int=0):
        x, y, weight = self._load_sample_data(input_path, samples, train_variables, weight_variable,
                                              class_labels, selection)
        x, y, weight = self._combine_sample_data(x, y, weight, scale_factors=scale_factors,
                                                 normalize_weight=normalize_weight,
                                                 scale_weight_by_mean=scale_weight_by_mean,
                                                 negative_weight_mode=negative_weight_mode)
        return x, y, weight
    
    def load_data_default(self, sample_kwargs:Dict, combine_kwargs:Dict, random_state:Optional[int]=-1):
        data = {}
        for input_type in ['train', 'val', 'test']:
            array_dir = self.get_directory("array")
            input_path = os.path.join(array_dir, f"{{sample}}_{input_type}.csv")
            x, y, weight = self._load_combined_data(input_path=input_path, **sample_kwargs,
                                                    **combine_kwargs)
            x, y, weight = self._shuffle_data(x, y, weight, random_state=random_state)
            data[f"x_{input_type}"] = x
            data[f"y_{input_type}"] = y
            data[f"weight_{input_type}"] = weight
        return data
                               
    def load_data_kfold(self, sample_kwargs:Dict, combine_kwargs:Dict, n_fold:int=5, datasets:Optional[List]=None,
                        random_state:Optional[int]=None):
        from sklearn.model_selection import KFold
        kfolds = {}
        kfold_splits = {}
        event_number_var = self.config['names']['fold']
        sample_kwargs['train_variables'].append(event_number_var)
        samples = sample_kwargs['samples']
        # need to have sample specific kfold for categorization
        for sample in samples:
            kfolds[sample] = KFold(n_splits=n_fold, shuffle=True, random_state=random_state)
        if datasets is None:
            datasets = ["train", "val"]
        sample_x = {sample: [] for sample in samples}
        sample_y = {sample: [] for sample in samples}
        sample_w = {sample: [] for sample in samples}
        for dataset in datasets:
            # just to make sure it's a valid dataset type
            data_type = DataType.parse(dataset).name.lower()
            array_dir = self.get_directory("array")
            input_path = os.path.join(array_dir, f"{{sample}}_{data_type}.csv")
            x, y, weight = self._load_sample_data(input_path=input_path, **sample_kwargs)
            for sample in samples:
                sample_x[sample].append(x[sample])
                sample_y[sample].append(y[sample])
                sample_w[sample].append(weight[sample])
        for sample in samples:
            sample_x[sample] = pd.concat([x for x in sample_x[sample]], ignore_index = True)
            sample_y[sample] = pd.concat([y for y in sample_y[sample]], ignore_index = True)
            sample_w[sample] = pd.concat([w for w in sample_w[sample]], ignore_index = True)
            kfold_splits[sample] = kfolds[sample].split(sample_x[sample])
        for _ in range(n_fold):
            sample_train_event_number = {}
            sample_val_event_number   = {}
            sample_x_train = {}
            sample_x_val = {}
            sample_y_train = {}
            sample_y_val = {}
            sample_w_train = {}
            sample_w_val = {}
            for sample in samples:
                train_index, val_index = next(kfold_splits[sample])
                sample_x_train[sample] = sample_x[sample].loc[train_index]
                sample_x_val[sample]   = sample_x[sample].loc[val_index]
                sample_y_train[sample] = sample_y[sample].loc[train_index]
                sample_y_val[sample]   = sample_y[sample].loc[val_index]
                sample_w_train[sample] = sample_w[sample].loc[train_index]
                sample_w_val[sample]   = sample_w[sample].loc[val_index]
                sample_train_event_number[sample] = sample_x_train[sample][event_number_var].values
                sample_val_event_number[sample]   = sample_x_val[sample][event_number_var].values
                sample_x_train[sample].drop(columns=event_number_var, inplace=True)
                sample_x_val[sample].drop(columns=event_number_var, inplace=True)
            x_train, y_train, weight_train = self._combine_sample_data(sample_x_train, sample_y_train,
                                                                       sample_w_train, **combine_kwargs)
            x_val, y_val, weight_val = self._combine_sample_data(sample_x_val, sample_y_val,
                                                                 sample_w_val, **combine_kwargs)
            # get test dataset
            array_dir = self.get_directory("array")
            input_path = os.path.join(array_dir, "{sample}_test.csv")
            x_test, y_test, weight_test = self._load_combined_data(input_path=input_path, **sample_kwargs,
                                                                   **combine_kwargs)
            data = {
                'x_train': x_train,
                'y_train': y_train,
                'weight_train': weight_train,
                'x_val': x_val,
                'y_val': y_val,
                'weight_val': weight_val,
                'x_test': x_test,
                'y_test': y_test,
                'weight_test': weight_test,
                'event_number_train': sample_train_event_number,
                'event_number_val': sample_val_event_number
            }
            yield data
            
    def load_data_custom_event(self, sample_kwargs:Dict, combine_kwargs:Dict,
                               train_event_number:Optional[Dict[str, np.ndarray]]=None,
                               val_event_number:Optional[Dict[str, np.ndarray]]=None,
                               test_event_number:Optional[Dict[str, np.ndarray]]=None,
                               random_state:Optional[int]=-1):
        data = {}
        event_number_var = self.config['names']['fold']
        samples = sample_kwargs['samples']
        # make a copy
        train_variables = list(sample_kwargs['train_variables'])
        sample_kwargs['train_variables'].append(event_number_var)
        array_dir = self.get_directory("array")
        input_path = os.path.join(array_dir, f"{{sample}}.csv")
        x_map, y_map, weight_map = self._load_sample_data(input_path=input_path, **sample_kwargs)
        sample_df = {}
        for sample in samples:
            df = x_map[sample].copy().reset_index()
            df['true_label']  = y_map[sample].reset_index()['true_label']
            df['weight']      = weight_map[sample].reset_index()['weight']          
            df.set_index(event_number_var, inplace=True)
            sample_df[sample] = df
        for (input_type, event_number) in [('train', train_event_number),
                                           ('val', val_event_number),
                                           ('test', test_event_number)]:
            if event_number is None:
                continue
            sample_x = {sample: [] for sample in samples}
            sample_y = {sample: [] for sample in samples}
            sample_w = {sample: [] for sample in samples}
            for sample in samples:
                sample_event_number = event_number.get(sample, None)
                # need to make sure the event numbers are unique to avoid further duplication
                sample_event_number = np.unique(sample_event_number)
                if sample_event_number is None:
                    raise ValueError(f"missing event number specification for the sample \"{sample}\"")
                df = sample_df[sample]
                try:
                    df_selected = df.loc[sample_event_number]
                except:
                    from pdb import set_trace
                    set_trace()
                sample_x[sample] = df_selected[train_variables]
                sample_y[sample] = df_selected[['true_label']]
                sample_w[sample] = df_selected[['weight']]
            x, y, weight = self._combine_sample_data(sample_x, sample_y,
                                                     sample_w, **combine_kwargs)
            x, y, weight = self._shuffle_data(x, y, weight, random_state=random_state)
            data[f"x_{input_type}"] = x
            data[f"y_{input_type}"] = y
            data[f"weight_{input_type}"] = weight
        return data            
    
    def _shuffle_data(self, *arrays, random_state:Optional[int]=-1):
        if random_state == -1:
            return arrays
        from sklearn.utils import shuffle
        return shuffle(*arrays, random_state=random_state)
        
    def load_data(self, samples:List[str], train_variables:List[str], weight_variable:str,
                  class_labels:Dict, scale_factors:Optional[Dict]=None, selection:Optional[str]=None,
                  normalize_weight:Optional[bool]=None, scale_weight_by_mean:Optional[bool]=None,
                  negative_weight_mode:Optional[int]=None, train_method:Optional[str]=None,
                  train_method_options:Optional[Dict]=None,
                  train_event_number:Optional[Dict[str, np.ndarray]]=None,
                  val_event_number:Optional[Dict[str, np.ndarray]]=None,
                  test_event_number:Optional[Dict[str, np.ndarray]]=None,
                  random_state:Optional[int]=-1):
        samples         = self.resolve_samples(samples)
        train_variables = self.resolve_variables(train_variables)
        class_labels    = self.resolve_class_labels(class_labels)

        sample_kwargs = {
            'samples': samples,
            'train_variables': train_variables,
            'weight_variable': weight_variable,
            'class_labels': class_labels,
            'selection': selection
        }
        combine_kwargs = {
            'scale_factors': scale_factors,
        }
        if normalize_weight is None:
            combine_kwargs['normalize_weight'] = self.config['training'].get('normalize_weight', True)
        else:
            combine_kwargs['normalize_weight'] = normalize_weight
        if scale_weight_by_mean is None:
            combine_kwargs['scale_weight_by_mean'] = self.config['training'].get('scale_weight_by_mean', True)
        else:
            combine_kwargs['scale_weight_by_mean'] = scale_weight_by_mean
        if negative_weight_mode is None:
            combine_kwargs['negative_weight_mode'] = self.config['training'].get('negative_weight_mode', 0)
        else:
            combine_kwargs['negative_weight_mode'] = negative_weight_mode
        if train_method is None:
            train_method = self.config['training']['method']
        if train_method_options is None:
            train_method_options = self.config['training'].get('method_options', {})
            
        if (train_event_number is None) and (val_event_number is None) and (test_event_number is None):
            train_method = TrainMethod.parse(train_method)
            if train_method == TrainMethod.DEFAULT:
                if (train_event_number is None) and (val_event_number is None):
                    return self.load_data_default(sample_kwargs, combine_kwargs, random_state=random_state)
            elif train_method == TrainMethod.KFOLD:
                n_fold   = train_method_options['n_fold']
                datasets = train_method_options['datasets']
                return self.load_data_kfold(sample_kwargs, combine_kwargs, n_fold=n_fold,
                                            datasets=datasets,
                                            random_state=None)
            else:
                raise ValueError(f"unknown train method \"{train_method}\"")
        # custom train, validation and test event
        else:
            return self.load_data_custom_event(sample_kwargs=sample_kwargs,
                                               combine_kwargs=combine_kwargs,
                                               train_event_number=train_event_number,
                                               val_event_number=val_event_number,
                                               random_state=random_state)   
    
    def print_channel_summary(self, channels:Optional[Union[List[str],str]]=None):
        if channels is None:
            channels = self.all_channels
        elif isinstance(channels, str):
            channels = [channels]
        for channel in channels:
            if channel not in self.all_channels:
                raise ValueError(f"unknwon channel: {channel}")
            selection = self.config['channels'][channel]['selection']
            train_samples = self.config['channels'][channel]['train_samples']
            test_samples = self.config['channels'][channel]['test_samples']
            train_variables = self.config['channels'][channel]['train_variables']
            class_labels = self.config['channels'][channel]['class_labels']
            train_samples = self.resolve_samples(train_samples)
            test_samples = self.resolve_samples(test_samples)
            train_variables = self.resolve_variables(train_variables)
            scale_factors = self.config['channels'][channel]['SF']
            self.stdout.info("=============================== CHANNEL SUMMARY ===============================")
            self.stdout.info("Channel Name: ".rjust(20) + f"{channel}")
            self.stdout.info("Channel Selection: ".rjust(20) + f"{selection}")
            self.stdout.info("*******************************************************************************")
            self.stdout.info("Train Samples: ".rjust(20) + ", ".join(train_samples))
            self.stdout.info("Test Samples: ".rjust(20) + ", ".join(test_samples))
            self.stdout.info("*******************************************************************************")
            self.stdout.info("Class Labels: ".rjust(20))
            for label in class_labels:
                samples = self.resolve_samples(class_labels[label])
                self.stdout.info(f"\t{label}: " + ", ".join(samples))
            self.stdout.info("*******************************************************************************")
            self.stdout.info("Train Variables: ".rjust(20) + ", ".join(train_variables))
            self.stdout.info("*******************************************************************************")
            self.stdout.info("Scale Factors: ".rjust(20) + str(scale_factors))
            self.stdout.info("*******************************************************************************")
            self.stdout.info("")
            
    @staticmethod
    def _get_class_label_encodings(class_labels:List):
        class_label_encodings = {}
        labelencoder = preprocessing.LabelEncoder()
        labelencoder.fit_transform(class_labels)
        class_label_encodings['raw']     = labelencoder.classes_
        class_label_encodings['encoded'] = np.arange(len(class_labels))
        return class_label_encodings
    
    def get_class_label_encodings(self):
        class_label_encodings = {}
        for channel in self.all_channels:
            class_labels = list(self.config['channels'][channel]['class_labels'])
            class_label_encodings[channel] = self._get_class_label_encodings(class_labels)
        return class_label_encodings
            
    def load_channel_data(self, channel:str, scale_factors:Optional[Dict]=None,
                          train_event_number:Optional[Dict[str, np.ndarray]]=None,
                          val_event_number:Optional[Dict[str, np.ndarray]]=None,
                          test_event_number:Optional[Dict[str, np.ndarray]]=None,
                          random_state:Optional[int]=-1):
        if channel not in self.all_channels:
            raise ValueError(f"unknown channel: {channel}")
        samples = self.config['channels'][channel]['train_samples']
        variables = self.config['channels'][channel]['train_variables']
        weight_variable = self.config['names']['weight']
        class_labels = self.config['channels'][channel]['class_labels']
        if scale_factors is None:
            scale_factors = self.config['channels'][channel]['SF']
        selection = self.config['channels'][channel]['selection']
        return self.load_data(samples, variables, weight_variable, class_labels,
                              scale_factors=scale_factors, selection=selection,
                              train_event_number=train_event_number,
                              val_event_number=val_event_number,
                              test_event_number=test_event_number,
                              random_state=random_state)