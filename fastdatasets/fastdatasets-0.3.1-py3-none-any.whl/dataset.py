# @Time    : 2022/9/20 21:55
# @Author  : tk
# @FileName: dataset.py

import typing
import os
import warnings
from tfrecords.python.io import gfile
from tfrecords.python.io.tf_record import *
from collections.abc import Iterator,Sized
from typing import Union,List,AnyStr

from .iterable_dataset import SingleRecordIterableDataset,MultiRecordIterableDataset
from .random_dataset import SingleRandomRecordDataset,MultiRandomRecordDataset
import copy


def RecordIterableDatasetLoader(data_path_or_data_iterator: Union[List[Union[AnyStr,typing.Iterator]],AnyStr,typing.Iterator],
                     buffer_size: typing.Optional[int] = 128,
                     cycle_length=1,
                     block_length=1,
                     options=TFRecordOptions(TFRecordCompressionType.NONE),
                     with_share_memory=False):
    if isinstance(data_path_or_data_iterator, list):
        if len(data_path_or_data_iterator) == 1:
            cls = SingleRecordIterableDataset(data_path_or_data_iterator[0], buffer_size, block_length, options,
                with_share_memory=with_share_memory
            )
        else:
            cls = MultiRecordIterableDataset(data_path_or_data_iterator, buffer_size, cycle_length, block_length, options)
    elif isinstance(data_path_or_data_iterator, str) or isinstance(data_path_or_data_iterator, Iterator):
        cls = SingleRecordIterableDataset(data_path_or_data_iterator, buffer_size, block_length, options,
            with_share_memory=with_share_memory
        )
    else:
        raise Exception('data_path must be list or single string')
    return cls

def RecordRandomDatasetLoader(data_path_or_data_list: typing.Union[typing.List,typing.AnyStr,typing.Sized],
                            index_path=None,
                            use_index_cache=True,
                            options=TFRecordOptions(TFRecordCompressionType.NONE),
                            with_share_memory=False):
    if isinstance(data_path_or_data_list, list):
        if len(data_path_or_data_list) == 1:
            cls = SingleRandomRecordDataset(data_path_or_data_list[0],index_path=index_path,use_index_cache=use_index_cache, options=options,
                with_share_memory=with_share_memory
            )
        else:
            cls = MultiRandomRecordDataset(data_path_or_data_list,index_path=index_path,use_index_cache=use_index_cache,options=options,
                                           with_share_memory=with_share_memory)
    elif isinstance(data_path_or_data_list, str) or isinstance(data_path_or_data_list, Sized):
        cls = SingleRandomRecordDataset(data_path_or_data_list, index_path=index_path,use_index_cache=use_index_cache,options=options,
                                        with_share_memory=with_share_memory)
    else:
        raise Exception('data_path must be list or single string')
    return cls

class RecordLoader:

    @staticmethod
    def IterableDataset(data_path_or_data_iterator: Union[List[Union[AnyStr,typing.Iterator]],AnyStr,typing.Iterator],
                     buffer_size: typing.Optional[int] = 128,
                     cycle_length=1,
                     block_length=1,
                     options=TFRecordOptions(TFRecordCompressionType.NONE),
                     with_share_memory=False):
        return RecordIterableDatasetLoader(data_path_or_data_iterator,
                     buffer_size,
                     cycle_length,
                     block_length,
                     options=options,with_share_memory=with_share_memory)

    @staticmethod
    def SingleIterableDataset( data_path_or_iterator: typing.Union[typing.AnyStr,typing.Iterator],
                 buffer_size: typing.Optional[int] = 64,
                 block_length=1,
                 options=TFRecordOptions(TFRecordCompressionType.NONE),
                 with_share_memory=False):

            return SingleRecordIterableDataset(data_path_or_iterator, buffer_size,block_length,options,
                                               with_share_memory=with_share_memory)

    @staticmethod
    def MultiIterableDataset(data_path_or_iterator: typing.List[typing.Union[typing.AnyStr,typing.Iterator]],
                 buffer_size: typing.Optional[int]=64,
                 cycle_length=None,
                 block_length=1,
                 options = TFRecordOptions(TFRecordCompressionType.NONE),
                 with_share_memory=False):

            return MultiRecordIterableDataset(data_path_or_iterator, buffer_size,cycle_length,block_length,options,
                                              with_share_memory=with_share_memory)

    @staticmethod
    def RandomDataset(data_path_or_data_list: typing.Union[typing.List, typing.AnyStr, typing.Sized],
                      index_path=None,
                      use_index_cache=True,
                      options=TFRecordOptions(TFRecordCompressionType.NONE),
                      with_share_memory=False):

        return RecordRandomDatasetLoader(data_path_or_data_list,index_path,use_index_cache,options,
                                         with_share_memory=with_share_memory)

    @staticmethod
    def SingleRandomDataset(data_path_or_data_list: typing.Union[typing.AnyStr,typing.Sized],
                 index_path: str = None,
                 use_index_cache=True,
                 options=TFRecordOptions(TFRecordCompressionType.NONE),
                 with_share_memory=False):
        return SingleRandomRecordDataset(data_path_or_data_list,index_path,use_index_cache,options=options,
                                         with_share_memory=with_share_memory)

    @staticmethod
    def MutiRandomDataset(data_path_data_list: List[typing.Union[typing.AnyStr,typing.Sized]],
                 index_path = None,
                 use_index_cache=True,
                 options = TFRecordOptions(TFRecordCompressionType.NONE),
                 with_share_memory=False):
        return MultiRandomRecordDataset(data_path_data_list,index_path,use_index_cache,options,
                                        with_share_memory=with_share_memory)