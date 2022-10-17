from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost()

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]



instance, prediction = MLsolver.get_instances(indexes=Indexes.Test, model=BTs, dataset=options.data, correct=True, n=3)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

explainer = ExplainerBT(BTs, instance)

abductive = explainer.compute_abductive_reason(n_iterations=50)

#print("abductive reason:", abductive)
print("time abductive:", stopwatch.elapsed_time(reset=True), "seconds")
print("len abductive:", len(abductive))

print("check:", explainer.is_abductive_reason(abductive))