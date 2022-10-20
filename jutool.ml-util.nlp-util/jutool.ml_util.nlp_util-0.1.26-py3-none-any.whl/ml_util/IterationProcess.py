from ml_util.IterationProcessModelBase import IterationProcessModelBase
from sample_util.SampleSet import SampleSet
from code_util.buffer import has_item_key, buffer_item, get_buffer_item
from code_util.log import log, process_status_bar
import time


class IterationProcess():
    """
    遍历执行过程
    """

    def __init__(self, model: IterationProcessModelBase, sample_set: SampleSet, state_obj=None, session_id=None):
        """
        初始化方法
        :param model: 需要进行遍历的IterationProcessModelBase模型
        :param sample_set: 遍历执行的数据set
        :param state_obj: 迭代状态信息
        :param session_id: 遍历的SessionID，同ID支持事务的进度记录
        """
        self._model = model
        self._set = sample_set
        self._session_key = session_id if session_id is not None else f"iter_p_{str(time.time())}"

        if has_item_key(self._session_key):
            self._iter_count, self._state_obj = get_buffer_item(self._session_key)
        else:
            log(f"当前未设置Seesion,设置随机ID : {self._session_key}")
            self._iter_count = 0
            self._state_obj = state_obj

    def execute(self, result_func=None, item_convert_fun=None):
        """
        执行遍历
        :param result_func: 结果的处理过程 （model返回的result， item_convert_fun返回的结果） 无返回值
        :param item_convert_fun: 每个Item进入model前的处理过程，(set遍历的item)-》返回待model处理结果
        :return: 无返回
        """
        skip_count = self._iter_count
        set_count = self._set.count()

        if skip_count == 0:
            self._model.prepare()
            buffer_item(self._session_key, (0, self._state_obj))

        p_bar = process_status_bar()  # (0, set_count)
        progress_value = skip_count

        for item in p_bar.iter_bar(self._set.skip(skip_count), value=skip_count, key="IterProcess", max=set_count):
            if item_convert_fun is None:
                nitem = item
            else:
                nitem = item_convert_fun(item)

            result = self._model.call(nitem, p_bar, self._state_obj)

            if result_func is not None:
                result_func(result, nitem)

            progress_value += 1
            buffer_item(self._session_key, (progress_value, self._state_obj))
