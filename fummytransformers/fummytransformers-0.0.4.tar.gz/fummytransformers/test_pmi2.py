from svd2vec import svd2vec
import pickle
import os
import glob

import multiprocessing as mp
import time

start = time.time()
# print(f"{mp.cpu_count()} cpus")

number_of_cores = mp.cpu_count()

os.system(f"echo {number_of_cores} cpus allocated")

fns = glob.glob(
    "/Users/xiaoou/Documents/projects/frwac_articles_pickles/*.pickle")

# for fn in fns:
total_documents = []
for i, fn in enumerate(fns):
    # os.system(f'echo {fns} loaded')
    if i < 1:
        with open(fn, 'rb') as f:
            documents = pickle.load(f)
        break

texts = [a[1].split() for a in documents]
# os.system(f"echo total documents = {len(total_documents)}")
print(len(texts))
print(texts[0])
raise Exception("strop")
# creating the words representation (can take a while)
os.system("echo training started")
svd = svd2vec(texts, window=2, verbose=True, workers=number_of_cores)
os.system("echo training completed")
svd.save("svd_1.bin")
os.system("echo model 1 saved")
svd.save_word2vec_format("svd_1.txt")
os.system("echo model 2 saved")
end = time.time()
os.system(f"echo {(end-start)/60}")
