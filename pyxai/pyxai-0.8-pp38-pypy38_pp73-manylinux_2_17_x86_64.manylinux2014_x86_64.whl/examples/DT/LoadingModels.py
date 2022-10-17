
#Use the file SavingModel to save te model before load it with this file !

from pyxai import Learning, Explainer, Tools

main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()
print("Time limit: ", Tools.Options.time_limit)

#Machine learning part
MLsolver, model = Learning.load(model_directory=Tools.Options.model_directory)

print("Load model time:", main_stopwatch.elapsed_time(), "seconds")

local_stopwatch.elapsed_time(reset=True)
instances = MLsolver.get_instances(
  dataset=Tools.Options.dataset, 
  indexes=Tools.Options.model_directory, 
  model=model, 
  backup_id=0)
print("Get instances time:", local_stopwatch.elapsed_time(reset=True), "seconds")

instance = instances[0][0]
prediction = instances[0][1]
print("instance:", instance)
print("prediction:", prediction)

explainer = Explainer.initialize(model, instance)
s = explainer.sufficient_reason()
print("check:", explainer.check_sufficient(s))