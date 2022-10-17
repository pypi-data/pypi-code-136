from pyxai import *

stopwatch = Stopwatch()

MLsolver = Xgboost(options.data)

BTs = MLsolver.evaluate(method=EvaluationMethod.LoadModel, output=EvaluationOutput.BoostedTrees, model_directory=options.model)[0]

print("time evaluate:", stopwatch.elapsed_time(reset=True), "seconds")

instances = MLsolver.get_instances(BTs, correct=True, n=100)

print("nInstances:", len(instances))

nVariablesInBiggestTree = max([len(set(tree.get_variables())) for tree in BTs.forest])

nVariablesInTrees = sum([len(tree.get_variables()) for tree in BTs.forest])

print("nVariablesInBiggestTree:", nVariablesInBiggestTree)  
print("nVariablesInTrees:", nVariablesInTrees) 

print("time get instances:", stopwatch.elapsed_time(reset=True), "seconds")

id_instance = 0
for instance, prediction in instances:
  explainer = ExplainerBT(BTs, instance)
  lenght_total = []
  time_total = []
  reduction_total = []
  for i in range(50): 
    print("Abductive number " + str(i) + " for instance " + str(id_instance) + " in progress ...")
    abductive = explainer.compute_abductive_reason(seed=i)

    lenght = len(abductive)
    time = float(stopwatch.elapsed_time(reset=True))
    reduction = int(100-(len(abductive)*100)/len(explainer.implicant)) 
    print("time abductive:", str(time), "seconds")
    print("len abductive:", lenght)
    print("percentage of reduction:", reduction, "%")
    lenght_total.append(lenght)
    time_total.append(time)
    reduction_total.append(reduction)
  print("initial size:", len(explainer.implicant))
  print("for instance " + str(id_instance) + ":")
  print("best time abductive:", min(time_total), "seconds")
  print("worst time abductive:", max(time_total), "seconds")

  print("best len abductive:", min(lenght_total))
  print("best percentage of reduction:", max(reduction_total), "%")
  id_instance += 1
