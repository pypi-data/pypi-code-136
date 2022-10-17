from pipeline import (
    PipelineFile,
    pipeline_function,
    pipeline_model,
)
import numpy as np
import torch
from xgboost import XGBClassifier, XGBRegressor
from cloudpickle import load as pickle_load
from torch.jit import load as torchscript_load


@pipeline_model
class PickleModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = np.atleast_2d(input_list)
        return self.model.predict(array).tolist()


@pipeline_model
class ClassifierPickleModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = np.atleast_2d(input_list)
        return self.model.predict_proba(array).tolist()


@pipeline_model
class TorchPickleModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = pickle_load(open(model_file.path, "rb"))
            self.model.eval()
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        input_tensor = torch.tensor(input_list)
        return self.model(input_tensor).tolist()


@pipeline_model
class TorchModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = torchscript_load(model_file.path)
            self.model.eval()
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        input_tensor = torch.tensor(input_list)
        return self.model(input_tensor).tolist()


@pipeline_model
class XGBClassifierModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = XGBClassifier()
            self.model.load_model(model_file.path)
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = np.atleast_2d(input_list)
        return self.model.predict_proba(array).tolist()


@pipeline_model
class XGBRegressorModel:
    def __init__(self):
        self.model = None

    @pipeline_function(run_once=True, on_startup=True)
    def load(self, model_file: PipelineFile) -> bool:
        try:
            self.model = XGBRegressor()
            self.model.load_model(model_file.path)
            return True
        except Exception as e:
            print(e)
            return False

    @pipeline_function
    def predict(self, input_list: list) -> list:
        array = np.atleast_2d(input_list)
        return self.model.predict(array).tolist()
