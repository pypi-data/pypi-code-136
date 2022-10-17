# -*- coding: utf-8 -*-
# @Time    : 2022/9/8 16:30

from fastdatasets import RecordLoader,TFRecordOptions,TFRecordCompressionType,TFRecordWriter,gfile
data_path = gfile.glob('d:/example.tfrecords*')
print(data_path)
options = TFRecordOptions(compression_type=None)
base_dataset = RecordLoader.IterableDataset(data_path_or_data_iterator=data_path,cycle_length=1,block_length=1,buffer_size=128,options=options)

print(type(base_dataset))
num = 0
for d in base_dataset:
    num +=1
print('base_dataset num',num)
base_dataset.reset()

def test_batch():
    global base_dataset
    base_dataset.reset()
    ds = base_dataset.repeat(2).repeat(2).repeat(3).map(lambda x: x + bytes('_aaaaaaaaaaaaaa', encoding='utf-8'))
    num = 0
    for _ in ds:
        num += 1
    print('repeat(2).repeat(2).repeat(3) num ', num)

    def filter_fn(x):
        if x == b'file2____2':
            return True
        return False
    base_dataset.reset()

    print('filter....')
    dataset = base_dataset.filter(filter_fn)
    i = 0
    for d in dataset:
        i += 1
        print(i,d)


    print('batch...')
    base_dataset.reset()
    dataset = base_dataset.batch(7)
    dataset = dataset.cache(11000)
    i = 0
    for d in dataset:
        i += 1
        print(i,d)
    print('unbatch...')
    base_dataset.reset()
    dataset = dataset.unbatch().cache(2).repeat(2).choice(10,[0,1,2]).repeat(2)
    i = 0
    for d in dataset:
        i += 1
        print(i, d)


def test_mutiprocess():
    print('mutiprocess...')
    base_dataset.reset()
    dataset = base_dataset.mutiprocess(3,0)
    i = 0
    for d in dataset:
        i += 1
        print(i,d)

    print('mutiprocess...')
    base_dataset.reset()
    dataset = base_dataset.mutiprocess(3,1)
    i = 0
    for d in dataset:
        i += 1
        print(i,d)

    print('mutiprocess...')
    base_dataset.reset()
    dataset = base_dataset.mutiprocess(3,2)
    i = 0
    for d in dataset:
        i += 1
        print(i,d)


test_batch()

#test_mutiprocess()