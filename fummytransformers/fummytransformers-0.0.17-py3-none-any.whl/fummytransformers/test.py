# # 2.3667990922927857
# from svd2vec import svd2vec
# # import svd2vec
# import pickle
# import os
# import glob
# # print(svd2vec.__file__)
# import multiprocessing as mp
# import time

# start = time.time()
# # print(f"{mp.cpu_count()} cpus")

# # number_of_cores = mp.cpu_count()
# number_of_cores = 16
# # number_of_cores = 1
# fnlp_punc = list('''!()-[]{};:'"\,<>./?@#$%^&*_~«»“”''')
# # os.system(f"echo {number_of_cores} cpus allocated")

# fns = glob.glob(
#     "/Users/xiaoou/Documents/data/output_stanza/lemmas_article/*.pickle")

# os.system(f"echo {len(fns)} pickles")

# documents = []

# fns = fns[:1]

# for fn in fns:
#     # os.system(f'echo {fns} loaded')
#     with open(fn, 'rb') as f:
#         document = pickle.load(f)
#         # remove punctuation
#         for x in document:
#             documents.append([y
#                               for y in x if y not in fnlp_punc])

# del fns
# # del document

# from utils import show_gpuinfo

# show_gpuinfo()
