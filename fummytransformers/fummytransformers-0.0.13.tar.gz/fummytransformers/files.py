import bz2
import os
import _pickle as cPickle
import py7zr
import pickle


def remove_exist(fn):
    if os.path.exists(fn):
        os.remove(fn)


def extract_7z(fn):
    with py7zr.SevenZipFile(fn, mode='r') as z:
        z.extractall("./fr_wac/")


def load_compressed_pickle(file):
    with bz2.BZ2File(file, 'rb') as f:
        return cPickle.load(file)


def dump_compressed_pickle(fn, data):
    with bz2.BZ2File(fn + '.pbz2', 'w') as f:
        cPickle.dump(data, f)


def dump_pickle(fn, obj):
    with open(fn + '.pickle', 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_pickle(fn):
    with open(fn, 'rb') as handle:
        return pickle.load(handle)


def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)


def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except:
        print("file doesn't exist")


def iter_documents(top_directory, ext):
    """Iterate over all documents and apply the function f"""
    for r, d, files in os.walk(top_directory):
        # print(files)
        for file in filter(
                lambda file: file.endswith(ext), files):
            yield os.path.join(r, file)
        # f(file)
