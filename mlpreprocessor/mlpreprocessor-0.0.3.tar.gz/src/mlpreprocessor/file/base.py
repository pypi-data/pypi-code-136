import os, random, shutil, math
from copy import deepcopy
import tarfile

def load_data_files(data_dir, file_list=[]):
    file_list = deepcopy(file_list)
    fns = os.listdir(data_dir)
    for fn in fns:
        full_fn = os.path.join(data_dir, fn)
        if os.path.isdir(full_fn):
            file_list = load_data_files(full_fn, file_list)
        else:
            file_list.append(full_fn)
    return file_list

def split_train_eval_files(
    data_dir, 
    eval_size=0.1,
    save_dir=None, 
    shuffle=True, 
    seed=1000, 
    valid_ext=[],
    remain_data=True
):
    data_files = load_data_files(data_dir)
    print('# data files:', len(data_files))
    if valid_ext:
        data_files = [f for f in data_files if f.split('.')[-1] in valid_ext]
    assert data_files, 'There is no valid files'
    if shuffle:
        random.seed(seed)
        random.shuffle(data_files)
    n_eval = int(len(data_files)*eval_size)
    train_list = data_files[:-n_eval]
    eval_list = data_files[-n_eval:]
    if save_dir:
        train_dir = os.path.join(save_dir, 'train')
        eval_dir = os.path.join(save_dir, 'eval')
        for _dir in [train_dir, eval_dir]:
            if not os.path.exists(_dir):
                os.makedirs(_dir)
        if remain_data:
            _func = shutil.copyfile
        else:
            _func = shutil.move
        for i, src_fn in enumerate(train_list):
            ext = src_fn.split('.')[-1]
            if ext==src_fn:
                ext = ''
            else:
                ext = f'.{ext}'
            dst_fn = os.path.join(train_dir, f'{i}{ext}')
            _func(src_fn, dst_fn)
        
        for i, src_fn in enumerate(eval_list):
            ext = src_fn.split('.')[-1]
            if ext==src_fn:
                ext = ''
            else:
                ext = f'.{ext}'
            dst_fn = os.path.join(eval_dir, f'{i}{ext}')
            _func(src_fn, dst_fn)
    return train_list, eval_list

def split_tar(name, data_dir, n=2, save_dir=None, remain_data=True):
    data_list =  load_data_files(data_dir)
    batch_size = int(math.ceil(len(data_list)/n))
    cnt = 0
    
    if save_dir is None:
        save_dir = ''
    if save_dir and not os.path.exists(save_dir):
        os.makedirs(save_dir)
    for i in range(0, len(data_list), batch_size):
        _data_list = data_list[i:i+batch_size]
        _fn = os.path.join(save_dir, f'{name}-{cnt}.tar.gz')
        with tarfile.open(_fn, "w:gz") as tar:
            for d in _data_list:
                tar.add(d)
                if not remain_data:
                    os.remove(d)
        cnt += 1

