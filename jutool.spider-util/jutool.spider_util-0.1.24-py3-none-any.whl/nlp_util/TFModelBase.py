import abc
from code_util.log import log_error
from ml_util.TrainableProcessModelBase import TrainableProcessModelBase, TrainableProcessState
from code_util.env import train_model_folder
from code_util.file import create_folder_if_not_exsited
import tensorflow as tf
import time, pickle, os


class TFTrainableProcessState(TrainableProcessState):
    def __init__(self):
        self.all_epoch_loss = []
        self.current_epoch_loss = []

    def add_epoch_loss(self, loss_value):
        self.current_epoch_loss.append(loss_value)

    def event_finish_epoch(self):
        self.all_epoch_loss.append(sum(self.current_epoch_loss))
        self.current_epoch_loss.clear()

    def info_of_batch(self):
        return f"Batch Loss：{self.current_epoch_loss[-1]}"

    def info_of_epoch(self):
        if len(self.all_epoch_loss) > 0:
            return f"Epoch Loss：{self.all_epoch_loss[-1]} -> {sum(self.current_epoch_loss)}"
        else:
            return f"Epoch Loss：{sum(self.current_epoch_loss)}"


class TFModelBase(TrainableProcessModelBase):
    def __init__(self, name, input_shapes: {}, dtype=tf.float32):
        super().__init__(name)

        self._input_tensors = {key: tf.keras.Input(shape=input_shapes[key], dtype=dtype) for key in input_shapes.keys()}
        self._output_tensor = self.diagram(self._input_tensors)

        self._model = tf.keras.Model(inputs=self._input_tensors, outputs=self._output_tensor)
        self.process_state_model = TFTrainableProcessState()

    @abc.abstractmethod
    def optimizer_obj(self):
        pass

    @abc.abstractmethod
    def diagram(self, input_tensors):
        pass

    @abc.abstractmethod
    def cal_loss(self, intput, model_result, label):
        pass

    def input_convert(self, intput):
        return intput

    def output_convert(self, model_result):
        return model_result

    def predict(self, input):
        return self.output_convert(self._model(self.input_convert(input)))

    def train(self, input, lable):
        with tf.GradientTape() as tape:
            pre_result = self.predict(input)
            loss = self.cal_loss(input, pre_result, lable)

        trainable_weights = self._model.trainable_weights
        gradients = tape.gradient(loss, trainable_weights)
        self.optimizer_obj().apply_gradients(zip(gradients, trainable_weights))

        self.process_state_model.add_epoch_loss(loss.numpy())
        return self.process_state_model

    def load(self, model_key: str):
        path = os.path.join(train_model_folder, f'{self.Name}_{model_key}.model')
        if not os.path.exists(path):
            log_error("没有此模型")

        with open(path, "rb") as f:
            model_dict = pickle.load(f)

        self._model.set_weights(model_dict['weight'])

    def save(self, model_key: str):
        create_folder_if_not_exsited(train_model_folder)

        model_dict = {'weight': self._model.trainable_weights}

        with open(os.path.join(train_model_folder, f'{self.Name}_{model_key}.model'), "wb") as f:
            pickle.dump(model_dict, f)
