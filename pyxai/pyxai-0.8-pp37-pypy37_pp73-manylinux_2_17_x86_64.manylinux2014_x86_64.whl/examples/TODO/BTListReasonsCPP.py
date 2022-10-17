from pyxai import *

from pycsp3 import UNSAT, UNKNOWN, OPTIMUM, SAT

stopwatch = Stopwatch()
stopwatchtotal = Stopwatch()

MLsolver = Xgboost()

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(dataset=options.data, indexes=options.model, model=BTs)
print("time get instances:", stopwatch.elapsed_time(reset=True), "seconds")
#instance, prediction = instances[34]
explainer = ExplainerBT(BTs)
print("time get instances:", stopwatch.elapsed_time(reset=True), "seconds")


explainer.display_information()
print("n_iterations: ", options.niterations)
print("time_limit: ", options.timelimit)

print()
id_instance = 0
for instance, prediction in instances:
  explainer.set_instance(instance)
  print("Instance " + str(id_instance) + " in progress ...")
  
  abductive = explainer.compute_abductive_reason(
    n_iterations=int(options.niterations), 
    time_limit=int(options.timelimit), 
    reason_expressivity=ReasonExpressivity.Features)

  length_reason = len(abductive)
  time = float(stopwatch.elapsed_time(reset=True))
  reduction_literals = int(100-(len(abductive)*100)/len(explainer.implicant)) 
  features_in_the_reason = explainer.reduce_instance(abductive)
  reduction_instance = int(100-(len(features_in_the_reason)*100)/len(instance)) 
  
  #check = explainer.is_abductive_reason(abductive, n_samples=100)
  #print("check:", check)
  
  print("initial size of literals:", len(explainer.implicant))
  print("initial size of the instance:", len(instance))
  
  print("time:", str(time), "seconds")
  print("length instance:", len(instance))
  print("length implicant:", len(explainer.implicant))
  print("length reason:", length_reason)
  print("number of features involved by the reason:", len(features_in_the_reason))
  print("number of features not involved by the reason:", len(instance)-len(features_in_the_reason))
  print("percentage of reduction of literals:", reduction_literals, "%")
  print("percentage of reduction of the instance:", reduction_instance, "%")
  print("total time:", stopwatchtotal.elapsed_time(), "seconds")
  
  id_instance += 1
  print()
  exit(0)