from pyxai import *
stopwatch = Stopwatch()

MLsolver = Xgboost()

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")


instances = MLsolver.get_instances(model=BTs, dataset=options.data, indexes=options.model, predictions=[0])


instance, prediction = instances[2]
explainer = ExplainerBT(BTs)
explainer.set_instance(instance)

nVariablesInBiggestTree = max([len(set(tree.get_variables())) for tree in BTs.forest])

print("nVariablesInBiggestTree:", nVariablesInBiggestTree)  

type = ReasonExpressivity.Features

print("instance : ", instance)
print("prediction:", prediction)
if type == ReasonExpressivity.Conditions:
  print("Work with conditions")
  abductive = explainer.compute_abductive_reason(reason_expressivity=type, n_iterations=1000)
  print("implicant: ", len(explainer.implicant), " -- abductive", len(abductive))
  print("percentage of reduction:", int(100 - (len(abductive) * 100) / len(explainer.implicant)), "%")
else :
  print("Work with Features")
  abductive = explainer.compute_abductive_reason(reason_expressivity=type, n_iterations=1000)
  features_in_the_reason = explainer.reduce_instance(abductive)
  print("len abductive:", len(features_in_the_reason), " ", len(instance))


#result, abductive = explainer.compute_minimal_abductive_reason_V3(time_limit=30, reason_expressivity=ReasonExpressivity.Conditions)
#print("abductive reason:", abductive)
print("time abductive:", stopwatch.elapsed_time(reset=True), "seconds")

#print("percentage of reduction:", int(100-(len(abductive)*100)/len(explainer.implicant)), "%")
#result, abductive = explainer.compute_minimal_abductive_reason_V3(time_limit=30, reason_expressivity=type)
#print(result, len(abductive))
#if len(abductive) > 0 :
print("check:", explainer.is_abductive_reason(abductive, n_samples = 20 ))

