import jieba
import jieba.posseg as pseg

from ml_util.MLComponentBase import MLComponentBase
from code_util.structures import func_check


class default_jieba(MLComponentBase):
    def __init__(self):
        super().__init__(["jieba"])

    @func_check
    def call(self, linked_item: str, ori_item=None):
        return [word for word in jieba.cut(linked_item)]

    def call_with_poss(self, linked_item: str, ori_item=None):
        #jieba.enable_paddle()
        words = pseg.cut(linked_item)
        return [(word, flag) for word, flag in words]
