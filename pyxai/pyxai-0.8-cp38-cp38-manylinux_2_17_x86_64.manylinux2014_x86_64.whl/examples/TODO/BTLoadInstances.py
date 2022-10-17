from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost()

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(indexes=options.instances, model=BTs, dataset=options.data)

print(instances)
