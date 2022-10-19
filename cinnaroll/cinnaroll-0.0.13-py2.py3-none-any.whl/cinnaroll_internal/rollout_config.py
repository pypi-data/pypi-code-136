import abc
from typing import Any, Dict, Optional


class RolloutConfig(abc.ABC):
    def __init__(self, *, project_id: str, model_object: Any, model_input_sample: Any, infer_func_input_format: str,
                 infer_func_output_format: str, infer_func_input_sample: Any, metrics: Optional[Dict[str, Any]] = None):
        """
        :param project_id: Required. ID of your project. Copy it from cinnaroll web app.
        :param model_object: Required. Your model's object.
            For Keras models, it has to be a tensorflow.keras.Model or its subclass.
            For PyTorch models, it has to be a subclass of torch.nn.Module.
        :param model_input_sample: Required. Something you can pass to your model object's predict function to get
        a prediction.
            For Keras or Tensorflow models, it's an argument to model.predict().
            For PyTorch models, it's an argument to myModel() where myModel is an object of your model class.
        :param infer_func_input_format: Required. Input format of your infer() function, one of:
            "json" - JSON
            "img"  - image that you can open with PIL.Image.open() or other image opening methods
            "file" - arbitrary file that you can open
        :param infer_func_output_format: Required. Output format of your infer() function, one of:
            "json" - JSON
            "img"  - image
        :param infer_func_input_sample: Required. Something you can pass to your infer function, that is in the format
        of input_format.
        :param metrics: Optional. Performance metrics of your model - a dictionary with "metric_name": metric_value
        items.
            You can also include 'dataset' key to designate name, version etc. of dataset you were using.
            Example:
            metrics = {
                'dataset': "mnist",
                'accuracy': accuracy_value,
                'f1_score': f1_value
            }
        """
        self.project_id = project_id
        self.model_object = model_object
        self.model_input_sample = model_input_sample
        self.infer_func_input_format = infer_func_input_format
        self.infer_func_output_format = infer_func_output_format
        self.infer_func_input_sample = infer_func_input_sample
        self.metrics = metrics

    @staticmethod
    @abc.abstractmethod
    def train_eval() -> None:
        """
        Paste the code that trains and evaluates your model here, but initialize model object earlier.
        cinnaroll.rollout() will call this function to train and evaluate your model, and save it to disk if
        a saved model doesn't exist already, or model on disk differs from the initialized in code.
        If you're loading a model (for example a pretrained model from disk or web) in your script, leave the function
        as is, with just "pass".
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def infer(model_object: Any, input_data: Any) -> Any:
        """
        Function that will be used in the deployed app to serve inferences.
        input_data should be in input_format from config,
        returned data should be in output_format from config.
        Exceptions raised here will make inference app return the exception's message
        and error code 500.
        """
        pass
