from pyxai import *
from pycsp3 import SAT, UNSAT, UNKNOWN, OPTIMUM

stopwatch = Stopwatch()
stopwatchtotal = Stopwatch()

MLsolver = Xgboost()

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(dataset=options.data, indexes=options.model, model=BTs)
print("time get instances:", stopwatch.elapsed_time(reset=True), "seconds")

explainer = ExplainerBT(BTs)
explainer.display_information()

print("time_limit: ", options.timelimit)

id_instance = 0
for instance, prediction in instances:
  explainer.set_instance(instance)
  
  assert prediction == explainer.target_prediction, "Bad prediction !"
  
  #weights_per_class = []
  #for cl in explainer.boosted_trees.classes:
  #  weights = [explainer.compute_weights(tree, tree.root, explainer.implicant) for tree in explainer.boosted_trees.forest if #tree.target_class == cl]
  #  assert (all(len(x) == 1 for x in weights))
  #  weights = [x[0] for x in weights]
  #  weights_per_class.append(sum(weights))
  #print(weights_per_class)
  #print("instance " + str(id_instance) + " in progress ...")
  #print("prediction:", prediction)
  #print("implicant:", explainer.implicant)
  result, minimal = explainer.compute_minimal_abductive_reason_V3(
    time_limit=int(options.timelimit),
    reason_expressivity=ReasonExpressivity.Features)


  length_reason = len(minimal)
  time = float(stopwatch.elapsed_time(reset=True))
  reduction_literals = int(100-(len(minimal)*100)/len(explainer.implicant)) 
  features_in_the_reason = explainer.reduce_instance(minimal)
  reduction_instance = int(100-(len(features_in_the_reason)*100)/len(instance)) 
  print("result:", result)
  if result == UNSAT or result == UNKNOWN:
    length_reason = len(explainer.implicant)
    reduction_literals = 0
    reduction_instance = 0
    features_in_the_reason = []

  print("time:", str(time), "seconds")
  print("length instance:", len(instance))
  print("length implicant:", len(explainer.implicant))
  print("length reason:", length_reason)
  print("number of features involved by the reason:", len(features_in_the_reason))
  print("number of features not involved by the reason:", len(instance)-len(features_in_the_reason))
  print("percentage of reduction of literals:", reduction_literals, "%")
  print("percentage of reduction of the instance:", reduction_instance, "%")
  print("total time:", stopwatchtotal.elapsed_time(), "seconds")

  assert explainer.is_abductive_reason(minimal, n_samples=10) == 100, "Bad test"
  id_instance += 1
  
  print()


