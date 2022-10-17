
from pyxai import Learning, Tools

#Evaluate and save the model
main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()

machine_learning = Learning.Scikitlearn(Tools.Options.dataset)
model = machine_learning.evaluate(
  method=Learning.HoldOut,
  output=Learning.DT)

machine_learning.save(model, model_directory="save_3")

print("Evaluate and save models time:", main_stopwatch.elapsed_time(), "seconds")

#Save some instance of your choice :)
local_stopwatch.elapsed_time(reset=True)
instances = machine_learning.get_instances(
  indexes=Learning.Test, 
  n=10, 
  model=model, 
  backup_directory="save_3",
  backup_id=0)

print("Save instance time:", local_stopwatch.elapsed_time(reset=True), "seconds")


