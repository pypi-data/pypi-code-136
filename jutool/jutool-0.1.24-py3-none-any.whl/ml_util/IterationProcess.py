from ml_util.IterationProcessModelBase import IterationProcessModelBase
from sample_util.SampleSet import SampleSet
from code_util.buffer import has_item_key, buffer_item, get_buffer_item
from code_util.log import log_error, log, process_status_bar
import time


class IterationProcess():
    """
    遍历执行过程
    """

    def __init__(self, model: IterationProcessModelBase, sample_set: SampleSet, session_id=None):
        self._model = model
        self._set = sample_set
        self._session_id = session_id if session_id is not None else str(time.time())

        self._session_key = f"iter_p_{self._session_id}"

        log(f"当前未设置Seesion,设置随机ID : {self._session_key}")

        if has_item_key(self._session_key):
            self._iter_count = get_buffer_item(self._session_key)
        else:
            self._iter_count = 0

    def execute(self, result_func, item_convert_fun=None):
        """
        执行遍历
        :param result_func: 结果的处理过程 （model返回的result， item_convert_fun返回的结果） 无返回值
        :param item_convert_fun: 每个Item进入model前的处理过程，(set遍历的item)-》返回待model处理结果
        :return:
        """
        skip_count = self._iter_count
        set_count = self._set.count()

        if skip_count == 0:
            self._model.prepare()
            buffer_item(self._session_key, 0)

        p_bar = process_status_bar()  # (0, set_count)
        progress_value = skip_count

        for item in p_bar.iter_bar(self._set.skip(skip_count), key="IterProcess", max=set_count):
            if item_convert_fun is None:
                nitem = item
            else:
                nitem = item_convert_fun(item)

            result = self._model.call(nitem)

            result_func(result, nitem)

            progress_value += 1
            buffer_item(self._session_key, progress_value)
