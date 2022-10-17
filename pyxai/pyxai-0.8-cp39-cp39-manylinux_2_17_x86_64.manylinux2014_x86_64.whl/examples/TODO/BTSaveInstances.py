from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost(options.data)

BTs = MLsolver.evaluate(method=EvaluationMethod.HoldOut, output=EvaluationOutput.BoostedTrees)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(indexes=Indexes.Mixed, correct=True, n=5, model=BTs, backup_directory="dataset/models")
