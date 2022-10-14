import time
from enum import Enum
from code_util.log import log_error
from code_util.env import buffer_folder
import os, re, importlib


class process_enum(Enum):
    SentenceCut = 1
    WordCut = 2
    Embedding = 3
    BertEmbedding = 4


class process_setting:
    def __init__(self):
        self.process_dic = {}
        self.process_object_dic = {}

    def __getitem__(self, item: process_enum):
        if item not in self.process_dic:
            nlp_util = importlib.import_module("nlp_util.components." + item.name)
            default_type = None
            for type in dir(nlp_util):
                if type.startswith("default_"):
                    default_type = type
                    break
            if default_type is None:
                log_error("找不到默认的component")

            default_type = getattr(nlp_util, default_type)

            self.process_object_dic[item], self.process_dic[item] = self._instance_type(default_type)
        return self.process_dic[item]

    def _instance_type(self, process_type):
        item = process_type()
        item.load_model(buffer_folder)
        default_type_call = getattr(item, "call")
        return item, default_type_call

    def replace_process(self, process_key: process_enum, process_type: type):
        self.process_object_dic[process_key], self.process_dic[process_key] = self._instance_type(process_type)

    def get_process_obj(self, process_key: process_enum):
        self.__getitem__(process_key)
        return self.process_object_dic[process_key]


default_process_setting = process_setting()
