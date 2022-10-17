from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost(options.data)

BTs = MLsolver.evaluate(method=EvaluationMethod.HoldOut, output=EvaluationOutput.SaveModel, model_directory="dataset/models")[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")
