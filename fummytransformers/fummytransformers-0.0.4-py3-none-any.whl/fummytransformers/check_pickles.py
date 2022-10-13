# for each folder an output file

# folders
import os
import multiprocessing as mp
from collections import defaultdict
from glob import glob
import pickle
import re

folders = glob("./*/")
print(folders)
corrupt_files = defaultdict(list)


def check_folder(fd):
    files = glob(fd+"*.pickle")
    log_fn = fd.split("/")[-2] + ".txt"
    if os.path.exists(log_fn):
        os.remove(log_fn)
    for fn in files:
        # read pickled and check it's corrupted
        with open(fn, "rb") as handler:
            try:
                # print("ok")
                p_file = pickle.load(handler)
                with open(log_fn, 'a') as f:
                    if len(p_file) != 10000 and len(p_file) != 8304:
                        f.write(str(len(p_file))+"\n")
                        # don't retain
                        f.write(re.sub(r"[^\d]", "", fn.split("/")[-1])+"\n")
            except:
                print(fn.split("/")[-1])


with mp.Pool(16) as p:
    p.map(check_folder, folders)
