

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

    result, minimal = explainer.minimal_tree_specific_reason(
      time_limit=int(Tools.Options.time_limit),
      reason_expressivity=Explainer.FEATURES)
    
    print(explainer.get_information(minimal))

    time = float(local_stopwatch.elapsed_time(reset=True))
    print("Reason time:", str(time), "seconds")
    print("Total time:", main_stopwatch.elapsed_time(), "seconds")
    
    assert explainer.check_abductive(minimal, n_samples=10) == 100, "Bad test"
    id_instance += 1
    print()


