from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost(options.data)

BTs = MLsolver.evaluate(method=EvaluationMethod.HoldOut, output=EvaluationOutput.SaveModel, model_directory="dataset/models")[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(indexes=Indexes.Test, n=100, model=BTs, backup_directory="dataset/models")

print("time get instances:", stopwatch.elapsed_time(reset=True), "seconds")
print("n selected instances:", len(instances))

