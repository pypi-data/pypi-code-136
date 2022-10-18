from ml_util.TrainableProcessModelBase import TrainableProcessModelBase
from sample_util.SampleSet import SampleSet
from code_util.log import process_status_bar


class BatchTrainable:
    """
    基于数据Batch的训练迭代
    """
    def __init__(self, model: TrainableProcessModelBase,
                 epochs=1000,
                 batch_size=10,
                 ):
        """
        初始化
        :param model: 需要迭代的模型
        :param epochs: 最大epoch次数
        :param batch_size: 每个batch的数量
        """
        self._model = model
        self._epochs = epochs
        self._batch_count = batch_size

    def train(self, sampleset: SampleSet, parse_batch_func):
        """
        训练方法
        :param sampleset: 数据的dataset
        :param parse_batch_func: 每batch数据的预处理过程
        :return: 无返回
        """
        ps_bar = process_status_bar()

        for epoch in ps_bar.iter_bar(range(self._epochs), key="epoch", max=self._epochs):

            batch_index = 0
            for sample in ps_bar.iter_bar(sampleset, key="batch", max=sampleset.count()):
                input_, lable_ = parse_batch_func(sample)
                train_state = self._model.train(input_, lable_)

                batch_info = train_state.info_of_batch()
                if batch_info is not None:
                    ps_bar.process_print(f"e:{batch_index}: {batch_info}")

                train_state.event_finish_batch()
                batch_index += 1

            self._model.save(f"_{epoch}")

            epoch_info = train_state.info_of_epoch()
            if epoch_info is not None:
                ps_bar.print_log(f"Epoch {epoch_info}: {epoch_info}")

            train_state.event_finish_epoch()

    def evaluation(self, sampleset: SampleSet):
        """
        评测方法，（未完成）
        :param sampleset: 需要评测的数据集
        :return:
        """
        pass
