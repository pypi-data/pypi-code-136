
from pyxai import Learning, Tools

#Evaluate and save the model
main_stopwatch = Tools.Stopwatch()
local_stopwatch = Tools.Stopwatch()

machine_learning = Learning.Xgboost(Tools.Options.dataset)
models = machine_learning.evaluate(
  method=Learning.LeaveOneGroupOut, 
  output=Learning.BT)

machine_learning.save(models, model_directory="save_2")

print("Evaluate and save models time:", main_stopwatch.elapsed_time(), "seconds")

#Save some instance of your choice :)
for id, model in enumerate(models):
  local_stopwatch.elapsed_time(reset=True)
  instances = machine_learning.get_instances(
    indexes=Learning.Test, 
    n=10, 
    model=model, 
    backup_directory="save_2",
    backup_id=id)

  print("Save instance time:", local_stopwatch.elapsed_time(reset=True), "seconds")

