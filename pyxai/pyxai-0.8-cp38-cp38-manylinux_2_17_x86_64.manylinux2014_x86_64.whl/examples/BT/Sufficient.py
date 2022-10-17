
from pyxai import Learning, Explainer, Tools

main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()
print("Time limit: ", Tools.Options.time_limit)

#Machine learning part
machine_learning = Learning.Xgboost()
models = machine_learning.evaluate(
  method=Learning.LoadModel, 
  output=Learning.BT, 
  model_directory=Tools.Options.model_directory)
print("Load model time:", main_stopwatch.elapsed_time(), "seconds")

#Explanation part
for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    dataset=Tools.Options.dataset, 
    indexes=Tools.Options.model_directory, 
    model=model, 
    backup_id=id)
  print("Get instances time:", local_stopwatch.elapsed_time(reset=True), "seconds")

  explainer = Explainer.initialize(model)
  
  id_instance = 0
  for instance, prediction in instances:
    explainer.set_instance(instance)
    local_stopwatch.elapsed_time(reset=True)

    sufficient = explainer.sufficient_reason()
    print("sufficient:", sufficient)
    print(explainer.get_information(sufficient))

    time = float(local_stopwatch.elapsed_time(reset=True))
    print("Reason time:", str(time), "seconds")
    print("Total time:", main_stopwatch.elapsed_time(), "seconds")
    
    assert explainer.check_abductive(sufficient, n_samples=10) == 100, "Bad test"
    id_instance += 1
    exit(0)
    print()


# elle est fausse du coup. sur la V2
#sufficient = (-8, -9, -14, 15, -18, -19, 22, 23, -28, -29, 30, -38, 39, -42, -48, -49, -50, -51, -54, -63, -74, -75, -78)

# ecoli V1, elle est bonne
#sufficient = (-8, -9, -16, -18, -19, 22, 23, -28, -29, 30, -38, 39, -42, -48, -49, -50, -51, -54, -63, -74, -75, -78)

