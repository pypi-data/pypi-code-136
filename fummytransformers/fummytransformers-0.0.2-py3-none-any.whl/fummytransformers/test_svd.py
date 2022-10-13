from svd2vec import svd2vec
# import svd2vec
# print(svd2vec.__file__)
documents = ["this is a test right left".split(
)*30, "this is the second test left right".split()*30]
svd = svd2vec(documents, window=2, min_count=0, size=4, verbose=True)
