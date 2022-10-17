from pyxai import Learning, Explainer, Tools
import numpy as np



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
n_features = []

for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    dataset=Tools.Options.dataset, 
    indexes=Tools.Options.model_directory, 
    model=model, 
    backup_id=id)
  print("Get instances time:", local_stopwatch.elapsed_time(reset=True), "seconds")

  explainer = Explainer.initialize(model)
  statistics = explainer.trees_statistics()
  n_features.append(statistics["n_features"])

print("n_features:", n_features)
print("AVG n_features:", round(sum(n_features)/len(n_features),2))
print("SD n_features:", round(np.std(n_features),2))