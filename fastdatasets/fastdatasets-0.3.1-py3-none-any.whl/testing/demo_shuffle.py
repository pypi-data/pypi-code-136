# @Time    : 2022/10/15 14:54
# @Author  : tk
# @FileName: demo_shuffle.py
import random

from fastdatasets import RecordLoader,TFRecordOptions,TFRecordCompressionType,TFRecordWriter,gfile
data_path = gfile.glob('d:/example.tfrecords*')
print(data_path)
options = TFRecordOptions(compression_type=None)
base_dataset = RecordLoader.RandomDataset(data_path,use_index_cache=False,options=options)

ids = list(range(len(base_dataset)))
random.shuffle(ids)
dataset = base_dataset.shuffle_by_ids(ids)

for i,d in enumerate(dataset):
    print(i + 1,d)
